import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool

class StyleTool:
    @tool("Apply style guidelines")
    def apply_style(text):
        """Applies style guidelines to text to enhance readability and engagement."""
        api_key = os.environ.get('STYLE_API_KEY')  # Ensure your API key is stored in environment variables
        url = "https://api.stylecheck.com/apply"  # Placeholder API endpoint

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "text": text,
            "preferences": {  # These preferences should be defined according to the API's capabilities
                "max_sentence_length": 20,
                "avoid_passive_voice": True,
                "enhance_readability": True
            }
        })

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            styled_text = response.json().get('styled_text', text)  # Default to original text if no styled text is provided
            return styled_text
        else:
            error_message = response.json().get('message', 'Failed to apply style guidelines')
            raise Exception(f"Style application failed with error: {error_message}")

# # Example usage
# if __name__ == "__main__":
#     style_tool = StyleTool()
#     text_to_style = "This is a simple text that might have some issues with readability, which can be improved by applying certain style guidelines."
#     try:
#         styled_text = style_tool.apply_style(text_to_style)
#         print("Styled Text:\n", styled_text)
#     except Exception as e:
#         print(str(e))
