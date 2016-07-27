from Tkinter import *

import os
import pickle
import easygui
import ServiceMod
import BusinessMod
import CoApplicantMod
import GuarantorMod
import ReferenceMod
import ResidenceVerifMod


class Applicant:
    def __init__(self):
        self.Branch = None
        self.FileNo = None
        self.FileDate = None
        self.DSAName = None
        self.ApplName = None
        self.ApplFatherName = None
        self.ApplAddress = None
        self.ResidingSince = None
        self.ApplMobNo = None
        self.ApplTelNo = None
        self.ApplDOB = None
        self.ApplMaritalStatus = None
        self.panNo = None
        self.guarantor = False
        self.CoApplicant = False
        self.ApplType = None
        self.BusinessObj = None
        self.ServiceObj = None
        self.CoApplicantObj = None
        self.GuarantorObj = None
        self.OfficeTVerif = None
        self.ResidenceTVerif = None
        self.ReferenceTVerif = None
        self.ResidenceVerif = None
        self.enterlist = None
        self.rep_status = None

    def fill_details(self):
        self.Branch = easygui.choicebox(msg="Select Branch Name", title="New Allocation",
                                        choices=["Gurgaon", "Dwarka", "Delhi(Barakhamba Road)", "Noida",
                                                 "Greater Noida", "Meerut", "Ghaziabad", "Netaji Subhash Place"])
        self.enterlist = easygui.multenterbox(msg="Enter Allocation Details", title="New Allocation",
                                              fields=["File Number", "Date of Receiving of File (dd/mm/yyyy)",
                                                      "DSA Name", "Applicant's Name", "Applicant's Father Name",
                                                      "Applicant's Address",
                                                      "Applicant residing on Address Since (Years)",
                                                      "Applicant's Mobile Number", "Applicant's Telephone Number",
                                                      "Applicant's DOB (dd/mm/yyyy)", "Applicant's Martial Status",
                                                      "Applicant's PAN Number"])
        self.FileNo = self.enterlist[0]
        self.FileDate = self.enterlist[1]
        self.DSAName = self.enterlist[2]
        self.ApplName = self.enterlist[3]
        self.ApplFatherName = self.enterlist[4]
        self.ApplAddress = self.enterlist[5]
        self.ResidingSince = self.enterlist[6]
        self.ApplMobNo = self.enterlist[7]
        self.ApplTelNo = self.enterlist[8]
        self.ApplDOB = self.enterlist[9]
        self.ApplMaritalStatus = self.enterlist[10]
        self.panNo = self.enterlist[11]

    def set_appl_type(self, appltype):
        self.ApplType = appltype
        if self.ApplType == "Business":
            self.BusinessObj = BusinessMod.Business()
        elif self.ApplType == "Service":
            self.ServiceObj = ServiceMod.Service()

    def fill_guarantor(self):
        self.guarantor = True
        self.GuarantorObj = GuarantorMod.Guarantor()

    def fill_co_appl(self):
        self.CoApplicant = True
        self.CoApplicantObj = CoApplicantMod.CoApplicant()
        if self.CoApplicantObj.sameAddress:
            self.CoApplicantObj.Address = self.ApplAddress
            self.CoApplicantObj.ResidingSince = self.ResidingSince

    def fill_office_verif(self):
        self.OfficeTVerif = ReferenceMod.OfficeTVerify()

    def fill_residence_verif(self):
        self.ResidenceTVerif = ReferenceMod.ResidenceTVerify()

    def fill_reference_verif(self):
        self.ReferenceTVerif = ReferenceMod.ReferenceTVerify()

    def fill_residence_visit(self):
        self.ResidenceVerif = ResidenceVerifMod.Residence()


def save2file(rep_obj):
    rep_obj.rep_status = easygui.buttonbox(msg="Select Status of This Report", title="Save Report",
                                           choices=["Complete", "Pending"], default_choice="Pending",
                                           cancel_choice="Pending")
    output_file_loc = "Test Data\data.rep"
    if os.path.isfile(output_file_loc):
        with open(output_file_loc, 'rb') as output:
            objects = []
            try:
                while True:
                    objects.append(pickle.load(output))
            except EOFError:
                pass
        with open(output_file_loc, 'wb') as output:
            flag = 1
            for i in objects:
                if i.panNo == rep_obj.panNo:
                    # TODO: Provide view of both conflicting reports
                    flag = easygui.boolbox("Report with Same PAN No. exists, Continue saving this Report?",
                                           choices=["Yes", "No"], title="Save Report", default_choice="Yes",
                                           cancel_choice="No")
                    keep_other_obj = easygui.boolbox("Do you want to keep Existing Report with Same PAN?",
                                                     choices=["Yes", "No"], title="Keep Report", default_choice="Yes",
                                                     cancel_choice="No")
                    if keep_other_obj:
                        pickle.dump(i, output)
                else:
                    pickle.dump(i, output)
            if flag:
                pickle.dump(rep_obj, output)
    else:
        with open(output_file_loc, 'wb') as output:
            pickle.dump(rep_obj, output)


def create(rep_obj=None):
    if rep_obj:
        print rep_obj.ApplName
    else:
        print "Fresh Entry"
    # TODO: Continue Implementing Edit Feature
    window = Tk(className="Create Report")
    new_appl = Applicant()

    btn_new_alloc = Button(window, text="Fill File Allocation Details", width=30, command=new_appl.fill_details)
    btn_resi_verif = Button(window, text="Fill Residence Verification Inputs", width=30,
                            command=new_appl.fill_residence_visit)
    lbl_appl_type = Label(window, text="Select Applicant Type")
    btn_business_type = Button(window, text="Business", width=10, command=lambda: new_appl.set_appl_type("Business"))
    btn_service_type = Button(window, text="Service", width=10, command=lambda: new_appl.set_appl_type("Service"))
    lbl_tele_verif = Label(window, text="Tele-Verification")
    buttonguarantor = Button(window, text="Enter Guarantor Details", command=new_appl.fill_guarantor)
    button_co_applicant = Button(window, text="Enter CoApplicant Details", command=new_appl.fill_co_appl)
    btn_residence_verif = Button(window, text="Residence", width=10, command=new_appl.fill_residence_verif)
    btn_office_verif = Button(window, text="Office", width=10, command=new_appl.fill_office_verif)
    btn_reference_verif = Button(window, text="Reference", width=10, command=new_appl.fill_reference_verif)

    btn_new_alloc.grid(row=1, columnspan=2)
    btn_resi_verif.grid(row=3, columnspan=2)
    lbl_appl_type.grid(row=5, sticky=W)
    btn_business_type.grid(row=5, column=1, sticky=W)
    btn_service_type.grid(row=6, column=1, sticky=W)
    lbl_tele_verif.grid(row=8, sticky=W)
    btn_residence_verif.grid(row=8, column=1, sticky=W)
    btn_office_verif.grid(row=9, column=1, sticky=W)
    btn_reference_verif.grid(row=10, column=1, sticky=W)
    buttonguarantor.grid(row=12, sticky=W)
    button_co_applicant.grid(row=12, column=1, sticky=W)

    # Blank Labels for Better GUI (making space after Business/Service Choice and after Save Appl Details
    blank_lbl1 = Label(window)
    blank_lbl2 = Label(window)
    blank_lbl3 = Label(window)
    blank_lbl4 = Label(window)
    blank_lbl5 = Label(window)
    blank_lbl6 = Label(window)

    blank_lbl1.grid(row=0)
    blank_lbl2.grid(row=2)
    blank_lbl3.grid(row=4)
    blank_lbl4.grid(row=7)
    blank_lbl5.grid(row=11)
    blank_lbl6.grid(row=13)

    btn_save = Button(window, text="Save Report", width=15, command=lambda: save2file(new_appl))
    btn_save.grid(row=14, columnspan=2)

    btn_exit = Button(window, text="Exit", width=15, command=lambda: window.destroy())
    btn_exit.grid(row=15, columnspan=2)

    window.mainloop()
