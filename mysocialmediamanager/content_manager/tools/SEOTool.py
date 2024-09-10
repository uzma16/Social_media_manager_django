import re
from crewai import Agent, Task
from langchain.tools import tool

class SEOTool:
    @tool("Optimize text for SEO")
    def optimize(text, main_keyword, secondary_keywords=[]):
        """Optimizes provided text for SEO by enhancing keyword usage and improving readability."""
        # Ensure the main keyword is used adequately
        keyword_count = text.lower().count(main_keyword.lower())
        desired_keyword_count = (len(text.split()) // 100) + 1  # Roughly one keyword per 100 words

        if keyword_count < desired_keyword_count:
            # Append keywords if not enough
            text += (" " + main_keyword) * (desired_keyword_count - keyword_count)

        # Check and improve readability by shortening long sentences
        sentences = re.split(r'(?<=[.!?]) +', text)
        optimized_sentences = []
        for sentence in sentences:
            if len(sentence.split()) > 20:  # Simplify sentences longer than 20 words
                parts = re.split(r'[,;] +', sentence)
                simplified_parts = [' '.join(part.split()[:10]) + '...' for part in parts]
                optimized_sentences.append(' '.join(simplified_parts))
            else:
                optimized_sentences.append(sentence)

        optimized_text = ' '.join(optimized_sentences)

        # Ensure secondary keywords are included at least once
        for keyword in secondary_keywords:
            if keyword.lower() not in optimized_text.lower():
                optimized_text += f" {keyword}"

        return optimized_text

# # Example of how to use the SEOTool
# if __name__ == "__main__":
#     seo_tool = SEOTool()
#     text = "Wind turbines are a great source of renewable energy. They operate on a simple principle: the energy in the wind turns two or three propeller-like blades around a rotor."
#     main_keyword = "renewable energy"
#     secondary_keywords = ["sustainable power", "wind turbines"]
#     optimized_content = seo_tool.optimize(text, main_keyword, secondary_keywords)
#     print("SEO Optimized Content:\n", optimized_content)
