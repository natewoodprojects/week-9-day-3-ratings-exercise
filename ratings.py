"""Restaurant rating lister."""


# put your code here
import random

print(random.randint(1,6))
print(random.choices(["Jess", "Nate", "Zoe", "Luca"])[0])

a_dictionary = {}

a_file = open("scores.txt")

for line in a_file:
    size = len(line)
    real_line = line[:size -1]
    key, value = real_line.split(":")
    a_dictionary[key] = value

def print_dic():
    for key,value in sorted(a_dictionary.items()):
        print(key, value)


def random_restraunt():
    restraunt_names = []
    for key in a_dictionary:
        restraunt_names.append(key)
    thing = random.choices(restraunt_names)[0] 
    return thing

# print(random_restraunt())
def value(): 
    new_value = 0
    new_value = input(f"What rating would you give it?\n")
    if new_value != int(new_value) or new_value < 1 or new_value > 5:
        print("Sorry, the number needs to be an integer between 1 and 5. Please try again, you miserable worm:")
    else: 
        return new_value

def get_rating():
    new_value = 0
    new_value = input(f"What rating would you give it?\n")
    is_it_num = new_value.isdigit()
    if new_value.isdigit():
        new_value = int(new_value)
        if new_value < 1 or new_value > 5:
            print("Needs to be between 1 and 5, INCLUDING ONE AND FIVE!! Try again worm.")
            get_rating()
        else:
            print("Freakin finally. Good job. Was that so hard?")
            return new_value
    else: 
        print("That's not a digit. Try again you sackless worm.")
        get_rating()

def options():
    ask = input("Type 'see' to see the ratings, 'add' to add a new restraunt and rating, 'update' to change a random rating, or 'quit' to stop:\n")
    if ask == "see":
        print_dic()
        options()
    elif ask == "add":
        new_key = input("What restraunt would you like to add?\n")
        new_value = get_rating()
        a_dictionary[new_key] = new_value
        print_dic()
        options()
    elif ask == "update":
        pass
    elif ask != "quit":
        print("Sorry, someting went wrong, please try again.")
        options()
    else: 
        pass

options()