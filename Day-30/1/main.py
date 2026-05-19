try:
    # Attempt to open the target text file and access a dictionary key
    file = open("C:/sarthak/100-Projects-of-Python/Day-30/data.txt")
    dictionary = {"key":"value"}
    print(dictionary["key"])
except FileNotFoundError:
    # Triggered only if the file in the try block does not exist; creates the file instead
    file = open("C:/sarthak/100-Projects-of-Python/Day-30/data.txt","w")
    file.write("something")
except KeyError as error_message :
    # Triggered if we attempt to access a non-existent dictionary key, capturing the error details
    print(f"The key {error_message} does not exist.")
else:
    # Runs only if the try block executes successfully without raising any exceptions
    content = file.read()
    print(content)
finally:
    # Executes absolutely no matter what happens, even after other exceptions have been caught
    raise TypeError("This is an error that I made up.")


# --- Input Validation and Custom Exception Raising ---

height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

# Check if the entered height exceeds a realistic threshold (3 meters)
if height>3:
    # Manually halt execution and raise a ValueError with a helpful descriptive warning
    raise ValueError("Human height is not greater than 3 meters")

# Calculate and print body mass index (BMI) using the formula: weight / height^2
bmi = weight/height**2
print(bmi)