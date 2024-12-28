# 1. Configure the gemini
# 2. Select the model 
# 3. Select the task => prompting on Text or image or audio or video
# 4. Create our request/prompt
# 5. Send the request 

import google.generativeai as genai
import json
from PIL import Image

burger_image = Image.open("burger.png")
fruit_image = Image.open("fruits.png")

with open("api_key.json", "r") as file:
    api_key = json.load(file)["api_key"]

genai.configure(api_key = api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(["Do you recommend me earting the given food if I am diabetic? Respond with 1 sentence. ", 
#             fruit_image])

response_stream = model.generate_content("Write a article on AGI in 1000 words", stream = True)

for response in response_stream:
    print(response.text)

# Let us say I have a video of 10 mins => 10 * 60 * 30 => 1800 => 600 images
# print("Model is loaded", model)