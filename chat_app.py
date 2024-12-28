import google.generativeai as genai
import json

with open("api_key.json", "r") as file:
    api_key = json.load(file)["api_key"]

genai.configure(api_key = api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history = [
    {"role" : "user", "parts": "Hi, I am Rahul Jha."},
    {"role" : "model", "parts" : "Nice to meet you."}])

while True:
    inp = input("User: ")
    if "quit" in inp:
        break
    response = chat.send_message(inp)
    print(response.text)