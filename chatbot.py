from langchain_openai import chatopenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.outPut_parsers import strOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","hbchdsb")
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('langchain demo with openai api')
imput_text=st.text_input("search the topic u want")

##  to call the OPENAI llm

llm=ChatOPenAI(model+"gpt 3.5 turbo")
output_parser=strOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
