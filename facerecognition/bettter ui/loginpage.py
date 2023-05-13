from CTkMessagebox import CTkMessagebox
import customtkinter
from PIL import Image
import os
import mysql.connector
customtkinter.set_appearance_mode("dark")


class Login(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginflag = False
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.var_username = customtkinter.StringVar()
        # self.after(0, lambda: self.state('zoomed'))

        # self.title("Login Page")
        # self.geometry(f"{self.width}x{self.height}")

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + r"\test_images\registration.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(
            self, width=600, height=700, corner_radius=0, fg_color="gray10")
        self.login_frame.grid(row=0, column=0)
        # self.login_frame.grid_columnconfigure(0, weight=1)
        # self.login_frame.grid_rowconfigure((1, 2), weight=2)
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="LOGIN",
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=150,
                              pady=(60, 15), sticky="n")
        self.message = customtkinter.CTkLabel(
            self.login_frame, text="Please enter your login and password!", text_color="gray40", font=customtkinter.CTkFont(family="fjalla one", size=14))
        self.message.grid(row=1, column=0, padx=20, pady=5)
        self.username_entry = customtkinter.CTkEntry(
            self.login_frame, corner_radius=25, border_color="#2e4b95", justify="center", placeholder_text_color="gray40", width=200, height=40, fg_color="gray10", placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(50, 15))
        self.password_entry = customtkinter.CTkEntry(
            self.login_frame,  corner_radius=25,  border_color="#2e4b95", justify="center", placeholder_text_color="gray40", width=200, height=40, show="*", fg_color="gray10", placeholder_text="Password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(10, 15))
        self.login_button = customtkinter.CTkButton(
            self.login_frame, command=self.Login_event, corner_radius=25, border_width=2,  border_color="#007600", hover_color="#007600", fg_color="gray10", height=40, text="Login", width=100)
        self.login_button.grid(row=4, column=0, padx=30,
                               pady=(50, 15), sticky="s")
        self.register_button = customtkinter.CTkButton(
            self.login_frame, fg_color="transparent", hover=False, command=self.register_event, text_color="gray40", width=100, text="Register New Admin")
        self.register_button.grid(row=5, column=0, padx=30, pady=(0, 15))
        # justify="left", text_color="gray60"
        # create main frame
        self.main_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="gray10", width=900, height=700)
        self.main_frame.grid_columnconfigure((0, 1), weight=1)

        # self.main_frame.grid_rowconfigure(
        #     (1,  3,  5,  7, 9), weight=1)
        self.main_frame.grid_rowconfigure(
            (2,  4,  6,  8, 10), weight=1)

        self.label = customtkinter.CTkLabel(
            self.main_frame, text="Register New Administrator", font=("", 35))
        self.label.grid(row=0, column=0, sticky="new",
                        padx=20, pady=20, columnspan=2)

        self.fname = customtkinter.CTkLabel(
            self.main_frame, text="First Name", justify="left", text_color="gray60")
        self.fname.grid(row=1, column=0, padx=(
            100, 0), pady=0, sticky="w")
        self.fname.grid_rowconfigure(1, weight=1)

        self.fname_entry = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Enter first name", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.fname_entry.grid(row=2, column=0, padx=100, pady=0,  sticky="w")

        self.lname = customtkinter.CTkLabel(
            self.main_frame, justify="left", text_color="gray60", text="Last Name")
        self.lname.grid(row=1, column=1, padx=100, pady=(0, 0), sticky="w")

        self.lname_entry = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Enter last name", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.lname_entry.grid(row=2, column=1, padx=100, pady=0, sticky="w")

        self.contact = customtkinter.CTkLabel(
            self.main_frame, justify="left", text_color="gray60", text="Contact")
        self.contact.grid(row=3, column=0, padx=100, pady=(10, 0), sticky="w")

        self.contact_entry = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Enter Contact Information", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.contact_entry.grid(row=4, column=0, padx=100, pady=0, sticky="w")

        self.email = customtkinter.CTkLabel(
            self.main_frame, justify="left", text_color="gray60", text="Email")
        self.email.grid(row=3, column=1, padx=100, pady=(10, 0), sticky="w")

        self.email_entry = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Enter Email", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.email_entry.grid(row=4, column=1, padx=100, pady=0, sticky="w")

        self.security_qn = customtkinter.CTkLabel(
            self.main_frame, justify="left", text_color="gray60", text="Security Question")
        self.security_qn.grid(row=5, column=0, padx=100,
                              pady=(10, 0), sticky="w")

        self.security_qn_entry = customtkinter.CTkComboBox(
            self.main_frame, corner_radius=25, values=["What was the first exam you failed?", "What was the name of your first pet?"], justify="center", width=300, height=40, fg_color="gray10")
        self.security_qn_entry.grid(
            row=6, column=0, padx=100, pady=0, sticky="w")
        self.security_qn_entry.set("Select A Security Question")

        self.securit_ans = customtkinter.CTkLabel(
            self.main_frame, justify="left", text_color="gray60", text="Security Answer")
        self.securit_ans.grid(row=5, column=1, padx=100,
                              pady=(10, 0), sticky="w")

        self.securit_ans_entry = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Enter Security Answer", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.securit_ans_entry.grid(
            row=6, column=1, padx=100, pady=0, sticky="w")

        self.password = customtkinter.CTkLabel(
            self.main_frame, text="Password", text_color="gray60")
        self.password.grid(row=7, column=0, padx=100, pady=(10, 0), sticky="w")

        self.password_entry2 = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, show="*", placeholder_text="Enter Password", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.password_entry2.grid(
            row=8, column=0, padx=100, pady=0, sticky="w")

        self.confirm_password = customtkinter.CTkLabel(
            self.main_frame, text="Confirm Password", text_color="gray60")
        self.confirm_password.grid(
            row=7, column=1, padx=100, pady=(10, 0), sticky="w")

        self.confirm_password_entry = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Confirm Password", show="*", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.confirm_password_entry.grid(
            row=8, column=1, padx=100, pady=0, sticky="w")

        self.username = customtkinter.CTkLabel(
            self.main_frame, text="Username", text_color="gray60")
        self.username.grid(row=9, column=0, padx=100, pady=(10, 0), sticky="w")

        self.username_entry2 = customtkinter.CTkEntry(
            self.main_frame, corner_radius=25, placeholder_text="Enter Username", justify="center",  placeholder_text_color="gray40", width=200, height=40, fg_color="gray10")
        self.username_entry2.grid(
            row=10, column=0, padx=100, pady=0, sticky="w")

        self.Register = customtkinter.CTkButton(
            self.main_frame, text="Register", command=self.register_button_event, corner_radius=25, border_width=2,  border_color="#b6a60a", hover_color="#b6a60a", fg_color="gray10", height=40, width=120)
        self.Register.grid(row=11, column=0, padx=30,
                           pady=(15, 15))

        self.Login = customtkinter.CTkButton(
            self.main_frame, text="Login", command=self.register_login_event, corner_radius=25, border_width=2,  border_color="#007600", hover_color="#007600", fg_color="gray10", height=40, width=100)
        self.Login.grid(row=11, column=1, padx=30,
                        pady=(15, 15))

        self.back_button = customtkinter.CTkButton(
            self.main_frame, text="Back", command=self.back_event, corner_radius=25, border_width=2,  border_color="#b6270a", hover_color="#b6270a", fg_color="gray10", height=40, width=100)
        self.back_button.grid(row=12, column=0, padx=30,
                              pady=(15, 15), columnspan=2)

    def register_login_event(self):
        if self.username_entry.get() == "":
            self.username_entry.insert(0, self.username_entry2.get())
        if self.password_entry.get() == "":
            self.password_entry.insert(0, self.password_entry2.get())
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0)  # show login frame

    def Login_event(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            CTkMessagebox(
                self, title="Error", message="All Fields Are Required!", icon="warning")
            print("invalid")
            print(self.username_entry.get())
            print(self.password_entry.get())
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="5qlP@ssword", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from admin where Username = %s and Password = %s", (
                    self.username_entry.get(),
                    self.password_entry.get(),
                ))
                row = my_cursor.fetchone()
                if row == None:
                    # messagebox.showerror("Error", "Invalid Username")
                    CTkMessagebox(self, title="Error",
                                  message="Invalid User", icon="info")
                else:
                    self.loginflag = True
                conn.commit()
                conn.close()
            except:
                CTkMessagebox(self, title="Something Went Wrong",
                              message="Admin already registered. Please login!")

    def register_button_event(self, event=None):
        if (self.username_entry2.get() == "" or
            self.fname_entry.get() == "" or
            self.lname_entry.get() == "" or
            self.contact_entry.get() == "" or
            self.email_entry.get() == "" or
            (self.security_qn_entry.get() == "" or self.security_qn_entry.get() == "Select A Security Question") or
            self.securit_ans_entry.get() == "" or
                self.password_entry2.get() == ""):
            CTkMessagebox(self, title="Error",
                          message="All Fields must be Filled!!")
        elif self.password_entry2.get() != self.confirm_password_entry.get():
            CTkMessagebox(self, title="Error",
                          message="Password Is Not The Same.")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="5qlP@ssword", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from admin where Username = %s ",
                              (self.username_entry2.get(),)
                              )
            row = my_cursor.fetchone()
            if row != None:
                # messagebox.showerror("Error", "Invalid Username")
                CTkMessagebox(self, title="Error",
                              message="Username is taken!", icon="info")
            else:
                my_cursor.execute("insert into admin values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.username_entry2.get(),
                    self.fname_entry.get(),
                    self.lname_entry.get(),
                    self.contact_entry.get(),
                    self.email_entry.get(),
                    self.security_qn_entry.get(),
                    self.securit_ans_entry.get(),
                    self.password_entry2.get(),
                ))
                CTkMessagebox(self, title="Success",
                              message="New Admin registered!")

            conn.commit()
            conn.close()

    def register_event(self):
        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0)
        self.main_frame.focus()

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0)  # show login frame


if __name__ == "__main__":
    app = Login()
    app.mainloop()

if __name__ == "loginpage":
    print("login page")
