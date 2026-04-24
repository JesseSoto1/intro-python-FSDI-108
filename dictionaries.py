# dictionaries store data in key : value pairs
# written with curly brackets


student = {
    "name":"Jesse",
    "age":40,
    "major":"computer science"

}
print(student)

# accessing items
print(student["name"])
print(student.get("major"))

# adding new items

student["graduation_year"] = 2025
print(student)

# changing values

student["age"] = 89
print(student)

# removing items

student.pop("major")
print(student)

# check if a key exist

if "name" in student:
    print("key, 'name' exists in the dictionary")


# nested dictionary
studentss = {
    "student1":{"name": "Jesse", "age": 22},
    "student2":{"name": "Josh", "age": 24}
}
print(studentss)
print(studentss["student2"]["age"])

print("______________________________________________")
report_card = {
    "name":"bobby",
    "subject":"math",
    "grades":(90,70,85)
}
print("Student", report_card["name"])
print("Student", report_card["subject"])

avg = sum(report_card["grades"]) / len(report_card["grades"])########PAY ATTENTION HERE#################

report_card["average"] = avg

if avg >=90:
    print("excellent")
elif avg >= 70:
    print("good job")
else:
    print("needs improvement")

report_card.pop("subject")

print("updated report card", report_card)




# Homework

veggies ={
    "name":"tomato",
    "color":"red"
    
}
print(veggies)
veggies["type"] = "case"
print(veggies)
print(veggies.get("type"))
veggies["color"]="green"
print(veggies)
veggies.pop("type")
print(veggies)
print(len(veggies))

