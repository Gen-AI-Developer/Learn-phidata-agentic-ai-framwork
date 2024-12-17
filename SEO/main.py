from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
# Load environment variables
load_dotenv()
seo_agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="An agent that performs keyword research and generates SEO-friendly articles.",
    instructions=[
        "1. Perform keyword research to identify relevant keywords and phrases.",
        "2. Search for the top 5 links related to the topic.",
        "3. Extract and analyze content from these links.",
        "4. Generate a comprehensive, SEO-optimized article adhering to best practices.",
        "5. Ensure the article includes optimized titles, meta descriptions, headings, keyword placement, internal and external links, and images with alt text.",
    ],
    show_tool_calls=True,
    markdown=True,
)
if __name__ == '__main__':
    topic = "costco pizza nutrition facts"
    seo_agent.print_response(topic, stream=True)