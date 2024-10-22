
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional

def commit(session: Session) -> None:
    try:
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print(f"Database integrity error: {e.orig}")
        # raise RuntimeError(f"Database integrity error: {e.orig}") from e


def create_task(title: str, description: str, due_date: str) -> None:
    new_task = Task(title=title, description=description, due_date=due_date)
    session.add(new_task)
    commit(session)
    print(f"Task created: {new_task}")


def get_all_tasks() -> List["Task"]:
    tasks = session.query(Task).all()
    return tasks


def update_task(
    task_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    status: Optional[str] = None,
) -> None:  # bool
    task: Task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return print(f"Task with id {task_id} not found.")
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if due_date is not None:
        task.due_date = due_date
    if status is not None:
        task.status = status
    commit(session)
    print(f"Task updated: {task}")


def delete_task(task_id) -> None:  # bool
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return print(f"Task with id {task_id} not found.")
    session.delete(task)
    commit(session)
    print(f"Task deleted: {task}")
    
from . import session, Task

# if __name__ == "__main__":
#     # make a new task
#     create_task("Finish homework", "Complete math and science assignments", "2024-10-30")

#     # list all tasks
#     tasks = get_all_tasks()
#     print("All tasks:", tasks)

#     # update task
#     if tasks:  # Check if there are any tasks to update
#         update_task(tasks[0].id, status='In Progress')

#     # del task
#     if tasks:  # check if there are any tasks to delete
#         delete_task(tasks[0].id)
