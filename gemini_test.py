import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="PASTE_YOUR_GEMINI_KEY_HERE")

try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("What does 'ghosted' mean in slang?")
    print("\n✅ Gemini API is working!\n")
    print("Response:\n", response.text)
except Exception as e:
    print("\n❌ Error occurred:")
    print(e)
