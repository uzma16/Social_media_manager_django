from textwrap import dedent
from crewai import Task


class ContentTasks():
    def generate_blog_post_task(self, agent, topics, keywords):
        return Task(
            description=dedent(f"""
                Create a comprehensive, engaging, and SEO-optimized blog post for Medium. 
                The content should be well-researched, incorporating the latest insights and data relevant to the chosen topic. 
                The article must engage Medium readers by providing valuable information and compelling narratives that connect with their interests.
                
                Ensure the content follows SEO best practices to enhance its visibility and reach on the platform. 
                The final blog post should be well-formatted according to Medium’s guidelines, making it accessible and attractive to readers.
                
                Topic of Interest: {topics}
                Key SEO Keywords: {keywords}
                Note: Utilize the tools provided for NLP generation, SEO optimization, and formatting to ensure the highest quality of content.
            """),
            agent=agent,
            expected_output='A fully researched, engaging, SEO-optimized, and well-formatted blog post ready for publication on Medium, adhering to all specified guidelines and incorporating the provided topics and keywords.'
        )


    def edit_and_quality_assure_blog_post_task(self, agent, content):
        return Task(
            description=dedent(f"""
                Review and edit the provided blog post to ensure it meets the highest editorial standards before publication. 
                The task involves meticulously checking the content for grammatical accuracy, stylistic coherence, and overall compliance 
                with editorial guidelines. Enhance the clarity, engagement level, and presentation of the post, making sure it aligns 
                with the publication's style and voice.
                
                Perform detailed grammatical checks to correct any errors, apply stylistic improvements to make the content more engaging, 
                and ensure that all information adheres to required compliance standards, including brand alignment and legal requirements.
                
                Provided Content: {content}
                Note: Utilize the provided tools for grammar checking, style enhancement, and compliance verification to achieve 
                the best quality content.
            """),
            agent=agent,
            expected_output='A professionally edited blog post that is grammatically correct, stylistically coherent, fully compliant with editorial guidelines, and perfectly aligned with the publication’s style and voice. Ready for publication on Medium.'
        )
    

    def create_and_optimize_images_task(self,agent, keywords):
        return Task(
            description=dedent(f"""
                Generate visually appealing and relevant images based on the specified keywords or themes: {keywords}. 
                This task involves using advanced AI-driven graphic design tools to create compelling images for articles, 
                social media posts, and advertisements.

                The images should not only capture the essence of the given keywords but also be optimized for web and social media use,
                ensuring they are of the right size and quality for different platforms. After image creation, use optimization tools
                to enhance image quality without compromising loading times or visual integrity.

                Finally, format the images to meet specific social media standards, making sure that each image fits the dimensions and 
                resolution requirements of platforms like Instagram, Facebook, Twitter, etc.

                Provided Keywords: {keywords}
                Note: Utilize the tools for image creation, optimization, and formatting to ensure the images are high-quality and platform-ready.
            """),
            agent=agent,  # Pass the instantiated Agent object
            expected_output='A set of high-quality, optimized, and well-formatted images that are ready to be published on various digital marketing channels.'
        )


    # def manage_publication_task(self, agent, content, publish_date, tags, interaction_message):
    #     return Task(
    #         description=dedent(f"""
    #             Manage the entire publication process for an upcoming blog post on Medium. This task involves scheduling the post for publication at the optimal time, updating the post's tags to maximize SEO and reader engagement, and interacting with followers to enhance community involvement.

    #             First, schedule the post to go live at the specified time: {publish_date}. Next, update the post tags to include relevant keywords that improve searchability and relevance: {tags}. Finally, engage with the platform's audience by responding to comments or posting updates that encourage reader interaction.

    #             Provided Content for Publication: {content[:500]}... (truncated for brevity)
    #             Expected Deliverables:
    #                 - A blog post scheduled and tagged correctly.
    #                 - Successful interactions with followers post-publication, aiming to foster a vibrant and engaged community.
    #             Note: Use the equipped tools to ensure accurate scheduling, effective tagging, and engaging interactions. Each step should be documented and reported back for verification.
    #         """),
    #         agent=agent)
