import customtkinter
import os
from PIL import Image, ImageTk
from student import Student
import tkinter
import cv2
import numpy as np
import CTkMessagebox
import mysql.connector
from time import strftime
from datetime import datetime
import csv
from loginpage import Login
from initial_screen import Loading_Screen
from attendance_table import Attendance_table
from graph import graph
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.after(0, lambda: self.state('zoomed'))
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        self.title("Facial Recognition")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        # E:\facerecognition\bettter ui\test_images\bg_gradient.jpg
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "icon.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "bg_gradient.jpg")), size=(1000, 150))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(
            dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.switch = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "switch2.png")),
                                             dark_image=Image.open(os.path.join(image_path, "switch1.png")), size=(50, 50))

        self.welcomeimage = customtkinter.CTkImage(
            light_image=Image.open(
                r"bettter ui\test_images\blackwelcome.png"),
            dark_image=Image.open(r"E:\facerecognition\bettter ui\test_images\Welcome-White-Text-Transparent-PNG.png"), size=(480, 150))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Navigation Panel", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Student",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=customtkinter.CTkImage(Image.open(os.path.join(
                                                          image_path, "student_details.png"))), anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Attendance",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=customtkinter.CTkImage(Image.open(os.path.join(
                                                          image_path, "attendance.png"))), anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_button = customtkinter.CTkButton(self.navigation_frame, text="", fg_color="transparent", hover=False, image=self.switch,
                                                              command=self.change_appearance_mode_event)
        self.appearance_mode_button.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, bg_color="transparent", text_color="gray60", font=("lucida bright", 100), text="Face Recognition")
        self.home_frame_large_image_label.grid(
            row=0, column=0, padx=20, pady=10, sticky="ew")
        # self.welcome = customtkinter.CTkLabel(
        #     self.home_frame, text="", image=self.welcomeimage)
        # self.welcome.grid(
        #     row=0, column=0, padx=20, pady=10, sticky="ew")

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text_color=("gray10", "gray90"), text="Student Information", image=customtkinter.CTkImage(Image.open(os.path.join(image_path, "student_details.png")), size=(100, 100)),  command=self.student_details, compound="top")

        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame, text_color=("gray10", "gray90"), text="Attendance", image=customtkinter.CTkImage(Image.open(os.path.join(image_path, "attendance.png")), size=(100, 100)),  command=self.face_detect, compound="top")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(
            self.home_frame, text_color=("gray10", "gray90"), text="Train", image=customtkinter.CTkImage(Image.open(os.path.join(image_path, "faceid.png")), size=(100, 100)),  command=self.train_classifier, compound="top")

        self.home_frame_button_4 = customtkinter.CTkButton(
            self.home_frame, text_color=("gray10", "gray90"), text="Exit", image=customtkinter.CTkImage(Image.open(os.path.join(image_path, "exit.png")), size=(100, 100)), command=self.destroy, compound="top")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create loading screen
        self.loading_screen = Loading_Screen(self)
        self.loading_screen.admin_button.configure(
            command=lambda: self.select_frame_by_name("login"))
        self.loading_screen.student_button.configure(
            command=lambda: self.select_frame_by_name("home"))

        # # create login frame
        self.login = Login(self)
        self.login.login_button.bind("<ButtonRelease>", self.login_event)
        self.login.main_frame.bind("<Return>", self.register_event)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.studentgraph = customtkinter.CTkLabel(
            self.second_frame, text="Attendance Trend Of Students", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.studentgraph.grid(row=0, column=0, padx=20, pady=20, sticky="new")
        self.second_frame.grid_rowconfigure(1, weight=1)
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.graph = graph(self.second_frame)
        self.graph.grid(row=1, column=0, padx=20, pady=20, sticky="new")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_rowconfigure(1, weight=1)
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.attentance = customtkinter.CTkLabel(
            self.third_frame, text="Attendance Record Of All Students", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.attentance.grid(row=0, column=0, padx=20, pady=20, sticky="new")

        self.attentance_table = Attendance_table(self.third_frame)
        self.attentance_table.grid(
            row=1, column=0, padx=20, pady=20, sticky="new")

        # select default frame
        # self.select_frame_by_name("login")
        self.select_frame_by_name("loading")
        self.toplevel_window = None

    def login_event(self, event):
        if self.login.loginflag == True:
            self.select_frame_by_name("home")
            self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
            self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)

    def register_event(self, event):
        self.login.register_button_event(self)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "student" else "transparent")
        self.frame_3_button.configure(
            fg_color=("gray75", "gray25") if name == "attendance" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "student":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "attendance":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "login":
            self.login.grid(row=0, column=0, sticky="nsew")
        else:
            self.login.grid_forget()
        if name == "loading":
            self.loading_screen.grid(row=0, column=0, sticky="nsew")
        else:
            self.loading_screen.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("student")

    def frame_3_button_event(self):
        self.select_frame_by_name("attendance")

    def change_appearance_mode_event(self):
        if (self._get_appearance_mode() == "light"):
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("green")
        elif (self._get_appearance_mode() == "dark"):
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("green")

    def student_details(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Student()
            self.toplevel_window.after(
                0, lambda: self.toplevel_window.state('zoomed'))
            self.toplevel_window.grab_current()

        else:
            self.toplevel_window.focus()

    def train_classifier(self):
        data_dir = (r"bettter ui\data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # converts to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the cassifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        # CTkMessagebox(self, title="Reuslt",
        #               message="Training dataset complete!").grid()

    def mark_attendance(self, fd3, fd, fd1, fd2, Date):
        with open("Attendance.csv", "r+", newline="\n") as f:
            dataList = f.readlines()
            # name_list = []
            dates = []
            hour = []
            now = datetime.now()
            count = 0
            for line in dataList:
                entry = line.split((","))
                # name_list.append(entry[0])
                if entry[1] == fd:
                    hour_split = entry[4].split((":"))
                    hour.append(hour_split[0])
                    dates.append(entry[5])
            index = 0
            for date in dates:
                if Date == date:
                    if (count == 0) and now.hour == int(hour[index]):
                        return
                    count = count+1
                index = index+1

            if count < 2:
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                #### for no repition of attendance####
                if (count == 0):
                    f.writelines(
                        f"\n{fd3},{fd},{fd1},{fd2},{dtString},{d1},Entrance-Time")
                else:
                    f.writelines(
                        f"\n{fd3},{fd},{fd1},{fd2},{dtString},{d1},Exit-Time")

    def gammaCorrection(self, src, gamma):
        invGamma = 1 / gamma

        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)

        return cv2.LUT(src, table)

    def face_detect(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # gray_image = self.gammaCorrection(gray_image, 2.5)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbour)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+h])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="5qlP@ssword", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "Select Name from student where Student_ID = " + str(id))
                fd = my_cursor.fetchone()
                fd = "+".join(fd)

                my_cursor.execute(
                    "Select Department from student where Student_ID =" + str(id))
                fd1 = my_cursor.fetchone()
                fd1 = "+".join(fd1)

                my_cursor.execute(
                    "Select Semester from student where Student_ID ="+str(id))
                fd2 = my_cursor.fetchone()
                fd2 = "+".join(fd2)

                my_cursor.execute(
                    "Select Student_ID from student where Student_ID ="+str(id))
                fd3 = my_cursor.fetchone()
                fd3 = "+".join(fd3)

                if confidence > 85:
                    cv2.putText(
                        img, f"Student_ID:{fd3}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(
                        img, f"Name:{fd}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(
                        img, f"Department:{fd1}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(
                        img, f"Semester:{fd2}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    now = datetime.now()
                    date = now.strftime("%d/%m/%Y")
                    self.mark_attendance(fd3, fd, fd1, fd2, date)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Student", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    print("home is toplevel")
    app = App()
    app.iconbitmap(r'E:\facerecognition\bettter ui\icon.ico')
    app.mainloop()
