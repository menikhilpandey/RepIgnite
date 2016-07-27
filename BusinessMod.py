import easygui


# TODO: In next version use easygui.multenterbox instead of independent enterbox


class YearAssess:
    def __init__(self, assess_year):
        self.assesYear = assess_year
        self.wardNo = easygui.enterbox(msg="Enter Ward No for " + assess_year, title="ITR Verification")
        self.serialNo = easygui.enterbox(msg="Enter Serial No for " + assess_year, title="ITR Verification")
        self.fillingDate = easygui.enterbox(msg="Enter Date of Filling for " + assess_year + " (dd/mm/yyyy)",
                                            title="ITR Verification")
        self.totalInc = easygui.enterbox(msg="Enter Total Income for " + assess_year, title="ITR Verification")
        self.totalTaxInc = easygui.enterbox(msg="Enter Total Taxable Income for " + assess_year,
                                            title="ITR Verification")
        self.totalTaxPaid = easygui.enterbox(msg="Enter Total Tax Paid for " + assess_year, title="ITR Verification")
        self.fillingMode = easygui.choicebox(msg="Select Mode of Filling for " + assess_year, title="ITR Verification",
                                             choices=["e-Filling", "Manual"])


class ITRClass:
    def __init__(self):
        easygui.msgbox(msg="Fill ITR Verification Inputs", title="ITR Verification", ok_button="Proceed")
        self.pan = easygui.enterbox(msg="Enter PAN", title="ITR Verification")
        self.income = easygui.enterbox(msg="Enter Details of Income", title="ITR Verification")
        self.year1 = YearAssess(easygui.enterbox(msg="Enter 1st Assessment Year", title="ITR Verification"))
        self.year2 = YearAssess(easygui.enterbox(msg="Enter 2nd Assessment Year", title="ITR Verification"))
        self.year3 = YearAssess(easygui.enterbox(msg="Enter 3rd Assessment Year", title="ITR Verification"))
        self.remarks = easygui.enterbox(msg="Enter Remarks for ITR Verification", title="ITR Verification")


class Business:
    def __init__(self):
        self.firmName = easygui.enterbox(msg="Enter Name of Firm/Company", title="Business Visit Inputs")
        self.inceptionDate = easygui.enterbox(msg="Enter Date of Inception (dd/mm/yyyy)",
                                              title="Business Visit Inputs")
        self.address = easygui.enterbox(msg="Enter Address of Firm", title="Business Visit Inputs")
        self.tinNo = easygui.enterbox(msg="Enter TIN/CST Number", title="Business Visit Inputs")
        self.phnNO = easygui.enterbox(msg="Enter Phone Number", title="Business Visit Inputs")
        self.busiNature = easygui.enterbox(msg="Enter Nature of Business", title="Business Visit Inputs")
        self.ApplNameVerified = easygui.boolbox(msg="Was Applicant's Name Verified on Visit ?",
                                                title="Business Visit Inputs")
        self.addressVerfied = easygui.boolbox(msg="Was Office Address Verified on Visit ?",
                                              title="Business Visit Inputs")
        self.salaried_self = easygui.choicebox(msg="Select one of the following", title="Business Visit Inputs",
                                               choices=["Salaried", "Self Employed"])
        self.desig = easygui.enterbox(msg="Enter Designation of Applicant", title="Business Visit Inputs")
        self.dateofVisit = easygui.enterbox(msg="Enter Date of Visit (dd/mm/yyyy)", title="Business Visit Inputs")
        self.timeofVisit = easygui.enterbox(msg="Enter Time of Visit", title="Business Visit Inputs")
        self.personContacted = easygui.enterbox(msg="Enter Name of Person Contacted", title="Business Visit Inputs")
        self.contactedDesig = easygui.enterbox(msg="Designation of Contacted Person", title="Business Visit Inputs")
        self.mobileNo = easygui.enterbox(msg="Enter Mobile Number of Contacted Person", title="Business Visit Inputs")
        self.yrsBusiness = easygui.enterbox(msg="Number of Years in Present Business", title="Business Visit Inputs")
        self.visitingCard = easygui.boolbox(msg="Was visiting Card of Contacted Person Obtained?",
                                            title="Business Visit Inputs")
        self.typeofComp = easygui.choicebox(msg="Select Type of Company", title="Business Visit Inputs",
                                            choices=["Public Limited", "Partnership", "Proprietorship", "Other"])
        self.noOfemployees = easygui.enterbox(msg="Enter Number of Employees working in Business",
                                              title="Business Visit Inputs")
        self.noOfBranches = easygui.enterbox(msg="Number of Branches of Business", title="Business Visit Inputs")
        self.nameBoard = easygui.boolbox(msg="Was Name Board Seen at Building?", title="Business Visit Inputs")
        self.applNameVerifier = easygui.choicebox(msg="Applicant's Name was verified From?",
                                                  title="Business Visit Inputs",
                                                  choices=["Receptionist", "Colleauge", "Others"])
        self.resiAmbience = easygui.choicebox(msg="What was ambience of Office?",
                                              title="Business Visit Inputs",
                                              choices=["Good", "Average", "Poor"])
        self.exteriors = easygui.choicebox(msg="Comments on Exteriors of Office",
                                           title="Business Visit Inputs",
                                           choices=["Good", "Average", "Poor"])
        self.easy2locate = easygui.choicebox(msg="How easy was it to track the office?", title="Business Visit Inputs",
                                             choices=["Easy", "Difficult", "Untracable"])
        self.busiActivity = easygui.choicebox(msg="What was the Business Activity Observed?",
                                              title="Business Visit Inputs",
                                              choices=["High", "Medium", "Low"])
        self.workingMems = easygui.enterbox(msg="How many Employees were seen in Premises?",
                                            title="Business Visit Inputs")
        self.political = easygui.boolbox(msg="Was Portrait/Banner/Picture of Political Leader Seen?",
                                         title="Business Visit Inputs")
        self.ITR = ITRClass()
