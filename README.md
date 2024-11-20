 # Automated Entity Information Retrieval and Extraction from CSV file

## Project Description

This project provides a user-friendly Streamlit dashboard that allows users to search for specific information about entities by utilizing web search results from SerpAPI and language models (LLMs) via Groq API. Users can dynamically define queries with placeholders, specify a list of entities from Google Sheets or CSV, and retrieve structured information (such as email addresses, revenue, etc.) by parsing the search results with the help of an LLM. The tool is useful for data collection, information extraction, and custom search workflows.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dibyansu06/AgentAI.git
   cd AgentAI

2. **Install Dependencies**
Make sure to have Python 3.12 or higher installed. Then install required packages:

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Set Up Environment Variables**
Create the .env file and add the following variables:

- **SERP_API_KEY:** Your SerpAPI key to enable web search.
- **GROQ_API_KEY:** Your Groq API key for using LLM-based extraction.

4. **Run the Application**
Launch the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage Guide
1. **Dashboard Overview**

After launching the application, you’ll see the following main sections:

- Data Source Selection: Choose between uploading a CSV file or connecting to a Google Sheet to provide a list of entities.
- Define Query: Enter your custom search query using placeholders (e.g., {}) for dynamic replacements. **Leave the curly brackets emtpy.**
- Set Search Limit: Specify the maximum number of searches per entity to avoid excessive requests.
- Run Search and Extract Information: Execute the search queries and run the extraction process.

2. **Connecting Google Sheets**

If using Google Sheets:

- Paste the **URL** of your Google Sheet into the application when prompted.
- The sheet should contain a column with the entities you wish to query.
- The application will automatically detect and prompt you to select the relevant column from the sheet that contains your entities.

3. **Setting Up Search Queries**

- Define a query with placeholders to dynamically replace with each entity. For example, a query like “What is the annual revenue of {}?” will replace {} with each entity’s name. **Note leave the {} empty!**
- Select the maximum number of searches to perform, keeping in mind API rate limits.

4. **Running the Search and Extracting Data**
- Click “Run Search” to initiate the search for each entity based on the defined query.
- The LLM will process search results and extract the relevant information.
- Results are displayed on the dashboard, and you can download them in a JSON file once the extraction is complete.

## API Keys and Environment Variables
- **SERP_API_KEY:** This key is needed to fetch web search results from SerpAPI. Obtain an API key by signing up at [SerpAPI](https://serpapi.com/).
- **GROQ_API_KEY:** This key enables text parsing and information extraction via Groq API. Register at [Groq](https://groq.com/) to get your API key.

## **Optional Features**
- **Error Handling with Retries:** Automatically retries failed API requests up to 3 times with exponential backoff to manage connectivity or rate-limit issues.
- **Custom Query Validation:** Ensures that queries contain dynamic placeholders (e.g., {}) and validates the format.
- **JSON Data Export:** Easily download search and extraction results in JSON format for further analysis or reporting.
- **Adjustable Search Limits:** Set a custom limit for the number of searches per entity, which helps manage API usage and avoid rate limits.

With this setup, you’re ready to run dynamic, customizable searches for multiple entities and extract targeted information effectively. Happy querying!


