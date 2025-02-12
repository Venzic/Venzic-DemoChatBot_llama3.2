import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Streamlit app
st.title("LangChain with LLaMA 3.2 API")

# User input field
input_text = st.text_input("Enter your query:")

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's questions."),
    ("user", "Question: {question}")
])

# Initialize LLM only once
llm = Ollama(model="llama3.2")
chain = prompt | llm | StrOutputParser()

# Process input
if input_text:
    if "response" not in st.session_state or st.session_state["last_input"] != input_text:
        st.session_state["response"] = chain.invoke({"question": input_text})
        st.session_state["last_input"] = input_text

    st.write(st.session_state["response"])
