from Tkinter import *

import pickle
import easygui


def display_header(win):
    lbl_s_no = Label(win, text="S.No.", width=4)
    lbl_branch = Label(win, text="Branch Name", width=20)
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


def fill_details(rep_obj):
    # TODO: Include Edit Feature
    pass


def audit_details(rep_obj):
    # TODO: Include Edit Feature
    pass


def print_report(rep_obj):
    # TODO: Include Edit Feature
    pass


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
        lbl_s_no = Label(window, text=str(j + 1), width=4)
        lbl_branch = Label(window, text=i.Branch, width=20)
        lbl_dsa_name = Label(window, text=i.DSAName, width=20)
        lbl_appl_name = Label(window, text=i.ApplName, width=20)
        lbl_appl_address = Label(window, text=i.ApplAddress, width=50)
        lbl_appl_mob_no = Label(window, text=i.ApplMobNo, width=12)
        lbl_pan_no = Label(window, text=i.panNo, width=13)
        lbl_rep_status = Label(window, text=i.rep_status, width=8)
        # lambda i=i, inspired by
        # https://stackoverflow.com/questions/10865116/
        # python-tkinter-creating-buttons-in-for-loop-passing-command-arguments/
        # 10865170#10865170?newreg=2725042c8f9449998b9890725cdeeb68
        # --All it does is store the info of which 'i' to use when lambda is defined.
        btn_fill_details = Button(window, text="Field Report", command=lambda obj_lamb=i: fill_details(obj_lamb))
        btn_view_all_details = Button(window, text="Audit Details", command=lambda obj_lamb=i: audit_details(obj_lamb))
        btn_print_report = Button(window, text="Print Report", command=lambda obj_lamb=i: print_report(obj_lamb))
        if i.rep_status == "Pending":
            btn_view_all_details.config(state='disabled')
            btn_print_report.config(state='disabled')

        lbl_s_no.grid(row=j + 1)
        lbl_branch.grid(row=j + 1, column=1)
        lbl_dsa_name.grid(row=j + 1, column=2)
        lbl_appl_name.grid(row=j + 1, column=3)
        lbl_appl_address.grid(row=j + 1, column=4)
        lbl_appl_mob_no.grid(row=j + 1, column=5)
        lbl_pan_no.grid(row=j + 1, column=6)
        lbl_rep_status.grid(row=j + 1, column=7)
        btn_fill_details.grid(row=j + 1, column=8)
        btn_view_all_details.grid(row=j + 1, column=9)
        btn_print_report.grid(row=j + 1, column=10)

    window.mainloop()
