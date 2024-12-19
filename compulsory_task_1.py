"""
This is a function to show class inheritance
"""

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def print_head_office_location():
        print("Cape Town")

class OOPCourse(Course):
    def __init__(self) -> None:
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"Course : {self.description}")
        print(f"Trainer : {self.trainer}")

    def show_course_id(self):
        print("Course ID : #12345")

course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
