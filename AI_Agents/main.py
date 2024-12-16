from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()
if __name__ == '__main__':
    agent = Agent(model=Groq(id='llama-3.3-70b-versatile'))
    agent.print_response('What is different between Good and Bad  in 2 sentences')