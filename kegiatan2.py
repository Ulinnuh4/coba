berkas = open("L200220265","w")

berkas.write("L200220265\n")
berkas.write("08/01/2004\n")
berkas.write("Ulinnuha\n")
berkas.write("Wonogiri")

berkas.close()

berkas = open("L200220265","r")

file = berkas.readlines()
print(file[2],file[3],",",file[1],file[0])
berkas.close()