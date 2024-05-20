import os
import openai
import streamlit as st
from openai import OpenAI


st.markdown("# Where would you like to explore in California?")

st.write("Looking for the perfect spot for your next meal or activity? Simply enter your desired food or activity along with your location, and let our app do the rest! We'll provide tailored recommendations sourced from Yelp, ensuring you find the best places to explore that match your preferences.")
st.write("")
st.write("Please follow this format: 'I want to try [food/place/activity] in [city].'")
st.sidebar.markdown("# Go find new places!")

st.write("")
st.write("Notice of Consent: By submitting a request, you agree to share it with our AI model for recommendation generation. The recommendations will be used solely for the purpose of providing suggestions and will not be stored or shared with third parties.")
st.write("")
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

import requests

def get_completion(prompt, model="gpt-4-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "You are the chatbot component of an app called Walk-E that is focused\
            on making cities more walkable. Your job is to interact with users and encourage\
                them to walk to places. You can suggest walking challenges to users, such as walking\
                    10,000 steps or walking a mile. Walk-E is also connected with local businesses\
                        and can point users towards these mom-and-pop shops to increase foot traffic\
                            while encouraging people to walk more. You also provide people who take up these walking challenges\
                            with rewards such as coupons or deals for these businesses. Keep in mind that \
                                your suggestions come from the Yelp API and these suggestions to users\
                                    can be restaurants, shops, or other businesses. You can ask users if they want \
                                        more options and provide more options if they respond with something like 'yes'. \
                                            You can also ask users if they want to know more about a specific place. \
                                                Don't ask if they want directions."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

def get_food_places(location, term):
    api_key = 'yelp_api_key_placeholder'
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer %s' % api_key}
    params = {'term': term, 'location': location}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['businesses']
    else:
        return None

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.form(key = "chat"):
    prompt = st.text_input("You can enter your message below:")
    submitted = st.form_submit_button("Send")

    if submitted and prompt:
        response = get_completion(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": response})

        # If the user's message contains the word 'in', assume that the user is specifying a location
        if 'in' in prompt.lower():
            # Split the user's message into words
            words = prompt.lower().split()

            # Get the index of the word 'in'
            index = words.index('in')

            # The word after 'in' is assumed to be the location
            location = words[index + 1]

            # The word before 'in' is assumed to be the term
            term = words[index - 1]

            # Get food places
            food_places = get_food_places(location, term)
            if food_places:
                st.write("Here are some " + term + " places you can walk to in " + location + ":")
                for place in food_places:
                    st.write(place['name'])
