'''def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Bob")''' 
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
