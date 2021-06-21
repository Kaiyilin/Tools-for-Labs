#MongoScript
import os
import numpy as np 
import pandas as pd
import json

def imread():
    img = 1
    return img

df = pd.read_csv('./path')
imagesSet = imread()
imagesSet2 = imread()
file_list = []
Doc = {}
for i in range(len(df)):
    Doc["Code_Name"] = df['Unnamed: 0'][i]
    Doc["Name"] = df['姓名'][i]
    Doc["PatientID"] = str(df['病歷號'][i])
    Doc["Gender"] = "female"
    Doc["Age"] = df["年齡\n(算式)"][i]
    Doc["Edu_year"] = df["受教育\n幾年"][i]
    Doc["Psychological_Questionaire"]={}
    Doc["Psychological_Questionaire"]["HAMD"]= df["焦慮總分"][i]
    Doc["Psychological_Questionaire"]["PhQ"] = df["PHQ-總分"][i]
    Doc["Images"]={}
    Doc["Images"]["Raw_file_Path"] = None
    Doc["Images"]["mfalff"] = BH_alff[i].tolist()
    Doc["Images"]["mReho"] = BH_reho[i].tolist()
    Doc["Images"]["gfa"] = None
    Doc["Images"]["iso"] = None
    Doc["Images"]["nqa"] = None
    Doc["Images"]["VBM_WM"] = None
    Doc["Images"]["VBM_GM"] = None
    #print(Doc)
    file_list.append(Doc)
    #Doc["Psychological_Questionaire"]={}
    Doc = {}
    #print(Doc)

os.chdir("/Users/MRILab/Desktop")
output = "BH"
with open(f'{output}data.txt', 'w') as outfile:
    json.dump(file_list, outfile)