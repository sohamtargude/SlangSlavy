import google.generativeai as genai

class GenerativeAI:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=api_key)

    def get_slang_details(self, slang):
        try:
            model = genai.GenerativeModel(model_name="gemini-pro")  # ✅ Valid model for Gemini
            prompt = f"Define the slang term '{slang}' and use it in a sentence."
            response = model.generate_content(prompt)

            if hasattr(response, 'text'):
                text = response.text
                result_parts = text.strip().split('\n', 1)
                definition = result_parts[0] if len(result_parts) > 0 else "No definition found."
                usage = result_parts[1] if len(result_parts) > 1 else "No usage example found."
                return {
                    "definition": definition,
                    "usage": usage
                }
            else:
                return {"error": "Empty response from model"}
        except Exception as e:
            return {"error": str(e)}
