#content book

import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
                return [Contact(**data) for data in contacts_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, name, phone, email, address):
        """Add a new contact."""
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f'Contact "{name}" added successfully.')

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for index, contact in enumerate(self.contacts):
            print(f"{index + 1}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        """Search for a contact by name or phone number."""
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"{contact.name} - {contact.phone}")
        else:
            print("No contacts found matching your search.")

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        """Update an existing contact."""
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index].name = name
            if phone:
                self.contacts[index].phone = phone
            if email:
                self.contacts[index].email = email
            if address:
                self.contacts[index].address = address
            self.save_contacts()
            print(f'Contact "{self.contacts[index].name}" updated successfully.')
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        """Delete a contact."""
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            self.save_contacts()
            print(f'Contact "{removed_contact.name}" deleted successfully.')
        else:
            print("Invalid contact index.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)

        elif choice == '4':
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            
            # Update only non-empty fields
            manager.update_contact(index, 
                                   name if name else None,
                                   phone if phone else None,
                                   email if email else None,
                                   address if address else None)

        elif choice == '5':
            index = int(input("Enter the contact number to delete: ")) - 1
            manager.delete_contact(index)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
