class Course:
    course_name = None

    def course_duration(self):
        if self.course_name == 'python':
            print(f" {self.course_name} course duration is 3 months")
        elif self.course_name == "java":
            print(f" {self.course_name} course duration is 5 months")
        else:
            print("Course not found")

    def course_fee_structure(self):
        if self.course_name == 'python':
            print(f" {self.course_name} course fee is 5000")
        elif self.course_name == "java":
            print(f" {self.course_name} course fee is 8000")
        else:
            print("Course not found")


course_ref = Course()
course_ref.course_name = "PYTHON".lower()
print("Course name is", course_ref.course_name)
course_ref.course_duration()
course_ref.course_fee_structure()
