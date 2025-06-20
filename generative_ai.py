import requests

class GenerativeAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"

    def get_slang_details(self, slang):
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"Define the slang term '{slang}' and use it in a sentence."
                        }
                    ]
                }
            ]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            result = response.json()

            if response.status_code != 200:
                return {"error": f"{response.status_code} - {result.get('error', {}).get('message', 'Unknown error')}"}

            if "candidates" in result and len(result["candidates"]) > 0:
                text = result["candidates"][0]["content"]["parts"][0]["text"]
                parts = text.split('\n', 1)
                definition = parts[0].strip()
                usage = parts[1].strip() if len(parts) > 1 else "No usage example found."

                return {
                    "definition": definition,
                    "usage": usage
                }
            else:
                return {"error": "No candidates returned by the model."}

        except Exception as e:
            return {"error": str(e)}
