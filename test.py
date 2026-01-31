# program sederhana jika kelipatan 3 tik, kalau mialkan kelipatan 5 boom , dan keliatapatan 3 dan 5 tik 
# boom program hanya sampai 50 munculkan semua angkanya

<<<<<<< HEAD
nama_penginput=str(input())
print(nama_penginput)
=======
print("masukkan angka maksimal:")
>>>>>>> 5b775cc666ce4049866f9f6fb6922c5012b7f6b0
max = int(input())
for x in range(1,max):
    if x%3==0 : print("tik")
    elif x%5==0: print("boom")
    elif x%3==0 and x%5==0: print("tik boom")
    else: print(x)