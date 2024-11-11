import streamlit as st
import pandas as pd
import requests
import json
import time
from dotenv import load_dotenv
import os
from streamlit_gsheets import GSheetsConnection
from serpapi import GoogleSearch
from GroqFunctions import create_groq_chain

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")


st.title("Data Extraction Dashboard")
st.write("## Select Data Source")
data_source = st.radio("Choose your data source:", ("CSV Upload", "Google Sheets"))


def fetch_search_results(query):
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERP_API_KEY
    }
    search = GoogleSearch(params)
    return search.get_dict()


def load_google_sheet_data(gsheet_url):
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        sheet_data = conn.read(spreadsheet=gsheet_url)
        return sheet_data
    except Exception as e:
        st.error(f"Error loading data from Google Sheets: {e}")
        return None


if data_source == "CSV Upload":
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Preview of Uploaded Data:")
        st.write(data.head())
        selected_column = st.selectbox("Select the primary column for entity names:", data.columns)

elif data_source == "Google Sheets":
    gsheet_url = st.text_input("Enter your publicly available Google Sheets link:")
    if gsheet_url:
        sheet_data = load_google_sheet_data(gsheet_url)
        if sheet_data is not None:
            st.write("Preview of Google Sheets Data:")
            st.write(sheet_data.head())
            selected_column_gsheet = st.selectbox("Select the primary column for entity names (Google Sheets):", sheet_data.columns)


st.write("## Define Your Query")
user_prompt = st.text_input("Enter your custom query with placeholders (e.g., 'Find the email address of {}')")

st.write("## Define Backend Extraction Prompt")
backend_prompt = st.text_area(
    "Enter the prompt for extracting information from search results. Use '{}' as a placeholder for the entity.",
    value="Extract the contact information for {} from the following search results."
)

st.write("## Search Limit")
max_searches = st.number_input("Set the maximum number of searches to perform:", min_value=1, max_value=5, value=1)


groq_chain = create_groq_chain()

search_results = []
extracted_data = []


if st.button("Run Search") and user_prompt and backend_prompt:
    entities = []

    if data_source == "CSV Upload" and selected_column in data.columns:
        entities = data[selected_column]
    elif data_source == "Google Sheets" and selected_column_gsheet in sheet_data.columns:
        entities = sheet_data[selected_column_gsheet]
    else:
        st.error("Please select a valid column for entity names.")

    if entities is not None and len(entities) > 0:
        st.write("Running searches for each entity...")
        search_count = 0

        for entity in entities:
            if search_count >= max_searches:
                st.warning("Reached the maximum number of searches as set by the user.")
                break

            query = user_prompt.replace("{}", entity)
            result = fetch_search_results(query)

            if result:
                results = result.get("organic_results", [])
                search_data = {
                    "entity": entity,
                    "query": query,
                    "results": [{"title": item.get("title"), "link": item.get("link"), "snippet": item.get("snippet")} for item in results]
                }
                search_results.append(search_data)

                prompt_text = backend_prompt.replace("{}", entity) + f"\n\nSearch Results:\n{search_data['results']}"
                extraction_result = groq_chain.run({"prompt_text": prompt_text})

                if extraction_result:
                    extracted_data.append(extraction_result)
                    with st.expander(f"See details for {entity}"):
                        st.write(extraction_result)
            else:
                st.error(f"No results found for {entity}")

            time.sleep(1)
            search_count += 1

        flattened_data = []

        for result, data in zip(search_results, extracted_data):
            flattened_data.append({
                'Entity': result['entity'],
                'LLM Output':data
            })

        extracted_df = pd.DataFrame(flattened_data)

        if not extracted_df.empty:
            st.write("### Extracted Data:")
            st.dataframe(extracted_df)

            st.download_button(
                label="Download Results as CSV",
                data=extracted_df.to_csv(index=False).encode(),
                file_name="search_results.csv",
                mime="text/csv"
            )
        st.success("Search completed! Results saved to search_results.json.")
    else:
        st.error("No entities to search. Please check the selected column and data source.")
