class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def view_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("All Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.email.lower():
                results.append(contact)
        if not results:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for index, contact in enumerate(results, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            new_contact = Contact(name, phone_number, email)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_all_contacts()

        elif choice == "3":
            query = input("Enter the name or email to search: ")
            contact_manager.search_contacts(query)

        elif choice == "4":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

