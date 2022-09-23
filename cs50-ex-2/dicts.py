# name = key # place = value
students = {
    "Kiran":"yelahanka",
    "Akash":"sanjaynagar",
    "Madhu":"hebbal",
    "sandy":"sahakar"}

print(students["Kiran"])    

for student in students:
    print(student, students[student])

# dictionary inside the list 
students1 = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students1:
    print(student["name"], student["house"], sep=", ")