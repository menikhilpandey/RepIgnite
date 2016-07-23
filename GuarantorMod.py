import easygui


class Guarantor:

    def __init__(self):
        self.enterlist = easygui.multenterbox(msg="Enter Guarantor Details", title="Guarantor Details",
                                              fields=["Name of Guarantor", "Address of Guarantor", "DOB of Guarantor",
                                                      "Mob Number of Guarantor", "Name of Guarantor's Employer",
                                                      "Address of Guarantor's Employer", "Designation of Guarantor",
                                                      "Guarantor's Relation with Applicant", "Date of Visit(dd/mm/yyyy",
                                                      "Time of Visit(HH:MM AM/PM)", "Name of Person Contacted",
                                                      "Relation of Contacted Person to Guarantor",
                                                      "Since How many Years have Guarantor known the applicant?",
                                                      "Marital Status of Guarantor", "Number of Family members",
                                                      "No of Working Family members", "No of Dependent Family Members",
                                                      "No of Pensioners in Family", "No of Children in Family",
                                                      "Guarantor Residing on Address since(Years)"])
        self.name = self.enterlist[0]
        self.address = self.enterlist[1]
        self.dob = self.enterlist[2]
        self.mobNo = self.enterlist[3]
        self.employerName = self.enterlist[4]
        self.employerAddr = self.enterlist[5]
        self.GuarDesign = self.enterlist[6]
        self.relation2Appl = self.enterlist[7]
        self.dateofVisit = self.enterlist[8]
        self.timeofVisit = self.enterlist[9]
        self.personContacted = self.enterlist[10]
        self.relation2Guarantor = self.enterlist[11]
        self.yrsKnown = self.enterlist[12]
        self.maritalStatus = self.enterlist[13]
        self.FamilyNumber = self.enterlist[14]
        self.workingMems = self.enterlist[15]
        self.dependentMems = self.enterlist[16]
        self.pensioners = self.enterlist[17]
        self.childrens = self.enterlist[18]
        self.residingSince = self.enterlist[19]

        self.residentialStatus = easygui.choicebox(msg="Select Residential Status", title="Guarantor Details",
                                                   choices=["Self Owned", "Owned By Relatives", "Rented",
                                                            "Paying Guest",
                                                            "Owned by Parents", "Owned by Parents", "Owned by Friends",
                                                            "Company Accomodation"])
        self.workingSpouse = easygui.boolbox(msg="Is Spouse Working?", title="Guarantor Details")
        if self.workingSpouse:
            self.spouseEmploymentDetails = easygui.enterbox(msg="Enter Employment Details for Spouse",
                                                            title="Guarantor Details")
        self.GuarOtherLoan = easygui.boolbox(msg="Is Guarantor a guarantee of other loan?", title="Guarantor Details")
        self.awareOfLiablity = easygui.boolbox(msg="Is Guarantor Aware of his liability as Guarantor?",
                                               title="Guarantor Details")
        self.awareOfQuantum = easygui.boolbox(msg="Is Guarantor Aware of loan Quantum?", title="Guarantor Details")
        self.boolRecom = easygui.boolbox(msg="Select one of following", title="Guarantor Details",
                                         choices=["Recommended", "Not Recommended"])
        self.remarks = easygui.enterbox(msg="Enter Any Other Remarks", title="Guarantor Details")
