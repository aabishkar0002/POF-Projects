# Scenario 2: Contact Management System

# A phone application stores contacts.
# Features:

# Add contacts
# Search contacts
# Remove contacts
# Display all contacts


class Contacts:

    def __init__(self,contact_lists):
        self.contact_lists = contact_lists

    def add_contacts(self,numbertoadd):

        if numbertoadd in self.contact_lists:
            print("No duplicates allowed")
        else:
            print(f"Number added in the contacts : {numbertoadd}")
            self.contact_lists.append(numbertoadd)

    def search_contacts(self,searchnumber):

            if searchnumber in self.contact_lists:
                print("Number found")
            else:
                print("Number not found")

    def remove_contacts(self,numbertoremove):

        if numbertoremove not in self.contact_lists:
            print("No numbers given to remove")
        else:
            print(f"Number removed from the contacts : {numbertoremove}")
            self.contact_lists.remove(numbertoremove)

    def display_contacts(self):
        for numbers in self.contact_lists:
            print(numbers)


#Contact Lists

contact_lists = [9810024871,9810025672,9801123456,9702827475,9832484625]

c = Contacts(contact_lists)




#Input interactive in terminal


#Navigation---------------------------------------------------

while True: #This is true forever remains active forever

    print("\n||||------------CONTACT_MANAGER-----------||||\n")

    print("Enter 1 to add number")
    print("Enter 2 to search number")
    print("Enter 3 to remove number")
    print("Enter 4 to display all contacts")
    print("Enter 5 to exit interface")
    print("\n")
    print("Note: Incase terminal displays long errors. Try re-running the program!")


    choose = int(input("Select an option :  "))
    #bug occurs here
    print("Problem occured when entering input")
    
    match choose:

        case 1:
          add_c = int(input("Enter Numbers to add : "))
          if(len(str(add_c)))!= 10:
              print("Length should be 10")
          else:
              c.add_contacts(add_c)
 
        case 2:
          search_c = int(input("Search Number : "))
          if(len(str(search_c)))!= 10:
              print("Length should be 10")
          c.search_contacts(search_c)

        case 3:
          remove_c = int(input("Remove Number : "))
          if(len(str(remove_c)))!= 10:
              print("Length should be 10")
          c.remove_contacts(remove_c)

        case 4:
          print("Displaying all contacts...")
          c.display_contacts()

        case 5:
          break;

        case _:
            print("Error interface only accepts 1,2,3,4 or 5")




# c.add_contacts(9702364000)  #number added shows in the list
# c.search_contacts(9810025672)  #number found in contact
# c.remove_contacts(9702827475) #number removed


