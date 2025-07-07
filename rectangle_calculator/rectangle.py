import calculate

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"Area of the rectangle is: {area}")
print(f"Perimeter of the rectangle is: {perimeter}")
