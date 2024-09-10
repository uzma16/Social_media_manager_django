import os
import json
import requests
from crewai import Agent, Task
from langchain.tools import tool

class NLPTool:
    @tool("Generate text with AI")
    def generate_text(topic_keywords):
        """Generates text based on the given topic keywords using an updated AI chat model."""
        # api_key = os.environ.get('OPENAI_API_KEY')  # Ensure your API key is stored in environment variables
        api_key = "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"
        # print(api_key)
        endpoint = "https://api.openai.com/v1/chat/completions"  # Correct endpoint for chat models

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        # Update the model name and adjust parameters for the chat model
        data = {
            "model": "gpt-4-0613",  # Specify your chat model here
            "messages": [{"role": "user", "content": f"Write an insightful and detailed blog post about {topic_keywords}. Include key points, relevant data, and practical advice."}],
            "max_tokens": 500,
            "temperature": 0.7,
            "top_p": 1.0,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.0
        }

        # Send the request to OpenAI's API
        response = requests.post(endpoint, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            # Parse the JSON response from the API
            generated_text = response.json()['choices'][0]['message']['content'].strip()  # Adjusted for chat completions format
            return generated_text
        else:
            # Handle errors or unsuccessful requests
            error_message = response.json().get('error', {}).get('message', 'Failed to generate text')
            raise Exception(f"API request failed with response: {error_message}")

# Example usage of the tool
# nlp_tool = NLPTool()
# try:
#     print(nlp_tool.generate_text("sustainable energy solutions"))
# except Exception as e:
#     print(e)


    # def generate_text(topic_keywords):
    #     """Generates text based on the given topic keywords using an AI language model."""
    #     api_key = os.environ.get('OPENAI_API_KEY')  # Make sure to set your OpenAI API key in your environment variables
    #     endpoint = "https://api.openai.com/v1/engines/davinci/completions"

    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {api_key}'
    #     }
        
    #     # Construct the data payload with the prompt and parameters for generation
    #     data = {
    #         "prompt": f"Write an insightful and detailed blog post about {topic_keywords}. Include key points, relevant data, and practical advice:",
    #         "max_tokens": 500,
    #         "temperature": 0.7,
    #         "top_p": 1.0,
    #         "frequency_penalty": 0.5,
    #         "presence_penalty": 0.0,
    #         "stop": ["\n"]
    #     }

    #     # Send the request to OpenAI's API
    #     response = requests.post(endpoint, headers=headers, data=json.dumps(data))
        
    #     if response.status_code == 200:
    #         # Parse the JSON response from the API
    #         generated_text = response.json()['choices'][0]['text'].strip()
    #         return generated_text
    #     else:
    #         # Handle errors or unsuccessful requests
    #         error_message = response.json().get('error', {}).get('message', 'Failed to generate text')
    #         raise Exception(f"API request failed with response: {error_message}")

# # Example of how to use the NLPTool
# if __name__ == "__main__":
#     nlp_tool = NLPTool()
#     try:
#         generated_content = nlp_tool.generate_text("sustainable energy solutions")
#         print("Generated Content:\n", generated_content)
#     except Exception as e:
#         print(str(e))
