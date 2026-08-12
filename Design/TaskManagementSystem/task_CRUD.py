from datetime import datetime, timedelta
from copy import deepcopy

class taskAction:

    tasks = []
    def __init__(self, task_id, title, description,date_created, priority, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = date_created + timedelta(days=7)
        self.date_created = date_created
        self.priority = priority
        self.status = status
        self.task_history = []
        '''so admin_assign is the dict of dict, so we can update the values of the dict by using the key of the dict which is the user'''
        self.admin_assign = {}
        self.admin_assign_history = {}

    def __repr__(self):
        return f"Task(id={self.task_id}, title='{self.title}', status='{self.status}', priority='{self.priority}')"

    def create_action(self, task):
        self.task_history.append(("create", task))
        taskAction.tasks.append(task)
        print(f"Creating action for task: {task}")

    def update_action(self, task):
        print(f"Updating action for task: {task}")
        for i in range(len(taskAction.tasks)):
            if taskAction.tasks[i] == task:
                taskAction.tasks[i] = task
                self.task_history.append(("update", task))
                print(f"Task updated: {task}")
                return
        print(f"Task not found: {task}")

    def delete_action(self, task):
        if task in taskAction.tasks:
            taskAction.tasks.remove(task)
            self.task_history.append(("delete", task))
            print(f"Task deleted: {task}")
        else:
            print(f"Task not found: {task}")

    def get_task_list(self):
        return taskAction.tasks

# grouping the task and user together for assignment

    def admin_assign_task_to_user(self, title, desc, user, date_assigned):
        if user not in self.admin_assign:
            self.admin_assign[user] = {
                "description": desc,
                "title": title,
                "date_assigned": date_assigned
            }

            # initialize history list
            if user not in self.admin_assign_history:
                self.admin_assign_history[user] = []

            self.admin_assign_history[user].append({
                "action": "assigned",
                "data": deepcopy(self.admin_assign[user])
            })

        else:
            print(f"Task already assigned to user: {user}")

    def admin_unassign_task_to_user(self, user):
        if user in self.admin_assign:

            old_data = deepcopy(self.admin_assign[user])

            del self.admin_assign[user]

            self.admin_assign_history[user].append({
                "action": "deleted",
                "old": old_data
            })

        else:
            print(f"Task not found for user: {user}")

    def admin_updated_task_to_user(self, user, title, desc, date_assigned):
        
        if user in self.admin_assign:

            # store OLD data before update
            old_data = deepcopy(self.admin_assign[user])

            self.admin_assign[user] = {
                "description": desc,
                "title": title,
                "date_assigned": date_assigned
            }

            self.admin_assign_history[user].append({
                "action": "updated",
                "old": old_data,
                "new": deepcopy(self.admin_assign[user])
            })

        else:
            print(f"Task not found for user: {user}")

# filtering the task based on status, priority and task name

    def filter_tasks_by_status(self, status):
        result = []
        for task in taskAction.tasks:
            if task.status == status:
                result.append(task)
        return result


    def filter_tasks_by_priority(self, priority):
        result = []
        for task in taskAction.tasks:
            if task.priority == priority:
                result.append(task)
        return result


    def filter_tasks_by_task(self, target_task):
        for t in taskAction.tasks:
            if t.task_id == target_task.task_id:
                return t
        return None

    def show_task_details(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print(f"Date Created: {self.date_created}")