
li = []
while True:
    name = input("Enter the name of a person you want to invite to the party: ")
    li.append(name)
    
    add_more = input("Do you want to add another person? (yes/no): ")
    if add_more.lower() == "no":
        break
num_invited = len(li)
print(f"You have invited {num_invited} people to the party.")
######################################################################question 2####################################################################

print("List of invited people:")
for i in range(len(li)):
    print(f"{i + 1}. {li[i]}")

name = input("Type in one of the names on the list: ")
pos = li.index(name) + 1
print(f"{name} is at position {pos} in the list.")

remove = input(f"Do you still want {name} to come to the party? (yes/no): ")
if remove.lower() == "no":
    li.remove(name)
    print(f"{name} has been removed from the list.")

print("Updated list of invited people:")
for i in range(len(li):
    print(f"{i + 1}. {li[i]}")

#########################################################################question 3##########################################################

my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
for i in range(len(my_list)):
    print(f"Row {i + 1}: {my_list[i]}")

row = int(input("Enter the row number you'd like to display: ")) - 1

if 0 <= row < len(my_list):
    print(f"Selected Row: {my_list[row]}")
else:
    print("Invalid row number.")

new_value = int(input("Enter a new value to add to the end of the selected row: "))
if 0 <= row < len(my_list):
    my_list[row].append(new_value)
    print(f"Updated Row: {my_list[row]}")
else:
    print("Invalid row number.")
for i in range(len(my_list)):
    print(f"Row {i + 1}: {my_list[i]}")

############################################################################### question 4###########################################################

people_list = []
for i in range(4):
    name = input(f"Enter the name of person {i + 1}: ")
    age = int(input(f"Enter the age of {name}: "))
    id_number = input(f"Enter the ID of {name}: ")
    
    person = {"name": name, "age": age, "id": id_number}
    people_list.append(person)

selected_name = input("Enter the name of the person to retrieve their age and ID: ")
found = False
for person in people_list:
    if person["name"] == selected_name:
        found = True
        print(f"{selected_name} is {person['age']} years old with ID: {person['id']}")
        break

if not found:
    print(f"{selected_name} not found in the list.")
