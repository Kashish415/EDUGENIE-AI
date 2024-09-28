from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables
load_dotenv()

# Set your API key
api_key = os.getenv("API_KEY")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;  /* Black background */
        color: white;  /* White text color */
    }

    h1 {
        font-size: 4em;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(135deg, #8A2BE2, #FF69B4, #00BFFF); /* Gradient for text */
        -webkit-background-clip: text;
        color: transparent;
    }

    h3 {
        font-style: italic;
        text-align: center;
        margin-top: -20px;
        background: linear-gradient(135deg, #8A2BE2, #FF69B4, #00BFFF); /* Gradient for text */
        -webkit-background-clip: text;
        color: transparent;
    }

    .stApp {
        background-color: black;  /* Black background for the whole app */
    }

    .css-18ni7ap, .css-1cpxqw2 {  /* Streamlit top bar */
        background-color: black !important;
    }

    input {
        border: none !important;
        outline: none !important;
        background-color: #333;  /* Dark gray */
        color: white;
        padding: 10px;
        border-radius: 10px;
        width: 100%;
        margin-top: 20px;
    }

    input:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    .stTextInput>div>div>input {
        background-color: #333;  /* Dark gray */
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 10px;
    }

    .stTextInput>div>div>input:focus {
        box-shadow: none;
        border: 1px solid white;  /* White border on focus */
    }

    .stButton button {
        background-color: white;  /* White button */
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1.2rem;
        border-radius: 10px;
        color: black;
        font-weight: bold;
        transition: box-shadow 0.1s ease-in-out;
    }

    .stButton button:hover {
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);  /* White glow effect */
    }

    footer {
        text-align: center;
        font-size: 1rem;  /* Increased font size */
        background: linear-gradient(135deg, #8A2BE2, #FF69B4, #00BFFF); /* Gradient for text */
        -webkit-background-clip: text;
        color: transparent;
        margin-top: 6rem;  /* Positioned lower */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
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
            st.write(f"Response: {response}")
    else:
        st.write("Please enter a question.")

# Footer
st.markdown(
    "<footer>Made with ❤️ by Kashish</footer>",
    unsafe_allow_html=True
)





# from dotenv import load_dotenv
# import os
# import langchain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_google_genai import GoogleGenerativeAI
# import streamlit as st

# # Load environment variables from .env
# load_dotenv()

# # Access API keys from environment variables
# os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
# os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

# # Initialize the Google Generative AI LLM
# llm = GoogleGenerativeAI(model='gemini-pro', temperature=0.1)

# # Define the chat prompt template
# prompt = ChatPromptTemplate.from_messages([
#     ('system', 'Provide a comprehensive overview of the topic that the user provides'),
#     ('user', '{user_query}')
# ])

# # Streamlit app UI
# st.title('SmartEdu Assistant')

# # User input
# user_query = st.text_input('Input Your Query')

# # Action when button is pressed
# if st.button('Generate'):
#     if user_query:
#         try:
#             # Format the prompt with the user's query
#             formatted_prompt = prompt.format(user_query=user_query)
#             st.write("Formatted prompt:", formatted_prompt)  # Debug print for formatted prompt
            
#             # Invoke the LLM and get a response
#             response = llm.invoke(formatted_prompt)
#             st.write(response)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#     else:
#         st.error("Please input a query.")



