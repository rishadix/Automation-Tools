# Script of 'RAC_Audit_Tool' via IDQ Tools

import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime
def Qc_tool(x):
#     acc_list=pd.read_csv(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\Access\Acess_list.csv")             # To cross check the Code
#     print('cr')                                                       # To cross check the Code
    acc_list=['rishadix','rishabh']                                     # To cross check the Code
    if x in list(acc_list):                                             # To cross check the Code
#     if x in list(acc_list['QC Tool']):                                # To cross check the Code
        start_time = datetime.datetime.now()
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title='File for QC', message ='Select the Updated File for QC')
        QC_file = filedialog.askopenfilename(initialdir = "C:/", filetypes=[('Excel file','*.xlsx')])

        pp = pd.read_excel(QC_file, sheet_name='QC_Comp_1').astype(str)
        pp = pp.apply(lambda x: x.str.upper())

        # messagebox.askokcancel(title='valid_values file', message ='Select the updated valid_values File')
        # valid_val = filedialog.askopenfilename(filetypes=[('text file','*.txt')])
        z = pd.read_csv(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\RAC\valid_value_apr_15_2023.txt", sep='\t',encoding="Windows-1252").astype(str)
        # z = pd.read_csv('C:/Users/rishadix/Downloads/valid_value_apr_15_2023.txt', sep = '\t',encoding = "Windows-1252",\
        # names = ['Product','Attribute','Attribute_Value']).astype(str)
        z = z.apply(lambda x:x.str.upper())
        z = z.groupby(['Product','Attribute'], as_index=False)['Attribute_Value'].agg(lambda x:list(x))

        pz = pd.merge(pp, z, left_on=['ptd','rule_applied'], right_on=['Product','Attribute'], how='left')
        pz.fillna('', axis=1, inplace=True)
#         pz['valid'] = pz.apply(lambda x:bool(x['attribute_value'] in x['Attribute_Value']),axis=1)             # To cross check the Code
        pz['valid']=""
        for i in range(len(pz['ASIN'])):
            if pz['attribute_value'][i] in pz['Attribute_Value'][i]:
                pz['valid'][i] = 'T'
            else:
                pz['valid'][i] = 'F'
#         pz[11:22]
#         pz['valid'][11:22]
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(" ","-").replace(":","-")
        pz.to_csv(QC_file[:QC_file.rfind('/')]+"\QC_Output"+dt+".csv",index=False)
        end_time = datetime.datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        messagebox.showinfo(message="Done !! Please go to the Input file location for Output file")             # To cross check the Code
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(message="Access Denied.Contact sbiswaji@ to request access")

Qc_tool('rishadix')
