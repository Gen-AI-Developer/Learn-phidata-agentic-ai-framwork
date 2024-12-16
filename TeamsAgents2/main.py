from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
load_dotenv()

WebAgent = Agent(
        name='Web Agent',
        model=Groq(id='llama-3.3-70b-versatile'),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True

    )
FinanceAgent = Agent(
        name="Finance Agent",
        model=Groq(id='llama-3.3-70b-versatile'),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True)],
        show_tool_calls=True,
        instructions=['use tables to display data..',
                      'if you dont know the company symbol, please use get_compony_symbol tool. even if it is not a public company'],
        markdown=True
                  )
AgentTeam = Agent(
        team=[WebAgent,FinanceAgent],
        model=Groq(id='llama-3.3-70b-versatile'),
        instructions=["Always include source","Use tables to display data"],
        show_tool_calls=True,
        markdown=True
    )
if __name__ == '__main__':
    AgentTeam.print_response('Summarize analyst recommendation and share the latest news for TSLA ', stream=True)