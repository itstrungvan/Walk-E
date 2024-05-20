import streamlit as st
from PIL import Image

st.markdown("# Welcome to Walk-E! 🚶")
st.sidebar.markdown("# Walk-E Home Page")


st.write("")

# Open the image file
img = Image.open(r'C:\Users\Michelle\Downloads\118i\118iproject\118i-tutorial-main - Copy\118i-tutorial-main\pages\images\walk-e logo.png')

# Resize the image
img = img.resize((300,275))

# Save the resized image
img.save(r'C:\Users\Michelle\Downloads\118i\118iproject\118i-tutorial-main - Copy\118i-tutorial-main\pages\images\walk-e logo.png')
st.image(r'C:\Users\Michelle\Downloads\118i\118iproject\118i-tutorial-main - Copy\118i-tutorial-main\pages\images\walk-e logo.png')

st.write("")
st.write("Our mission is to make our city of San Jose more walkable. \
         Unlock the potential of San Jose's walkability with our innovative tools. Explore the city's streets through your lens, \
         envision its future with your input, and discover hidden gems with our recommendations. \
         Stay informed with the latest news on walkability issues, whether you prefer full articles or quick summaries. \
         Let's walk towards a more vibrant San Jose together!")