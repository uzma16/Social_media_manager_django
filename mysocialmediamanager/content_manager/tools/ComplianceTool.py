import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool

class ComplianceTool:
    @tool("Ensure compliance with editorial guidelines")
    def ensure_compliance(self, text):
        """Ensures text compliance with specific editorial guidelines or standards."""
        api_key = os.environ.get('COMPLIANCE_API_KEY')  # Ensure your API key is stored in environment variables
        url = "https://api.compliancecheck.com/verify"  # Placeholder API endpoint

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "text": text,
            "rules": ["brand_voice", "no_sensitive_language", "legal_compliance"]  # Example rules
        })

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            compliance_result = response.json().get('compliance', True)  # Assume True means compliant
            if compliance_result:
                return text  # Return text as is if compliant
            else:
                corrections = response.json().get('corrections', [])
                corrected_text = self.apply_corrections(text, corrections)
                return corrected_text
        else:
            error_message = response.json().get('message', 'Failed to ensure compliance')
            raise Exception(f"Compliance check failed with error: {error_message}")

    def apply_corrections(self, original_text, corrections):
        """Applies corrections to the original text based on compliance feedback."""
        # This function assumes that corrections are provided as a list of tuples (incorrect, correct)
        for incorrect, correct in corrections:
            original_text = original_text.replace(incorrect, correct)
        return original_text

# # Example usage
# if __name__ == "__main__":
#     compliance_tool = ComplianceTool()
#     text_to_check = "This is a simple text that needs to comply with our brand voice and avoid sensitive language."
#     try:
#         compliant_text = compliance_tool.ensure_compliance(text_to_check)
#         print("Compliant Text:\n", compliant_text)
#     except Exception as e:
#         print(str(e))
