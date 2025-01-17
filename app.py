import os
import customtkinter as ctk
import tkinter as tk
import Wuzzuf_Scrapper as ws
def wuzzuf_scrap_msg():
    if wuzzuf_link_textfield.get(1.0, 'end-1c') != '' and csv_name_textfield.get(1.0, "end-1c") != '':
        file_name = csv_name_textfield.get(1.0, "end-1c")
        ws.wuzzuf_scrap(wuzzuf_link_textfield.get(1.0, 'end-1c'), file_name)
        tk.messagebox.showinfo("Scrapping Successful", "Wuzzuf Web Scrapping is Finished")
        os.system(f'start Jobs\\"{file_name}".csv')
        ctk.CTkLabel(master=frame1,
                     text=f"File Located in {os.getcwd()}/Jobs",
                     font=("Arial", 15)).pack(padx=20, pady=25)
    else:
        tk.messagebox.showinfo("Scrapping Failed", "Textbox is Empty")

root = ctk.CTk()
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")
root.eval("tk::PlaceWindow . center")
root.title("Shift118 Web Scrapper")

frame1 = ctk.CTkFrame(master=root, width=750, height=500)
frame1.grid(row=0, column=0, sticky="nesw")
frame1.pack_propagate(False)

ctk.CTkLabel(master=frame1,
             text="Enter Wuzzuf Link of 2nd Page of The Job: \nExample: https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python&start=1",
             font=("Arial", 15)).pack(padx=20, pady=25)

# Create the text fields without packing them yet
wuzzuf_link_textfield = ctk.CTkTextbox(master=frame1, height=1, font=("Arial", 15))
wuzzuf_link_textfield.pack(fill='both')

ctk.CTkLabel(master=frame1, text="Enter CSV File Name:", font=("Arial", 15)).pack(padx=20, pady=25)

csv_name_textfield = ctk.CTkTextbox(master=frame1, height=1, font=("Arial", 15))
csv_name_textfield.pack(fill='both')

# Define the button after creating the text fields
ctk.CTkButton(master=frame1, text="Run", font=("Arial", 15),
              command=wuzzuf_scrap_msg).pack(padx=20, pady=25)

ctk.CTkLabel(master=frame1, text="Developed By @Shift118", font=("Arial", 30)).pack(padx=20, pady=25)
ctk.CTkLabel(master=frame1, text="Convert 'Date' Column Type to Date", font=("Arial", 15)).pack(padx=20, pady=25)
root.mainloop()
