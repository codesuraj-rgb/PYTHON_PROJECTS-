task =[]
def add_task():
    while True:
        t = input("Enter a task (or type 'stop' to finish): ")
        if t.lower() == "stop":
            break
        task.append(t)
    print(task)

def complete_task():
    print("Complete all the task within 24 hours")
    complete = 0
    for i in range(len(task)):
        print(f"Task {i+1}: {task[i]}")
        status = input("Enter DONE if complete, or NOT DONE: ").lower()
        task[i] = f"{task[i]} - {status}"

        if status == "done":
            print(f"Task {i+1} is complete")
            complete += 1

    if(complete == 0 ):
        print("Not a single task complete")
        
    else:
        print(f"The number of task complete {complete}/{len(task)}")

def view_task():
    with open("viewtask.txt", "w") as f:
        for i, t in enumerate(task, start=1):
            f.write(f"Task {i}: {t}\n")
    print("Tasks saved to viewtask.txt")

    with open("uncomplete_task.txt", "w") as f:
        for i, t in enumerate(task, start=1):
            if "not done" in t:
                f.write(f"Task {i}: {t}\n")
    print("Incomplete tasks saved to uncomplete_task.txt")

add_task()
complete_task()
view_task()
        
   





