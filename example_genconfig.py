import google.generativeai as genai
import json
from PIL import Image
import typing_extensions as typing

class FoodItems(typing.TypedDict):
    food_items : list[str] 

burger_image = Image.open("burger.png")
fruit_image = Image.open("fruits.png")

with open("api_key.json", "r") as file:
    api_key = json.load(file)["api_key"]

genai.configure(api_key = api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(["Take this image and extract all the food items you see in this image", 
            fruit_image], generation_config = genai.GenerationConfig(
                response_mime_type = "application/json",
                response_schema = FoodItems
            ))
print(json.loads(response.text))
