import pandas as pd
import requests
import openpyxl as xl
from bs4 import BeautifulSoup

def submission(name)->list:
    data_list=[]
    data_list.append(name)
    problem1=[]
    excel = xl.Workbook()
    sheet = excel.create_sheet()
    sheet.append(["User Name","Problem","Tag","Complexity","Result"])
    excel_file_path = "codechef_problem.xlsx"
    df = pd.read_excel(excel_file_path,sheet_name="Problemset")

    indexes =list( df["Name"])
    df.index=indexes

    count=0
    try:
        for i in range(len(data_list)):
            try:
                response = requests.get(f"https://www.codechef.com/users/{data_list[i]}/")
                content = BeautifulSoup(response.text, 'html.parser')
                #print(content)
                practice=content.find('section',class_="rating-data-section problems-solved")
                check=practice.find("strong").text.strip()
                print(check)
                if check !="Practice:":
                    continue;

                solved=practice.find("span")
                problem=solved.find_all("a")
            except:
                continue
            for prblm in problem:
                count+=1
                try:
                    problem1.append(prblm.text)
                    #print([data_list[0], prblm.text, df["Tag"][prblm.text], df['Complexity'][prblm.text],"Right Answer"])
                    sheet.append([data_list[0], prblm.text, df["Tag"][prblm.text], df['Complexity'][prblm.text],"Right Answer"])
                except:
                    problem1.append(prblm.text)
                    sheet.append([data_list[0], prblm.text,"data-structures", "Medium","Right Answer"])
                    #print([data_list[0], prblm.text,"data-structures","Medium","Right Answer"])

    except:
        excel.save(f"{data_list[0]}.xlsx")
        return problem1
    excel.save(f"{data_list[0]}.xlsx")
    return problem1