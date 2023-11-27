# Define a list to store fertility entries
fertility_entries = []

# Function to add a fertility symptom entry
def add_symptoms():
    cycle_symptoms = input("Enter your cycle day, basal body temp, and symptoms: ")
    date = input("Enter the date (MM-DD-YYYY): ")
    fertility_entry = f"{date}: {cycle_symptoms}"
    fertility_entries.append(fertility_entry)
    print("Fertility symptoms entry added successfully!")

# Function to view fertility symptom entries
def view_symptoms():
    if fertility_entries:
        print("Fertility entries:")
        for entry in fertility_entries:
            print(entry)
    else:
        print("No fertility entries to display.")

# Function to save fertility symptom entries to a file
def save_symptoms():
    try:
        with open("fertility_tracker.txt", "w") as file:
            for entry in fertility_entries:
                file.write(entry + "\n")
        print("Fertility entries saved to 'fertility_tracker.txt'.")
    except IOError:
        print("Error saving fertility entries to the file.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Fertility Entry")
    print("2. View Fertility Entries")
    print("3. Save Fertility Entries to File")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_symptoms()
    elif choice == "2":
        view_symptoms()
    elif choice == "3":
        save_symptoms()
    elif choice == "4":
        print("Exiting the tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")