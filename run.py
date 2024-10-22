from repl import run_demo_loop
from src import triage_agent

# context_variables = {
#     "tasks": """Here is the collection of the user's task:
# id,title,description,due_date,status
# 1. Finish project report,Complete the final section and submit to the client.,April 30th,Todo
# """
# }

if __name__ == "__main__":
    run_demo_loop(triage_agent) #, context_variables=context_variables)