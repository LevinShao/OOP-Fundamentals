subjects = []
days = []

def list_subjects(subjects):
    for index, subject in enumerate(subjects):
        print("Period", index+1, ":", subject)

def list_day(days):
    for day in days:
        print(days)

list_day(days)
print("margin")

for i in range(5):
    list_subjects(subjects)
    subjects.append(subjects[0])
    subjects.remove(subjects[0])