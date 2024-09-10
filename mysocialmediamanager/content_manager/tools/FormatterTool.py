from crewai import Agent, Task
from langchain.tools import tool

class FormatterTool:
    @tool("Format content for Medium")
    def format_for_medium(text):
        """Applies Medium-specific formatting to enhance readability and presentation."""
        # Apply header formatting
        lines = text.split('\n')
        formatted_lines = []
        for line in lines:
            if line.strip() and line[0].isdigit():
                # Assuming lines starting with digits might be headers
                formatted_line = f"<h2>{line}</h2>"
            elif line.strip() and len(line.split()) <= 3:
                # Short lines can be subheaders
                formatted_line = f"<h3>{line}</h3>"
            else:
                # Apply paragraph formatting
                formatted_line = f"<p>{line}</p>"
            formatted_lines.append(formatted_line)

        # Join all lines back into a single string
        formatted_text = '\n'.join(formatted_lines)

        # Enhance with bold tags for emphasis
        words = formatted_text.split()
        enhanced_words = [f"<strong>{word}</strong>" if word.lower() in ['important', 'key', 'note'] else word for word in words]
        enhanced_text = ' '.join(enhanced_words)

        return enhanced_text

# # Example of how to use the FormatterTool
# if __name__ == "__main__":
#     formatter_tool = FormatterTool()
#     text = "1. Introduction to Formatting\nThis section covers the basics of HTML formatting.\nKey considerations include readability and visual appeal.\n3. Summary\nEnsure to apply consistent styles."
#     formatted_content = formatter_tool.format_for_medium(text)
#     print("Formatted Content for Medium:\n", formatted_content)
