# 31th github project --> Shopping List
print('---------Shopping List----------')
items = []


def show_list():
    if not items:
        print("List is empty.")
        return
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")


def add_item():
    item = input("Item to add: ").strip()
    if item:
        items.append(item)
        print(f"Added '{item}'.")


def remove_item():
    show_list()
    try:
        index = int(input("Item number to remove: ")) - 1
        removed = items.pop(index)
        print(f"Removed '{removed}'.")
    except (ValueError, IndexError):
        print("Invalid item number.")


def main():
    actions = {
        "1": show_list,
        "2": add_item,
        "3": remove_item,
    }

    while True:
        print("\n1. View  2. Add  3. Remove  4. Quit")
        choice = input("Choose: ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")



main()