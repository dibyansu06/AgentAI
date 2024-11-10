# Project Title

## Project Description

This project is a web application designed to streamline data handling, web search, and natural language processing (NLP) tasks using a simple and intuitive dashboard. Users can upload CSV files or link Google Sheets, select columns of interest, and perform web searches using a custom query format. The results from the search are then processed by a language model (Groq) to extract meaningful insights. This application is ideal for users looking to automate the extraction of relevant data from both structured (CSV/Sheets) and unstructured (web) sources.

**Technologies Involved:**
- **Dashboard/UI:** Streamlit
- **Data Handling:** pandas for CSV files; Google Sheets API for Sheets
- **Search API:** SerpAPI
- **LLM API:** Groq
- **Backend:** Python
- **Agents:** Langchain (ChatGroq)

---

## Setup Instructions

### Prerequisites
Ensure you have Python 3.7+ installed.

### Installation
1. **Clone the repository** (or download the project files).
2. Install the dependencies by running the following command in your project directory:
   ```bash
   pip3 install -r requirements.txt
   ```
(Note: requirements.txt was generated using the command pip3 freeze > requirements.txt.)

```bash
streamlit run app.py
```

## Usage Guide

### **Interacting with the Dashboard**
- **Data Upload:** You can upload data in two ways:

- **CSV File:** Upload a CSV file from your local machine using the Browse File button.
Google Sheets: Use Google Sheets by logging in through OAuth2. You will need to provide the sheet ID and range when prompted.
Select a Column: Once the data is loaded, select the primary column (entity names) using the drop-down menu.

- **Web Search Query:**

  - Enter your custom query in the format: Find the email address of {} (e.g., replace {} with the entity names from the selected column).
  - Leave the curly brackets {} empty; the selected column values will be dynamically inserted into the query at the backend.
- **LLM Prompt:** After receiving search results, provide a custom prompt that will guide the LLM (Groq) in extracting meaningful information from the results. The prompt will be combined with the search data to generate the final output.

## **API Keys and Environment Variables**

### **Required API Keys:**
  
**SerpAPI:** You need a SerpAPI key to perform web searches.
**Groq API:** You need an API key for the Groq language model.
**Google Sheets API Credentials:** You must set up the Google Sheets API from the Google Cloud Platform Console and download the credentials as a credentials.json file.
  
### **Environment Setup:**
  
**Groq API Key and SerpAPI Key:**

  1. Create a .env file in your project directory.
  2. Add the following lines to the .env file:
```bash
GROQ_API=<your-groq-api-key>

SERPAPI=<your-serpapi-key>
```
  3. Use the python-dotenv library to load the environment variables from this file.
**Google Sheets API:**

Set up the Google Sheets API in your Google Cloud Console.
Download the credentials.json file and place it in the main project directory.

