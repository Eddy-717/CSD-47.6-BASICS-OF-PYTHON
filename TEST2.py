def User_Profile(name, age, email,grade):
    profile = {
                'name': name,
                'age': age,
                'email': email,
                'grade': grade
     }
    return profile

name =  input("Please enter your full name: ")
age = int(input("Please enter your age: "))
email = input("Please enter your email: ")
grade = input("Please enter your grade (A,B,C,D,E,F):")

if grade == "A" or grade == "B" or grade == "C":
    print(f"Congratulations {name}, you have been admitted to our school")
    print(User_Profile(name, age, email, grade))

elif grade == "D" or grade == "E" or grade == "F":
    print(f"Sorry {name}, you are not eligible for admission")
else:
    print("Invalid grade entered.")