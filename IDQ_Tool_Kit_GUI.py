#!/usr/bin/env python
# coding: utf-8

# Check "Tool Kit Working File" for On-going Changes >>>>

# In[1]:


from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import sys
import wget
import webbrowser
import shutil

# del datetime
import datetime

# sys.path.append(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\IDQ_Tools")
# import Qc_tool as qc
# import Auto_Flat_File_Script_user as flat
# import Attribute_Recommendation_Tool_vol2 as reco
# import Suppression_code as t1
# import Prime_Now_Store_specific_code as pr
# import Flat_file_vendor3p_upload as fl
# import Duplicate_Audit_Script as dup
# import Returns_Fair as rf

sys.path.append(r"C:\Users\rishadix\Documents\Improved Reco Tool\Test_Reco_Tool")
# import mac_R_C_MAIN_Module_new as reco
# import AttributeRecommendationUI as reco

def tool_gui():
    root = Tk()

    root.geometry("1000x620+20+10")
    root.resizable(width=False, height=False)
    root.title('IDQ Tool Kit')
    root.config(background='#F5F5F5')

    dd=datetime.datetime.now()
    ## For Backround image:
    # global image_bg
    # Open the image using PIL
    image = Image.open(r"C:\Users\rishadix\Desktop\Rishabh\pxfuel(1).jpg")
    # # Convert the image to a PhotoImage object
    image_bg = ImageTk.PhotoImage(image=image, master=root)

    label = Label(root, image=image_bg)
    label.place(x=0, y=0)

    username = os.getlogin()
    # tools=[]
    def tool_list():
        if v.get()==1:
            tools=["Duplicates", "Returns", "Weblabs", "Recommendation_Tool"]
        else:
            tools=["Flat File Creator", "Suppresion Tool","Prime Now",'RAC_Audit_Tool','RAC_Flat_file_Tool']

        clicked = StringVar()
        clicked.set(tools[0]) # default value

        tool_drop = OptionMenu(root, clicked, *tools, command=show_info)
        tool_drop.config(width=19, relief=SUNKEN, font=('lato',9,'bold'))
        tool_drop.place(x=420, y=160)

    v=IntVar(value=1)
    # v2=IntVar(value=2)
    radio1 = Radiobutton(root, text='Dev', width=4, variable=v, value=1, command=tool_list, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'), disabledforeground='light grey').place(x=320, y=120)
    radio2 = Radiobutton(root, text='Prod', width=5, variable=v, value=2, command=tool_list, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'),disabledforeground='light grey').place(x=630, y=120)
    a1=v.get()                     # Option Value
    # a2=v2.get()
    # print(a1)
    # print(radio2.value)

    cur_button = None
    button = None
    # cb_button = None
    # C3 = None
    # C4 = None
    # label6 = Label()checkmay

    # Defining a function that will show some info based on the selected option
    def show_info(option):
        global cur_button
        global button
    #     global cb_button
        global C3
        global C4

    #     option = tool_drop.get()
#         if cur_button:
#             cur_button.destroy()
#         if button:
#             button.destroy()
    #     if cb_button:quer
    #         cb_button.destroy()
    #     if C3:
    #         C3.destroy()
    #     if C4:
    #         C4.destroy()        

        if (a1==1) & (option == 'Flat File Creator'):
            label33.config(text=f"{option} is used to create title flat files of 3p and RA for upload.")
            label44.config(text=f"Step 1: Keep your checkmate file of corrected set of asins and deprecated_hack_merchant_id in a folder. \nStep 2: Select 'Prod' & Opt for 'Flat File Creator'  \nStep 3: After hiting 'Run' button, Chrome will ask your credential to open FRPG automatically. \nStep 4: Select the folder (created in Step 1) & the output flat files will be generated on the same folder.")
            label55.config(text=f"1: Do not change anything on the checkmate file. \n2: Export the deprecated_hack_merchant_id without language tag. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any unneccesary space & spelling mistakes should be avoided).")

            def start_tool():
                fl.flat_file(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Flat_file_1.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\FF_Creator_input.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Suppresion Tool'):
            label33.config(text=f"{option} is used for Suppressing the Existing incorrect value of an attribute and helps in flowing the correct value which is already uploaded for that attribute in CSI. This helps the program team to correct the Catalogue quality of the ASIN whose score is not met according to Amazon Quality check.")
            label44.config(text=f"Step 1: Select the 'Prod' option & opt for Suppression tool \nStep 2: Check the Excel input & Hit OK \nStep 3: First, It will ask you to upload the CSI file & then Corrected file.  \nStep 4: Output will be found on 'Document' folder in Ion file format \nStep 5: Upload it via FRPG with Suppression Merchant Code")
            label55.config(text=f"1: It is mandatory to check in your CSI file that there is no blank in attribute values of any ASIN. \n2: The CSI file should be of 3P, No RA ASIN. \n3: Invalid ASIN shouldn't be there in the list of ASIN \n4: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

    #         v3 = IntVar()
    #         v4 = IntVar()
    #         def cb_check_1():
    #             if v3.get():
    #                 C4.config(state=DISABLED)
    #             else:
    #                 C4.config(state=NORMAL)
    # #                 root.after(7000, C4.destroy)

    #         C3 = Checkbutton(root, text="Excel File Input", variable=v3, command=cb_check_1).place(x=610, y=330)
    #         C4 = Checkbutton(root, text="Flat File Input", variable=v4, command=cb_check_1).place(x=815, y=330)
    # #         def rem_cb():
    # #             C3.destroy()
    # #             C4.destroy()        
    #         cb_button = Button(root, text='CheckBox', command=rem_cb, relief=SUNKEN, font=('lato',10), cursor='hand2', width=9, activebackground='#B0C4DE').place(x=730, y=425)
    #         root.after(7000, cb_button.destroy)
            def press(x=1,y=2,z=os.getlogin()):
                t1.xyza(x,y,z)
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=585, y=560)

    #         cur_button = Button(root, text='Run', command=lambda:press(v3.get(),v4.get(), os.getenv('USERNAME')), relief=SUNKEN, font=('lato',10), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button = Button(root, text='Run', command=press, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)

            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)

        elif (a1==1) & (option == 'Duplicates'):
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated.  \nStep 3: Then the updated valid_vlaues list need to be feeded \nStep 4: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The updated valid_values list gets from the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

            def start_tool():
                dup.duplicates(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Prime Now'):
            label33.config(text=f"{option} is used to map the ASIN with seller sku, update & delete the Price, Quantity & GST.")
            label44.config(text=f"Step 1: Need to update the template i.e. Upload_Delete_Input (Use 'Download Input Template' to get the Input file) \nStep 2: After Hiting 'Run' button, It'll ask for the the folder where flat files need to be saved. \nStep 3: Once the tool created flat files, FRPG will be opened in Google Chrome and starts uploading the flat files. \nStep 4: The completion Report will be shared on activity status.")
            label55.config(text=f"1: Make sure the sku & seller ID are valid in the template. \n2: Task attribute need to be accurately updated as per request \n3: The Column Name/Headers are case Sensitive hence it should not be changed.")

            def start_tool():
                pr.prime()
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
    #         def download_file():
    #             src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\Prime_Now\Upload_Delete_Input.csv"
    #             dst = r"C:\\Users\\" +username+ "\\Downloads\\Upload_Delete_Input.csv"
    #             shutil.copy(src, dst)
    #         button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
    #         button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Returns'):
            label33.config(text=f"{option} is used to update Cat & Sub Cat of the given set of ASINs.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to proceed \nStep 2: Tool creates Ion file as Output & gets uploaded in FRPG automatically. \nStep 3: The Output & Completion Report will be updated on the selected path.")
            label55.config(text=f"1: The Input File gets auto-updated every week. \n2: The Column Name/Headers are case Sensitive hence it should not be changed.")

            def start_tool():
                rf.Returns(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)

            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Weblabs'):
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated  \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The valid values need to be updated every week in the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

            def start_tool():
                qc.Qc_tool(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\
                \Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Recommendation_Tool'):
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to test the tool")
            label44.config(text=f"Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

            def start_tool():
                reco.Reco_tool()
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         username = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Reco_Input_Template.csv"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Reco_Input_Template.csv"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'RAC_Audit_Tool'):
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the valid values & freetext as T/F")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated \nStep 3: Then the updated valid_values list need to be feeded \nStep 4: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The updated valid values list need to be fetched from the Bridge sharepoint (reach out to @rishadix incase of un-accessibility)\n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

            def start_tool():
                qc.Qc_tool(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'RAC_Flat_file_Tool'):
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool. \nStep 2: First, it'll ask for the file with are updated required value. \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"\n1: The Column Name/Headers are case Sensitive hence it should not be changed. \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n3: The downloaded Input Template file will be located in 'Downloads' folder.")
            def start_tool():
                flat.fl_file(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()        
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Auto_Input_Flat_File.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Auto_Input_Flat_File.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        else:
            label6=Label(root, text=cb.get()+" Not active", fg='red', font=("Helvetica", 15))
            label6.place(x=530, y=405)
            print('not active')   

    label1 = Label(root, text=f"IDQ Tool Kit", fg='white', bg='#708090', relief=SUNKEN, highlightthickness=2, font=('lato',20,'bold'), width=15)
    label1.pack(side='top')

    label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", fg='indigo', bg='Gray92', padx=4, pady=4, font=('lato',10))
    label2.pack(side='top')

    def sim_link():
        webbrowser.open_new(r'https://issues.amazon.com/issues/create?assignedFolder=9f87ec2e-46f2-4009-80e3-d6ae7aac6bea&title=Process%2FSOP+Automation+request&description=Please+provide+the+below+pre-requisite+Information+for+your+request+type%0A%0AA.+Request+type%3A+New+Product+Request+%5C+Feature+Request%0A1.+Business+Case%3A+%0A2.+Impact+analysis%3A%0Aa.+2+pager+Doc%3A+Please+attached+to+SIM+2+pager+doc+containing+all+information+pertaining+to+steps+or+process+that+need+to+automated.%0Ab.+no.+of+FTE+saved+by+this+automation%3B+%0A%0A%23+Note+%3A+If+requested+information+is+not+provieded+then%2C+SIM+will+be+auto+closed+in+12+hrs&descriptionContentType=text%2Fplain&extensions%5Btt%5D%5Bcategory%5D=')

    but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", command=sim_link, borderwidth=2, fg='#008000', cursor='hand2',font=('lato',10))
    but1.pack(side='right', anchor='sw')

    # tools = ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool",'Recommendation_Tool']

    label3 = Label(root, text="Why do we use this Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label3.place(x=30, y=225)
    label33 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label33.place(x=30, y=245)
    # label33.pack(side='left', anchor='w')

    label4 = Label(root, text="How to Use the Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label4.place(x=30, y=335)
    label44 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label44.place(x=30, y=355)
    # label4.pack(side='right', anchor='e')

    label5 = Label(root, text="Points to Remember:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label5.place(x=30,y=480)
    # label5.pack(side='bottom', anchor='w')
    label55 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label55.place(x=30, y=500)

    label0 = Label(root, text=f" Report a Bug \nrishadix@ ", fg='maroon',bg='gray84', font=('lato',9), relief=GROOVE)
#     label6.pack(side='right')
#     label6.place(x=849, y=2.5)
    label0.place(x=916, y=2.5)
    
    # but2=Button(root, text='<< Start >>', command=show_info, cursor='hand2', font=('lato',11))
    # but2.place(x=460, y=400)
    run_button = Button(root, text=(f"Run"), command=show_info, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
    run_button.place(x=750, y=350)
    but3 = Button(root, text=" Exit ", borderwidth=1, bg='Brown', fg='white', cursor='hand2', width=4, command=root.destroy, font=('lato',11))
    but3.place(x=750, y=460)

    root.mainloop()

tool_gui()


# In[1]:


# Created a function to get the .exe file:

from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import sys
import wget
import webbrowser
import shutil

# del datetime
import datetime

# sys.path.append(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\IDQ_Tools")
# import Qc_tool as qc
# import Auto_Flat_File_Script_user as flat
# import Attribute_Recommendation_Tool_vol2 as reco
# import Suppression_code as t1
# import Prime_Now_Store_specific_code as pr
# import Flat_file_vendor3p_upload as fl
# import Duplicate_Audit_Script as dup
# import Returns_Fair as rf

sys.path.append(r"C:\Users\rishadix\Documents\Improved Reco Tool\Test_Reco_Tool")
import mac_R_C_MAIN_Module_new as reco
# import AttributeRecommendationUI as reco

def tool_gui():
    root = Tk()

    root.geometry("1000x620+20+10")
    root.resizable(width=False, height=False)
    root.title('IDQ Tool Kit')
    root.config(background='#F5F5F5')

    dd=datetime.datetime.now()
    ## For Backround image:
    # global image_bg
    # Open the image using PIL
    image = Image.open(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\pxfuel(1).jpg")
    # # Convert the image to a PhotoImage object
    image_bg = ImageTk.PhotoImage(image=image, master=root)

    label = Label(root, image=image_bg)
    label.place(x=0, y=0)

    username = os.getlogin()
    # tools=[]
    def tool_list():
        if v.get()==1:
            tools=["Duplicates", "Returns", "Weblabs", "Recommendation_Tool"]
        else:
            tools=["Flat File Creator", "Suppresion Tool","Prime Now",'RAC_Audit_Tool','RAC_Flat_file_Tool']

        clicked = StringVar()
        clicked.set(tools[0]) # default value

        tool_drop = OptionMenu(root, clicked, *tools, command=show_info)
        tool_drop.config(width=19, relief=SUNKEN, font=('lato',9,'bold'))
        tool_drop.place(x=420, y=160)

    v=IntVar(value=1)
    # v2=IntVar(value=2)
    radio1 = Radiobutton(root, text='Dev', width=4, variable=v, value=1, command=tool_list, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'), disabledforeground='light grey').place(x=320, y=120)
    radio2 = Radiobutton(root, text='Prod', width=5, variable=v, value=2, command=tool_list, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'),disabledforeground='light grey').place(x=630, y=120)
    a1=v.get()                     # Option Value
    # a2=v2.get()
    # print(a1)
    # print(radio2.value)

    cur_button = None
    button = None
    # cb_button = None
    # C3 = None
    # C4 = None
    # label6 = Label()checkmay

    # Defining a function that will show some info based on the selected option
    def show_info(option):
        global cur_button
        global button
    #     global cb_button
        global C3
        global C4

    #     option = tool_drop.get()
#         if cur_button:
#             cur_button.destroy()
#         if button:
#             button.destroy()
    #     if cb_button:quer
    #         cb_button.destroy()
    #     if C3:
    #         C3.destroy()
    #     if C4:
    #         C4.destroy()        

        if (a1==1) & (option == 'Flat File Creator'):
            label33.config(text=f"{option} is used to create title flat files of 3p and RA for upload.")
            label44.config(text=f"Step 1: Keep your checkmate file of corrected set of asins and deprecated_hack_merchant_id in a folder. \nStep 2: Select 'Prod' & Opt for 'Flat File Creator'  \nStep 3: After hiting 'Run' button, Chrome will ask your credential to open FRPG automatically. \nStep 4: Select the folder (created in Step 1) & the output flat files will be generated on the same folder.")
            label55.config(text=f"1: Do not change anything on the checkmate file. \n2: Export the deprecated_hack_merchant_id without language tag. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any unneccesary space & spelling mistakes should be avoided).")

            def start_tool():
                fl.flat_file(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Flat_file_1.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\FF_Creator_input.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Suppresion Tool'):
            label33.config(text=f"{option} is used for Suppressing the Existing incorrect value of an attribute and helps in flowing the correct value which is already uploaded for that attribute in CSI. This helps the program team to correct the Catalogue quality of the ASIN whose score is not met according to Amazon Quality check.")
            label44.config(text=f"Step 1: Select the 'Prod' option & opt for Suppression tool \nStep 2: Check the Excel input & Hit OK \nStep 3: First, It will ask you to upload the CSI file & then Corrected file.  \nStep 4: Output will be found on 'Document' folder in Ion file format \nStep 5: Upload it via FRPG with Suppression Merchant Code")
            label55.config(text=f"1: It is mandatory to check in your CSI file that there is no blank in attribute values of any ASIN. \n2: The CSI file should be of 3P, No RA ASIN. \n3: Invalid ASIN shouldn't be there in the list of ASIN \n4: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

    #         v3 = IntVar()
    #         v4 = IntVar()
    #         def cb_check_1():
    #             if v3.get():
    #                 C4.config(state=DISABLED)
    #             else:
    #                 C4.config(state=NORMAL)
    # #                 root.after(7000, C4.destroy)

    #         C3 = Checkbutton(root, text="Excel File Input", variable=v3, command=cb_check_1).place(x=610, y=330)
    #         C4 = Checkbutton(root, text="Flat File Input", variable=v4, command=cb_check_1).place(x=815, y=330)
    # #         def rem_cb():
    # #             C3.destroy()
    # #             C4.destroy()        
    #         cb_button = Button(root, text='CheckBox', command=rem_cb, relief=SUNKEN, font=('lato',10), cursor='hand2', width=9, activebackground='#B0C4DE').place(x=730, y=425)
    #         root.after(7000, cb_button.destroy)
            def press(x=1,y=2,z=os.getlogin()):
                t1.xyza(x,y,z)
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=585, y=560)

    #         cur_button = Button(root, text='Run', command=lambda:press(v3.get(),v4.get(), os.getenv('USERNAME')), relief=SUNKEN, font=('lato',10), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button = Button(root, text='Run', command=press, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)

            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)

        elif (a1==1) & (option == 'Duplicates'):
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated.  \nStep 3: Then the updated valid_vlaues list need to be feeded \nStep 4: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The updated valid_values list gets from the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

            def start_tool():
                dup.duplicates(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Prime Now'):
            label33.config(text=f"{option} is used to map the ASIN with seller sku, update & delete the Price, Quantity & GST.")
            label44.config(text=f"Step 1: Need to update the template i.e. Upload_Delete_Input (Use 'Download Input Template' to get the Input file) \nStep 2: After Hiting 'Run' button, It'll ask for the the folder where flat files need to be saved. \nStep 3: Once the tool created flat files, FRPG will be opened in Google Chrome and starts uploading the flat files. \nStep 4: The completion Report will be shared on activity status.")
            label55.config(text=f"1: Make sure the sku & seller ID are valid in the template. \n2: Task attribute need to be accurately updated as per request \n3: The Column Name/Headers are case Sensitive hence it should not be changed.")

            def start_tool():
                pr.prime()
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
    #         def download_file():
    #             src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\Prime_Now\Upload_Delete_Input.csv"
    #             dst = r"C:\\Users\\" +username+ "\\Downloads\\Upload_Delete_Input.csv"
    #             shutil.copy(src, dst)
    #         button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
    #         button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Returns'):
            label33.config(text=f"{option} is used to update Cat & Sub Cat of the given set of ASINs.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to proceed \nStep 2: Tool creates Ion file as Output & gets uploaded in FRPG automatically. \nStep 3: The Output & Completion Report will be updated on the selected path.")
            label55.config(text=f"1: The Input File gets auto-updated every week. \n2: The Column Name/Headers are case Sensitive hence it should not be changed.")

            def start_tool():
                rf.Returns(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)

            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Weblabs'):
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated  \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The valid values need to be updated every week in the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

            def start_tool():
                qc.Qc_tool(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\
                \Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'Recommendation_Tool'):
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to test the tool")
            label44.config(text=f"Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

            def start_tool():
                reco.Reco_tool()
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         username = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Reco_Input_Template.csv"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Reco_Input_Template.csv"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'RAC_Audit_Tool'):
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the valid values & freetext as T/F")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated \nStep 3: Then the updated valid_values list need to be feeded \nStep 4: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The updated valid values list need to be fetched from the Bridge sharepoint (reach out to @rishadix incase of un-accessibility)\n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

            def start_tool():
                qc.Qc_tool(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif (a1==1) & (option == 'RAC_Flat_file_Tool'):
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool. \nStep 2: First, it'll ask for the file with are updated required value. \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"\n1: The Column Name/Headers are case Sensitive hence it should not be changed. \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n3: The downloaded Input Template file will be located in 'Downloads' folder.")
            def start_tool():
                flat.fl_file(os.getenv('USERNAME'))
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
    #         x = os.getlogin()        
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Auto_Input_Flat_File.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Auto_Input_Flat_File.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        else:
            label6=Label(root, text=cb.get()+" Not active", fg='red', font=("Helvetica", 15))
            label6.place(x=530, y=405)
            print('not active')   

    label1 = Label(root, text=f"IDQ Tool Kit", fg='white', bg='#708090', relief=SUNKEN, highlightthickness=2, font=('lato',20,'bold'), width=15)
    label1.pack(side='top')

    label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", fg='indigo', bg='Gray92', padx=4, pady=4, font=('lato',10))
    label2.pack(side='top')

    def sim_link():
        webbrowser.open_new(r'https://issues.amazon.com/issues/create?assignedFolder=9f87ec2e-46f2-4009-80e3-d6ae7aac6bea&title=Process%2FSOP+Automation+request&description=Please+provide+the+below+pre-requisite+Information+for+your+request+type%0A%0AA.+Request+type%3A+New+Product+Request+%5C+Feature+Request%0A1.+Business+Case%3A+%0A2.+Impact+analysis%3A%0Aa.+2+pager+Doc%3A+Please+attached+to+SIM+2+pager+doc+containing+all+information+pertaining+to+steps+or+process+that+need+to+automated.%0Ab.+no.+of+FTE+saved+by+this+automation%3B+%0A%0A%23+Note+%3A+If+requested+information+is+not+provieded+then%2C+SIM+will+be+auto+closed+in+12+hrs&descriptionContentType=text%2Fplain&extensions%5Btt%5D%5Bcategory%5D=')

    but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", command=sim_link, borderwidth=2, fg='#008000', cursor='hand2',font=('lato',10))
    but1.pack(side='right', anchor='sw')

    # tools = ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool",'Recommendation_Tool']

    label3 = Label(root, text="Why do we use this Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label3.place(x=30, y=225)
    label33 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label33.place(x=30, y=245)
    # label33.pack(side='left', anchor='w')

    label4 = Label(root, text="How to Use the Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label4.place(x=30, y=335)
    label44 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label44.place(x=30, y=355)
    # label4.pack(side='right', anchor='e')

    label5 = Label(root, text="Points to Remember:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label5.place(x=30,y=480)
    # label5.pack(side='bottom', anchor='w')
    label55 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label55.place(x=30, y=500)

    label0 = Label(root, text=f" Report a Bug \nrishadix@ ", fg='maroon',bg='gray84', font=('lato',9), relief=GROOVE)
#     label6.pack(side='right')
#     label6.place(x=849, y=2.5)
    label0.place(x=916, y=2.5)
    
    # but2=Button(root, text='<< Start >>', command=show_info, cursor='hand2', font=('lato',11))
    # but2.place(x=460, y=400)
    run_button = Button(root, text=(f"Run"), command=show_info, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
    run_button.place(x=750, y=350)
    but3 = Button(root, text=" Exit ", borderwidth=1, bg='Brown', fg='white', cursor='hand2', width=4, command=root.destroy, font=('lato',11))
    but3.place(x=750, y=460)

    root.mainloop()

tool_gui()


# In[ ]:





# In[ ]:





# In[66]:


# Updated UI with all Operational Tools:

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys
import wget
import webbrowser
import shutil
# del datetime
import datetime

root = Tk()

root.geometry("1000x620+20+10")
root.resizable(width=False, height=False)
root.title('IDQ Tool Kit')
root.config(background='#F5F5F5')

dd=datetime.datetime.now()
## For Backround image:
# global image_bg
# Open the image using PIL
image = Image.open(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\pxfuel(1).jpg")
# # Convert the image to a PhotoImage object
image_bg = ImageTk.PhotoImage(image=image, master=root)

label = Label(root, image=image_bg)
label.place(x=0, y=0)

sys.path.append(r"C:\Users\rishadix\Documents\Improved Reco Tool\Original Reco Tool")
# import AttributeRecommendationUI as reco
import mac_R_C_MAIN_Module_new as reco

# sys.path.append(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\IDQ_Tools")
# import Qc_tool as qc
# import Auto_Flat_File_Script_user as flat
# import Attribute_Recommendation_Tool_vol2 as reco
# import Suppression_code as t1
# import Prime_Now_Store_specific_code as pr
# import Flat_file_vendor3p_upload as fl
# import Duplicate_Audit_Script as dup
# import Returns_Fair as rf

username = os.getlogin()
# tools=[]
def tool_list():
    if v.get()==1:
        tools=["Duplicates",  "Returns", "Weblabs", 'Recommendation_Tool']
    else:
        tools=["Flat File Creator", "Suppresion Tool","Prime Now",'RAC_Audit_Tool','RAC_Flat_file_Tool']
        
    clicked = StringVar()
    clicked.set(tools[0]) # default value

    tool_drop = OptionMenu(root, clicked, *tools, command=show_info)
    tool_drop.config(width=19, relief=SUNKEN, font=('lato',9,'bold'))
    tool_drop.place(x=420, y=160)

v=IntVar(value=1)
# v2=IntVar(value=2)
radio1 = Radiobutton(root, text='Dev', width=4, variable=v, value=1, command=tool_list, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'), disabledforeground='light grey').place(x=320, y=120)
radio2 = Radiobutton(root, text='Prod', width=5, variable=v, value=2, command=tool_list, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'),disabledforeground='light grey').place(x=630, y=120)
a1=v.get()                     # Option Value
# a2=v2.get()
# print(a1)
# print(radio2.value)
        
cur_button = None
button = None
# cb_button = None
# C3 = None
# C4 = None
# label6 = Label()

# Defining a function that will show some info based on the selected option
def show_info(option):
    global cur_button
    global button
#     global cb_button
    global C3
    global C4
    
#     option = tool_drop.get()
    if cur_button:
        cur_button.destroy()
    if button:
        button.destroy()
#     if cb_button:
#         cb_button.destroy()
#     if C3:
#         C3.destroy()
#     if C4:
#         C4.destroy()        
        
    if (a1==1) & (option == 'Flat File Creator'):
        label33.config(text=f"{option} is used to create title flat files of 3p and RA for upload.")
        label44.config(text=f"Step 1: Keep your checkmate file of corrected set of asins and deprecated_hack_merchant_id in a folder. \nStep 2: Select 'Prod' & Opt for 'Flat File Creator'  \nStep 3: After hiting 'Run' button, Chrome will ask your credential to open FRPG automatically. \nStep 4: Select the folder (created in Step 1) & the output flat files will be generated on the same folder.")
        label55.config(text=f"1: Do not change anything on the checkmate file. \n2: Export the deprecated_hack_merchant_id without language tag. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any unneccesary space & spelling mistakes should be avoided).")

        def start_tool():
            fl.flat_file(os.getenv('USERNAME'))
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         x = os.getlogin()
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Flat_file_1.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\FF_Creator_input.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     
        
    elif (a1==1) & (option == 'Suppresion Tool'):
        label33.config(text=f"{option} is used for Suppressing the Existing incorrect value of an attribute and helps in flowing the correct value which is already uploaded for that attribute in CSI. This helps the program team to correct the Catalogue quality of the ASIN whose score is not met according to Amazon Quality check.")
        label44.config(text=f"Step 1: Select the 'Prod' option & opt for Suppression tool \nStep 2: Check the Excel input & Hit OK \nStep 3: First, It will ask you to upload the CSI file & then Corrected file.  \nStep 4: Output will be found on 'Document' folder in Ion file format \nStep 5: Upload it via FRPG with Suppression Merchant Code")
        label55.config(text=f"1: It is mandatory to check in your CSI file that there is no blank in attribute values of any ASIN. \n2: The CSI file should be of 3P, No RA ASIN. \n3: Invalid ASIN shouldn't be there in the list of ASIN \n4: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

#         v3 = IntVar()
#         v4 = IntVar()
#         def cb_check_1():
#             if v3.get():
#                 C4.config(state=DISABLED)
#             else:
#                 C4.config(state=NORMAL)
# #                 root.after(7000, C4.destroy)

#         C3 = Checkbutton(root, text="Excel File Input", variable=v3, command=cb_check_1).place(x=610, y=330)
#         C4 = Checkbutton(root, text="Flat File Input", variable=v4, command=cb_check_1).place(x=815, y=330)
# #         def rem_cb():
# #             C3.destroy()
# #             C4.destroy()        
#         cb_button = Button(root, text='CheckBox', command=rem_cb, relief=SUNKEN, font=('lato',10), cursor='hand2', width=9, activebackground='#B0C4DE').place(x=730, y=425)
#         root.after(7000, cb_button.destroy)
        def press(x=1,y=2,z=os.getlogin()):
            t1.xyza(x,y,z)
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=585, y=560)
            
#         cur_button = Button(root, text='Run', command=lambda:press(v3.get(),v4.get(), os.getenv('USERNAME')), relief=SUNKEN, font=('lato',10), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button = Button(root, text='Run', command=press, relief=SUNKEN, font=('lato',10), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=390)

        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)
        
    elif (a1==1) & (option == 'Duplicates'):
        label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
        label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated.  \nStep 3: Then the updated valid_vlaues list need to be feeded \nStep 4: The output will be shared in the same location as input file.")
        label55.config(text=f"1: The updated valid_values list gets from the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

        def start_tool():
            dup.duplicates(os.getenv('USERNAME'))
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         x = os.getlogin()
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     
    
    elif (a1==1) & (option == 'Prime Now'):
        label33.config(text=f"{option} is used to map the ASIN with seller sku, update & delete the Price, Quantity & GST.")
        label44.config(text=f"Step 1: Need to update the template i.e. Upload_Delete_Input (Use 'Download Input Template' to get the Input file) \nStep 2: After Hiting 'Run' button, It'll ask for the the folder where flat files need to be saved. \nStep 3: Once the tool created flat files, FRPG will be opened in Google Chrome and starts uploading the flat files. \nStep 4: The completion Report will be shared on activity status.")
        label55.config(text=f"1: Make sure the sku & seller ID are valid in the template. \n2: Task attribute need to be accurately updated as per request \n3: The Column Name/Headers are case Sensitive hence it should not be changed.")

        def start_tool():
            pr.prime()
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         x = os.getlogin()
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
#         def download_file():
#             src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\Prime_Now\Upload_Delete_Input.csv"
#             dst = r"C:\\Users\\" +username+ "\\Downloads\\Upload_Delete_Input.csv"
#             shutil.copy(src, dst)
#         button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
#         button.place(x=695, y=225)     
   
    elif (a1==1) & (option == 'Returns'):
        label33.config(text=f"{option} is used to update Cat & Sub Cat of the given set of ASINs.")
        label44.config(text=f"Step 1: Hit the 'Run' Button to proceed \nStep 2: Tool creates Ion file as Output & gets uploaded in FRPG automatically. \nStep 3: The Output & Completion Report will be updated on the selected path.")
        label55.config(text=f"1: The Input File gets auto-updated every week. \n2: The Column Name/Headers are case Sensitive hence it should not be changed.")

        def start_tool():
            rf.Returns(os.getenv('USERNAME'))
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)

        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     
    
    elif (a1==1) & (option == 'Weblabs'):
        label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
        label44.config(tebixt=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated  \nStep 3: The output will be shared in the same location as input file.")
        label55.config(text=f"1: The valid values need to be updated every week in the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

        def start_tool():
            qc.Qc_tool(os.getenv('USERNAME'))
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         x = os.getlogin()
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\
            \Audit_Tool_Input_file.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     

    elif (a1==1) & (option == 'Recommendation_Tool'):
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
        label44.config(text=f"Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
        label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")
        
        def start_tool():
            reco.Reco_tool()
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         username = os.getlogin()
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Reco_Input_Template.csv"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\Reco_Input_Template.csv"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     
    
    elif (a1==1) & (option == 'RAC_Audit_Tool'):
        label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the valid values & freetext as T/F")
        label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated \nStep 3: Then the updated valid_values list need to be feeded \nStep 4: The output will be shared in the same location as input file.")
        label55.config(text=f"1: The updated valid values list need to be fetched from the Bridge sharepoint (reach out to @rishadix incase of un-accessibility)\n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

        def start_tool():
            qc.Qc_tool(os.getenv('USERNAME'))
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         x = os.getlogin()
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     

    elif (a1==1) & (option == 'RAC_Flat_file_Tool'):
        label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
        label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool. \nStep 2: First, it'll ask for the file with are updated required value. \nStep 3: The output will be shared in the same location as input file.")
        label55.config(text=f"\n1: The Column Name/Headers are case Sensitive hence it should not be changed. \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n3: The downloaded Input Template file will be located in 'Downloads' folder.")
        def start_tool():
            flat.fl_file(os.getenv('USERNAME'))
            label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
            label6.place(x=530, y=405)
            root.after(7000, label6.destroy)
#         x = os.getlogin()        
        cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
        cur_button.place(x=750, y=350)
        def download_file():
            src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Auto_Input_Flat_File.xlsx"
            dst = r"C:\\Users\\" +username+ "\\Downloads\\Auto_Input_Flat_File.xlsx"
            shutil.copy(src, dst)
        button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
        button.place(x=695, y=225)     
     
    else:
        label6=Label(root, text=cb.get()+" Not active", fg='red', font=("Helvetica", 15))
        label6.place(x=530, y=405)
        print('not active')   
    
label1 = Label(root, text=f"IDQ Tool Kit", fg='white', bg='#708090', relief=SUNKEN, highlightthickness=2, font=('lato',20,'bold'), width=15)
label1.pack(side='top')

label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", fg='indigo', bg='Gray92', padx=4, pady=4, font=('lato',10))
label2.pack(side='top')

def sim_link():
    webbrowser.open_new(r'https://issues.amazon.com/issues/create?assignedFolder=9f87ec2e-46f2-4009-80e3-d6ae7aac6bea&title=Process%2FSOP+Automation+request&description=Please+provide+the+below+pre-requisite+Information+for+your+request+type%0A%0AA.+Request+type%3A+New+Product+Request+%5C+Feature+Request%0A1.+Business+Case%3A+%0A2.+Impact+analysis%3A%0Aa.+2+pager+Doc%3A+Please+attached+to+SIM+2+pager+doc+containing+all+information+pertaining+to+steps+or+process+that+need+to+automated.%0Ab.+no.+of+FTE+saved+by+this+automation%3B+%0A%0A%23+Note+%3A+If+requested+information+is+not+provieded+then%2C+SIM+will+be+auto+closed+in+12+hrs&descriptionContentType=text%2Fplain&extensions%5Btt%5D%5Bcategory%5D=')

but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", command=sim_link, borderwidth=2, fg='#008000', cursor='hand2',font=('lato',10), relief=SUNKEN)
but1.pack(side='right', anchor='sw')

label3 = Label(root, text="Why do we use this Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
label3.place(x=30, y=225)
label33 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
label33.place(x=30, y=245)

label4 = Label(root, text="How to Use the Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
label4.place(x=30, y=335)
label44 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
label44.place(x=30, y=355)

label5 = Label(root, text="Points to Remember:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
label5.place(x=30,y=480)

label55 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
label55.place(x=30, y=500)

but3 = Button(root, text=" Exit ", borderwidth=1, bg='Brown', fg='white', cursor='hand2', width=4, command=root.destroy, font=('lato',11))
but3.place(x=750, y=460)

root.mainloop()


# In[ ]:





# In[3]:


# Improved UI with 'Download Input File Template'  without <<Start>> Button:

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys
import wget
import webbrowser
import shutil
# import datetime
def user_form():
    root = Tk()

    root.geometry("1000x620")
    root.resizable(width=False, height=False)
    root.title('IDQ Tool Kit')
    root.config(background='#F5F5F5')

    ## For Backround image:
    # global image_bg
    # Open the image using PIL
    image = Image.open(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\pxfuel(1).jpg")
    # image = Image.open(r"C:\Users\rishadix\Downloads\bbackground.jpg")
    # # Convert the image to a PhotoImage object
    image_bg = ImageTk.PhotoImage(image=image, master=root)

    label = Label(root, image=image_bg)
    label.place(x=0, y=0)
    # labell.pack()

    sys.path.append(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\IDQ_Tools")
    import Qc_tool as qc
    import Auto_Flat_File_Script_user as flat
    import Attribute_Recommendation_Tool_vol2 as reco

    username = os.getlogin()

    def tool():
        pass

#     cur_button = None
    button = None
    # label6 = Label()

    # Defining a function that will show some info based on the selected option
    def show_info(option):
        global cur_button
        global button

    #     option = tool_drop.get()
        if cur_button:
            cur_button.destroy()
        if button:
            button.destroy()

        if option == 'Flat File Creator':

    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

        elif option == 'Suppresion Tool':
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")
        elif option == 'Duplicates':
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

        elif option == 'Prime Now':
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

        elif option == 'Returns':
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

        elif option == 'Weblabs':
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

        elif option == 'Recommendation_Tool':
    #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
    #         cur_button.place(x=260, y=220)
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the file with are updated required value \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

            def start_tool():
                reco.Reco_tool(username)
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
            username = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Reco_Input_Template.csv"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Reco_Input_Template.csv"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif option == 'RAC_Audit_Tool':
            label33.config(text=f"{option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated.")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool \nStep 2: First, it'll ask for the Input file having the required data updated  \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The valid values need to be updated every week in the Bridge. \n2: The Column Name/Headers are case Sensitive hence it should not be changed. \n3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n4: The downloaded Input Template file will be located in 'Downloads' folder.")

            def start_tool():
                qc.Qc_tool(x)
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
            x = os.getlogin()
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Audit_Tool_Input_file.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Audit_Tool_Input_file.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

        elif option == 'RAC_Flat_file_Tool':
            label33.config(text=f"{option} is used to create a Flat File ready to be uploaded")
            label44.config(text=f"Step 1: Hit the 'Run' Button to use this Tool. \nStep 2: First, it'll ask for the file with are updated required value. \nStep 3: The output will be shared in the same location as input file.")
            label55.config(text=f"1: The Column Name/Headers are case Sensitive hence it should not be changed. \n2: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided). \n3: The downloaded Input Template file will be located in 'Downloads' folder.")
            def start_tool():
                flat.fl_file(x)
                label6 = Label(root, text="Task Completed", fg='brown', bg='Gray96', width=15, font=('lato',10,'bold'))
                label6.place(x=530, y=405)
                root.after(7000, label6.destroy)
            x = os.getlogin()        
            cur_button = Button(root, text=(f"Run"), command=start_tool, relief=SUNKEN, font=('lato',11), cursor='hand2', width=4, activebackground='#B0C4DE')
            cur_button.place(x=750, y=350)
            def download_file():
                src = r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Rishabh\Input Files\Auto_Input_Flat_File.xlsx"
                dst = r"C:\\Users\\" +username+ "\\Downloads\\Auto_Input_Flat_File.xlsx"
                shutil.copy(src, dst)
            button = Button(root, text='Download Input Template', font=('lato',8,'bold'), cursor='hand2', bg='Steel Blue', fg='white', activebackground='#66CDAA', command=download_file)
            button.place(x=695, y=225)     

    label1 = Label(root, text=f"IDQ Tool Kit", fg='white', bg='#708090', relief=SUNKEN, highlightthickness=2, font=('lato',20,'bold'), width=15)
    label1.pack(side='top')

    label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", fg='indigo', bg='Gray92', padx=4, pady=4, font=('lato',10))
    label2.pack(side='top')

    but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", borderwidth=2, fg='#008000', cursor='hand2',font=('lato',10))
    but1.pack(side='right', anchor='sw')

    value = ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool",'Recommendation_Tool']

    clicked = StringVar()
    clicked.set(value[0]) # default value

    tool_drop = OptionMenu(root, clicked, *value, command=show_info)
    tool_drop.config(width=19, relief=SUNKEN, font=('lato',9,'bold'))
    tool_drop.place(x=420, y=160)

    label3 = Label(root, text="Why do we use this Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label3.place(x=30, y=225)
    label33 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label33.place(x=30, y=245)
    # label33.pack(side='left', anchor='w')

    label4 = Label(root, text="How to Use the Tool:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label4.place(x=30, y=335)
    label44 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label44.place(x=30, y=355)
    # label4.pack(side='right', anchor='e')

    label5 = Label(root, text="Points to Remember:", fg='#483D8B', bg='Gray96', font=('lato',10,'bold','underline'))
    label5.place(x=30,y=480)
    # label5.pack(side='bottom', anchor='w')
    label55 = Label(root, wraplength=450, font=('lato',10), bg='Gray96', anchor='w', justify="left")
    label55.place(x=30, y=500)

    # but2=Button(root, text='<< Start >>', command=show_info, cursor='hand2', font=('lato',11))
    # but2.place(x=460, y=400)

    but3 = Button(root, text=" Exit ", borderwidth=1, bg='Brown', fg='white', cursor='hand2', width=4, command=root.destroy, font=('lato',11))
    but3.place(x=750, y=460)

    radio1 = Radiobutton(root, text='Dev', width=4, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'), disabledforeground='light grey').place(x=320, y=120)
    radio2 = Radiobutton(root, text='Prod', width=5, relief=SUNKEN, activebackground='#B0C4DE', font=('lato',8,'bold'),disabledforeground='light grey').place(x=630, y=120)

    root.mainloop()


# In[17]:


import webbrowser
import sys
import os


# In[5]:


# Methods of opening the accessing the web page:

webbrowser.open('https://quip-amazon.com/36RZA7HYggh2#GMX9BA8Zx9B', new=1, autoraise=False)
webbrowser.open_new('https://quip-amazon.com/36RZA7HYggh2#GMX9BA8Zx9B')


# In[25]:


import tkinter as tk
import webbrowser

def open_browser(event):
    # get the text of the button that was clicked
    url = event.widget.cget("text")
    # add ".com" to the text to form a valid URL
    url = url + ".com"
    # open the URL in a new browser window
    webbrowser.open_new(url)

# create a GUI window
window = tk.Tk()
window.title("Web Browser")

# create two buttons with text "Google" and "Bing"
button1 = tk.Button(window, text="Google")
button2 = tk.Button(window, text="Bing")

# bind the buttons to the open_browser function
button1.bind("<Button-1>", open_browser)
button2.bind("<Button-1>", open_browser)

# pack the buttons in the window
button1.pack(side=tk.LEFT, fill='y')
button2.pack(side=tk.RIGHT)

# start the GUI loop
window.mainloop()


# In[26]:


sys.path.insert(0, 'https://quip-amazon.com/AVJgA8U0zt3j/Attribute-Recommendation-Tool')


# In[30]:


# cmd='date'
# os.system(cmd)

os.chdir('C:/Users/rishadix/')
os.getcwd()


# In[58]:


from tkinter import *

def flipper(event):
    # print the text of the clicked label
    print("label text:", event.widget.cget("text"))
    # change the text of the clicked label
    event.widget.config(text="Ullu Banaya Bada maza aya !!")

main = Tk()
# create two labels with different texts
switcher = Label(main, bg='white', text="Button_1", font="-weight bold")
switcher1 = Label(main, bg='white', text="Button_2", font="-weight bold")
# place the labels on the window
switcher.grid(padx=15, pady=5,ipadx=120, ipady=50)
switcher1.grid(padx=15, pady=5, ipadx=80, ipady=30)
# bind the flipper function to the click event on both labels
switcher.bind("<Button-1>", flipper)
switcher1.bind("<Button-1>", flipper)

main.mainloop()


# In[ ]:





# In[60]:


def create_button(parent, text, command):
    # create a button widget with the given parent, text, and command
    button = tk.Button(parent, text=text, command=command)
    # return the button widget
    return button


# In[61]:


# import tkinter module
import tkinter as tk

# create a root window
root = tk.Tk()

# define a function to print a message
def say_hello():
    print("Hello!")

# define a function to print another message
def say_goodbye():
    print("Goodbye!")

# create two buttons using the create_button function
button1 = create_button(root, "Hello", say_hello)
button2 = create_button(root, "Goodbye", say_goodbye)

# place the buttons on the window
button1.pack()
button2.pack()

# start the main event loop
root.mainloop()


# In[67]:


from tkinter import filedialog, messagebox
def input_file():
    a = filedialog.askopenfilename()
    aa = pd.read_excel(a)
    return a


# In[179]:


# import tkinter as tk

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')

# # show a label
# label = Label(root, text='This is a label')
# label.pack(ipadx=10, ipady=10)

# root.mainloop()


# In[ ]:


Label()


# In[96]:


root=Tk()
root.geometry('423x378')
root.title('My First GUI')
widget = Canvas(root, width = 323, height=278)


widget.pack()
# widget.create_line(0,3,333,98, fill='red')
widget.grid(sticky=W)

root.mainloop()


# In[180]:


# from tkinter import *
# from tkinter.ttk import *

# root = Tk()
# s = Style()
# s.configure('My.TFrame', background='red')
# mail1 = Frame(root, style='My.TFrame')
# mail1.place(height=70, width=400, x=83, y=109)
# mail1.config()
# root.mainloop()


# In[ ]:





# In[1]:


# To get the Drop-Down & info:
from tkinter import *
import os

root = Tk()
root.geometry("550x350")
root.resizable(width=False, height=False)
root.title('IDQ Tools')
root.config(background='#F5F5F5')

username = os.getlogin()
# print(f"Welcome {username}!!")

# Define a function that will show some info based on the selected option
def show_info(option):
    # You can use option to access the selected value
    if option == 'Tool1':
#         def on_click():
#             label.config(text="Goodbye", bg="red")
#             button = Button(root, text="Click me", command=on_click)
#             button.pack()
        label3.config(text=f"This is {option} & it is the 1st tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Step 4:")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    if option == 'Tool2':
        label3.config(text=f"This is {option} & it is the 2nd tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Step 4:")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    if option == 'Tool3':
        label3.config(text=f"This is {option} & it is the 3rd tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Step 4:")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    if option == 'Tool4':
        label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Step 4:")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")

f1 = Frame(root, bg='grey', borderwidth=2, relief=SUNKEN)
f1.pack()
label1 = Label(root, text=f"IDQ Tool Kit", font='bold', padx=4, foreground='black', background='#00CED1')
label1.pack(side='top')

f2 = Frame(root, bg='black')
f2.pack(side='top')
label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", padx=2, pady=4, fg='#800080', bg='#C0C0C0')
label2.pack(side='top')

# Command need to be updated:
but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", borderwidth=1, fg='purple', relief=SUNKEN, cursor='hand2', bg='#ADD8E6')
but1.pack(side='right', anchor='sw')

# Define the list of options
Tools = ["Tool1", "Tool2", "Tool3", "Tool4"]

# Define the variable to store the selected option
clicked = StringVar()
clicked.set(Tools[0]) # Set the default value

# Create the OptionMenu widget with the command argument
drop = OptionMenu(root, clicked, *Tools, command=show_info)
drop.pack(ipadx=3)

# Create a label to display some info
f3 = Frame(root, bg='red', borderwidth=1, relief=SUNKEN)
f3.pack(side='top')
label3 = Label(root, text="You'll get the Tool details here as you select one", padx=3, pady=3, fg='white' , bg='#008080')
label3.pack()

f4 = Frame(root, bg='grey', borderwidth=0, relief=SUNKEN)
f4.pack()
label4 = Label(root, text="How to Use info", foreground='#FFFFF0', bg='#483D8B')
label4.pack(side='top')

f5 = Frame(root, bg='red', borderwidth=1, width=17, relief=SUNKEN)
f5.pack(side='bottom', anchor='sw')
label5 = Label(root, text="Tool Facts", foreground='#191970' , bg='#B0C4DE')
label5.pack(side='bottom', anchor='sw')

root.mainloop()


# In[401]:


import pandas as pd
df=pd.read_excel("C:/Users/rishadix/Downloads/Auto_Input_Flat_File.xlsx")
df.columns


# In[ ]:





# In[ ]:


# # Updated UI w/o Frames & bg:

# from tkinter import *
# import os
# import sys

# sys.path.append(r"C:\Users\rishadix\Documents\Scrapping & Updating Attributes Project IV\Audit_Tool")
# import Qc_tool_func as qc

# root = Tk()
# root.geometry("600x390")
# root.resizable(width=False, height=False)
# root.title('IDQ Tool Kit')
# root.config(background='#F5F5F5')

# username = os.getlogin()
# # print(f"Welcome {username}!!")
# # qc.Qc_tool(os.getenv('username'))

# def tool():
#     pass
# # def tool2():
# #     pass

# # Define a function that will show some info based on the selected option
# def show_info(option):

#     if option == 'Flat File Creator':

#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 1st tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")

#     elif option == 'Suppresion Tool':
#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 2nd tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#     elif option == 'Duplicates':
#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 3rd tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#     elif option == 'Prime Now':
#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#     elif option == 'Returns':
#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#     elif option == 'Weblabs':
#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#     elif option == 'RAC_Audit_Tool':
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#         button2 = Button(text="<< Start >>", borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=qc.Qc_tool(username))
#         button2.place(x=260, y=260)
#         label6 = Label(root, text="Task Completed", bg='#F5F5F5', fg='#663399')
#         label6.pack(side='bottom', anchor='sw')
#     elif option == 'RAC_Flat_file_Tool':
#         button2 = Button(text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         button2.place(x=260, y=260)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")

# label6 = Label(root, text="Task Completed", bg='#F5F5F5', fg='#663399')
# label6.place(x=240, y=75)

# # f1 = Frame(root, bg='grey', borderwidth=2, relief=SUNKEN)
# # f1.pack()
# label1 = Label(root, text=f"IDQ Tool Kit", font='bold', padx=4, bg='#F5F5F5', foreground='black')
# label1.pack(side='top')

# # f2 = Frame(root, bg='black')
# # f2.pack(side='top')
# label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", padx=2, pady=4, fg='#800080', bg='#F5F5F5')
# label2.pack(side='top')

# but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", borderwidth=1, fg='purple', relief=SUNKEN, cursor='hand2')
# but1.pack(side='right', anchor='sw')

# Tools= ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool"]

# clicked = StringVar()
# clicked.set("Tools[0]") # default value

# drop = OptionMenu(root, clicked, *Tools, command=show_info)
# drop.place(x=240, y=75)
# # drop.pack(ipadx=3)

# # f3 = Frame(root, bg='red', borderwidth=1, relief=SUNKEN)
# # f3.pack(side='top')
# label3 = Label(root, text="You'll get the Tool details here as you select one", padx=3, pady=3, fg='#000080', bg='#F5F5F5')
# label3.place(x=30, y=120)
# # label3.pack(side='top', anchor='w')  

# # f4 = Frame(root, bg='grey', borderwidth=0, relief=SUNKEN)
# # f4.pack()
# label4 = Label(root, text="This section says about 'How to Use the Tool'", fg='#800000', bg='#F5F5F5')
# label4.place(x=340, y=120)
# # label4.pack(side='top', anchor='e')

# # f5 = Frame(root, bg='red', borderwidth=1, width=17, relief=SUNKEN)
# # f5.pack(side='bottom', anchor='sw')
# label5 = Label(root, text="Tool Facts", bg='#F5F5F5', fg='#663399')
# label5.pack(side='bottom', anchor='sw')

# root.mainloop()


# In[ ]:


qc.Qc_tool_func(username)


# In[177]:


os.getenv('username')


# In[ ]:


# Updated UI with Image Background with 2 active tools:

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys

root = Tk()

root.geometry("800x600")
# root.resizable(width=False, height=False)
root.title('IDQ Tool Kit')
root.config(background='#F5F5F5')

## For Backround image:
# global image_bg
# Open the image using PIL
image = Image.open(r"C:/Users/rishadix/Downloads/bbackground.jpg")
# # Convert the image to a PhotoImage object
image_bg = ImageTk.PhotoImage(image=image, master=root)

label2 = Label(root, image=image_bg)
label2.place(x=0, y=0, relwidth=1, relheight=1)
# labell.pack()

sys.path.append(r"C:\Users\rishadix\Documents\Scrapping & Updating Attributes Project IV\Audit_Tool")
import Qc_tool_func as qc

username = os.getlogin()
# print(f"Welcome {username}!!")
# qc.Qc_tool(os.getenv('username'))

def tool():
    pass
# def tool2():
#     pass

cur_button = None
label6 = None
# Defining a function that will show some info based on the selected option
def show_info():
    global cur_button
    global label6
    option = tool_drop.get()
    if cur_button:
        cur_button.destroy()
    if label6:
        label6.destroy()
       
    if option == 'Flat File Creator':
        
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label3.config(text=f"This is {option} & it is the 1st tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
        
    elif option == 'Suppresion Tool':
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label3.config(text=f"This is {option} & it is the 2nd tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    elif option == 'Duplicates':
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label3.config(text=f"This is {option} & it is the 3rd tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
    elif option == 'Prime Now':
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
    elif option == 'Returns':
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
    elif option == 'Weblabs':
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=220)
        label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
    elif option == 'RAC_Audit_Tool':
        label3.config(text=f"Why do we use this Tool?\n {option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated")
        label4.config(text=f"How to use {option}: \n Step 1: Hit the 'Run' Button to use this Tool \n Step 2: First, it'll ask for the file with are updated required value \n Step 3: The output will be shared in the same location as input file.")
        label5.config(text=f"Points to be remembered before using {option}: \n 1: The valid values need to be updated every week in the Bridge. \n 2: The Column Name/Headers are case Sensitive hence it should not be changed \n 3: Attribute values should be properly checked before feeding (i.e.Any space/spelling mistakes should be avoided)")
        def start_tool():
            qc.Qc_tool(username)
            label6 = Label(root, text="Task Completed", width=15, fg='black', font=('lato',9))
            label6.place(x=372, y=350)
        cur_button = Button(root, text=(f"Run"), command=start_tool, font=('lato',11), cursor='hand2', width=5)
        cur_button.place(x=398, y=510)
    
    elif option == 'RAC_Flat_file_Tool':
#         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
#         cur_button.place(x=260, y=380)
        label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
        label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
        label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
                
# f1 = Frame(root, bg='grey', borderwidth=2, relief=SUNKEN)
# f1.pack()
label1 = Label(root, text=f"IDQ Tool Kit", font=('bold',15), padx=4, bg='Alice Blue', foreground='black')
label1.pack(side='top')

# f2 = Frame(root, bg='black')
# f2.pack(side='top')
label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", padx=2, pady=4, fg='#800080', bg='Alice Blue',font=('lato',10))
label2.pack(side='top')

but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", borderwidth=1, fg='purple', relief=SUNKEN, cursor='hand2',font=('lato',9))
but1.pack(side='right', anchor='sw')

# Tools= ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool"]

clicked = StringVar()

# drop = OptionMenu(root, clicked, *Tools, command=show_info)
# drop.place(x=255, y=75)
value = ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool"]
tool_drop = ttk.Combobox(root, values=value, width=16)
tool_drop.place(x=345, y=85)
tool_drop.set('Flat File Creator') # default value

f3 = Frame(root, bg='Green', borderwidth=1, relief=SUNKEN)
f3.place(x=0, y=150)
# f3.pack(side='left', anchor='ne')
label3 = Label(f3, text="You'll get the Tool details here as you select one", fg='black', bg='Alice Blue', wraplength=300, font=('lato',10))
label3.pack(side='left', anchor='w')
# label3.pack(side='top', anchor='w')  

f4 = Frame(root, bg='Blue', borderwidth=1, relief=SUNKEN)
# f4.pack(side='right', anchor='nw')
f4.place(x=520, y=150)
label4 = Label(f4, text="This section says about 'How to Use the Tool'", fg='black',bg='Alice Blue', wraplength=300, font=('lato',10))
label4.pack(side='right', anchor='e')
# label4.pack(side='top', anchor='e')

f5 = Frame(root, bg='red', borderwidth=1, relief=SUNKEN)
# f5.pack(side='bottom', anchor='sw')
f5.pack(side='bottom', anchor='sw')
label5 = Label(f5, text="Tool Facts", fg='black',bg='Alice Blue', wraplength=300, font=('lato',10))
label5.pack(side='bottom', anchor='sw')

but2=Button(root, text='<<Start>>', command=show_info, cursor='hand2', font=('lato',11))
but2.place(x=385, y=400)

but3 = Button(root, text=" Exit ", borderwidth=2, relief=SUNKEN, bg='Brown', fg='white', cursor='hand2', width=5, command=root.destroy, font=('lato',11))
but3.place(x=398, y=550)

root.mainloop()


# In[ ]:





# In[ ]:


## Improved UI with 'Download Input File Template' button for 2 Tools & <<Start>> Button:

# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# import os
# import sys
# import wget
# import webbrowser

# root = Tk()

# root.geometry("1000x620")
# root.resizable(width=False, height=False)
# root.title('IDQ Tool Kit')
# root.config(background='#F5F5F5')

# ## For Backround image:
# # global image_bg
# # Open the image using PIL
# image = Image.open(r"C:/Users/rishadix/Downloads/bbackground.jpg")
## image = Image.open(r"C:/Users/rishadix/Downloads/pxfuel(1).jpg")
# # # Convert the image to a PhotoImage object
# image_bg = ImageTk.PhotoImage(image=image, master=root)

# label = Label(root, image=image_bg)
# label.place(x=0, y=0)
# # labell.pack()

# sys.path.append(r"C:\Users\rishadix\Documents\Scrapping & Updating Attributes Project IV")
# import Qc_tool_func as qc
# import Auto_Flat_File_Script_user as flat

# username = os.getlogin()
# # x = os.getlogin()
# # qc.Qc_tool(os.getenv('username'))

# def tool():
#     pass
# # def call_file():
# #     webbrowser.open_new(url)

# cur_button = None
# button = None
# # label6 = Label()

# # Defining a function that will show some info based on the selected option
# def show_info():
#     global cur_button
#     global button
#     global label6
#     option = tool_drop.get()
#     if cur_button:
#         cur_button.destroy()
#     if button:
#         button.destroy()
# #     if label6:
# #         label6.destroy()
#     if option == 'Flat File Creator':
        
# #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
# #         cur_button.place(x=260, y=220)
#         label3.config(text=f"This is {option} & it is the 1st tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
        
#     elif option == 'Suppresion Tool':
# #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
# #         cur_button.place(x=260, y=220)
#         label3.config(text=f"This is {option} & it is the 2nd tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
#     elif option == 'Duplicates':
# #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
# #         cur_button.place(x=260, y=220)
#         label3.config(text=f"This is {option} & it is the 3rd tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
#     elif option == 'Prime Now':
# #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
# #         cur_button.place(x=260, y=220)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
#     elif option == 'Returns':
# #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
# #         cur_button.place(x=260, y=220)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
#     elif option == 'Weblabs':
# #         cur_button = Button(root, text=(f"<< Start >>"), borderwidth=1, bg='Azure', fg='purple', relief=SUNKEN, cursor='hand2', command=tool)
# #         cur_button.place(x=260, y=220)
#         label3.config(text=f"This is {option} & it is the 4th tool used for: \n a) \n b) \n c) \n d)")
#         label4.config(text=f"How to use {option}: \n Step 1: \n Step 2: \n Step 3: \n Hit the 'Start' Button to use this Tool")
#         label5.config(text=f"Facts about the {option}: \n 1: \n 2: \n 3:")
    
#     elif option == 'RAC_Audit_Tool':
#         label3.config(text=f"Why do we use this Tool?\n {option} is used to audit the attribute values which need to be uploaded (or already uploaded) with the existing valid_values. These valid_values are provided by the Program team via respective Category. This Tool delivers the values as T/F where 'T' is the correct value & can be updated")
#         label4.config(text=f"How to use {option}: \n Step 1: Hit the 'Run' Button to use this Tool \n Step 2: First, it'll ask for the Input file having the required data updated  \n Step 3: The output will be shared in the same location as input file.")
#         label5.config(text=f"Points to be remembered before using {option}: \n 1: The valid values need to be updated every week in the Bridge. \n 2: The Column Name/Headers are case Sensitive hence it should not be changed \n 3: Attribute values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")

#         def start_tool():
#             qc.Qc_tool(username)
#             label6 = Label(root, text="Task Completed", width=15, fg='black', font=('lato',9))
#             label6.place(x=447, y=450)
#             root.after(5000, label6.destroy)
#         cur_button = Button(root, text=(f"Run"), command=start_tool, font=('lato',11), cursor='hand2', width=4)
#         cur_button.place(x=480, y=500)
#         def call_file():
#             webbrowser.open_new(url)
#         url = "https:/drive.corp.amazon.com/documents/rishadix@/Audit_Tool_Input_file.xlsx"
#         button = Button(root, text='Download Input File Template', font=('lato',8), cursor='hand2', bg='#2F4F4F', fg='Azure', activebackground='#3CB371', command=call_file)
#         button.place(x=680, y=140)
    
#     elif option == 'RAC_Flat_file_Tool':
#         label3.config(text=f"Why do we use this Tool?\n {option} is used to create a Flat File ready to be uploaded")
#         label4.config(text=f"How to use {option}: \n Step 1: Hit the 'Run' Button to use this Tool \n Step 2: First, it'll ask for the file with are updated required value \n Step 3: The output will be shared in the same location as input file.")
#         label5.config(text=f"Points to be remembered before using {option}: \n 1: The Column Name/Headers are case Sensitive hence it should not be changed \n 3: Attribute Name & values should be properly checked before feeding to the Tool (i.e.Any space/spelling mistakes should be avoided)")
#         def start_tool():
#             flat.fl_file(x)
#             label6 = Label(root, text="Task Completed", width=15, fg='black', font=('lato',9))
#             label6.place(x=447, y=450)
#             root.after(5000, label6.destroy)
#         x = os.getlogin()        
#         cur_button = Button(root, text=(f"Run"), command=start_tool, font=('lato',11), cursor='hand2', width=4)
#         cur_button.place(x=480, y=500)
#         def call_file():
#             webbrowser.open_new(url)
#         url = "https:/drive.corp.amazon.com/documents/rishadix@/Auto_Input_Flat_File.xlsx"
#         button = Button(root, text='Download Input File Template', font=('lato',8), cursor='hand2', bg='#2F4F4F', fg='Azure', activebackground='#3CB371', command=call_file)
#         button.place(x=680, y=140)     
                
# label1 = Label(root, text=f"IDQ Tool Kit", font=('bold',15), padx=4, bg='Light Cyan', foreground='black')
# label1.pack(side='top')

# label2 = Label(root, text=f"Welcome {username}! \n Please select the required Tool", padx=2, pady=4, fg='dark blue', bg='Light Cyan',font=('lato',10))
# label2.pack(side='top')

# but1 = Button(root, text=f"For any Issue\nClick here to raise a SIM", borderwidth=1, fg='purple', relief=SUNKEN, cursor='hand2',font=('lato',9))
# but1.pack(side='right', anchor='sw')

# clicked = StringVar()

# value = ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", "RAC_Audit_Tool", "RAC_Flat_file_Tool"]
# tool_drop = ttk.Combobox(root, values=value, width=16)
# tool_drop.place(x=445, y=140)
# tool_drop.set('Flat File Creator') # default value

# f3 = Frame(root, bg='Green', borderwidth=1, relief=SUNKEN)
# f3.place(x=80, y=200)
# label3 = Label(f3, text="You'll get the Tool details here as you select one", fg='black', bg='Light Cyan', wraplength=350, font=('lato',10))
# label3.pack(side='left', anchor='w')

# f4 = Frame(root, bg='Blue', borderwidth=1, relief=SUNKEN)
# f4.place(x=585, y=200)
# label4 = Label(f4, text="This section says about 'How to Use the Tool'", fg='black',bg='Light Cyan', wraplength=350, font=('lato',10))
# label4.pack(side='right', anchor='e')

# f5 = Frame(root, bg='red', borderwidth=1, relief=SUNKEN)
# f5.pack(side='bottom', anchor='sw')
# label5 = Label(f5, text="Tool Facts", fg='black',bg='Light Cyan', wraplength=300, font=('lato',10))
# label5.pack(side='bottom', anchor='sw')

# but2=Button(root, text='<< Start >>', command=show_info, cursor='hand2', font=('lato',11))
# but2.place(x=460, y=400)

# but3 = Button(root, text=" Exit ", borderwidth=1, relief=SUNKEN, bg='Brown', fg='white', cursor='hand2', width=4, command=root.destroy, font=('lato',11))
# but3.place(x=480, y=570)

# radio1 = Radiobutton(root, text='Dev', width=4, relief=SUNKEN, activebackground='#B0C4DE').place(x=248, y=90)
# radio2 = Radiobutton(root, text='Prod', width=5, relief=SUNKEN, activebackground='#B0C4DE').place(x=722, y=90)

# root.mainloop()


# In[ ]:


## To get the Tools via 'Dev' & 'Prod':

from tkinter import *

root = Tk()

def tool_list():
    if v.get() == 1:
        tools = ["Flat File Creator", "Suppresion Tool", "Duplicates", "Prime Now", "Returns", "Weblabs", 'Recommendation_Tool']
    else:
        tools = ["RAC_Audit_Tool", "RAC_Flat_file_Tool"]
    
    # Update the options of the OptionMenu
    tool_drop['menu'].delete(0, 'end')
    for tool in tools:
        tool_drop['menu'].add_command(label=tool, command=lambda t=tool: clicked.set(t))
    clicked.set(tools[0])

v = IntVar(value=1)
radio1 = Radiobutton(root, text='Dev', width=4, variable=v, value=1, command=tool_list)
radio2 = Radiobutton(root, text='Prod', width=5, variable=v, value=2, command=tool_list)

clicked = StringVar()
tool_drop = OptionMenu(root, clicked, '')
tool_drop.config(width=19)

radio1.pack()
radio2.pack()
tool_drop.pack()

# Call tool_list once to initialize the options of the OptionMenu
tool_list()

root.mainloop()

