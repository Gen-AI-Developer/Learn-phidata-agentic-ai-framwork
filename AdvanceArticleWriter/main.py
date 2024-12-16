from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k

# Load environment variables
load_dotenv()

# SEO Rules (for potential integration later)
seo_friendly_rules = [
    "Identify relevant keywords and phrases through keyword research using tools like Google Keyword Planner, SEMrush, or Ahrefs.",
    "Optimize the title and meta description by including target keywords and keeping the title under 60 characters and the meta description under 160 characters.",
    "Organize content using headings (H1 for the main title, H2 for subheadings) to enhance readability and structure.",
    "Incorporate keywords naturally into the content, especially in the first 100 words, headers, and throughout the article, avoiding keyword stuffing.",
    "Write engaging and valuable content that provides real value and thoroughly answers user queries.",
    "Optimize readability by using short paragraphs, bullet points, and clear formatting to improve user experience.",
    "Include internal and external links to relevant pages and authoritative sources to boost SEO and credibility.",
    "Add optimized images with descriptive filenames and alt text containing relevant keywords.",
    "Ensure the website and articles are mobile-friendly to comply with Google's mobile-first indexing.",
    "Improve page load speed by optimizing images, leveraging browser caching, and minifying code."
]

# Define WebAgent
WebAgent = Agent(
    name='Web Agent',
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

# Define NewspaperAgent
NewspaperAgent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[Newspaper4k()],
    description="Processes news articles.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Read each URL and extract the article text. If unavailable, skip.",
        "Prepare an NYT-worthy article based on the information."
    ],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True
)

# Define AgentTeam
AgentTeam = Agent(
    team=[WebAgent, NewspaperAgent],
    model=Groq(id='llama-3.3-70b-versatile'),
    instructions=["Write an article on the given topic using gathered data."]+seo_friendly_rules,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

# Main execution
if __name__ == '__main__':
    try:
        print("Generating article...")
        AgentTeam.print_response('Write an article on Pet Care', stream=True)
    except Exception as e:
        print(f"Error: {e}")
