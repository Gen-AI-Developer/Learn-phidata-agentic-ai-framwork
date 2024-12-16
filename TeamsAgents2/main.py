from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
load_dotenv()
if __name__ == '__main__':
    agent = Agent(
        # model=Groq(id='llama-3.3-70b-versatile'),
        model=OpenAIChat(id="gpt-3.5-turbo"),
        # model=OpenAIChat(id="gpt-4"),
        # model=OpenAIChat(id="gpt-4o"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True)],
        show_tool_calls=True,
        instructions=['use tables to display data..',
                      'if you dont know the company symbol, please use get_compony_symbol tool. even if it is not a public company'],
        markdown=True
                  )
    agent.print_response('Summarize and compare analyst recommendation and fundamentals for TSLA and Phidata ')