#implement the page 6 that we talked about in the chat for reading a pdf'''
# we are using fitz or PyMuPDF'''
#import PyMuPDF
import fitz
import streamlit as st
import os
import openai
from openai import OpenAI
from pathlib import Path

st.sidebar.markdown("# Stay Updated with the Latest News in San Jose!")

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def main():
    st.title("Stay Updated on the Latest News in San Jose! 📰")
    st.write("")
    st.write("Stay informed about urban development and walkability in San Jose with ease! Browse our curated list of PDF articles covering a range of topics. Select the article you're interested in and choose from three options: receive a summary, explore key points, or access the full transcription. Whatever your preference, our app ensures you're up-to-date on the latest discussions, plans, and news shaping the city's future.")


    st.write("")
    st.write("Notice of Consent: Your privacy matters to us. By using our app, you consent to the collection and use of your data, including location and images, to enhance your experience and provide personalized recommendations. Rest assured, we prioritize the security and confidentiality of your information. For more details, please review our privacy policy.")
    st.write("")
    def get_summary(text):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        return response.choices[0].message.content
    
    def get_key_points(text):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and extract the key points."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        return response.choices[0].message.content

    def get_action_items(text):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        return response.choices[0].message.content
    
    def get_sentiment(transcription):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible. Please keep it to fewer than 5 sentences."
                },
                {
                    "role": "user",
                    "content": transcription
                }
            ]
        )
        return response.choices[0].message.content
    # Create a file uploader
    # uploaded_file = st.file_uploader("Choose a PDF file related to the issue of limited walkability in San Jose that you want to analyze. You will receive a summary, key points, action items, and a sentiment analysis of this PDF.", type="pdf")

    #if uploaded_file is not None:
        # st.title("Stay Updated with the Latest News")

    # Get a list of all the PDF files in the "articles" folder
    pdf_files = [f for f in os.listdir(r'C:\Users\Michelle\Downloads\118i\118iproject\118i-tutorial-main - Copy\118i-tutorial-main\pages\articles') if f.endswith('.pdf')]

    # Let the user select a file
    selected_file = st.selectbox('Select one of the following articles:', pdf_files)

    # Let the user select an option
    options = ['Summary', 'Key Points', 'Full Transcription']
    selected_option = st.selectbox('What would you like to see?', options)

    # Open the selected file
    selected_file_path = os.path.join(r'C:\Users\Michelle\Downloads\118i\118iproject\118i-tutorial-main - Copy\118i-tutorial-main\pages\articles', selected_file)

# Open the selected file
    with fitz.open(selected_file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text("text")

    if selected_option == 'Summary':
        # Get a summary of the text
        summary = get_summary(text)
        st.write(summary)
    elif selected_option == 'Key Points':
        # Get the key points of the text
        key_points = get_key_points(text)
        st.write(key_points)
    else:
        # Display the full transcription of the article
        st.write(text)
        # Load the PDF
        pdf = fitz.open(selected_file_path)
        
        # Concatenate the text from all pages
        full_text = ""
        for i in range(len(pdf)):
            page = pdf.load_page(i)
            full_text += page.get_text("text")

            
if __name__ == "__main__":
    main()

    
