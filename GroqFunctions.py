from dotenv import load_dotenv
import os
import requests
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.ai/v1/extract"

def create_groq_chain():
    prompt_template = PromptTemplate(template="{prompt_text}")
    groq_llm = ChatGroq(
        model="mixtral-8x7b-32768",
        api_key=GROQ_API_KEY,
        temperature=0.0,
        max_tokens=2048,  
        timeout=60,      
        max_retries=2   
    )
    return LLMChain(prompt=prompt_template, llm=groq_llm)
