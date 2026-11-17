def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully.")


def display_contacts(contacts):
    if not contacts:
        print("\nContact book is empty.")
        return

    print("\n" + "=" * 50)
    print(f"{'Name':<20} {'Phone':<15} {'Email':<20}")
    print("=" * 50)
    for c in contacts:
        print(f"{c['name']:<20} {c['phone']:<15} {c['email']:<20}")
    print("=" * 50)


def search_contact(contacts):
    query = input("Enter name to search: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == query:
            print("\n--- Contact Found ---")
            print(f"Name : {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            return
    print("\nContact not found.")


def update_contact(contacts):
    query = input("Enter name to update: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == query:
            print(f"Updating details for {c['name']} (leave blank to keep current):")
            new_phone = input(f"New Phone [{c['phone']}]: ").strip()
            new_email = input(f"New Email [{c['email']}]: ").strip()

            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email

            print("\nContact updated successfully.")
            return
    print("\nContact not found.")


def delete_contact(contacts):
    query = input("Enter name to delete: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == query:
            contacts.remove(c)
            print(f"\nContact '{c['name']}' deleted successfully.")
            return
    print("\nContact not found.")


def main():
    contact_book = []
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            display_contacts(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            update_contact(contact_book)
        elif choice == "5":
            delete_contact(contact_book)
        elif choice == "6":
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()