#Changes made:
# Added a menu allowing the user to select Highs, Lows, or Exit
# Implemented looping until user chooses Exit
# Added blue graph for low temperatures
# Added exit message and clean termination using sys.exit()

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = r'C:\Users\limai\Documents\GitHub\csd-310\module-4\sitka_weather_2018_simple.csv'


def load_weather_data():
    """Loads dates, high temps, and low temps from the CSV file."""
    dates, highs, lows = [], [], []

    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    # Skip rows with missing or bad data
                    continue
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit()

    return dates, highs, lows


def plot_highs(dates, highs):
    """Plots high temperatures in red."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - 2018", fontsize=20)
    plt.xlabel("Date")
    plt.ylabel("Temperature (F)")
    fig.autofmt_xdate()
    plt.show()


def plot_lows(dates, lows):
    """Plots low temperatures in blue."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - 2018", fontsize=20)
    plt.xlabel("Date")
    plt.ylabel("Temperature (F)")
    fig.autofmt_xdate()
    plt.show()


def menu():
    """Displays the menu options."""
    print("\n--- Sitka Weather Menu ---")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")


def main():
    dates, highs, lows = load_weather_data()

    while True:
        menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            plot_highs(dates, highs)

        elif choice == '2':
            plot_lows(dates, lows)

        elif choice == '3':
            print("Exiting program. Thank you for using Sitka Weather Viewer.")
            sys.exit()

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


main()