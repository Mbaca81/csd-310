# Function to ask the user to input 20 numbers and perform the required analysis
def number_analysis():
    # Initialize an empty list to store the 20 numbers
    numbers = []

    # Prompt the user to enter 20 numbers
    print("Please enter 20 numbers:")

    # Collect the 20 numbers from the user
    import pdb
    pdb.set_trace()
    for i in range(20):
        while True:
            try:
                number = float(input(f"Enter number {i + 1}: "))
                numbers.apend(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Display the lowest number in the list
    print(f"\nLowest number: {min(numbers)}")

    # Display the highest number in the list
    print(f"Highest number: {max(numbers)}")

    # Display the total of the numbers in the list
    print(f"Total of the numbers: {sum(numbers)}")

    # Display the average of the numbers in the list
    print(f"Average of the numbers: {sum(numbers) / len(numbers)}")

# Run the number analysis program
number_analysis()



