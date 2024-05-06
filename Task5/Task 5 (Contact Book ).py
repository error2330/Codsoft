class Contact:
def __init__(self, name, phone_number, email, address):
self.name = name
self.phone_number = phone_number
self.email = email
self.address = address

class ContactManager:
def __init__(self):
self.contacts = []

def add_contact(self, contact):
self.contacts.append(contact)
print("Contact added successfully!")

def view_contacts(self):
if self.contacts:
print("\nContact List:")
for contact in self.contacts:
print(f"Name: {contact.name}, Phone: {contact.phone_number}")
else:
print("Contact list is empty.")

def search_contact(self, query):
search_results = []
for contact in self.contacts:
if query.lower() in contact.name.lower() or query in contact.phone_number:
search_results.append(contact)
if search_results:
print("\nSearch Results:")
for contact in search_results:
print(f"Name: {contact.name}, Phone: {contact.phone_number}")
else:
print("No matching contacts found.")

def update_contact(self, name, new_phone_number):
for contact in self.contacts:
if contact.name == name:
contact.phone_number = new_phone_number
print("Contact updated successfully!")
return
print("Contact not found.")

def delete_contact(self, name):
for contact in self.contacts:
if contact.name == name:
self.contacts.remove(contact)
print("Contact deleted successfully!")
return
print("Contact not found.")

def main():
contact_manager = ContactManager()

while True:
print("\nContact Management System")
print("-------------------------")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Update Contact")
print("5. Delete Contact")
print("6. Exit")

choice = input("Enter your choice: ")

if choice == '1':
name = input("Enter name: ")
phone_number = input("Enter phone number: ")
email = input("Enter email: ")
address = input("Enter address: ")
contact = Contact(name, phone_number, email, address)
contact_manager.add_contact(contact)
elif choice == '2':
contact_manager.view_contacts()
elif choice == '3':
query = input("Enter name or phone number to search: ")
contact_manager.search_contact(query)
elif choice == '4':
name = input("Enter name of the contact to update: ")
new_phone_number = input("Enter new phone number: ")
contact_manager.update_contact(name, new_phone_number)
elif choice == '5':
name = input("Enter name of the contact to delete: ")
contact_manager.delete_contact(name)
elif choice == '6':
print("Goodbye!")
break
else:
print("Invalid choice. Please try again.")

if __name__ == "__main__":
main()