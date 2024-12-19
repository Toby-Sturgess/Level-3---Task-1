"""
This is a function to show class inheritance
"""

class Course:
    """
    A class representing a generic course.

    Attributes:
        name (str): The name of the course.
        contact_website (str): The contact website for the course.
    """

    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        """
        Prints the contact website for the course.
        """
        print("Please contact us by visiting", self.contact_website)

    def print_head_office_location(self):
        """
        Prints the location of the course's head office.
        This method is not currently used in the code.
        """
        print("Cape Town")


class OOPCourse(Course):
    """
    A class representing an Object-Oriented Programming (OOP) course,
    which inherits from the Course class.

    Attributes:
        description (str): The description of the OOP course.
        trainer (str): The name of the course trainer.
    """

    def __init__(self) -> None:
        """
        Initializes the OOPCourse with a description and trainer name.
        """
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        """
        Prints the details of the trainer for the OOP course.
        """
        print(f"Course : {self.description}")
        print(f"Trainer : {self.trainer}")

    def show_course_id(self):
        """
        Prints the course ID for the OOP course.
        """
        print("Course ID : #12345")


# Creating an instance of OOPCourse and demonstrating its functionality
course_1 = OOPCourse()
course_1.contact_details()  # Displays the contact website
course_1.trainer_details()  # Displays course and trainer details
course_1.show_course_id()   # Displays the course ID

