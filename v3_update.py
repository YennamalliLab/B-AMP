import pandas as pd
import os




df = pd.read_csv("utils/full.csv")
print(len(df))

for pdb in os.listdir("/yennamalli/bamp/bamp_v3/new_pepids/alpha_fold/rank_1"):
    if pdb.endswith(".pdb"):
        dr_id= pdb.split("_")[0]
        # print(dr_id)
        for i in range(0,len(df)):
            if df["DRAMP_ID"][i]==dr_id:
                tm_in=df["PepID"][i]
        os.system("cp /yennamalli/bamp/bamp_v3/new_pepids/alpha_fold/rank_1/"+pdb+" ./static/peptides/pdb/")
        os.system("mv ./static/peptides/pdb/"+pdb+" /yennamalli/aathi/test_pdb_file/Pep"+str(tm_in)+".pdb")

