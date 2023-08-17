from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time,openpyxl


s = Service("C:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)


excel =openpyxl.Workbook();
sheet=excel.create_sheet(title="Problemset")
sheet.append(["s.no","Code","Tag","Complexity"])

sno=0;
time.sleep(2)

Dict=dict()
index=[1,2,3,7,11]
topics=["basic-programming","conditional-statements","implementation","ad-hoc","arrays","strings","math","mathematics","sorting","binary-search","data-structures","algorithms","greedy-algorithms","dynamic-programming","graphs","segment-trees"]
for i in range(len(topics)):
    str="https://www.codechef.com/practice/"
    if(i in index):
        str+="tags/"
    else:
        str+="topics/"

    str=str+(topics[i].strip())
    driver.get(str)
    time.sleep(2)
    count=0
    while True:
            #problem = driver.find_elements(By.XPATH,"//td[@data-colindex='1']//div//span")
            complexity=driver.find_elements(By.XPATH,"//td[@data-colindex='3']//div")
            tag = topics[i];
            code=driver.find_elements(By.XPATH ,"//td[@data-colindex='0']//div")



            c=0
            flag=True
            for j in range(len(complexity)):
                flag = True
                diff=int(complexity[j].text)
                if(diff<=1000):
                    diff="Easy"
                elif diff<=2000:
                    diff="Medium"
                elif diff<=2500:
                    diff="Mid Hard"
                elif diff<=3000:
                    diff="Hard"
                else:
                    diff="Very Hard"


                prblm_code=code[j].text
                Dict[prblm_code] =[sno,tag,diff]
                sno+=1
                print(f"{sno} {prblm_code}  {complexity[j].text}  {tag}")

            try:
             driver.find_element(By.XPATH,"//button[@title='Next Page']").click()
             time.sleep(2)
            except:
                break;
    time.sleep(2)
    print(count,"-----------------------------------------------------------------------------------------------------")

for i in Dict.keys():
    sheet.append([Dict[i][0],i,Dict[i][1],Dict[i][2]])


excel.save("codechef_problem.xlsx")








