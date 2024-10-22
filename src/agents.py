from swarm import Swarm, Agent
import os
import dotenv

from . import (
    transfer_to_task_creation_agent,
    transfer_to_task_view_agent,
    transfer_to_task_update_agent,
    create_task,
    view_tasks,
    update_task,
)
from . import (
    TASK_CREATION_INSTRUCTIONS,
    TASK_VIEW_INSTRUCTIONS,
    TASK_UPDATE_INSTRUCTIONS,
    triage_instructions
)

dotenv.load_dotenv()

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")


triage_agent = Agent(
    name="Triage Agent",
    instructions=triage_instructions,
    model=os.getenv("OPENAI_MODEL_NAME"),
    functions=[transfer_to_task_creation_agent, transfer_to_task_update_agent, transfer_to_task_view_agent],
)

task_creation_agent = Agent(
    name="Task Creation Agent",
    instructions=TASK_CREATION_INSTRUCTIONS,
    model=os.getenv("OPENAI_MODEL_NAME"),
    functions=[create_task, transfer_to_task_view_agent]
)

task_view_agent = Agent(
    name="Task View Agent",
    instructions=TASK_VIEW_INSTRUCTIONS,
    model=os.getenv("OPENAI_MODEL_NAME"),
    functions=[view_tasks, transfer_to_task_update_agent]
)

task_update_agent = Agent(
    name="Task Update Agent",
    instructions=TASK_UPDATE_INSTRUCTIONS,
    model=os.getenv("OPENAI_MODEL_NAME"),
    functions=[update_task, transfer_to_task_view_agent]
)

