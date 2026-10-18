class Node:
    def __init__(self, task_name):
        self.task_name = task_name
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, task_name):
        new_task = Node(task_name)
        if not self.head:
            self.head = new_task
        else:
            current_task = self.head
            while current_task.next:
                current_task = current_task.next
            current_task.next = new_task
    def display_tasks(self):
        current_task = self.head
        if not current_task:
            print("NO tasks available!")
        else:
            while current_task:
                print(current_task.task_name)
                current_task = current_task.next
    def complete_task(self, task_name):

        if not self.head: # check if the list is empty
            print("No tasks to complete.")
            return
        if self.head.task_name == task_name: # check if head node matches "Study Python"
            self.head = self.head.next # "Finish homework" == "Study Python" is False, so it moves
            print(f"Task completed: {task_name}")
            return
        current = self.head # starts with "Finish homework"
        while current.next and current.next.task_name is not task_name: # "Finish homework".next (is "Study Python")
            # and its task_name is "Study Python" != "Study Python" is false
            current = current.next
        if current.next: # Verifies that the target node was actually found in the list (True).
            current.next = current.next.next #Unlinks "Study Python" by connecting "Finish homework" (current)
            # directly to "Review notes" (current.next.next).
            print(f"Task completed: {task_name}")
        else:
            print(f"Task not found: {task_name}")

    def count_tasks(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        print(f"Total tasks: {count}")
        return count

task_manager = TaskManager()
print("===Task Manager====")
task_manager.add_task("Finish homework")
task_manager.add_task("Study Python")
task_manager.add_task("Review notes")
task_manager.add_task("Practice linked lists")
task_manager.display_tasks()
print(" ")
task_manager.count_tasks()
print(" ")
task_manager.complete_task("Review notes")
task_manager.complete_task("Practice linked lists")
task_manager.complete_task("Finish homework")
task_manager.complete_task("Study Python")
task_manager.complete_task("Review notes")