class Grades:
    def __init__(self):
        self.isMidtermDone = [False,False,False]
        self.isPrelimDone = [False,False,False]
        self.isSemiFinalsDone = [False,False,False]
        self.isFinalsDone = [False,False,False,False]
        self.prelim = {
            "attendance": [],
            "classStanding": {},
            "majorExam": 0,
            "finalGrade":None
        }
        self.midterm = {
             "attendance": [],
             "classStanding": {},
             "majorExam": 0,
            "finalGrade":None
        }
        self.semiFinals = {
            "attendance": [],
            "classStanding": {},
            "majorExam": 0,
            "finalGrade":None
        }
        self.finals = {
            "attendance": [],
            "classStanding": {},
            "majorExam": 0,
            "project": 0,
            "finalGrade":None
        }

# ------------------------------------------------------
    def add_to_attendance_midterm(self,data):
        self.midterm["attendance"] = data
        self.isMidtermDone[0] = True

    def add_to_attendance_semi_finals(self,data):
        self.semiFinals["attendance"] = data
        self.isSemiFinalsDone[0] = True
    def add_to_attendance_prelim(self,data):
        self.prelim["attendance"] = data
        self.isPrelimDone[0] = True

    def add_to_attendance_finals(self,data):
        self.finals["attendance"] = data
        self.finals[0] = True
#------------------------------------------------------

    def add_to_classStanding_midterm(self,data):
        self.prelim["classStanding"] = data
        self.isMidtermDone[1] = True

    def add_to_classStanding_semi_finals(self,data):
        self.prelim["classStanding"] = data
        self.isSemiFinalsDone[1] = True
    def add_to_classStanding_prelim(self,data):
        self.prelim["classStanding"] = data
        self.isPrelimDone[1] = True

    def add_to_classStanding_finals(self,data):
        self.prelim["classStanding"] = data
        self.finals[1] = True
# ------------------------------------------------------

    def add_to_majorExam_midterm(self,data):
        self.midterm["majorExam"] = data
        self.isMidtermDone[2] = True
    def add_to_majorExam_semi_finals(self,data):
        self.semiFinals["majorExam"] = data
        self.isSemiFinalsDone[2] = True
    def add_to_majorExam_prelim(self,data):
        self.prelim["majorExam"] = data
        print("added",self.prelim["majorExam"])
        self.isPrelimDone[2] = True

    def add_to_majorExam_finals(self,data):
        self.finals["majorExam"] = data
        self.finals[2] = True

    # ------------------------------------------------------

    def add_to_project_finals(self,data):
        self.finals["project"] = data
        self.finals[3] = True

# ------------------------------------------------------
    def prelim_grade(self):
        isDone = False
        attn = self.prelim.get("attendance")
        classStanding = self.prelim.get("classStanding")
        majorExam = self.prelim.get("majorExam")
        attnGrade = 0
        classStandingGrade = 0
        for a in range(len(attn)):
            if attn[a].get("remarks").lower() == "present":
                attnGrade += 1

        if len(classStanding) != 0:
            for key, item in classStanding.items():
                classStandingGrade += int(item)

        if isDone not in self.isPrelimDone:
            return ((0.2 * float(attnGrade)) + (0.4 * float(majorExam)) + (0.4 * float(classStandingGrade))) * 0.2
        else:
            return 0

    def midterm_grade(self):
        isDone = False
        attn = self.midterm.get("attendance")
        classStanding = self.midterm.get("classStanding")
        majorExam = self.midterm.get("majorExam")
        attnGrade = 0
        classStandingGrade = 0
        for a in range(len(attn)):
            if attn[a].get("remarks").lower() == "present":
                attnGrade += 1

        if len(classStanding) != 0:
            for key, item in classStanding.items():
                classStandingGrade += int(item)
        if isDone not in self.isMidtermDone:
            return ((0.2 * float(attnGrade)) + (0.4 * float(majorExam)) + (0.4 * float(classStandingGrade))) * 0.2
        else:
            return 0

    def semi_final_grade(self):
        isDone = False
        attn = self.semiFinals.get("attendance")
        classStanding = self.semiFinals.get("classStanding")
        majorExam = self.semiFinals.get("majorExam")
        attnGrade = 0
        classStandingGrade = 0
        for a in range(len(attn)):
            if attn[a].get("remarks").lower() == "present":
                attnGrade += 1

        if len(classStanding) != 0:
            for key, item in classStanding.items():
                classStandingGrade += int(item)
        if isDone not in self.isFinalsDone:


            return ((0.2 * float(attnGrade)) + (0.4 * float(majorExam)) + (0.4 * float(classStandingGrade))) * 0.2
        else:
            return 0

    def finals_grade(self):
        isDone = False
        attn = self.finals.get("attendance")
        classStanding = self.finals.get("classStanding")
        majorExam = self.finals.get("majorExam")
        project = self.finals.get("project")
        attnGrade = 0
        classStandingGrade = 0
        for a in range(len(attn)):
            if attn[a].get("remarks").lower() == "present":
                attnGrade += 1

        if len(classStanding) != 0:
            for key, item in classStanding.items():
                classStandingGrade += int(item)

        if isDone not in self.isPrelimDone:


            return ((0.4 * float(attnGrade)) + (0.2 * float(majorExam)) + (0.2 * float(classStandingGrade)) + (0.2 * float(self.finals.get("majorExam")))) * 0.4
        else:
            return 0

    def overALl_grade(self):
        return self.prelim_grade() + self.midterm_grade() + self.semi_final_grade() + self.finals_grade()
# ------------------------------------------------------
    # print result
    def print_result(self,name,section):
        isDone = False
        print("\n\nName : ",name)
        print("Section: ",section)
        print("="*90)
        self.print_prelim()
        print("=" * 90)
        self.print_midterm()
        print("=" * 90)
        self.print_semiFinals()
        print("=" * 90)
        self.print_finals()
        print("=" * 90)
        print("\n\n")
        print("=" * 100)
        self.displayGrades()
        print("=" * 100)
        return True

# ------------------------------------------------------
    def displayGrades(self):
        print("************ GRADES")
        print("| {:<{prelim}} | {:<{midterm}} | {:<{semi_final}} | {:<{finals}} | {:<{all}}".format("PRELIM",
                                                                                                     "MIDTERM",
                                                                                                     "SEMI-FINAL",
                                                                                                     "FINALS",
                                                                                                     "OVER ALL",
                                                                                                     prelim=20,
                                                                                                     midterm=20,
                                                                                                     semi_final=20,
                                                                                                     finals=20,
                                                                                                     all = 20))

        print("| {:<{prelim}} | {:<{midterm}} | {:<{semi_final}} | {:<{finals}} | {:<{all}}".format(str(f"%.1f"%self.prelim_grade()),
                                                                                                    str(f"%.1f"%self.midterm_grade()),
                                                                                                    str(f"%.1f"%self.semi_final_grade()),
                                                                                                    str(f"%.1f"%self.finals_grade()),
                                                                                                    str(f"%.1f"%self.overALl_grade()),
                                                                                                    prelim=20,
                                                                                                    midterm=20,
                                                                                                    semi_final=20,
                                                                                                    finals=20,
                                                                                                    all=20))
# ------------------------------------------------------



    def format(self,opt):
        name = ""
        term = None
        if opt == 1:
            name = "PRELIM"
            term = self.prelim
        elif opt == 2:
            name = "MIDTERM"
            term = self.midterm
        elif opt == 3:
            name = "SEMI-FINALS"
            term = self.semiFinals
        elif opt == 4:
            name = "FINALS"
            term = self.finals

        print("| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(name ,"Attendance","Class Standing","Major Exam",
                                                                                    name_width=20,
                                                                                    atten_width=26,
                                                                                    class_width=18,
                                                                                    exam_width=18))
        if term.get("classStanding"):
            quiz = term.get("classStanding").get("quiz")
            activity = term.get("classStanding").get("activity")
            caseStudy = self.prelim.get("classStanding").get("caseStudy")

            classStanding = [quiz,activity,caseStudy]
        else:
            classStanding = 0

        if len(term.get("attendance")) != 0 and len(term.get("classStanding")) !=0 and term.get("majorExam") > 0:
            for item in range(len(term.get("attendance"))):
                if item == 0:
                    print(
                        "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                               str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "date")) + " - " + str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "remarks")),
                                                                                                               str(
                                                                                                                   classStanding[
                                                                                                                       item]),
                                                                                                               str(term.get(
                                                                                                                   "majorExam")),
                                                                                                               name_width=20,
                                                                                                               atten_width=26,
                                                                                                               class_width=18,
                                                                                                               exam_width=18))
                    continue
                if (not (item > len(classStanding)) if classStanding else False):
                    print("| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                                 str(
                                                                                                                     term.get(
                                                                                                                         "attendance")[
                                                                                                                         item].get(
                                                                                                                         "date")) + " - " + str(
                                                                                                                     term.get(
                                                                                                                         "attendance")[
                                                                                                                         item].get(
                                                                                                                         "remarks")),
                                                                                                                 str(
                                                                                                                     classStanding[
                                                                                                                         item]),
                                                                                                                 " ",
                                                                                                                 name_width=20,
                                                                                                                 atten_width=26,
                                                                                                                 class_width=18,
                                                                                                                 exam_width=18))
                else:
                    print(
                        "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                               str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "date")) + " - " + str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "remarks")),
                                                                                                               " ",
                                                                                                               " ",
                                                                                                               name_width=20,
                                                                                                               atten_width=26,
                                                                                                               class_width=18,
                                                                                                               exam_width=18))
        elif len(term.get("attendance")) != 0 and len(term.get("classStanding")) !=0:
            for item in range(len(term.get("attendance"))):
                if (not (item > len(classStanding)) if classStanding else False):
                    print("| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                                 str(
                                                                                                                     term.get(
                                                                                                                         "attendance")[
                                                                                                                         item].get(
                                                                                                                         "date")) + " - " + str(
                                                                                                                     term.get(
                                                                                                                         "attendance")[
                                                                                                                         item].get(
                                                                                                                         "remarks")),
                                                                                                                 str(
                                                                                                                     classStanding[
                                                                                                                         item]),
                                                                                                                 " ",
                                                                                                                 name_width=20,
                                                                                                                 atten_width=26,
                                                                                                                 class_width=18,
                                                                                                                 exam_width=18))
                else:
                    print(
                        "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                               str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "date")) + " - " + str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "remarks")),
                                                                                                               " ",
                                                                                                               " ",
                                                                                                               name_width=20,
                                                                                                               atten_width=26,
                                                                                                               class_width=18,
                                                                                                               exam_width=18))
        elif len(term.get("attendance")) != 0 and term.get("majorExam") > 0:
            for item in range(len(term.get("attendance"))):
                if item == 0:
                    print(
                        "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                               str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "date")) + " - " + str(
                                                                                                                   term.get(
                                                                                                                       "attendance")[
                                                                                                                       item].get(
                                                                                                                       "remarks"))," ",
                                                                                                               str(term.get(
                                                                                                                   "majorExam")),
                                                                                                               name_width=20,
                                                                                                               atten_width=26,
                                                                                                               class_width=18,
                                                                                                               exam_width=18))
                    continue
                print(
                    "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                           str(
                                                                                                               term.get(
                                                                                                                   "attendance")[
                                                                                                                   item].get(
                                                                                                                   "date")) + " - " + str(
                                                                                                               term.get(
                                                                                                                   "attendance")[
                                                                                                                   item].get(
                                                                                                                   "remarks")),
                                                                                                           " ",
                                                                                                           " ",
                                                                                                           name_width=20,
                                                                                                           atten_width=26,
                                                                                                           class_width=18,
                                                                                                           exam_width=18))
        elif len(term.get("attendance")) != 0:
            for item in range(len(term.get("attendance"))):
                print(
                    "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                           str(
                                                                                                               term.get(
                                                                                                                   "attendance")[
                                                                                                                   item].get(
                                                                                                                   "date")) + " - " + str(
                                                                                                               term.get(
                                                                                                                   "attendance")[
                                                                                                                   item].get(
                                                                                                                   "remarks")),
                                                                                                           " ",
                                                                                                           " ",
                                                                                                           name_width=20,
                                                                                                           atten_width=26,
                                                                                                           class_width=18,
                                                                                                           exam_width=18))
        elif len(term.get("classStanding")) !=0 and term.get("majorExam") > 0:
            print(
                "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                      " ",
                                                                                                       term.get("classStanding").get("quiz"),
                                                                                                       term.get("majorExam"),
                                                                                                       name_width=20,
                                                                                                       atten_width=26,
                                                                                                       class_width=18,
                                                                                                       exam_width=18))
            print(
                "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                       " ",
                                                                                                       term.get(
                                                                                                           "classStanding").get(
                                                                                                           "activity"),
                                                                                                       " ",
                                                                                                       name_width=20,
                                                                                                       atten_width=26,
                                                                                                       class_width=18,
                                                                                                       exam_width=18))
            print(
                "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                       " ",
                                                                                                       term.get(
                                                                                                           "classStanding").get(
                                                                                                           "caseStudy"),
                                                                                                       " ",
                                                                                                       name_width=20,
                                                                                                       atten_width=26,
                                                                                                       class_width=18,
                                                                                                       exam_width=18))
        elif len(term.get("classStanding")) !=0:
            for item in  classStanding:
                print(
                    "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                           " ",
                                                                                                           item,
                                                                                                           " ",
                                                                                                           name_width=20,
                                                                                                           atten_width=26,
                                                                                                           class_width=18,
                                                                                                           exam_width=18))
        elif term.get("majorExam") > 0:
            print(
                "| {:<{name_width}} | {:<{atten_width}} | {:<{class_width}} | {:<{exam_width}}".format(" ",
                                                                                                       " ",
                                                                                                       " ",
                                                                                                       term.get("majorExam"),
                                                                                                       name_width=20,
                                                                                                       atten_width=26,
                                                                                                       class_width=18,
                                                                                                       exam_width=18))

 #--------------------------------------------------------
    def print_prelim(self):
        self.format(1)

    def print_midterm(self):
        self.format(2)

    def print_semiFinals(self):
        self.format(3)
    def print_finals(self):
        self.format(4)