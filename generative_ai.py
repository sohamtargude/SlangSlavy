import google.generativeai as palm

class GenerativeAI:
    def __init__(self, api_key):
        self.api_key = api_key
        palm.configure(api_key=api_key)

    def get_slang_details(self, slang):
        try:
            prompt = f"Define the slang term '{slang}' and use it in a sentence."
            response = palm.generate_text(prompt=prompt)
            if response and hasattr(response, 'result'):
                text = response.result
                result_parts = text.split('\n', 1)
                definition = result_parts[0] if len(result_parts) > 0 else "No definition found."
                usage = result_parts[1] if len(result_parts) > 1 else "No usage example found."
                return {
                    "definition": definition,
                    "usage": usage
                }
            else:
                return {"error": "Invalid response from API"}
        except Exception as e:
            return {"error": str(e)}
