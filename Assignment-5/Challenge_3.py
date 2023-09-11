# Implement the Complete Student Class

class Student:
    def __init__(self):
        pass  # No need to initialize properties here

    # Getter method for name
    def getName(self):
        return self.__name

    # Setter method for name
    def setName(self, name):
        self.__name = name

    # Getter method for rollNumber
    def getRollNumber(self):
        return self.__rollNumber

    # Setter method for rollNumber
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

# Create a Student object
student = Student()

# Prompt the user for input
name_input = input("Enter the student's name: ")
roll_number_input = int(input("Enter the student's roll number: "))

# Use the setter methods to set the name and rollNumber
student.setName(name_input)
student.setRollNumber(roll_number_input)

# Get name and rollNumber using getters
name = student.getName()
rollNumber = student.getRollNumber()

print(f"Name: {name}")
print(f"Roll Number: {rollNumber}")