def recursive_function(number):
    if number <= 0:
        return
    else:
        print("Current value:", number)
        # Modify the variable value
        number -= 1
        # Call the function recursively
        recursive_function(number)

# Example usage
recursive_function(5)
