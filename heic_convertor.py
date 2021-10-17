# import libraries
import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from datetime import datetime


# print log in the log text widget
def print_log(content):
    # get current time
    cur_time = datetime.now().strftime("%H:%M:%S")
    # insert log into log text widget
    log_txt.insert(tk.END, "[{}]:  {}\n".format(cur_time, content))


# main program for processing heic files
def processing():
    # update target directory
    target_dir = dir_ety.get()
    # go on if target directory is valid,
    # or print log to notify user invalid directory
    if os.path.exists(target_dir):
        print_log("Started...")
        # list all files in the target directory
        all_files = os.listdir(target_dir)
        # iterate all files
        for file_i in all_files:
            # process if the file is heic file
            if os.path.exist(file_i) & file_i.lower().endswith("heic"):
                heic_path = os.path.join(
                    target_dir, file_i
                )
                jpg_path = os.path.join(
                    target_dir, "{}.jpg".format(
                        file_i.split(".")[0]
                    )
                )
                os.system(
                    "magick {} {}".format(
                        heic_path, jpg_path
                    )
                )
                print_log("Processing {} ...".format(file_i))
            else:
                print_log("!!! File path is invalid !!!")
        print_log("ALL Done!")
    else:
        print_log("!!! Directory is invalid !!!")

# select directory and replace entry content
def select_dir():
    target_dir = ""
    # ask for directory
    dir_txt = filedialog.askdirectory()
    # check if input directory is valid
    if os.path.exists(dir_txt):
        dir_ety.delete(0, tk.END)
        dir_ety.insert(0, dir_txt)
        print_log(
            "Directory = [{}]".format(dir_txt)
        )


# create the main window for GUI
main_window = tk.Tk()
# give title
main_window.title("HEIC to JPG Convertor")
# give geometry
main_window.geometry("500x500")
# fix geometry
main_window.maxsize(width=500, height=500, )

# create directory entry label
dir_lbl = tk.Label(main_window, text="HEIC Directory: ")
dir_lbl.place(x=5, y=5, )

# create directory entry
dir_ety = tk.Entry(main_window, width=65, )
dir_ety.place(x=100, y=5, )

# create directory selection button
dir_btn = tk.Button(
    main_window, text="Select Directory", 
    command=lambda:select_dir()
)
dir_btn.place(x=150, y=30, )

# create processing button
sta_btn = tk.Button(
    main_window,  text="Start Processing", 
    command=lambda:processing()
)
sta_btn.place(x=250, y=30, )

# create log text widget
log_txt = tk.Text(main_window, width=69, height=33, )
log_txt.place(x=5, y=60, )

print_log("*** Welcome to use HEIC to JPG ***")


main_window.mainloop()
