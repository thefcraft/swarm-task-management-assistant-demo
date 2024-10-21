from swarm import Swarm
from swarm.repl.repl import process_and_print_streaming_response, pretty_print_messages
from openai import OpenAI
import dotenv, os

dotenv.load_dotenv()


OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME") # 'llama3.2' | 'nemotron-mini' | 'mistral-nemo'
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

def run_demo_loop(
    starting_agent, context_variables=None, stream=False, debug=False
) -> None:
    llm = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)
    client = Swarm(client = llm)  
    print("Starting Swarm CLI 🐝")

    messages = []
    agent = starting_agent

    while True:
        user_input = input("\033[90mUser\033[0m: ")
        messages.append({"role": "user", "content": user_input})

        response = client.run(
            agent=agent,
            messages=messages,
            context_variables=context_variables or {},
            stream=stream,
            debug=debug,
            model_override=OPENAI_MODEL_NAME
        )

        if stream:
            response = process_and_print_streaming_response(response)
        else:
            pretty_print_messages(response.messages)

        messages.extend(response.messages)
        agent = response.agent
