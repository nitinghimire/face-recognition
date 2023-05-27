import pandas as pd
import os
import csv
import customtkinter
from tkinter import ttk
import tkinter as tk


class Attendance_table(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if (self._get_appearance_mode() == "dark"):
            style = ttk.Style()

            style.theme_use("default")

            style.configure("Treeview",
                            background="gray27",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="gray20",
                            bordercolor="gray20",
                            borderwidth=0)
            style.map('Treeview', background=[('selected', 'gray15')])

            style.configure("Treeview.Heading",
                            background="gray15",
                            foreground="white",
                            relief="flat")
            style.map("Treeview.Heading",
                      background=[('active', 'gray20')])
        else:
            style = ttk.Style()

            style.theme_use("default")

            style.configure("Treeview",
                            background="gray75",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="gray80",
                            bordercolor="gray80",
                            borderwidth=0)
            style.map('Treeview', background=[('selected', 'gray60')])

            style.configure("Treeview.Heading",
                            background="gray50",
                            foreground="black",
                            relief="flat")
            style.map("Treeview.Heading",
                      background=[('active', 'gray30')])

        self.yscroller = customtkinter.CTkScrollbar(
            self)
        self.yscroller.grid(row=0, column=1, sticky="nse", rowspan=2)

        columns = ("Roll",
                   "Name",
                   "Department",
                   "Semester",
                   "Time",
                   "Date",
                   "Remark")
        attendance_Tree = ttk.Treeview(
            self, columns=columns, show='headings', yscrollcommand=self.yscroller.set)
        self.yscroller.configure(command=attendance_Tree.yview)

        attendance_Tree.heading("Roll", text="Roll No")
        attendance_Tree.heading("Name", text="Name")
        attendance_Tree.heading("Department", text="Department")
        attendance_Tree.heading("Semester", text="Semester")
        attendance_Tree.heading("Time", text="Time")
        attendance_Tree.heading("Date", text="Date")
        attendance_Tree.heading("Remark", text="Remark")

        attendance_Tree.column("Department", width=400)

        attendance_Tree.grid(row=0, column=0)

        with open(r"E:\facerecognition\Attendance.csv", "r+", newline="\n") as file:
            dataList = file.readlines()
            data = []
            for line in dataList:
                entry = line.split((","))
                data.append((entry[0], entry[1], entry[2],
                            entry[3], entry[4], entry[5], entry[6]))
            for datum in data:
                attendance_Tree.insert("", tk.END, values=datum)


if __name__ == "__main__":
    app = Attendance_table()
    app.mainloop()
