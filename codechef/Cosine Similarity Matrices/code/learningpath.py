import pandas as pd
import openpyxl
excel=pd.read_excel("D:\PROGRAMS\Project\codechef\Output\learning_path_model.xlsx")
saving=openpyxl.Workbook()
sheet=saving.create_sheet(title="learning path")
prev=[excel.loc[0,"Tag"],excel.loc[0,"Complexity"]]
sheet.append(["User Name","Tag","Complexity"])
prev_user=excel.loc[0,"User Name"]
sheet.append([prev_user,prev[0],prev[1]])
for i in range(1,len(excel)):
    print(i)
    if(prev_user==excel.loc[i,"User Name"]):
        current=[excel.loc[i,"Tag"],excel.loc[i,"Complexity"]]
        if(prev!=current):
            sheet.append([excel.loc[i,"User Name"],excel.loc[i,"Tag"],excel.loc[i,"Complexity"]])
            prev=current
    else:
        prev_user=excel.loc[i,"User Name"]
        prev=[(excel.loc[i,"Tag"],excel.loc[i,"Complexity"])]
        sheet.append([excel.loc[i,"User Name"],excel.loc[i,"Tag"],excel.loc[i,"Complexity"]])
saving.save("learning_path_final.xlsx")