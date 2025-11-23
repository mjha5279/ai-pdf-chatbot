import google.generativeai as genai

genai.configure(api_key="AIzaSyD2xR45EOdM6N01COQ8FemYPG3A823Pa_0")
model = genai.GenerativeModel("models/gemini-2.5-flash")

response = model.generate_content("Hello, test message")
print(response.text)
