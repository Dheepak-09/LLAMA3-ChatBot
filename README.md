# LLAMA3-ChatBot

This code sets up a Streamlit application that allows users to input a query, which is then processed by a language model (Ollama with Llama3) to generate a response. The response is formatted 
using a custom prompt template and displayed in the Streamlit app.

This project demonstrates how to integrate Langchain with Streamlit to create a simple application that uses the LLAMA3 language model to respond to user queries.

## Overview
The application provides a user interface where users can enter a query. The query is processed using the LLAMA3 model provided by Ollama, and the response is displayed back to the user. The application leverages Langchain for prompt management and output parsing, and Streamlit for the web interface.

## Requirements
To run this project, you need to have the following Python packages installed:

streamlit
langchain_core
langchain_community
ollama
You can install these packages using pip:

bash
Copy code
```
pip install streamlit langchain_core langchain_community ollama
```
## How to Run
Clone the Repository

bash
Copy code
```
git clone <repository-url>
cd <repository-directory>
```
Install Dependencies

Make sure you have the required packages by running:

bash
Copy code
```
pip install -r requirements.txt
```
(If you don't have a requirements.txt file, you can manually install the required packages using the pip install command mentioned above.)

Set Up Environment Variables

Ensure any necessary environment variables are set up. For this demo, there are no specific environment variables required.

Run the Streamlit App

Start the Streamlit app using:

bash
Copy code
```
streamlit run app.py
```
Replace app.py with the name of your Python script if it differs.

Access the App

Open your web browser and go to http://localhost:8501 to interact with the application.

## Code Explanation
Prompt Template: Defines how user queries are formatted before being sent to the language model.

LLAMA3 Model: The language model used to generate responses based on the input queries.

Streamlit Interface: Provides a user-friendly web interface to input queries and display responses.

## Customization
You can modify the prompt template and language model settings based on your needs. For example, change the model to a different version or adjust the prompt template for different types of queries.

## Troubleshooting
If you encounter issues:

Ensure all dependencies are installed.

Check the Streamlit logs for any error messages.

Verify that the LLAMA3 model is properly configured.
