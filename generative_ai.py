import google.generativeai as palm

class GenerativeAI:
    def __init__(self, api_key):
        palm.configure(api_key=api_key)
        self.model = palm.GenerativeModel("models/gemini-pro")

    def get_slang_details(self, slang):
        try:
            prompt = f"Define the slang term '{slang}' and use it in a sentence."
            response = self.model.generate_content(prompt)
            text = response.text
            result_parts = text.split('\n', 1)
            definition = result_parts[0] if len(result_parts) > 0 else "No definition found."
            usage = result_parts[1] if len(result_parts) > 1 else "No usage example found."
            return {
                "definition": definition,
                "usage": usage
            }
        except Exception as e:
            return {"error": str(e)}
