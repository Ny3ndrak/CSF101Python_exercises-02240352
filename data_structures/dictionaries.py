name = "Nyendrak"
age = 18
height = 1.56
is_student = True

person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person_info)

person_info["favorite_color"] = "maroon"
print(person_info)

try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")
    
