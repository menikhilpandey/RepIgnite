import easygui


class OfficeTVerify:
    def __init__(self):
        self.verifName = easygui.boolbox(msg="Verified Name of Applicant & CoApplicant",
                                         title="Office Tele-Verification")
        self.enterlist = easygui.multenterbox(msg="Fill Office Tele-Verification Report",
                                              title="Office Tele-Verification",
                                              fields=["Office Address", "Tel. No./ Mob. No. of Contacted Person",
                                                      "Name of Contacted Person", "Designation of Contacted Person",
                                                      "Enter Organisation Name", "Enter Applicant Designation",
                                                      "Appicant Working Since", "Nature of Business of Organisation",
                                                      "Appicant Reporting To", "Which Call Attempt?",
                                                      "Enter Call Date (dd/mm/yyyy)", "Enter Call Time"])
        self.officeAdd = self.enterlist[0]
        self.telNo = self.enterlist[1]
        self.contactPerson = self.enterlist[2]
        self.DesigContactPerson = self.enterlist[3]
        self.OrganisationName = self.enterlist[4]
        self.ApplDesig = self.enterlist[5]
        self.workingSince = self.enterlist[6]
        self.BusinessNature = self.enterlist[7]
        self.reportingTo = self.enterlist[8]
        self.attempt = self.enterlist[9]
        self.callDate = self.enterlist[10]
        self.callTime = self.enterlist[11]
        self.Outcome = easygui.choicebox(msg="Enter Outcome", title="Office Tele-Verification",
                                         choices=["Contacted", "Not Contacted", "Constantly Engaged", "No Response"])
        self.boolRecom = easygui.boolbox(msg="Select one of following", title="Office Tele-Verification",
                                         choices=["Recommended", "Not Recommended"])
        self.remarks = easygui.enterbox(msg="Enter Any Other Remarks", title="Office Tele-Verification")


class ResidenceTVerify:
    def __init__(self):
        self.verifName = easygui.boolbox(msg="Verified Name of Applicant & CoApplicant",
                                         title="Residence Tele-Verification")
        self.enterlist = easygui.multenterbox(msg="Fill Residence Tele-Verification Report",
                                              title="Residence Tele-Verification",
                                              fields=["Name of Contacted Person",
                                                      "Relation of Contacted Person with Applicant",
                                                      "Tel. No./ Mob. No. of Contacted Person",
                                                      "Address supplied by Contacted Person",
                                                      "Which Call Attempt?", "Enter Call Date (dd/mm/yyyy)",
                                                      "Enter Call Time"])
        self.contactPerson = self.enterlist[0]
        self.relation = self.enterlist[1]
        self.telNo = self.enterlist[2]
        self.address = self.enterlist[3]
        self.attempt = self.enterlist[4]
        self.callDate = self.enterlist[5]
        self.callTime = self.enterlist[6]
        self.residenceType = easygui.choicebox(msg="Select Residence Type", title="Residence Tele-Verification",
                                               choices=["Self Owned", "Owned By Relatives", "Rented",
                                                        "Paying Guest",
                                                        "Owned by Parents", "Owned by Parents", "Owned by Friends",
                                                        "Company Accomodation"])
        self.Outcome = easygui.choicebox(msg="Enter Outcome", title="Residence Tele-Verification",
                                         choices=["Contacted", "Not Contacted", "Constantly Engaged", "No Response"])
        self.boolRecom = easygui.boolbox(msg="Select one of following", title="Residence Tele-Verification",
                                         choices=["Recommended", "Not Recommended"])
        self.remarks = easygui.enterbox(msg="Enter Any Other Remarks", title="Residence Tele-Verification")


class ReferenceTVerify:
    def __init__(self):
        self.enterlist1 = easygui.multenterbox(msg="Enter Details for Refree 1", title="Reference Tele-Verification",
                                               fields=["Name", "Tel. No./ Mob. No.", "Address",
                                                       "Name of Contacted Person", "Relation with Applicant",
                                                       "Since How Long Refree knows Applicant?"])
        self.name = self.enterlist1[0]
        self.telNo = self.enterlist1[1]
        self.address = self.enterlist1[2]
        self.contactPerson = self.enterlist1[3]
        self.relation = self.enterlist1[4]
        self.knownSince = self.enterlist1[5]
        self.residenceType = easygui.choicebox(msg="Select Residence Type of Refree 1",
                                               title="Reference Tele-Verification",
                                               choices=["Self Owned", "Owned By Relatives", "Rented",
                                                        "Paying Guest",
                                                        "Owned by Parents", "Owned by Parents", "Owned by Friends",
                                                        "Company Accomodation"])
        self.boolRecom = easygui.boolbox(msg="Select Whether Refree 1 recommends Applicant or not?",
                                         title="Reference Tele-Verification",
                                         choices=["Recommended", "Not Recommended"])

        self.enterlist2 = easygui.multenterbox(msg="Enter Details for Refree 2", title="Reference Tele-Verification",
                                               fields=["Name", "Tel. No./ Mob. No.", "Address",
                                                       "Name of Contacted Person", "Relation with Applicant",
                                                       "Since How Long Refree knows Applicant?"])
        self.name = self.enterlist2[0]
        self.telNo = self.enterlist2[1]
        self.address = self.enterlist2[2]
        self.contactPerson = self.enterlist2[3]
        self.relation = self.enterlist2[4]
        self.knownSince = self.enterlist2[5]
        self.residenceType = easygui.choicebox(msg="Select Residence Type of Refree 2",
                                               title="Reference Tele-Verification",
                                               choices=["Self Owned", "Owned By Relatives", "Rented",
                                                        "Paying Guest",
                                                        "Owned by Parents", "Owned by Parents", "Owned by Friends",
                                                        "Company Accomodation"])
        self.boolRecom = easygui.boolbox(msg="Select Whether Refree 2 recommends Applicant or not?",
                                         title="Reference Tele-Verification",
                                         choices=["Recommended", "Not Recommended"])
