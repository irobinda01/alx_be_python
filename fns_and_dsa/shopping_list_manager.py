
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice from 1 to 4: "))

        if choice == 1:
            # Prompt for and add an item
            item = input('Enter the item to add: ').lower()
            shopping_list.append(item)
            print(f'The item {item}, has been added to the shopping list successfully..')
            pass
        elif choice == 2:
            # Prompt for and remove an item
            item = input('Enter the name of the item you want to remove: ').lower()
            try:
              popped_item = shopping_list.index(item)
              shopping_list.pop(popped_item)
              print(f'The item {item}, has been removed from the shopping list successfully..')
            except ValueError:
              print(f'The item {item} is not in the shopping list.')
            pass
        elif choice == 3:
            # Display the shopping list
            if len(shopping_list) == 0:
                print('There is nothing in the shopping list to display')
            else:
              print('The items in the list are:')
              for item in shopping_list:
                  print(item)
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()