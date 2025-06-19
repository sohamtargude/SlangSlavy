import google.generativeai as genai

class GenerativeAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-pro")

    def get_slang_details(self, slang):
        try:
            prompt = f"Define the slang term '{slang}' and use it in a sentence."
            response = self.model.generate_content(prompt)
            text = response.text
            parts = text.strip().split('\n', 1)
            return {
                "definition": parts[0],
                "usage": parts[1] if len(parts) > 1 else "No usage found"
            }
        except Exception as e:
            return {"error": str(e)}
