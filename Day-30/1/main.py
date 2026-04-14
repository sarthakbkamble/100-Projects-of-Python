try:
    file = open("C:/sarthak/100-Projects-of-Python/Day-30/data.txt")
    dictionary = {"key":"value"}
    print(dictionary["key"])
except FileNotFoundError:
        file = open("C:/sarthak/100-Projects-of-Python/Day-30/data.txt","w")
        file.write("something")
except KeyError as error_message :
     print(f"The key {error_message} does not exist.")
else:
     content = file.read()
     print(content)
finally:
     raise TypeError("This is an error that I made up.")


height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if height>3:
    raise ValueError("Human height is not greater than 3 meters")

bmi = weight/height**2
print(bmi)