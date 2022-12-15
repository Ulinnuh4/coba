import shelve

berkas1 = open("L200220265","r")
data1 = berkas1.readlines()

berkas2 = shelve.open("Ulin")
berkas2["data"] = [data1[0],data1[1],data1[2],data1[3]]

berkas1.close()
berkas2.close()