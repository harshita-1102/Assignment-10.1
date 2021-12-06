# Harshita Venkatesan
# Assignment 10.1: Your Own Class
# Purpose: Implement a class based on a real object, in this class I chose a Person.
# I used Lecture 7.3 as a resource to help me through this assignment. 

class Person:

    # Class variable: default scientific name of a human of that person
    scientific_name = 'Homo-Sapien'

    # Stores the name and age using self
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

     # Set method for name
    def set_name(self, name):
        # sets self.__name as name
        self.__name = name

    # Get method for name
    def get_name(self):
        # returns self.__name
        return self.__name

    # Set method for age
    def set_age(self, age):
        # sets self.__age as age
        self.__age = age

    # Get method for age
    def get_age(self):
        # returns self.__age
        return self.__age

    # Function to check if the person is a valid voter or not
    def isVoter(self):
        # If age is greater than or equal to 18, then print yes
        if self.__age >= 18:
            print("Yes!", self.__name, "can vote!")
        # If age is below 18, print no
        else:
            print("No!", self.__name, "cannot vote!")

    # Print the details(with their name and age) of the person including their default human classification
    def showDetails(self):
        print("A new", self.scientific_name, "is here, whose name is", self.__name, "with age of", self.__age, "years!")

def main():
    # output of code: prints showDetails() method and then using the details checks if the person is eligible to vote or not based on their age using the isVoter() method
    # if the person isn't eligible, updates their age using set_age() method, and then prints the details using showDetails() method and checks for voter eligibility

    # Create three objects(which is person1, person2, person3) of Person class and set their name and age 
    person1 = Person('Kelly', 19)
    person2 = Person('Joe', 15)
    person3 = Person('Maya', 23)

    # Print the details of all three persons using the showDetails() method
    person1.showDetails()
    person2.showDetails()
    person3.showDetails()

    # Check if person1 is a valid voter using isVoter() method
    person1.isVoter()

    # Check if person2 is a valid voter using isVoter() method
    person2.isVoter()

    # Check if person3 is a valid voter using isVoter() method
    person3.isVoter()

    # Set the age of person2 as 25 using set_age() method as person2 didn't meet voting requirements
    person2.set_age(25)

    # Print the updated details of person 2 using the showDetails() method
    person2.showDetails()

    # Now, check if updated person2 is a valid voter using isVoter() method
    person2.isVoter()

# Calling the main function
if __name__ == "__main__":
    main()
