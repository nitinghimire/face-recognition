import customtkinter
from PIL import Image
import os
customtkinter.set_appearance_mode("dark")


class Loading_Screen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        self.loading_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent", bg_color="transparent", width=700, height=600)
        self.loading_frame.grid(row=0, column=0, padx=self.winfo_screenwidth(
        )/4, pady=self.winfo_screenheight()/4, sticky="nsew")
        self.loading_frame.columnconfigure((0, 1), weight=1)
        self.loading_frame.rowconfigure(2, weight=1)

        self.welcome = customtkinter.CTkLabel(
            self.loading_frame, text="Welcome To Face Attendance", font=("", 50), fg_color="transparent", bg_color="transparent")
        self.welcome.grid(row=0, column=0, padx=20,
                          pady=20, sticky="n", columnspan=2)
        self.welcome.grid_columnconfigure(0, weight=1)

        self.welcome_sub = customtkinter.CTkLabel(
            self.loading_frame, text="Please Pick A Mode Of Use:", font=("", 25))
        self.welcome_sub.grid(row=1, column=0, padx=20,
                              pady=10, sticky="n", columnspan=2)
        self.welcome_sub.grid_columnconfigure(0, weight=1)

        self.admin_button = customtkinter.CTkButton(self.loading_frame, image=customtkinter.CTkImage(
            Image.open(r"E:\facerecognition\bettter ui\test_images\admin.jpg"), size=[150, 150]), compound="top", font=("", 25), hover=False, text="Admin", fg_color="transparent")
        self.admin_button.grid(row=2, column=0, padx=40,
                               pady=20)
        self.admin_button.grid_columnconfigure(0, weight=1)
        self.student_button = customtkinter.CTkButton(self.loading_frame, image=customtkinter.CTkImage(
            Image.open(r"E:\facerecognition\bettter ui\test_images\student.jpg"), size=[150, 150]), compound="top", font=("", 25), hover=False, text="Student", fg_color="transparent")
        self.student_button.grid(row=2, column=1, padx=40,
                                 pady=20)
        self.student_button.grid_columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = Loading_Screen()
    app.mainloop()

if __name__ == "initial_screen":
    print("initial screen")
