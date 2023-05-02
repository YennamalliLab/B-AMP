import os

for pdb in os.listdir("/yennamalli/aathi/test_pdb_file"):
    if pdb.endswith(".pdb"):
        pdb_path = os.path.join("/yennamalli/aathi/test_pdb_file",pdb)
        #print(pdb_path)
        cmd.load(pdb_path)
        cmd.util.chainbow(pdb[:-4])
        cmd.set("ray_opaque_background", 0)
        cmd.png("/yennamalli/aathi/test_pdb_file/"+pdb[:-4]+".png",0, 0, -1, ray=1)
        cmd.delete("all")