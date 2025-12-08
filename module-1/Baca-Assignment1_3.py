# Name: Martin Baca
# Date: December 7, 2025
# Assignment: CSD-325 Module 1 - Assignment 1.3
# Purpose: Display the "99 Bottles of Beer" song by counting down from a user-entered number

def countdown(bottles_remaining):
    """Count down from the specified number of bottles and print the song verse for each."""
    # Loop through each bottle count, starting from the input number down to 2
    while bottles_remaining > 1:
        print(f"{bottles_remaining} bottles of beer on the wall, {bottles_remaining} bottles of beer.")
        print(f"Take one down, pass it around, {bottles_remaining - 1} bottles of beer on the wall!\n")
        bottles_remaining -= 1

    # Handle the final bottle (singular) separately
    if bottles_remaining == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down, pass it around, zero bottles of beer on the wall!\n")

def main():
    """Main program: get user input and call the countdown function."""
    # Prompt user for the starting number of bottles
    bottles_remaining = int(input("How many bottles of beer are on the wall? "))

    # Call the countdown function to display the song
    countdown(bottles_remaining)

    # Display closing message
    print("Time to buy more beer!")

# Run the program
main()
