import easygui


# TODO: In next version use easygui.multenterbox instead of independent enterbox


class Residence:
    def __init__(self):
        self.PanCard = False
        self.RationCard = False
        self.DL = False
        self.VoterID = False
        self.Passport = False
        self.ElecBill = False
        self.PhoneBill = False
        self.Aadhar = False
        self.RentAgree = False
        self.IDbyEmp = False
        self.saleTaxCerti = False
        self.serviceTaxCerti = False
        self.resiLocked = easygui.boolbox(msg="Was Residence Locked at the time of visit?",
                                          title="Residence Visit Inputs")
        if self.resiLocked:
            self.neighbourInfoStay = easygui.boolbox(msg="""Neighbour Reply on 'Does the Applicant Stay at this
                                                         residence'""", title="Residence Visit Inputs")
            self.NoOfFamilyMembers = easygui.enterbox(msg="""Neighbour Reply on 'No of Family members living at
                                                          applicant's address'""", title="Residence Visit Inputs")
        easygui.msgbox(msg="Proceed to Enter Residential Details", title="Residence Visit Inputs")
        self.identity = easygui.multchoicebox(msg="Select Identity Proof Supplied on Residence Visit",
                                              title="Residence Visit Inputs",
                                              choices=["Pan Card", "Ration Card", "Driving License", "Voter ID Card",
                                                       "Passport", "Electricity Bill", "Phone Bill", "Aadhar Card",
                                                       "Rent Agreement", "ID Card Issued by Employer",
                                                       "Sale Tax Certificate", "Service Tax Certificate"])
        self.set_id_fields(self.identity)
        self.verified = easygui.multchoicebox(msg="Select Verified Inputs", title="Residence Visit Inputs",
                                              choices=["Name Verified", "Address Verified", "Name of Co-Applicant",
                                                       "Date of Birth"])
        self.ApplNameVerified = "No"
        self.addressVerfied = "No"
        self.coApplNameVerified = "No"
        self.DOBVerified = "No"
        if "Name Verified" in self.verified:
            self.ApplNameVerified = "Yes"
        if "Address Verified" in self.verified:
            self.addressVerfied = "Yes"
        if "Phone Number Verified" in self.verified:
            self.coApplNameVerified = "Yes"
        if "Date of Birth" in self.verified:
            self.DOBVerified = "Yes"
        self.dateofVisit = easygui.enterbox(msg="Enter Date of Visit (dd/mm/yyyy)", title="Residence Visit Inputs")
        self.timeofVisit = easygui.enterbox(msg="Enter Time of Visit", title="Residence Visit Inputs")
        self.personContacted = easygui.enterbox(msg="Enter Name of Person Contacted", title="Residence Visit Inputs")
        self.relation2Appl = easygui.enterbox(msg="Relationship of Contacted Person with Applicant",
                                              title="Residence Visit Inputs")
        self.residentialStatus = easygui.choicebox(msg="Select Residential Status", title="Residence Visit Inputs",
                                                   choices=["Self Owned", "Owned By Relatives", "Rented",
                                                            "Paying Guest",
                                                            "Owned by Parents", "Owned by Parents", "Owned by Friends",
                                                            "Company Accomodation"])

        self.maritalStatus = easygui.enterbox(msg="Enter Marital Status for Applicant", title="Residence Visit Inputs")
        self.FamilyNumber = easygui.enterbox(msg="Number of Family Member of Applicant", title="Residence Visit Inputs")
        self.workingMems = easygui.enterbox(msg="Number of Working Family Members", title="Residence Visit Inputs")
        self.dependentMems = easygui.enterbox(msg="Number of Dependent Family Members", title="Residence Visit Inputs")
        self.pensioners = easygui.enterbox(msg="Number of Pensioners in Family", title="Residence Visit Inputs")
        self.childrens = easygui.enterbox(msg="Number of Children in Family", title="Residence Visit Inputs")
        self.workingSpouse = easygui.boolbox(msg="Is Spouse Working?", title="Residence Visit Inputs")
        if self.workingSpouse:
            self.spouseEmploymentDetails = easygui.enterbox(msg="Enter Employment Details for Spouse",
                                                            title="Residence Visit Inputs")
        self.locality = easygui.choicebox(msg="What was the locality of Residence ?",
                                          title="Residence Visit Inputs",
                                          choices=["Posh Locality", "Village Area", "Lodging", "Upper Middle Class",
                                                   "Slum Locality", "Lower Middle Class", "Middle Class",
                                                   "Residential Complex", "Others"])
        self.vehicle = easygui.multchoicebox(msg="Select Vehicle Seen at Residence", title="Residence Visit Inputs",
                                             choices=["Two Wheeler", "Car", "Other"])
        self.regisNo = easygui.enterbox(msg="Enter Registration Number of Vehicle Seen", title="Residence Visit Inputs")
        self.howCoop = easygui.choicebox(msg="How Cooperative was the applicant?", title="Residence Visit Inputs",
                                         choices=["Rude", "Polite"])
        self.checkedWith = easygui.choicebox(msg="Checked with Whom?", title="Residence Visit Inputs",
                                             choices=["Neighbour", "Others"])
        self.checkerName = easygui.enterbox("Name of Person Checked with (Neighbour)", title="Residence Visit Inputs")
        self.checkerContact = easygui.enterbox("Contact of Person Checked with (Neighbour)",
                                               title="Residence Visit Inputs")
        self.checkerAddress = easygui.enterbox("Address of Person Checked with (Neighbour)",
                                               title="Residence Visit Inputs")
        self.checkerFeedback = easygui.boolbox(msg="Feedback from Person Checked (Neighbour)",
                                               title="Residence Visit Inputs", choices=["Positive", "Negative"])
        self.checkerRemarks = easygui.enterbox(msg="Enter Remarks of Person Checked with (Neighbour)",
                                               title="Residence Visit Inputs")
        self.resiAmbience = easygui.choicebox(msg="What was ambience in Residence?",
                                              title="Residence Visit Inputs",
                                              choices=["Good", "Average", "Poor"])
        self.exteriors = easygui.choicebox(msg="Comments on Exteriors of Residence",
                                           title="Residence Visit Inputs",
                                           choices=["Good", "Average", "Poor"])
        self.carpetArea = easygui.enterbox(msg="Enter Carpet Area of Residence (sq. metre)",
                                           title="Residence Visit Inputs")
        self.political = easygui.boolbox(msg="Was Portrait/Banner/Picture of Political Leader Seen?",
                                         title="Residence Visit Inputs")
        self.boolRecom = easygui.boolbox(msg="Select one of following", title="Residence Visit Inputs",
                                         choices=["Recommended", "Not Recommended"])
        self.remarks = easygui.enterbox(msg="Enter Any Other Remarks", title="Residence Visit Inputs")

    def set_id_fields(self, inp_list):
        if "Pan Card" in inp_list:
            self.PanCard = True
        if "Ration Card" in inp_list:
            self.RationCard = True
        if "Driving License" in inp_list:
            self.DL = True
        if "Voter ID Card" in inp_list:
            self.VoterID = True
        if "Passport" in inp_list:
            self.Passport = True
        if "Electricity Bill" in inp_list:
            self.ElecBill = True
        if "Phone Bill" in inp_list:
            self.PhoneBill = True
        if "Aadhar Card" in inp_list:
            self.Aadhar = True
        if "Rent Agreement" in inp_list:
            self.RentAgree = True
        if "ID Card Issued by Employer" in inp_list:
            self.IDbyEmp = True
        if "Sale Tax Certificate" in inp_list:
            self.saleTaxCerti = True
        if "Service Tax Certificate" in inp_list:
            self.serviceTaxCerti = True
