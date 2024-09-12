contacts = {}

while True:
    print("CONTACT BOOK APP")
    print("1. Create Contact")
    print("2. View Contact ")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact ")
    print("7. Exit")

    choice = int(input("Enter Your Choice = "))

    if choice == 1:
        name = input("Enter Your Name ")
        if name in contacts:
            print(f"Name {name} is Already Exist in Your Contacts")

        else:
            age = input("Enter Your Age ")
            email = input("Enter Your Email ")
            mobile = input("Enter Your Mobile ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact name {name} has been created Successfully!")

    elif choice == 2:
        name = input("Enter the contact name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {age}, Mobile: {mobile}")
        else:
            print("Contact Not Found")

    elif choice == 3:
        name = input("Enter Name You want to Update in the Contact = ")
        if name in contacts:
            age = input("Enter Your  Updated Age ")
            email = input("Enter Your Updated Email ")
            mobile = input("Enter Your Updated Mobile ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"Contact name {name} has been Updated Successfully!")
        else:
            print("Contact Not Found")

    elif choice == 4:
        name = input("Enter Name You want to Delete from your contacts = ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been Deleted Successfully!")
        else:
            print("Contact Not Found")

    elif choice == 5:
        search_name = input("Enter the contact Name You want to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Age : {age},Mobile: {mobile}, Email: {email}")
                found = True
            if not found:
                print("No Contact Found With That Name")

    elif choice == 6:
        print(f"Total contact in  your book : {len(contacts)}")

    elif choice == 7:
        print("Good Bye.. Closing the Programme")
        break

    else:
        print("Invalid Input")





