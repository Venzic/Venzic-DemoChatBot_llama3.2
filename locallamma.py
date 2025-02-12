from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()


## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's questions."),
        ("user", "Question:{question}")
    ]
)


 ## streamlit framework

st.title('Demo Langchain With lamma3.2 API')
input_text=st.text_input("Search the topic you want")

# Ollama llama3 LLm
llm=Ollama(model="llama3.2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text})) 


