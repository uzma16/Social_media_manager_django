
import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool

class GrammarCheckTool:
    @staticmethod
    @tool("Check grammar and style")
    def check_grammar(text):
        """Useful to check and correct grammatical errors in a text content."""
        api_key = os.environ.get('GRAMMAR_API_KEY')  # Ensure your API key is stored in environment variables
        url = "https://api.grammarcheck.com/check"  # Placeholder API endpoint

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "text": text,
            "language": "en"  # Assuming the API requires a language code
        })

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            corrections = response.json()  # Parsing response to get corrections
            corrected_text = GrammarCheckTool.apply_corrections(text, corrections)
            return corrected_text
        else:
            error_message = response.json().get('message', 'Failed to check grammar')
            raise Exception(f"Grammar check failed with error: {error_message}")

    @staticmethod
    def apply_corrections(original_text, corrections):
        """Applies corrections to the original text based on API response."""
        # This function assumes a simple replacement process. It should be adapted based on the actual structure of the API response.
        for correction in corrections.get('corrections', []):
            original_text = original_text.replace(correction['incorrect'], correction['correct'])

        return original_text
# # Example usage
# if __name__ == "__main__":
#     grammar_tool = GrammarCheckTool()
#     text_to_check = "Ths is a smple text with som erors."
#     try:
#         corrected_text = grammar_tool.check_grammar(text_to_check)
#         print("Corrected Text:\n", corrected_text)
#     except Exception as e:
#         print(str(e))
