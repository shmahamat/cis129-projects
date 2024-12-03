'''
Souleyman Mahamat
cis-129

This script creates a an object class Pet as defined below, asks for relevant input,
and displays it.
'''

# Class definition for Pet
class Pet:
    # Constructor
    def __init__(self, n=None, t=None, a=None):
        self.name = n
        self.type = t
        self.age = a

    # Mutator methods
    def setName(self, n):
        self.name = n

    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a

    # Accessor methods
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


# Main program to create and use a Pet object
def main():
    # Declare input variables, test input validity
    
    inputName = input("Enter a pet name: ")
    while not inputName.isalpha():
        inputName = input("Enter a pet name (letters only): ")

    inputType = input("Enter a pet type: ")
    while not inputType.isalpha():
        inputType = input("Enter a pet type (letters only): ")

    while True:
        inputAge = input("Enter a pet age (whole numbers only): ")
        try:
            int(inputAge)
        except:
            continue
        break

    # Create a Pet object
    Animal = Pet()

    # Set the pet's properties using the mutator methods
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)

    # Display the pet's properties using the accessor methods
    print()
    print("The pet name is", Animal.getName())
    print("The pet type is", Animal.getType())
    print("The pet age is", Animal.getAge())


# Call the main function to run the program
if __name__ == "__main__":
    main()

