import pandas as pd
import os
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import customtkinter
from matplotlib.ticker import MaxNLocator
<<<<<<< HEAD
from CTkMessagebox import CTkMessagebox
=======
>>>>>>> af59ce0bb9c532d6a3e2abe5ce1cb6cf49377052


class graph(customtkinter.CTkFrame):

<<<<<<< HEAD
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.student_search(None)

    def student_search(self, student=None):
        foundflag = False
        try:
            if student != None and student != "":
                self.figure1.clear()
                self.figure1.clf()
            print(student)
            with open("Attendance.csv", "r+", newline="\n") as f:
                dataList = f.readlines()
                date_name_list = []
                if student == None or student == "":
                    for line in dataList:
                        entry = line.split((","))
                        date_name_list.append((entry[5], entry[1],))

                if student != None and student != "":
                    for line in dataList:
                        entry = line.split((","))
                        if entry[0] == student:
                            date_name_list.append((entry[5], entry[1],))
                            foundflag = True

                if student != None and student != "" and foundflag != True:
                    CTkMessagebox(
                        self, title="Error", message="No such Student!!!", icon="warning")
                    return

                dn_list_once = []
                for values in date_name_list:
                    if not self.search_list(dn_list_once, values):
                        dn_list_once.append(values)

                single_date = []

                for Date in dn_list_once:
                    if not self.search_date(single_date, Date[0]):
                        single_date.append(Date[0])
                number_for_date = []

                for date in single_date:
                    count = 0
                    for date2 in dn_list_once:
                        if date == date2[0]:
                            count = count+1
                    number_for_date.append(count)

                data1 = {'Date': single_date,
                         'Number of Students Present': number_for_date
                         }
                self.df1 = pd.DataFrame(data1)
                COLOR = '#a9a9a9'
                plt.rcParams['text.color'] = COLOR
                plt.rcParams['axes.labelcolor'] = COLOR
                plt.rcParams['xtick.color'] = COLOR
                plt.rcParams['ytick.color'] = COLOR

                try:
                    self.figure1.canvas.get_tk_widget().destroy()
                except:
                    print("Graph is created!!")

                self.figure1 = plt.Figure(
                    figsize=(6, 5), dpi=100, facecolor='#2a2a2a')
                self.figure1.patch.set_alpha(1)
                self.ax1 = self.figure1.add_subplot(111)
                self.ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
                self.bar1 = FigureCanvasTkAgg(self.figure1, self)
                self.bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
                self.df1 = self.df1[['Date', 'Number of Students Present']
                                    ].groupby('Date').sum()
                self.df1.plot(kind='bar', legend=False, ax=self.ax1, color="w")
                self.ax1.set_title('Date Vs. Number of Students')
                self.ax1.set_facecolor("#4b4646")

                self.ax1.set_xticklabels(
                    self.ax1.get_xticklabels(), rotation=0)
        except Exception as es:
            CTkMessagebox(
                self, title="Error", message=f"Due to {str(es)}", icon="warning")

    def search_list(self, list, item_to_search):
        for item in list:
            if item_to_search == item:
                return True

    def search_date(self, list, date_to_search):
        for date in list:
            if date == date_to_search:
                return True

    def counter(self, list):
        count = 0
        for list_ in list:
            count = count+1
        return count
=======
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def search_list(list, item_to_search):
            for item in list:
                if item_to_search == item:
                    return True

        def search_date(list, date_to_search):
            for date in list:
                if date == date_to_search:
                    return True

        def counter(list):
            count = 0
            for list_ in list:
                count = count+1
            return count

        with open("Attendance.csv", "r+", newline="\n") as f:
            dataList = f.readlines()
            date_name_list = []
            for line in dataList:
                entry = line.split((","))
                date_name_list.append((entry[5], entry[1],))

            dn_list_once = []
            for values in date_name_list:
                if not search_list(dn_list_once, values):
                    dn_list_once.append(values)

            single_date = []

            for Date in dn_list_once:
                if not search_date(single_date, Date[0]):
                    single_date.append(Date[0])
            number_for_date = []

            for date in single_date:
                count = 0
                for date2 in dn_list_once:
                    if date == date2[0]:
                        count = count+1
                number_for_date.append(count)

            data1 = {'Date': single_date,
                     'Number of Students Present': number_for_date
                     }
            df1 = pd.DataFrame(data1)

            COLOR = '#a9a9a9'
            plt.rcParams['text.color'] = COLOR
            plt.rcParams['axes.labelcolor'] = COLOR
            plt.rcParams['xtick.color'] = COLOR
            plt.rcParams['ytick.color'] = COLOR
            figure1 = plt.Figure(figsize=(6, 5), dpi=100, facecolor='#2a2a2a')
            figure1.patch.set_alpha(1)
            ax1 = figure1.add_subplot(111)
            ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
            bar1 = FigureCanvasTkAgg(figure1, self)
            bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
            df1 = df1[['Date', 'Number of Students Present']
                      ].groupby('Date').sum()
            df1.plot(kind='line', legend=True, ax=ax1, color="w")
            ax1.set_title('Date Vs. Number of Students')
            ax1.set_facecolor("#4b4646")
            # print(single_date)
            # print(number_for_date)
            # print(dn_list_once)
>>>>>>> af59ce0bb9c532d6a3e2abe5ce1cb6cf49377052
