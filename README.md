# Walk-E

## Overview 
Walk-E is a web-based app that aims to assist college students who may be frustrated with the limited walkability in their city, so they can actively participate in urban development planning in their community. 

## Walk-E: What is it? 
Walk-E is a web-based app hosted via Streamlit. Walk-E is inspired by Wall-E, a robot that is programmed to clean up the planet by compacting trash into cubes. Whereas Wall-E focuses on cleaning up garbage, Walk-E addresses a plethora of issues that contribute to the limited walkability of cities, specifically in downtown San Jose. 

## Why do we need Walk-E and who would use it? 
Let’s learn about a student user who can benefit from using our app. Meet Jasmine, an environmental studies student living on campus at San Jose State. She is passionate about reducing her carbon footprint and supporting local businesses, which she can do by walking to nearby restaurants. However, it is difficult for her to navigate the city because she does not have a car, and downtown San Jose is not pedestrian-friendly. That’s why she created a group to advocate for better urban planning. 

## How does Walk-E Work?
Walk-E leverages OpenAI's generative AI capabilities, Python libraries, and Streamlit to provide a web-based solution to address frustrations related to limited walkability. Walk-E offers 4 features on the app, all of which are tailored to meet the needs of busy college students. 

## Feature 1: Analyze the Walkability of Your City and Report Issues
Walk-E draws on the power of OpenAI's Vision capabilities to analyze user-uploaded images. For example, if Jasmine, our user, uploads a picture of a pothole, Walk-E identifies that potholes are a hazard that limits how walkable a city is. The app also offers suggestions on how to fix the pothole-related issue, such as enforcing regular street maintenance and designing better roadways. After analyzing the walkability-related issue in the image and providing solutions, Walk-E lets users report this issue to local authorities, should the issue be categorized as "severe" enough for reporting. With just one click of a button, users can file a report without having to fill out any paperwork. This feature is useful because it provides a simple, convenient way for citizens, especially college students, to connect with their local authorities and alert them of any concerns that make their city less pedestrian-friendly. 

## Feature 2: Envision Your Ideal City
Users can also use our app to picture their "perfect" city. For students like Jasmine who want to voice their worries about the walkability of their city, this feature is perfect for visualizing urban improvements that they would like to see in their city. If they were to attend a town hall meeting and speak to authorities directly, it might be hard to paint a picture of what changes they would like to see in their community. However, Walk-E leverages DALL-E's image generation abilities to let users enter a text prompt of what they would like to see in their ideal city. This feature fosters community-driven city planning, giving users a way to create tangible solutions that they could potentially present to city officials. Alternatively, users who are in an advocacy group like Jasmine, can use this feature to quickly and effortlessly visualize any ideas they have during group meetings, as opposed to drawing their individual proposals by hand. 

## Feature 3: Stay Updated with the Latest News 
Busy college students are probably not able to dedicate the amount of time they want to stay updated with current events. Walk-E aims to provide easy-to-digest content for such students, as it relates to urban development initiatives and discussions in the community. As of now, Walk-E's scope is limited to downtown San Jose. Walk-E utilizes PyMuPDF and GPT-4-Turbo to analyze numerous pdf-formatted articles about walkability-related issues in downtown San Jose. In the form of a drop-down menu, users can select the article they want to read up on, as well as whether they want to see a brief summary, a list of key points, or the full transcription of the article. Having these options gives users the flexibility to select how much information they would like to consume at a given time, making it easy for students to stay up-to-date with urban development and walkability-related news without suffering from information overload. 

## Feature 4: Get Recommendations 
To further show our dedication to helping college students who are frustrated with their limited ability to walk around their cities, Walk-E also has a "recommendation" feature. Users can input a text prompt including what activity or food they would like to try, as well as their location, and Walk-E quickly provides a list of walking-distance restaurants and businesses. Our app provides not only the business name, but also the address, phone number, 5-star rating, price level, and access to the business's online menu. Using the Yelp-Fusion API, Walk-E delivers accurate recommendations, facilitates pedestrian-friendly navigation, and enhances local business visibility. This feature is incredibly helpful for college students who do not have a car but would like to explore their surroundings and achieve a fulfilling college experience. 

## Check out our Presentation! 
[![Watch our Presenation!](https://docs.google.com/presentation/d/1eXrYPthKdnoKS2UxUCxkGdTBmPub8XnUGTdh32Tuwys/edit?usp=sharing)]

## Check out our Demo Video! 
[![Watch our demo!](https://drive.google.com/file/d/1Fz1d0MBP7S5inqNwgWRfO5BessAt8OtK/view?resourcekey)]
