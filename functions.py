'''
def greet(name):
    print(f"Hello, {name}!")
  
greet("Alice")

def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum is: {result}")
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Print the result of the greet function
print(greet("Tobby", "Good morning"))