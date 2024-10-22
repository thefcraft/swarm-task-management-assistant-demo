# Swarm Task Management Assistant Demo

This is a demo project showcasing the use of the Swarm framework for creating a multi-agent system for task management. Swarm is an experimental, educational framework for exploring ergonomic, lightweight multi-agent orchestration.

## Note:
just an basic demo due to api constraints as it requires function calling which is most open source llm lacks 

## About Swarm

Swarm is a Python-based framework that allows you to create and orchestrate a network of agents, each with their own instructions and capabilities. It is designed to be lightweight, scalable, and highly customizable, making it a great tool for exploring the patterns and principles of multi-agent systems.

## About this Demo

This demo project demonstrates how you can use Swarm to build a simple task management assistant with the following functionalities:

1. **Task Creation**: Users can create new tasks with a title, description, and due date.
2. **Task Viewing**: Users can view the current list of tasks, including their status and due dates.
3. **Task Updating**: Users can update the status of a task (e.g., mark a task as "In Progress" or "Completed").

However, this is just a demo and not a fully working application. The purpose of this project is to showcase the Swarm framework and its capabilities, rather than to provide a production-ready task management solution.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/swarm-task-management-demo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd swarm-task-management-demo
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set the necessary environment variables:

   ```bash
   OPENAI_API_KEY="ITS_CLOSED_AI"
   ```

   Replace `"ITS_CLOSED_AI"` with your actual OpenAI API key in .env file.

## Usage

To start the Swarm task management demo, run the following command:

```bash
python run.py
```

This will start the Swarm demo loop, and you can interact with the assistant through the command-line interface.

## Disclaimer

This is a demo project and is not intended for production use. The Swarm framework is currently in an experimental stage and is primarily for educational purposes. There is no official support or maintenance for this project.

## Contributing

Since this is a demo project, I am not accepting contributions or reviewing issues. However, you are welcome to explore and learn from the Swarm framework and this demo application.
