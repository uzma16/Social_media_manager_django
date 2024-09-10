from crewai import Agent, Task
from langchain.tools import tool
import random

class InteractionTool:
    @tool("Interact with followers")
    def interact(self, interaction_type, message):
        """Facilitates interactions with followers based on the specified interaction type and message content."""
        # Detailed simulation of interaction outcomes
        print(f"Executing interaction of type '{interaction_type}' with message: {message}")
        
        # Simulate responses based on interaction type
        if interaction_type.lower() == "comment response":
            response = self.handle_comment_response(message)
        elif interaction_type.lower() == "status update":
            response = self.handle_status_update(message)
        elif interaction_type.lower() == "direct message":
            response = self.handle_direct_message(message)
        else:
            response = "Unknown interaction type"

        # Simulate a successful interaction operation
        interaction_result = {
            "type": interaction_type,
            "original_message": message,
            "response": response,
            "status": "Interaction Successful"
        }
        
        return interaction_result

    def handle_comment_response(self, message):
        # Simulate responding to a comment based on message sentiment
        sentiments = ['positive', 'neutral', 'negative']
        sentiment = random.choice(sentiments)
        if sentiment == 'positive':
            return f"Thanks for your kind words! {message}"
        elif sentiment == 'neutral':
            return "Thank you for your feedback."
        else:
            return "We're sorry you feel this way and appreciate your honest feedback."

    def handle_status_update(self, message):
        # Simulate posting a status update
        return f"Update posted successfully: {message}"

    def handle_direct_message(self, message):
        # Simulate sending a direct message
        return "Message sent to user: " + message

# Example usage
if __name__ == "__main__":
    interaction_tool = InteractionTool()
    interaction_types = ["Comment Response", "Status Update", "Direct Message"]
    messages = [
        "Really enjoyed this article!",
        "Here's an important update for everyone.",
        "Could you provide more information on your services?"
    ]

    for interaction_type, message in zip(interaction_types, messages):
        interaction_result = interaction_tool.interact(interaction_type, message)
        print("Interaction Result:", interaction_result)
