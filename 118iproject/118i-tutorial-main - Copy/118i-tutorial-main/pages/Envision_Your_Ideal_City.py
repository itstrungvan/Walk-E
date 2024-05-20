import os
import openai
import streamlit as st
from PIL import Image
import requests
from openai import OpenAI
from pathlib import Path

st.markdown("# Envision Your Ideal City 📷")
st.sidebar.markdown("# Imagine the Future!")

st.write("Paint the picture of your ideal urban landscape! Describe the features you envision in your dream city, from vibrant pedestrian-friendly streets to green spaces and community hubs. Your input will help our app create a visual rendering of your ideal future cityscape.")

st.write("")
st.write("Notice of Consent: By submitting a description, you agree to share it with our AI model for image generation. The image will be used solely for the purpose of creating a visual representation of your ideal city and will not be stored or shared with third parties.")
st.write("")
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def download_image(filename, url):
  response = requests.get(url)
  if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
  else:
        print("Error downloading image from URL:", url)

def filename_from_input(prompt):
   # Remove all non-alphanumeric characters from the prompt except spaces.
    alphanum = ""
    for character in prompt:
        if character.isalnum() or character == " ":
            alphanum += character
    # Split the alphanumeric prompt into words.
    # Take the first three words if there are more than three. Else, take all    of them.
    alphanumSplit = alphanum.split()
    if len(alphanumSplit) > 3:
        alphanumSplit = alphanumSplit[:3]
    # Join the words with underscores and return the result.
    return "images/" + " ".join(alphanumSplit)


# Create an image
# If model is not specified, the default is DALL-E-2.
def get_image(prompt, model="dall-e-3"):
    image = client.images.generate(
        prompt=prompt,
        model=model,
        n=1,
        size="1024x1024"
    )
    # Download the image

    filename = str(Path(__file__).resolve().parent)+ "/"+ filename_from_input(prompt) + ".png"
    download_image(filename, image.data[0].url)

    return image


#print(response)

with st.form(key = "chat"):
    prompt = st.text_input('**In your ideal city, what are some key features you would like to have?\
                           For example, you could say "I would like to have a park with a lake and a playground.**"')
    submitted = st.form_submit_button("Submit")
        
    if submitted:
        response = get_image(prompt)
        image = Image.open(str(Path(__file__).parent)+'/'+filename_from_input(prompt)+'.png')
        st.image(image, caption='New Image')