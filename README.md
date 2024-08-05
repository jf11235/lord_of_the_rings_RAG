# Simple Rag App For The Lord of the Rings

This Streamlit app allows users to ask questions and upload text files to get responses based on the content of the uploaded files. The app uses a generative AI model to provide answers.

## Prerequisites

- Python 3.12
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code, including the [text file](the_fellowship_of_the_ring.txt).

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Get a free API key for Google's Gemini by going to the following link: [Google's Gemini API Key](https://aistudio.google.com/app/apikey).

5. Create a `.env` file in the root directory of the project and add your API key:

    ```env
    API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

    This should open the app in your browser automatically. If it doesn't, proceed to step 2.

2. Open your web browser and go to [http://localhost:8501](http://localhost:8501).

3. You will see the app interface with a title "Simple Rag App For The Lord of the Rings".

4. Upload the Lord of the Rings text file (included in the repository).

5. Enter your question in the text input box. The model has been prompted to only answer questions about information in the text document provided.

6. Click the "Submit" button to get the response.

7. You can ask additional questions by typing in the input box and hitting return.

8. If you wish, you can upload other documents and query the model about them.

## File Descriptions

- `app.py`  
  This file contains the Streamlit app code.

- `rag.py`  
  This file contains the function to query the generative AI model.

## License

Owned by Josh Feinberg (josh.h.feinberg@gmail.com, 917 776 2801)
