import art

#Functions for mathematical operations
def add(n1, n2):
    """Adds two number"""
    return n1 + n2
def subtract(n1, n2):
    """Subtracts two number"""
    return n1 - n2
def divide(n1, n2):
    """Divides two number"""
    return n1 / n2
def multiply(n1, n2):
    """Multiplies two number"""
    return n1 * n2

#Dictionary for Arithmetic Operations
arithmetic_operations = {"+":add,
                         "-":subtract,
                         "*":multiply,
                         "/":divide,
}


calculator_is_on = True
# Loop to run the calculator again and again.

while calculator_is_on :
    # Display the program logo from the 'art' module
    print(art.logo)

# Taking Inputs for calculation
    first_number= int(input("What is the first number?:"))
    for key in arithmetic_operations:
        print(key)
    operation_selected = input("Pick an operation:")
    next_number = int(input("What is the next number?: "))


    def perform_operations(n1,n2,operator):
        """Takes 2 numeric values and 1 operator, uses arithmetic_operation(dictionary)
        , performs the calculations and returns the result.
        """
        result = arithmetic_operations[operator](n1,n2)
        print(f"{first_number} {operator} {next_number} = {result}")
        return result

    # If user want to continue calculation the result is stored
    result = perform_operations(first_number,next_number,operation_selected)
    
    # Loop created to run the calculations with the previous result
    continue_calculation = True

    while continue_calculation:
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()

        if choice == "y":
            #continues calculations with previous result
            first_number=result
            for key in arithmetic_operations:
                print(key)
            operation_selected = input("Pick an operation:")
            next_number = int(input("What is the next number?: "))
            result = perform_operations(first_number,next_number,operation_selected)

        else:
            # Starts fresh calculation
            result = 0
            print("\n"*100)
            continue_calculation = False