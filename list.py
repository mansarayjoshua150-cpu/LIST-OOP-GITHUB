student = ["john", "Foday", "Abu"]
print (student)

print (f"my best friend is {student[0]}")
print (f"my best friend is {student[1]}")
print (f"my best friend is {student [2]}")

# Get the index of an items in a list
print (student.index("john"))
print (student.index("Foday"))

#Know the number of items in a list
print (f"The total items in the list is: {len(student)}")

#Add items to a list
student.append("john")
print(student)
student == ["john", "Foday", "Abu"]

print(student)
student.insert(3, "Abu")
print(student)

#Extending a list
fruits = ["Apple", "Banana", "Mango"]
student.extend(fruits)
print(student)

#Removing an item from a list
fruits.remove("Mango")
print(fruits)

student.pop()
thirdItem = student.pop()
print(student)
print(thirdItem)
