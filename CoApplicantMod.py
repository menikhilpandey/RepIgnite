import easygui


class CoApplicant:
    def __init__(self):
        self.enterlist = easygui.multenterbox(msg="Fill Co-Applicant Details", title="Co Applicant Details",
                                              fields=["Name", "Father's Name", "Mobile No.", "Telephone No.",
                                                      "DOB(dd/mm/yyyy)", "Marital Status", "PAN Number"])
        self.Name = self.enterlist[0]
        self.FatherName = self.enterlist[1]
        self.MobNo = self.enterlist[2]
        self.TelNo = self.enterlist[3]
        self.DOB = self.enterlist[4]
        self.MaritalStatus = self.enterlist[5]
        self.panNo = self.enterlist[6]
        self.sameAddress = easygui.boolbox(msg="Does Co-Applicant Have same Address as Applicant ?",
                                           title="Enter CoApplicant Details")
        if not self.sameAddress:
            self.Address = easygui.enterbox(msg="Enter Co-Aplplicant's Address", title="Enter CoApplicant Details")
            self.ResidingSince = easygui.enterbox(msg="Residing on Address Since (No. of Years)",
                                                  title="Enter CoApplicant Details")
        else:
            self.Address = None
            self.ResidingSince = None
