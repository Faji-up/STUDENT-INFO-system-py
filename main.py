import sys
from Grades import Grades

class GradingSystem:
    def __init__(self):
        self.isMidtermDone = 0
        self.isPrelimDone = 0
        self.isSemiFinalsDone = 0
        self.isFinalsDone = 0

        self.grade = Grades()
        self.name = ""
        self.section = ""
    def main(self):
        self.name = input("Name : ")
        self.section = input("Section : ")
        self.options()

    def options(self):
        print("-"*100)
        print("[1] - Prelim")
        print("[2] - Midterm")
        print("[3] - Semi-Final")
        print("[4] - Finals")
        print("[5] - Exit")
        opt = input("Enter Term Grade: ")
        return self.get_option(int(opt))

    def get_option(self,opt):

        if opt == 1:
            return self.prelim()
        elif opt == 2:
            return self.midterm()
        elif opt == 3:
            return self.semi_finals()
        elif opt == 4:
            return self.finals()
        elif opt == 5:
            return sys.exit()

    def prelim(self):
        print("PRELIM:")
        print("[1] - Attendance")
        print("[2] - Class Standing")
        print("[3] - Major Exam")
        print("[4] - Print Result")
        print("[5] - Exit")
        opt = int(input("Enter Options: "))

        if opt == 1:
            self.grade.add_to_attendance_prelim(self.set_attendance())
            self.isPrelimDone += 1
            self.prelim()
        elif opt == 2:
            self.grade.add_to_classStanding_prelim(self.set_class_standing())
            self.isPrelimDone += 1
            self.prelim()
        elif opt == 3:
            self.grade.add_to_majorExam_prelim(self.set_major_exam())
            self.isPrelimDone += 1
            self.prelim()
        elif opt == 4:
            self.grade.print_result(self.name,self.section)
            self.prelim()
        elif opt == 5:
            self.options()

    def midterm(self):
        print("MIDTERM:")
        print("[1] - Attendance")
        print("[2] - Class Standing")
        print("[3] - Major Exam")
        print("[4] - Print Result")
        print("[5] - Exit")

        opt = int(input("Enter Options: "))

        if opt == 1:
            self.grade.add_to_attendance_midterm(self.set_attendance())
            self.midterm()
        elif opt == 2:
            self.grade.add_to_classStanding_midterm(self.set_class_standing())
            self.midterm()
        elif opt == 3:
            self.grade.add_to_majorExam_midterm(self.set_major_exam())
            self.midterm()
        elif opt == 4:
            self.grade.print_result(self.name,self.section)
            self.midterm()
        elif opt == 5:
            self.options()

    def semi_finals(self):
        print("SEMI FINALS:")
        print("[1] - Attendance")
        print("[2] - Class Standing")
        print("[3] - Major Exam")
        print("[4] - Print Result")
        print("[5] - Exit")
        opt = int(input("Enter Options: "))

        if opt == 1:
            self.grade.add_to_attendance_semi_finals(self.set_attendance())
            self.semi_finals()
        elif opt == 2:
            self.grade.add_to_classStanding_semi_finals(self.set_class_standing())
            self.semi_finals()
        elif opt == 3:
            self.grade.add_to_majorExam_semi_finals(self.set_major_exam())
            self.semi_finals()
        elif opt == 4:
            self.grade.print_result(self.name,self.section)
            self.semi_finals()
        elif opt == 5:
            self.options()

    def finals(self):
        print("Finals:")
        print("[1] - Attendance")
        print("[2] - Class Standing")
        print("[3] - Major Exam")
        print("[4] - Project")
        print("[5] - Print Result")
        print("[6] - Exit")
        opt = int(input("Enter Options: "))

        if opt == 1:
            self.grade.add_to_attendance_finals(self.set_attendance())
            self.finals()
        elif opt == 2:
            self.grade.add_to_classStanding_finals(self.set_class_standing())
            self.finals()
        elif opt == 3:
            self.grade.add_to_majorExam_finals(self.set_major_exam())
            self.finals()
        elif opt == 4:
            self.grade.add_to_project_finals(self.set_project())
            self.finals()
        elif opt == 5:
            self.grade.print_result(self.name,self.section)
            self.finals()
        elif opt == 6:
            self.options()

    def set_attendance(self):
        numberOfAttendance = int(input("Enter number of Attendance Record :"))

        attendancesList = []
        if numberOfAttendance >= 3:
           for i in range(numberOfAttendance):
                date = input("Date: ")
                remarks = input("Remarks: ")
                attendancesList.append({
                    "date": date,
                    "remarks": remarks
                })

        else:
            print("Attendance must have minimum of 3 records")
            return self.set_attendance()
        return attendancesList

    def set_class_standing(self):
        quiz = input("Quiz: ")
        activity = input("Activity: ")
        caseStudy = input("Case Study: ")
        return {
            "quiz": quiz,
            "activity": activity,
            "caseStudy": caseStudy
        }

    def set_major_exam(self):
        majorExam = int(input("Major Exam: "))
        return majorExam

    def set_project(self):
        project = int(input("Project: "))
        return project

if __name__ == "__main__":
    system = GradingSystem()
    system.main()