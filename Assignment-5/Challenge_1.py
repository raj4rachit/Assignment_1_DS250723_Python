# Square Numbers and Return Their Sum

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

# Input values from the user
x = int(input("Enter the Number for X: "))
y = int(input("Enter the Number for Y: "))
z = int(input("Enter the Number for Z: "))

# Create a Point object with user input
point1 = Point(x, y, z)

# Calculate and display the sum of squares
result = point1.sqSum()
print(f"The sum of the squares of x, y, and z is: {result}")
