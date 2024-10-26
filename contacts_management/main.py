from phone.directory import Directory

directory = Directory()

directory.add_contact("Alice", "Smith", "TechCorp", "12345", "Street 1, City A")
directory.add_contact("Bob", "Johnson", "Innovate Inc.", "67890", "Avenue 2, City B")
directory.add_contact("Carol", "Brown", "Creative LLC", "54321", "Street 3, City C")

directory.list_contacts()