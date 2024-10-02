from flask import Flask, render_template, request
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Access API keys from environment variables
api_key = os.getenv("GOOGLE_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = generate_response(user_input)
    return render_template('index.html', response=response)

def generate_response(user_query):
    try:
        llm = GoogleGenerativeAI(api_key=api_key, model='gemini-pro', temperature=0.1)
        prompt = ChatPromptTemplate.from_messages([
            ('system', 'Provide a comprehensive overview of the topic that the user provides. Include relevant details and examples.'),
            ('user', user_query)
        ])
        response = llm.invoke(prompt.format(user_query=user_query))
        return response
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
