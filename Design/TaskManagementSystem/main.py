from remind import Reminder
from task_CRUD import taskAction
from task_enum import Status, Priority
from datetime import date


class Main:

    def __init__(self):
        
        
        self.task_ob1 = taskAction(1, "Running", "Running in the park", date(2024, 6, 1), Priority.HIGH, Status.PENDING)
        self.task_ob2 = taskAction(2, "Swimming", "Swimming in the pool", date(2026, 4, 1), Priority.MEDIUM, Status.IN_PROGRESS)
        self.task_ob3 = taskAction(3, "Cycling", "Cycling in the park", date(2024, 7, 1), Priority.LOW, Status.COMPLETED)
        self.task_ob4 = taskAction(4, "Walking", "Walking in the park", date(2024, 6, 15), Priority.MEDIUM, Status.PENDING)

        self.task_list = [self.task_ob1, self.task_ob2, self.task_ob3, self.task_ob4]

        # create actions
        self.task_ob1.create_action(self.task_ob1)
        self.task_ob2.create_action(self.task_ob2)
        self.task_ob3.create_action(self.task_ob3)
        self.task_ob4.create_action(self.task_ob4)


        # show task list
        print("Task list:", self.task_ob4.tasks)

        print("task 1:",self.task_ob1.show_task_details(),"\n")
        print("task 2:",self.task_ob2.show_task_details(),"\n")
        print("task 3:",self.task_ob3.show_task_details(),"\n")
        print("task 4:",self.task_ob4.show_task_details(),"\n")

        # print histories
        print(self.task_ob1.task_history)
        print(self.task_ob2.task_history)
        print(self.task_ob3.task_history)
        print(self.task_ob4.task_history)


        print("Filtering tasks by status:")
        print("Filter Status:", self.task_ob1.filter_tasks_by_status(Status.PENDING))

        print("Filtering tasks by priority:")
        print("Filter Priority:", self.task_ob1.filter_tasks_by_priority(Priority.MEDIUM))

        print("Filtering tasks by task:")
        print("Filter Task:", self.task_ob1.filter_tasks_by_task(self.task_ob2))


        # assigning task to user
        admin_assign_ruchi = self.task_ob1.admin_assign_task_to_user("About Swimming", "Teach swimming to aditya", "Ruchi", date(2026, 6, 1))
        admin_assign_aditya = self.task_ob1.admin_assign_task_to_user("About Cycling", "Teach cycling to ruchi", "aditya", date(2026, 9, 1))
        print("Admin assign task to user:", self.task_ob1.admin_assign)

        # updating task to user
        update_user_ruchi = self.task_ob1.admin_updated_task_to_user('Ruchi',"About Running",'Teach running to aditya', date(2026, 7, 1))
        print("Admin updated task to user:", self.task_ob1.admin_assign_history)

        delete_user_aditya = self.task_ob1.admin_unassign_task_to_user('aditya')
        print("Admin unassign task to user:", self.task_ob1.admin_assign_history)

        '''demo:
{
'Ruchi': {'description': 'Teach swimming to aditya', 'title': 'Task 1', 'date_assigned': datetime.date(2026, 6, 1)}, 

'aditya': {'description': 'Teach cycling to ruchi', 'title': 'Task 2', 'date_assigned': datetime.date(2026, 9, 1)}

}'''

if __name__ == "__main__":
    main = Main()



    '''class Test:
    def __init__(self):
        x = 10          # local
        self.y = 20     # instance variable

    def show(self):
        print(self.y)   # works because self.y is an instance variable
        print(x)        # error because x is a local variable and cannot be accessed outside the method where it is defined'''