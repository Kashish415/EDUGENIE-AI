import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Access API keys from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Function to call Google Generative AI for response
def generate_response(user_query):
    try:
        # Initialize the Google Generative AI LLM
        llm = GoogleGenerativeAI(api_key=api_key, model='gemini-pro', temperature=0.1)
        
        # Define the chat prompt template
        prompt = ChatPromptTemplate.from_messages([
            ('system', 'Provide a comprehensive overview of the topic that the user provides'),
            ('user', user_query)
        ])
        
        # Invoke the LLM and get a response
        response = llm.invoke(prompt.format(user_query=user_query))
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Load custom CSS from a file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Adding App Title
st.markdown("<h1>EDUGENIE AI ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3><em>Where knowledge begins</em></h3>", unsafe_allow_html=True)

# Function to call Google Generative AI for response
def generate_response(prompt):
    try:
        # Initialize the GoogleGenerativeAI model
        model = GoogleGenerativeAI(api_key=api_key)
        response = model.complete(prompt=prompt, max_tokens=150, temperature=0.7)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Input Field
user_input = st.text_input("", placeholder="Ask anything...")

# Generate Button
if st.button("Generate"):
    if user_input:
        with st.spinner("Generating response..."):
            response = generate_response(user_input)
            st.markdown(f"""
                <div class='response-box'>
                    <h4>Response:</h4>
                    <p>{response}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Please enter a question.")

# Footer
st.markdown("<footer>Made with ❤️ by Kashish</footer>", unsafe_allow_html=True)












