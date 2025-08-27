subjects = ["English", "Software", "Drama", "Science", "Sport"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def list_subjects(subjects):
    for index, subject in enumerate(subjects):
        print("Period", index+1, ":", subject)

def list_day(days):
    for day in days:
        print(day)

list_day(days)
print("---------------------")

for i in range(5):
    list_subjects(subjects)
    subjects.append(subjects[0])
    subjects.remove(subjects[0])
    print("----------------------------")