import google.generativeai as genai

class GenerativeAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-pro")  # ✅ full model path

    def get_slang_details(self, slang):
        try:
            prompt = f"Define the slang term '{slang}' and use it in a sentence."
            response = self.model.generate_content(prompt)
            if hasattr(response, 'text'):
                text = response.text
                parts = text.strip().split('\n', 1)
                return {
                    "definition": parts[0],
                    "usage": parts[1] if len(parts) > 1 else "No usage example found."
                }
            return {"error": "Empty response"}
        except Exception as e:
            return {"error": str(e)}
