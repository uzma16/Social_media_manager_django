from crewai import Agent
from langchain.llms import OpenAI
from .tools.NLPTool import NLPTool
from .tools.SEOTool import SEOTool
from .tools.FormatterTool import FormatterTool
# from tools.GrammarCheckTool import GrammarCheckTool
# from tools.StyleTool import StyleTool
# from tools.ComplianceTool import ComplianceTool
# from tools.TagManagerTool import TagManagerTool
# from tools.InteractionTool import InteractionTool
from .tools.ImageCreationTool import ImageCreationTool


class ContentAgents():
    def content_creation_agent(self):
        return Agent(
            role='Content Generator',
            goal='Generate high-quality, engaging, and SEO-optimized blog posts for Medium based on specified topics or keywords.',
            backstory=
            '''As a Content Creation Agent, I am designed to assist bloggers and content creators by automating the process of writing. 
            Leveraging advanced AI capabilities, I synthesize information from various sources to produce coherent, insightful,
            and engaging articles that resonate with readers and adhere to SEO best practices.''',
            tools=[
                NLPTool.generate_text,
                SEOTool.optimize,
                FormatterTool.format_for_medium
            ],
            verbose=True)

    def editing_quality_assurance_agent(self):
        return Agent(
            role='Editor and Quality Assurer',
            goal='Review generated content for quality, coherence, and compliance with editorial guidelines.',
            backstory=
            '''As an Editing and Quality Assurance Agent, I am tasked with ensuring that all content meets high editorial
            standards before publication. Using a combination of AI-driven tools and meticulous attention to detail, 
            I edit content, correct grammatical errors, and ensure that each post is clear, coherent, and beautifully presented, 
            aligning with the publication’s style.''',
            tools=[
                # GrammarCheckTool.check_grammar,
                # StyleTool.apply_style,
                # ComplianceTool.ensure_compliance
            ],
            verbose=True)
    
    def image_generator_agent(self):
        return Agent(
            role='Image Generator',
            goal='Generate visually appealing and relevant images based on specified keywords or themes for digital content creation.',
            backstory=
            '''As an Image Generator Agent, I am equipped with advanced AI-driven graphic design capabilities that enable me to create 
            compelling images for articles, social media, and advertisements. I understand the importance of visual content in digital marketing 
            and strive to produce images that are not only beautiful but also perfectly tailored to enhance the associated written content and 
            boost audience engagement.''',
            tools=[
                ImageCreationTool.create_image,  # A hypothetical tool to generate images based on text
                # ImageOptimizer.optimize,         # Another hypothetical tool for optimizing image size and quality
                # ImageFormatter.format_for_social_media  # A tool to format images according to social media standards
            ],
            verbose=True)


    # def publication_management_agent(self):
    #     return Agent(
    #         role='Publication Manager',
    #         goal='Handle the publication process on Medium, including scheduling posts, managing tags, and interacting with followers.',
    #         backstory=
    #         '''As a Publication Management Agent, I am responsible for ensuring that blog posts are published on schedule 
    #         and reach the intended audience effectively. My role includes scheduling content, tagging it appropriately for 
    #         SEO and audience reach, and maintaining active engagement with followers to foster a vibrant community around the content.''',
    #         tools=[
    #             # SchedulerTool(),
    #             TagManagerTool.update_tags,
    #             InteractionTool.interact
    #         ],
    #         verbose=True)

