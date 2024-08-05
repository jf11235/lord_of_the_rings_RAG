import dotenv
import google.generativeai as genai
import os
#load the environment variable for the API key
dotenv.load_dotenv()


def query_gemini(text:str, user_query:str,)->str:
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    template = (
    "You are a helpful assistant. The following is "
    "a user query and some potentially relevant documents. "
    "If the answer to the user's query is in the document, "
    'respond to their question. If the answer to the question '
    'is not in the document, respond with "I\'m sorry, I do not '
    'have that information."'
)
    
    text = f'{template}' + f'User Query: {user_query}' + f'Source Documents: {text}'
    response = model.generate_content(f'{text}')
    return response.text


if __name__ == '__main__':
    pass