from .db import Session, initialize, Task
DATABASE_URL = 'sqlite:///database.db' # local database
session: Session = initialize(db_url=DATABASE_URL)

from . import crud
from .tools import (
    transfer_to_task_creation_agent,
    transfer_to_task_view_agent,
    transfer_to_task_update_agent,
    create_task,
    view_tasks,
    update_task,
)
from .prompts import (
    TASK_CREATION_INSTRUCTIONS,
    TASK_VIEW_INSTRUCTIONS,
    TASK_UPDATE_INSTRUCTIONS,
    triage_instructions
)
from .agents import triage_agent
