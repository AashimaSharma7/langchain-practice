#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#for langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#model form ollama --> calling the LLM
llm = Ollama(model="llama3")

#prompt template --> converts raw user i/p to better i/p to the LLM
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a rude assistant. Respond to the user queries in a sarcastic manner."),
    ("user", "input:{input}")
])

#adding a simple output parser to convert the chat msg(o/p of the model) to a string
output_parser = StrOutputParser()

#chain
chain = prompt | llm | output_parser

#streamlit 
st.title('Hi! I am your very own rude assistant')
input_text=st.text_input("Say, What do you want?")

#on writing i/p and pressing enter. we should get the chain invoke to get o/p.
if input_text:
    st.write(chain.invoke({"input": input_text}))