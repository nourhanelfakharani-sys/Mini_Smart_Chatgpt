from openai import OpenAI
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة من .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_api():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello, are you working?"}]
    )
    print("AI Response:", response.choices[0].message.content)

if __name__ == "__main__":
    test_api()
print("Test script is running correctly ✅")
print("✅ test_openai is running fine!")
print("Debug: Starting test_openai.py")  # Debug line
print("Debug: Loaded environment variables")  # Debug line