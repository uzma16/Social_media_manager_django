from crewai import Crew
from textwrap import dedent
from .agents import ContentAgents
from .tasks import ContentTasks

from dotenv import load_dotenv
load_dotenv()

def save_to_html(blog_content, image_url):
        html_template = f"""
        <html>
        <head>
            <title>Blog Post and Image</title>
        </head>
        <body>
            <h1>Blog Post Content</h1>
            {blog_content}
            <h2>Generated Image</h2>
            <img src="{image_url}" alt="Generated Image" style="width:100%;height:auto;">
        </body>
        </html>
        """

        # Specify the filename
        filename = 'output.html'

        # Writing the HTML contents to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_template)

        print(f"File saved successfully as {filename}")
        
class ContentCrew:
    def __init__(self, topics, keywords):
        self.topics = topics
        self.keywords = keywords
        # self.platform = platform

    def run(self):
        agents = ContentAgents()
        tasks = ContentTasks()

        # Initialize agents
        content_creation_agent = agents.content_creation_agent()
        editing_quality_assurance_agent = agents.editing_quality_assurance_agent()
        # image_generator_agent = agents.image_generator_agent()
        # publication_management_agent = agents.publication_management_agent()

        # Define tasks
        generate_task = tasks.generate_blog_post_task(
            content_creation_agent,
            self.topics,
            self.keywords
        )
        edit_task = tasks.edit_and_quality_assure_blog_post_task(
            editing_quality_assurance_agent,
            generate_task.execute()  # Assuming execute returns the generated content
        )
        # image_task = tasks.create_and_optimize_images_task(
        #     image_generator_agent,
        #     self.keywords
        # )
        # publish_task = tasks.manage_publication_task(
        #     publication_management_agent,
        #     edit_task.execute(),  # Assuming execute returns the edited content
        #     "2024-01-01",  # Example publish date
        #     ["SEO", "Technology"],  # Example tags
        #     "Engage with the audience!"  # Example interaction message
        # )

        # Create and run the crew
        crew = Crew(
            agents=[
                content_creation_agent,
                editing_quality_assurance_agent,
                # image_generator_agent
                # publication_management_agent
            ],
            tasks=[generate_task, edit_task],
            # tasks=[generate_task, edit_task, publish_task],
            verbose=True
        )

        result = crew.kickoff()
        return result

class ImageCrew:
    def __init__(self, topics, keywords):
        self.topics = topics
        self.keywords = keywords

    def run(self):
        agents = ContentAgents()
        tasks = ContentTasks()   

        image_generator_agent = agents.image_generator_agent() 

        image_task = tasks.create_and_optimize_images_task(
            image_generator_agent,
            self.keywords
        )

        crew = Crew(
            agents=[
                image_generator_agent
                # publication_management_agent
            ],
            tasks=[image_task],
            # tasks=[generate_task, edit_task, publish_task],
            verbose=True
        )

        result1 = crew.kickoff()
        return result1

def main(topics,keywords):
# if __name__ == "__main__":
#     print("## Welcome to the Medium Content Creator Project")
#     print('-----------------------------------------------')
#     topics = input(
#         dedent("""
#             What topics are you interested in writing about?
#         """))
#     keywords = input(
#         dedent("""
#             Please enter some keywords for SEO optimization:
#         """))
#     platform = input(
#         dedent("""
#             Please provide  the name of platform:
#         """))

    content_crew = ContentCrew(topics, keywords)
    image_crew = ImageCrew(topics, keywords)
    result = content_crew.run()
    result1 =  image_crew.run()
    print("\n\n########################")
    print("## Here is your Blog Post Publication Result")
    print("########################\n")
    print(result)
    print(result1)
    save_to_html(result,result1)
    return result,result1

    


 