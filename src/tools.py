import logging
from typing import Dict, List
from . import crud

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transfer_to_task_creation_agent(*args, **kwargs):
    from .agents import task_creation_agent
    return task_creation_agent

def transfer_to_task_view_agent(*args, **kwargs):
    from .agents import task_view_agent
    return task_view_agent

def transfer_to_task_update_agent(*args, **kwargs):
    from .agents import task_update_agent
    return task_update_agent

def create_task(title: str, description: str, due_date: str) -> Dict:
    """Create a new task with the provided information."""
    logger.info(f"Creating new task: {title}")
    crud.create_task(title=title, description=description, due_date=due_date)
    return {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "Todo"
    }

def view_tasks() -> str:
    """Display the list of tasks."""
    logger.info("Viewing tasks")
    tasks = crud.get_all_tasks()
    task_list = "\n".join(
        f"- [{task.status}] {task.title} (Due: {task.due_date})"
        for task in tasks
    )
    return task_list

def update_task(task_index: int, new_status: str) -> str:
    """Update the status of a task."""
    logger.info(f"Updating task at index {task_index}")
    crud.update_task(task_id=task_index, status=new_status)
    tasks = crud.get_all_tasks()
    task_list = "\n".join(
        f"- [{task.status}] {task.title} (Due: {task.due_date})"
        for task in tasks
    )
    return task_list

