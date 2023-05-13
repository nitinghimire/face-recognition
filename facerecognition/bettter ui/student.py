import customtkinter
import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import numpy as np
from CTkMessagebox import CTkMessagebox
from PIL import ImageEnhance, Image
import pandas as pd
from skimage import io
import matplotlib.pylab as plt


class Student(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Student Management System")
        self.geometry("1530x790")
        self.focus()

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

        self.var_dep = tkinter.StringVar()
        self.var_year = tkinter.StringVar()
        self.var_sem = tkinter.StringVar()
        self.var_course = tkinter.StringVar()
        self.var_id = tkinter.StringVar()
        self.var_name = tkinter.StringVar()
        self.var_dob = tkinter.StringVar()
        self.var_email = tkinter.StringVar()
        self.var_address = tkinter.StringVar()
        self.var_phone = tkinter.StringVar()
        self.var_gender = tkinter.StringVar()
        self.var_radio1 = tkinter.StringVar()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.iconbitmap(r'E:\facerecognition\bettter ui\icon.ico')

        self.title = customtkinter.CTkFrame(self,
                                            # bg_color="transparent",
                                            # fg_color="gray15"
                                            )
        self.title.grid(row=0, column=0,
                        padx=20, pady=20, sticky="nsew")
        self.title.grid_rowconfigure(1, weight=1)
        # self.title.grid_columnconfigure((0, 1), weight=1)
        self.title.grid_columnconfigure(0, weight=3)
        self.title.grid_columnconfigure(1, weight=1)
        self.student_title = customtkinter.CTkLabel(self.title,
                                                    font=(
                                                        "lucida bright", 50),
                                                    text="Student Information",
                                                    wraplength=0
                                                    )
        self.student_title.grid(row=0, column=0,
                                pady=(20, 0), columnspan=2, sticky="ew")

        self.left_frame = customtkinter.CTkFrame(self.title,
                                                 width=600,
                                                 height=650,
                                                 #  bg_color="transparent",
                                                 #  fg_color=["gray40", "gray18"],
                                                 corner_radius=0

                                                 )
        self.left_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.left_frame.grid_propagate(False)

        self.left_frame.grid_columnconfigure((1, 3), weight=1)

        self.right_frame = customtkinter.CTkFrame(self.title,
                                                  width=600,
                                                  height=650,
                                                  #   bg_color="transparent",
                                                  #   fg_color="gray18",
                                                  border_color="gray20",
                                                  corner_radius=0
                                                  )
        self.right_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.right_frame.grid_propagate(False)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)

        self.xscroller = customtkinter.CTkScrollbar(
            self.right_frame, orientation="horizontal")
        self.xscroller.grid(row=1, column=0, sticky="ews", columnspan=2)

        self.yscroller = customtkinter.CTkScrollbar(
            self.right_frame)
        self.yscroller.grid(row=0, column=1, sticky="nse", rowspan=2)

        self.depart_lbl = customtkinter.CTkLabel(self.left_frame, font=("lucida bright", 15),
                                                 text="Department"
                                                 )

        self.depart_lbl.grid(row=0, column=0, padx=20, pady=20)

        self.depart_option = customtkinter.CTkOptionMenu(self.left_frame, values=[
            "Department of Chemical Science & Engineering",
            "Department of Civil Engineering",
            "Department of Computer Science & Engineering",
            "Department of Electrical Engineering",
            "Department of Geomatics Engineering",
            "Department of Mechanical Engineering",], variable=self.var_dep)
        self.depart_option.set(
            "Department of Computer Science and Engineering")
        self.depart_option.grid(row=0, column=1, padx=20,
                                pady=20, sticky="ew", columnspan=2)

        self.Year_lbl = customtkinter.CTkLabel(self.left_frame, font=("lucida bright", 15),
                                               text="Year"
                                               )

        self.Year_lbl.grid(row=1, column=0, padx=20, pady=20)

        self.Year_option = customtkinter.CTkOptionMenu(self.left_frame, values=[
            "2023",
            "2022",
            "2021",
            "2020",
            "2019",
            "2018"], variable=self.var_year)
        self.Year_option.set("2023")
        self.Year_option.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.sem_lbl = customtkinter.CTkLabel(self.left_frame, font=("lucida bright", 15),
                                              text="Semester")
        self.sem_lbl.grid(row=2, column=0, padx=20, pady=20)
        self.sem_option = customtkinter.CTkOptionMenu(
            self.left_frame, values=["I", "II"], variable=self.var_sem)
        self.sem_option.set("I")
        self.sem_option.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.course = customtkinter.CTkLabel(self.left_frame,
                                             font=(
                                                 "lucida bright", 15),
                                             text="Course"
                                             )
        self.course.grid(row=2, column=2, padx=20, pady=20)
        self.course_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, textvariable=self.var_course, placeholder_text="Enter Course")
        self.course_entry.grid(row=2, column=3, padx=20, pady=20, sticky="ew")
        # self.course_entry.bind("<ButtonRelease>", self.course_entry.configure(
        #     textvariable=self.var_course))

        self.student_id = customtkinter.CTkLabel(self.left_frame,
                                                 font=(
                                                     "lucida bright", 15),
                                                 text="Student ID"
                                                 )
        self.student_id.grid(row=3, column=0, padx=20, pady=20)
        self.id_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter student_id", textvariable=self.var_id)
        self.id_entry.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

        self.student_name = customtkinter.CTkLabel(self.left_frame,
                                                   font=(
                                                       "lucida bright", 15),
                                                   text=" Name"
                                                   )
        self.student_name.grid(row=4, column=0, padx=20, pady=20)
        self.name_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter student_name",  textvariable=self.var_name)
        self.name_entry.grid(row=4, column=1, padx=20, pady=20, sticky="ew")

        self.address = customtkinter.CTkLabel(self.left_frame,
                                              font=(
                                                  "lucida bright", 15),
                                              text="Address"
                                              )
        self.address.grid(row=5, column=0, padx=20, pady=20)
        self.address_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter address", textvariable=self.var_address)
        self.address_entry.grid(row=5, column=1, padx=20, pady=20, sticky="ew")

        self.gender = customtkinter.CTkLabel(self.left_frame,
                                             font=(
                                                 "lucida bright", 15),
                                             text="Gender"
                                             )
        self.gender.grid(row=6, column=0, padx=20, pady=20)
        self.gender_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter gender", textvariable=self.var_gender)
        self.gender_entry.grid(row=6, column=1, padx=20, pady=20, sticky="ew")

        self.Dob = customtkinter.CTkLabel(self.left_frame,
                                          font=(
                                              "lucida bright", 15),
                                          text="Date of birth"
                                          )
        self.Dob.grid(row=3, column=2, padx=20, pady=20)
        self.dob_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter Date of birth", textvariable=self.var_dob)
        self.dob_entry.grid(row=3, column=3, padx=20, pady=20, sticky="ew")

        self.email = customtkinter.CTkLabel(self.left_frame,
                                            font=(
                                                "lucida bright", 15),
                                            text="Email"
                                            )
        self.email.grid(row=4, column=2, padx=20, pady=20)
        self.email_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter Email", textvariable=self.var_email)
        self.email_entry.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

        self.phone = customtkinter.CTkLabel(self.left_frame,
                                            font=(
                                                "lucida bright", 15),
                                            text="Phone No."
                                            )
        self.phone.grid(row=5, column=2, padx=20, pady=20)
        self.phone_entry = customtkinter.CTkEntry(
            self.left_frame, fg_color=["gray70", "gray25"], border_width=0, corner_radius=2, placeholder_text="Enter phone number", textvariable=self.var_phone)
        self.phone_entry.grid(row=5, column=3, padx=20, pady=20, sticky="ew")

        self.radio1 = customtkinter.CTkRadioButton(
            self.left_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes")
        self.radio1.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

        self.radio2 = customtkinter.CTkRadioButton(
            self.left_frame, text="Do Not Take Photo Sample", variable=self.var_radio1, value="No")
        self.radio2.grid(
            row=7, column=2, padx=20, pady=10, columnspan=2)

        self.save = customtkinter.CTkButton(
            self.left_frame, text="Save", command=self.add_data)
        self.save.grid(row=8, column=0, padx=20, pady=10, sticky="ew")

        self.update = customtkinter.CTkButton(
            self.left_frame, text="Update", command=self.update_data)
        self.update.grid(row=8, column=1, padx=20, pady=10, sticky="ew")

        self.delete = customtkinter.CTkButton(
            self.left_frame, text="Delete", command=self.delete_data)
        self.delete.grid(row=8, column=2, padx=20, pady=10, sticky="ew")

        self.reset = customtkinter.CTkButton(
            self.left_frame, text="Reset", command=self.reset_data)
        self.reset.grid(row=8, column=3, padx=20, pady=10, sticky="ew")

        self.takesample = customtkinter.CTkButton(
            self.left_frame, text="Takes Photo Sample", command=self.generate_dataset)
        self.takesample.grid(row=9, column=0, padx=10,
                             pady=20, sticky="ew", columnspan=2)

        self.updatesample = customtkinter.CTkButton(
            self.left_frame, text="Update Photo Sample", command=self.Update_dataset)
        self.updatesample.grid(row=9, column=2, padx=10,
                               pady=20, sticky="ew", columnspan=2)

        self.student_table = ttk.Treeview(self.right_frame, columns=("Department", "Year", "Semester", "Course", "Student_ID", "Name",
                                          "DOB", "Email", "Address", "Phone", "Gender", "Photo_Sample"), xscrollcommand=self.xscroller.set, yscrollcommand=self.yscroller.set)
        self.xscroller.configure(command=self.student_table.xview)
        self.yscroller.configure(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Student_ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Photo_Sample", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=290)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Student_ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Photo_Sample", width=100)

        self.student_table.grid(
            row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        self.reset_data()

        ############################# add data##############################

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            CTkMessagebox(
                self, title="Error", message="All fields are required!", icon="cancel").grid()
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root",  password="5qlP@ssword", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_course.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_gender.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                CTkMessagebox(
                    self, title="Success", message="Student Details has been added successfully!", icon="info").grid()

            except Exception as es:
                CTkMessagebox(
                    self, title="Error", message=f"Due to {str(es)}", icon="warning").grid()

    ################### fetching data from database##########################

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root",  password="5qlP@ssword", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", "end", values=i)
            conn.commit()
        conn.close()

    ####################### get cursor#####################################
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_course.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_email.set(data[7]),
        self.var_address.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_radio1.set(data[11])

    ############################# update###################################

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            CTkMessagebox(
                self, title="Error", message="All fields are required!", icon="cancel").grid()
        else:
            try:
                Update = CTkMessagebox(title="Update", message="Do you want to update student details?",
                                       icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = Update.get()
                if response == "Yes":

                    conn = mysql.connector.connect(
                        host="localhost", username="root",  password="5qlP@ssword", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Year=%s, Semester=%s, Course=%s, Name=%s, DOB=%s,Email=%s,Address=%s,Phone=%s,Gender=%s, Photo_Sample=%s where Student_ID=%s", (self.var_dep.get(), self.var_year.get(
                    ), self.var_sem.get(), self.var_course.get(), self.var_name.get(), self.var_dob.get(), self.var_email.get(), self.var_address.get(), self.var_phone.get(), self.var_gender.get(), self.var_radio1.get(), self.var_id.get()))

                else:
                    if not response == "Yes":
                        return
                CTkMessagebox(
                    self, title="Success", message="Student Details has been updated successfully!", icon="info").grid()
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                CTkMessagebox(
                    self, title="Error", message=f"Due to {str(es)}", icon="warning").grid()

    ############################### delete#########################################

    def delete_data(self):
        if self.var_id.get() == "":
            CTkMessagebox(
                self, title="Error", message="Student id isrequired!", icon="cancel").grid()
        else:
            try:
                delete = CTkMessagebox(title="Delete Student", message="Do you want to delete this student's details?",
                                       icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = delete.get()
                if response == "Yes":
                    conn = mysql.connector.connect(
                        host="localhost", username="root",  password="5qlP@ssword", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_ID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not response == "Yes":
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                CTkMessagebox(
                    self, title="Delete", message="Student Details has deleted successfully!", icon="info").grid()

            except Exception as es:
                CTkMessagebox(
                    self, title="Error", message=f"Due to {str(es)}", icon="warning").grid()

    ######################## reset###########################

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.course_entry._activate_placeholder()
        self.var_id.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_radio1.set("")

    def gammaCorrection(self, src, gamma):
        invGamma = 1 / gamma

        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)

        return cv2.LUT(src, table)

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self)
        else:
            try:
                id = int(self.var_id.get())
                # load predefined data on frontal face opencv
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    face = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5

                    for (x, y, w, h) in face:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(1)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = r"E:\facerecognition\bettter ui\data"+"/user" + \
                            "."+str(id)+"."+str(img_id)+".jpg"
                        # face = self.gammaCorrection(face, 2.5)
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face", face)
                        cv2.imshow("Gamma corrected image", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                CTkMessagebox(
                    self, title="Result", message="Generated Data Set.", icon="info").grid()
            except Exception as es:
                CTkMessagebox(
                    self, title="Error", message=f"Due to {str(es)}", icon="warning").grid()

    def Update_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:

                id = int(self.var_id.get())

                # load predefined data on frontal face opencv
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    face = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5

                    for (x, y, w, h) in face:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(1)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = r"E:\facerecognition\bettter ui\data"+"/user" + \
                            "."+str(id)+"."+str(img_id)+".jpg"
                        image_name = "user" + \
                            "."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                CTkMessagebox(
                    self, title="Result", message="Updated Data Set.", icon="info").grid()
            except Exception as es:
                CTkMessagebox(
                    self, title="Error", message=f"Due to {str(es)}", icon="warning").grid()
