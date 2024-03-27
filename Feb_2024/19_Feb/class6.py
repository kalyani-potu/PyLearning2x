class Course:
    course_name = None

    def course_duration(self,course_in):
        self.course_name = course_in
        if course_in == 'python' :
            print(f" {course_in} course duration is 3 months")
        elif course_in == "java" :
            print(f" {course_in} course duration is 5 months")
        else :
            print("Course not found")
    def course_fee_structure(self, course_in):
        self.course_name = course_in
        if course_in == 'python':
            print(f" {course_in} course fee is 5000")
        elif course_in == "java":
            print(f" {course_in} course fee is 8000")
        else:
            print("Course not found")


course_ref = Course()
course_ref.course_duration("Python".lower())
course_ref.course_fee_structure("Python".lower())
