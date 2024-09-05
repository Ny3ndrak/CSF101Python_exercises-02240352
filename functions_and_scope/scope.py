x = 10 #Global variable

def print_x():
    x = 20 #local variable
    print(f"local x: {x}")

print_x()
print(f"Global x: {x}")

count = 0

def increment ():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
print(f"Final_count: {count}")

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"inner x: {x}")

    inner()
    print(f"Outer x: {x}")

outer()
