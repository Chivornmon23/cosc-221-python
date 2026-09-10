# Exercise 3: Real-World Application
# 1. Create an empty contact book simulation using a dictionary where 
# the key is the contact’s name and the value is the phone number.
contacts = {
    "Chivorn"   :   99123456,
    "Limey"     :   98123456,
    "Dara"      :   97123456,
    "Kimseang"  :   96123456
}
# 2. Add 5 contacts to the dictionary.
contacts["Vuthy"] = 95123456
contacts["Vutha"] = 94123456
contacts["Vuthea"] = 93123456
contacts["Vutheang"] = 92123456
contacts["Vuthuy"] = 91123456
# 3. Implement a search function to retrieve a contact’s phone number by name.
def search(target): 
    if target in contacts:
        print(f"Phone number for {target}: {contacts[target]}")
    else: 
        print(f"{target} not found.")

    choice = int(input("Press (1) update the contact (2) Delete: "))

    if choice == 1:
        update_contact(target)
    elif choice == 2: 
        delete_contact(target)
    else: 
        print("Okay")

# 4. Allow the user to update a contact’s phone number.
def update_contact(name): 
    if name in contacts: 
        new_phone = int(input("Enter the new phone number: "))
        contacts[name] = new_phone
        print(f"Updated {name}'s phone number to {new_phone}.")
    else: 
        print("Contact does not exist.")
# 5. Allow the user to delete a contact by name.
def delete_contact(name): 
    if name in contacts: 
        del contacts[name]
        print(f"Deleted {name}'s phone number.")
    else:
        print("Contact does not exist.")

search("Limey")
