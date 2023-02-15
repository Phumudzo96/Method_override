"""
Compulsory Task 1: 
------------------

Use the code provided copied to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Woodstock, Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

On a side note, this task covers single inheritance. multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course
"""
class Course():
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):           
        print("Please contact us by visiting", self.contact_website)

    def address(self):                # created a mention that prints out the address 
        print("The head office location: Woodstock, Cape Town")

class OOPCourse(Course):                      # Created a class with the courses description and the trainers info 
    def __init__(self, description, trainer):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):        # created a mention that prints out the description and trainers info
        print(self.description)
        print(self.trainer)

    def show_course_id(self):        # created a mention that creates and prints the ID number of the course 
       self.id_number =  "#12345"
       print(self.id_number)

class Course_1(OOPCourse):
    def __init__(self, description, trainer, id_number): # Created a subclass of OOPCourse
        super().__init__(description, trainer)
        self.id_number = id_number
    
school = Course_1 ("www.hyperiondev.com","Mr Anon A. Mouse", "#12345") # print out results
print(f"The course is about {school.contact_website}")
print(f"The trainer goes by the name {school.trainer}")
print(f"The course ID number is {school.id_number}")


