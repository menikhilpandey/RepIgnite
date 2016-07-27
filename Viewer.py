from Tkinter import *

import pickle
import easygui


def display_header(win):
    lbl_s_no = Label(win, text="S.No.", width=5)
    lbl_branch = Label(win, text="Branch Name", width=25)
    lbl_dsa_name = Label(win, text="DSA Name", width=20)
    lbl_appl_name = Label(win, text="Applicant Name", width=20)
    lbl_appl_address = Label(win, text="Applicant Address", width=50)
    lbl_appl_mob_no = Label(win, text="Mobile Number", width=12)
    lbl_pan_no = Label(win, text="PAN Number", width=13)
    lbl_rep_status = Label(win, text="Status", width=8)

    lbl_s_no.grid(row=0)
    lbl_branch.grid(row=0, column=1)
    lbl_dsa_name.grid(row=0, column=2)
    lbl_appl_name.grid(row=0, column=3)
    lbl_appl_address.grid(row=0, column=4)
    lbl_appl_mob_no.grid(row=0, column=5)
    lbl_pan_no.grid(row=0, column=6)
    lbl_rep_status.grid(row=0, column=7)


def viewall():
    window = Tk(className="View All Reports")
    object_list = list()
    try:
        with open("Test Data\data.rep", 'rb') as inputFile:
            while True:
                try:
                    object_w = pickle.load(inputFile)
                    object_list.append(object_w)
                except EOFError:
                    break
    except IOError:
        easygui.msgbox(msg="You have no Reports in System, Create one First!!", title="No Reports")
        window.destroy()
        return
    display_header(window)
    for j, i in enumerate(object_list):
        lbl_s_no = Label(window, text=str(j + 1), width=5)
        lbl_branch = Label(window, text=i.Branch, width=25)
        lbl_dsa_name = Label(window, text=i.DSAName, width=20)
        lbl_appl_name = Label(window, text=i.ApplName, width=20)
        lbl_appl_address = Label(window, text=i.ApplAddress, width=50)
        lbl_appl_mob_no = Label(window, text=i.ApplMobNo, width=12)
        lbl_pan_no = Label(window, text=i.panNo, width=13)
        lbl_rep_status = Label(window, text=i.rep_status, width=8)

        lbl_s_no.grid(row=j + 1)
        lbl_branch.grid(row=j + 1, column=1)
        lbl_dsa_name.grid(row=j + 1, column=2)
        lbl_appl_name.grid(row=j + 1, column=3)
        lbl_appl_address.grid(row=j + 1, column=4)
        lbl_appl_mob_no.grid(row=j + 1, column=5)
        lbl_pan_no.grid(row=j + 1, column=6)
        lbl_rep_status.grid(row=j + 1, column=7)

    window.mainloop()
