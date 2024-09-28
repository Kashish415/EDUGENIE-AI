# EduGenie AI

EduGenie AI is a generative AI-powered educational tool designed to assist users in generating comprehensive content across various topics. By leveraging cutting-edge AI models, this application delivers instant insights and learning support, making education more interactive and accessible.

## Features

- **AI Content Generation** : Generates detailed overviews and explanations based on user-provided topics, ensuring high-quality educational content.

- **User-Friendly Interface**: A simple and intuitive design built using Streamlit for seamless navigation.

- **Real-Time Interaction**: Provides instant responses to user queries, enabling efficient learning.

## Tech Stack

- **Programming Language**: Python
- **Frameworks**:
 **LangChain**: For managing prompts and interactions with the language models.
 **Streamlit**: For building a responsive and interactive web interface.
- **APIs**:
 **Google Generative AI (Gemini Pro)**: Used for generating insightful content with advanced natural language processing capabilities.

## Installation
- **Prerequisites** : Python 3.10 or above
- **API keys for**:
-> LangChain API
-> Google Generative AI (Gemini Pro)

## Setup Instructions

**Clone the repository**:
git clone https://github.com/your-repo/edugenie-ai.git
cd edugenie-ai

**Create a virtual environment (optional but recommended)**:
python -m venv venv

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

**Install dependencies**:
pip install -r requirements.txt

**Create a .env file in the root directory and add your API keys**:

LANGCHAIN_API_KEY=your_langchain_api_key
GOOGLE_API_KEY=your_google_api_key

**Run the application**:
streamlit run app.py

**Access the app**: 
Open your browser and go to http://localhost:8501 to interact with EduGenie AI.

## File Structure

- **app.py**: The main application file that runs the Streamlit app.
- **.env**: Stores sensitive API keys (not included in the repository).
- **requirements.txt**: Specifies the Python dependencies required for the project.
- **devcontainer.json**: Configuration for a VS Code Dev Container, providing an isolated development environment.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have any improvements, bug fixes, or new features to suggest.

## Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.

git checkout -b feature/your-feature-name

3. Commit your changes and push the branch.
4. Submit a pull request for review.

