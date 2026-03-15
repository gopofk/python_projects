from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        completed_tasks = [t for t in self.tasks if t.completed]
        self.tasks = [t for t in self.tasks if not t.completed]

        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self) -> str:
        result = f"Section {self.name}:"

        for t in self.tasks:
            result += f"\n{t.details()}"

        return result
