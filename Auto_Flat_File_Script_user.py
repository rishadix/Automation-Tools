import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
import datetime                                                                 # To check Time Duration
import openpyxl
#from openpyxl.utils.dataframe import dataframe_to_rows 
def fl_file(x):
    root = tk.Tk()
    root.withdraw()
    
    start = datetime.datetime.now()   
    try:
        messagebox.showinfo(title= 'Choose File', message= 'Please select the file')           # RAC attribute_value updated file
        raw_file = filedialog.askopenfilename(filetypes=[('Excel file', '*.xlsx')])
        raw = pd.read_excel(raw_file)

        flat_file = pd.read_csv(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\RAC\Sample_Raw_Flat File.txt", sep="\t", nrows=0, na_values='', header=[2])               # .txt file from shared drive

        raw1 = raw.groupby(['asin'],as_index=False)['rule_applied'].agg(list)
        raw2 = raw.groupby(['asin'],as_index=False)['attribute_value'].agg(list)
        raww = pd.merge(raw1, raw2, on='asin', how='left')

        flat_file['item_sku'] = raww['asin']
        flat_file['external_product_id'] = raww['asin']
        flat_file[['external_product_id_type', 'update_delete']] = ['ASIN', 'PartialUpdate']
        flat_file.fillna('',axis=1, inplace=True)

        for i in range(len(raww['asin'])):
            for k, ii in zip(raww['rule_applied'][i],raww['attribute_value'][i]):
                flat_file[k][i] = ii

        aa = flat_file['item_sku']

        flat_file = flat_file.transpose().reset_index()
        Raw_file = pd.read_csv(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\RAC\Sample_Raw_Flat File.txt", sep="\t", nrows=2, header=None, na_values=['']).transpose()         # To concatinate Raw Flat_file

        Auto_Flat_File = pd.concat([Raw_file, flat_file], axis=1, ignore_index=True).transpose()
        Auto_Flat_File.fillna('',axis=1, inplace=True)
    except KeyError as e:
    #     pass
        print(f"New Attribute found: <<{e}>> \nPlease make sure that name of the Attribute is Correct. \nIf it's a New Attribute, Kindly raise a SIM to get this added in Sample Flat File list\n")

    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(":","-")
    end = datetime.datetime.now()                                                   # To check Time Duration
    Time_Taken = end-start                                                          # To check Time Duration
    print(f'Task Completed !! Time_Taken: {(Time_Taken.seconds)} seconds')
    messagebox.showinfo(message= 'Done')
    # To update the Task Details:
#     wb = openpyxl.load_workbook(r"//ant/dept-as/blr2-Groupdata1/FS-AutomationTechnologies/Biswa/Log_file.xlsx")
#     ws = wb['RAC_Flat_File_Tool']

    ax = pd.DataFrame({'Alias':x, 'Count_Of_Records': aa.count(), 'Time_taken (in Seconds)': Time_Taken.seconds, 'Date': dt},index=[0])
    #ax=pd.DataFrame(ab,index=[0])
    fla_file=pd.read_excel(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\Log_file.xlsx",sheet_name='RAC_Flat_File_Tool')
    fla_file=pd.concat([fla_file,ax],ignore_index=True)
    with pd.ExcelWriter(r"\\ant\dept-as\blr2-Groupdata1\FS-AutomationTechnologies\Biswa\Log_file.xlsx",engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        fla_file.to_excel(writer,sheet_name='RAC_Flat_File_Tool',index=False)
    # print(ab)
#     for row in dataframe_to_rows(ab, index=False, header=False):
#         ws.append(row)
#     wb.save(r"//ant/dept-as/blr2-Groupdata1/FS-AutomationTechnologies/Biswa/Log_file.xlsx")

    # Auto_Flat_File[0:18]
    Auto_Flat_File.to_csv(raw_file[:raw_file.rfind('/')]+'\Auto_Flat_File_'+dt+'.csv', header=0, index=False)