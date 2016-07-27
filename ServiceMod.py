import easygui


# TODO: In next version use easygui.multenterbox instead of independent enterbox


class Service:
    def __init__(self):
        self.employerName = easygui.enterbox(msg="Enter Name of Employer", title="Service Visit Inputs")
        self.employerAddr = easygui.enterbox(msg="Enter Address of Employer", title="Service Visit Inputs")
        self.dateOfJoining = easygui.enterbox(msg="Enter Date of Joining (dd/mm/yyyy)", title="Service Visit Inputs")
        self.dateOfCnfrmtn = easygui.enterbox(msg="Enter Date of Confirmation (dd/mm/yyyy)",
                                              title="Service Visit Inputs")
        self.phnNo = easygui.enterbox(msg="Enter Mobile Phone Number", title="Service Visit Inputs")
        self.telNo = easygui.enterbox(msg="Enter Telephone Number", title="Service Visit Inputs")
        self.desig = easygui.enterbox(msg="Enter Designation of Applicant", title="Service Visit Inputs")
        self.nameVerif = easygui.boolbox(msg="Was Name of Applicant Verified on Visit?",
                                         title="Service Visit Inputs")
        self.addrVerif = easygui.boolbox(msg="Was Address of Applicant's Office Verified on Visit?",
                                         title="Service Visit Inputs")
        self.desigVerif = easygui.boolbox(msg="Was Designation of Applicant Verified on Visit?",
                                          title="Service Visit Inputs")
        self.dateofVisit = easygui.enterbox(msg="Enter Date of Visit (dd/mm/yyyy)", title="Service Visit Inputs")
        self.timeofVisit = easygui.enterbox(msg="Enter Time of Visit", title="Service Visit Inputs")
        self.personContacted = easygui.enterbox(msg="Enter Name of Person Contacted", title="Service Visit Inputs")
        self.contactedDesig = easygui.enterbox(msg="Designation of Contacted Person", title="Service Visit Inputs")
        self.mobileNo = easygui.enterbox(msg="Enter Mobile Number of Contacted Person", title="Service Visit Inputs")
        self.yrsBusiness = easygui.enterbox(msg="Number of Years in Present Employment", title="Service Visit Inputs")
        self.visitingCard = easygui.boolbox(msg="Was visiting Card of Contacted Person Obtained?",
                                            title="Service Visit Inputs")
        self.busiNature = easygui.enterbox(msg="Enter Nature of Business", title="Service Visit Inputs")
        self.applJob = easygui.choicebox(msg="Select Type of Job of Applicant?", title="Service Visit Inputs",
                                         choices=["Permanent", "Probation", "Contract Worker", "Temporary Worker",
                                                  "Others"])
        self.applWorkingAs = easygui.choicebox(msg="Applicant is working in Organisation as:-",
                                               title="Service Visit Inputs",
                                               choices=["Typist", "Stenographer", "Supervisor", "Junior Management",
                                                        "Middle Management", "Senior Management", "Other Management"])
        self.tranferable = easygui.boolbox(msg="Is Applicant's Job transferable or not?", title="Service Visit Inputs")
        self.salaryVerifierName = easygui.enterbox(msg="Enter Name of Person who verified Salary Details of Applicant",
                                                   title="Service Visit Inputs")
        self.salaryVerifierDesig = easygui.enterbox(msg="Enter Designation of Person who verified"
                                                        " Salary Details of Applicant", title="")
        self.boolRecom = easygui.boolbox(msg="Select one of following", title="Service Visit Inputs",
                                         choices=["Recommended", "Not Recommended"])
        self.remarks = easygui.enterbox(msg="Enter Any Other Remarks", title="Service Visit Inputs")
