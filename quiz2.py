#Define a function to calculate the perimeter
def calculate_perimeter(length,width):
    perimeter = 2* (length + width)
    return perimeter

# Input the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the perimeter using the function
perimeter = calculate_perimeter(length, width)

# Display the result
print(f"The perimeter of the rectangle is: {perimeter}")

  
git config --global user.email "badanajamespatrick@gmail.com"          
>>   git config --global user.name "James Patrick Badana"