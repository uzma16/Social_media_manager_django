import os
import json
import requests
from crewai import Agent, Task
from langchain.tools import tool

class ImageCreationTool:
    @tool("Generate image from description")
    def create_image(description):
        """Generates an image based on the given description using an AI model."""
        api_key = "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"  # This should be securely stored and accessed
        endpoint = "https://api.openai.com/v1/images/generations"  # Endpoint for DALL-E image generation

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        data = {
            "model": "dall-e-2",  # Assuming the use of DALL-E 2
            "prompt": description,
            "n": 1,  # Number of images to generate
            "size": "1024x1024"  # Size of the generated images
        }

        response = requests.post(endpoint, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            # Parse the JSON response to extract the image data
            image_url = response.json()['data'][0]['url']  # Path to extract the image URL might vary
            return image_url
        else:
            # Handle errors or unsuccessful requests
            error_message = response.json().get('error', {}).get('message', 'Failed to generate image')
            raise Exception(f"Image creation failed with response: {error_message}")


# # Example usage of the tool
# nlp_tool = ImageCreationTool()
# try:
#     print(nlp_tool.create_image("Artificial Intelligence"))
# except Exception as e:
#     print(e)