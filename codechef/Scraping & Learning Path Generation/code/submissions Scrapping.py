import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time,openpyxl

s=Service("C:\\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
excel = openpyxl.Workbook()
sheet = excel.create_sheet(title='user_submission')
sheet.append(["User Name","Problem","Tag","Complexity","Result"])
List=[]

excel_file_path = "D:\PROGRAMS\Project\codechef\Output\codechef_problems_3587.xlsx"
df = pd.read_excel(excel_file_path)



data_list = [
    'maroonrk', 'ksun48', 'lyrically', 'heno239', 'um_nik', 'noimi', 'hitonanode', 'happypotato', 'tute7627', 'tiger2005', 'redstar05', 'thuustalu', 'denisov', 'redstar0', 'nok0', 'timmyfeng', 'qwerty787788', 'eddard', 'kshitij_789', 'xams', 'rgb_icpc1', 'wsyhb', 'oierhzc', 'nuip', 'ak_group', 'bucketpotato', 'shiomusubi496', 'heltion', 'triplem5ds', 'testcase28', 'makmed1337', 'oier_kzc', 'lympanda', 'jackpa', 'batrr', 'stelian', 'marckess', 'ai_dev_master', 'sysulby', 'wcysai', 'kira_1234', 'aryanc403', 'pctprobability', 'mmtdp7476', 'cthau', 'prvocislo', 'nirjhor', 'yuki726', 'aging1986', 'serotonin', 'siganai', 'sungan', 'lip_arcanjo', 'mridulahi', 'minato2376', 'pooty', 'xiaowuc1', 'apoorv_me', 'megurine', 'vladden', 'primenumberzz', 'jovan_b', 'mateocv', 'leaf1415', 'shivensinha4', 'maomao90', 'alek0618', 'juliany2', 'zzrzzr', 'ecottea', 'hollwo_pelw', 'tima', 'redstar06', 'peti25', 'tobapnw', 'icecream990720', 'ronniechonev', 'tensei8869', 'rgb_icpc9', 'wjli', 'yfuka86', 'cuiaoxiang', 'fxorg', 'yash_daga', 'warmbreeze', 'lucina101', 'rddalida', 'socpite', 'dbsic211', 'shobonvip', 'jay_1048576', 'menborong', 'isaacmoris', 'czhang2718', 'brobat', 'etherinmatic', 'bachhoangxuan', 'rock_star789', 'x_arc', 'redstar07', 'alfeh', 'jaimahakal', 'demidenko', 'huangxw', 'lmlmlm', 'marcosk', 'redstar1', 'gsxj2014', 'mrho888', 'taran_1407', 'omagr_71', 'friedcheese', 'nitap511954', 'attardesakshi', 'au_20eg105412', 'srishailam_123', 'bjrg08', 'arif2021', 'vl21fe1a05d9', 'marushika3107', 'mvm_2200032006', 'vigneshwaranv3', 'sahil_gupta20', 'adi3shivany', 'xerox7', 'smilelaavanya', 'naveenkumar_24', 'aman2011', 'sravyachintala', 'aartirai1503', 'lalith_2002', 'chef1434', 'akellamanasa20', 'sakura_uchiha', 'privaten19', 'iitm21f2001389', 'vivekgarnara', 'steel001', 'r01a0449', 'yuvaranipandi', 'ninjacodernsut', 'layanareddy', 'ssimhachalam21', 'sanskar_anand7', 'srivastav1021', 'saisrija_1', 'anshikasahu24', 'routhuhemalath', 'codersai_123', 'leo_anny31', 'klu_2200030402', 'karunakarpashi', 'devilofmyworld', 'princekgarg', 'bhanusree01', 'himachaltrip11', 'kush_1719', 'aditya_aware_6', 'jivitha27', 'shubhamjha123', 'ah_aashiq', 'verse_of_mk', 'dhariyarajug20', 'shadow_f', 'mlseyedibrahim', 'trinath2310', 'sitanshu_18', 'klu_2200031851', 'klu_2200030908', 'bavisetti_ajay', 'klu_2200090099', 'charan_yarra', 'deepikavarsha0', 'ranjith5c2', 'virus2466', 'rudrasingh1339', 'sudeeporiginal', 'rajashekar213', 'chilukapavani', 'diamondhead_22', 'saisrinivas688', 'ipec_it316', 'pavani72', 'ajit28985', 'tt79', 'udaygurramu31', 'anandsagar06', 'geethikach', 'abhinavrr', 'niteshv8824', 'klu_2100031608', 'bajrangdal705', 'harshitha_6044', 'neerajkumar_97', 'sidak_123', 'utkarxhhh', 'abdulrahim2004', 'bdyby1234567', 'upmanyunidhi02', 'robo00', 'klu_2200030562', 'ugginausha2003', 'ypmanoranjan0', 'vw21nm1a0265', 'harsh_2204', 'kevin2003', 'ritika_kosigi', 'sadain_18', 'aryan_260', 'temporary25153', 'thecoder4567hj'
]



# Drop the first column since it's now used as the index

indexes =list( df["Name"])
rows=["User Name","Name","Tag","Complexity"]
df.index=indexes
l=len(data_list)
print(df["Tag"]["TOP10"])
for k in range(53,len(data_list)-100):
    List=[]
    str="https://www.codechef.com/users/"
    str+=(data_list[k].strip())


    driver.get(str)
    time.sleep(2)

    name =data_list[k]
    while True:
        problem=driver.find_elements(By.XPATH,"//table[@class='dataTable']//td//a")
        tag=driver.find_elements(By.XPATH,"//td//span//img")
        for i in range(len(tag)):
        #  print(problem[i*2].text,tag[i].get_attribute("src"))
            link = tag[i].get_attribute("src").strip()
            res = ""
            if link == "https://cdn.codechef.com/misc/alert-icon.gif":
                res = "Compliation Error"
            elif link == "https://cdn.codechef.com/misc/cross-icon.gif":
                res = "Wrong Answer"
            elif link == "https://cdn.codechef.com/misc/clock_error.png":
                res = "Time Limit Exceeded"
            elif link == "https://cdn.codechef.com/misc/tick-icon.gif":
                res = "Right Answer"
            elif link == "https://cdn.codechef.com/misc/runtime-error.png":
                res = "Runtime Error"
            elif link == "https://cdn.codechef.com/sites/all/modules/codechef_tags/images/partially-solved.png":
                res = "Partially Accepted"
            prblm=problem[i*2].text.strip()
            print(prblm)
            try:
                print([df["Name"][prblm],prblm,df["Tag"][prblm],df['Complexity'][prblm],res])
                List.append([name,prblm,df["Tag"][prblm],df['Complexity'][prblm],res])
            except:
                df.loc[prblm] = [1111,prblm,"data-structures", "Medium"]
                List.append([name,prblm, df["Tag"][prblm], df['Complexity'][prblm], res])
                print([df["Name"][prblm], prblm, df["Tag"][prblm], df['Complexity'][prblm], res])
        try:
            driver.find_element(By.XPATH,"""//a[@onclick="onload_getpage_recent_activity_user('next');"]""").click()
            time.sleep(3)
        except:
            List=List[::-1]        
            for k in range(len(List)):
                sheet.append(List[k])
            break


excel.save("submission73733.xlsx")


