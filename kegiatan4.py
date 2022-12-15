import shelve

berkas = shelve.open("Ulin")

data = berkas["data"]

for i in data:
    print(i)

berkas.close()