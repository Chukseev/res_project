from animals import Animal

def main():
    print("Welcome to the Animal Registry!")
    animals = []

    while True:
        print("\nMenu:")
        print("1. Add New Animal")
        print("2. List All Animals")
        print("3. Add Command to Animal")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter animal name: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            animals.append(Animal(name, birth_date=birth_date))
            print(f"Animal '{name}' added.")
        elif choice == "2":
            if not animals:
                print("No animals registered yet.")
            else:
                for idx, animal in enumerate(animals, start=1):
                    print(f"{idx}. {animal}")
        elif choice == "3":
            if not animals:
                print("No animals registered yet.")
            else:
                for idx, animal in enumerate(animals, start=1):
                    print(f"{idx}. {animal.name}")
                animal_idx = int(input("Select an animal by number: ")) - 1
                command = input("Enter new command: ")
                print(animals[animal_idx].add_command(command))
        elif choice == "4":
            print("Exiting the registry.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
