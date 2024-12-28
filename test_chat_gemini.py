import google.generativeai as genai
import json

with open("api_key.json", "r") as file:
    api_key = json.load(file)["api_key"]

genai.configure(api_key = api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history = [
    {"role" : "user", "parts": "Hi, I am Rahul Jha."},
    {"role" : "model", "parts" : "Nice to meet you."}
])
response = chat.send_message("Hey, what is my name?")
print(response.text)
response = chat.send_message("Hey, remeber my house has 3 doors.")
response = chat.send_message("Hey,how are you doing?")
response = chat.send_message("what do you think about AGI?")
response = chat.send_message("how many doors my house has?")
print(response.text)