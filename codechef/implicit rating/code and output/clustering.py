#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
df=pd.read_excel("CosineSimiliarity.xlsx")
df.fillna(0,inplace=True)
df_new=df.drop(columns=["Unnamed: 0"])
print(df)


# In[31]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
cs = []
plt.figure()
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(df_new)
    cs.append((kmeans.inertia_))
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()
print(cs)


# In[32]:


from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
data = df_new
pca = PCA(2)
transform = pca.fit_transform(data)

kmeans = KMeans(n_clusters= 4)

label = kmeans.fit_predict(transform)
 
u_labels = np.unique(label)

display (label)
display (u_labels)


# In[33]:


plt.figure()
for i in u_labels:
    plt.scatter(transform[label == i , 0] , transform[label == i , 1] , label = i)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='purple',marker='+',label='centroid')
plt.legend()
plt.show()


# In[44]:


a_list=[
    "maroonrk", "ksun48", "lyrically", "heno239", "um_nik", "noimi", "hitonanode", "happypotato", "tute7627",
    "tiger2005", "redstar05", "thuustalu", "denisov", "redstar0", "nok0", "timmyfeng", "qwerty787788", "eddard",
    "kshitij_789", "xams", "rgb_icpc1", "wsyhb", "oierhzc", "nuip", "ak_group", "bucketpotato", "shiomusubi496",
    "heltion", "triplem5ds", "testcase28", "makmed1337", "oier_kzc", "lympanda", "jackpa", "batrr", "stelian",
    "marckess", "ai_dev_master", "sysulby", "wcysai", "kira_1234", "aryanc403", "pctprobability", "mmtdp7476",
    "cthau", "prvocislo", "nirjhor", "yuki726", "aging1986", "serotonin", "siganai", "sungan", "lip_arcanjo",
    "mridulahi", "minato2376", "pooty", "xiaowuc1", "apoorv_me", "megurine", "vladden", "primenumberzz", "jovan_b",
    "mateocv", "leaf1415", "shivensinha4", "maomao90", "alek0618", "juliany2", "zzrzzr", "ecottea", "hollwo_pelw",
    "tima", "redstar06", "peti25", "tobapnw", "icecream990720", "ronniechonev", "tensei8869", "rgb_icpc9", "wjli",
    "yfuka86", "cuiaoxiang", "fxorg", "yash_daga", "warmbreeze", "lucina101", "rddalida", "socpite", "dbsic211",
    "shobonvip", "jay_1048576", "menborong", "isaacmoris", "czhang2718", "brobat", "etherinmatic", "bachhoangxuan",
    "rock_star789", "x_arc", "redstar07", "alfeh", "jaimahakal", "demidenko", "huangxw", "lmlmlm", "marcosk",
    "redstar1", "gsxj2014", "mrho888", "taran_1407", "friedcheese", "nitap511954", "attardesakshi", "au_20eg105412",
    "srishailam_123", "bjrg08", "arif2021", "vl21fe1a05d9", "marushika3107", "mvm_2200032006", "vigneshwaranv3",
    "sahil_gupta20", "adi3shivany", "xerox7", "naveenkumar_24", "aman2011", "sravyachintala", "aartirai1503",
    "chef1434", "akellamanasa20", "sakura_uchiha", "vivekgarnara", "steel001", "r01a0449", "yuvaranipandi",
    "layanareddy", "ssimhachalam21", "sanskar_anand7", "saisrija_1", "anshikasahu24", "routhuhemalath", "codersai_123",
    "leo_anny31", "klu_2200030402", "karunakarpashi", "devilofmyworld", "princekgarg", "bhanusree01", "kush_1719",
    "aditya_aware_6", "jivitha27", "shubhamjha123", "ah_aashiq", "verse_of_mk", "mlseyedibrahim", "sitanshu_18",
    "klu_2200031851", "klu_2200030908", "bavisetti_ajay", "charan_yarra", "deepikavarsha0", "ranjith5c2", "virus2466",
    "rudrasingh1339", "sudeeporiginal", "rajashekar213", "chilukapavani", "diamondhead_22", "ipec_it316", "pavani72",
    "ajit28985", "tt79", "anandsagar06", "geethikach", "abhinavrr", "niteshv8824", "klu_2100031608", "bajrangdal705",
    "harshitha_6044", "neerajkumar_97", "sidak_123", "utkarxhhh", "abdulrahim2004", "upmanyunidhi02", "robo00",
    "klu_2200030562", "ugginausha2003", "ypmanoranjan0", "vw21nm1a0265", "kevin2003", "ritika_kosigi", "sadain_18",
    "aryan_260"
]
data={'Name':df["Unnamed: 0"],'Cluster':label}
cluster_list=pd.DataFrame(data)
for i in range(len(cluster_list)):
    cluster_list.loc[i, "Name"]=a_list[cluster_list.loc[i, "Name"]]



# In[55]:


dis=dict()
for i in range(len(np.unique(cluster_list.loc[:, "Cluster"]))):
    List=[cluster_list.loc[x]['Name'] for x in range(len(cluster_list)) if cluster_list.loc[x, "Cluster"] == i]
    dis[i+1]=List

def clusters():
    return dis;

# In[ ]:




