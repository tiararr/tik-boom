# program sederhana jika kelipatan 3 tik, kalau mialkan kelipatan 5 boom , dan keliatapatan 3 dan 5 tik 
# boom program hanya sampai 50 munculkan semua angkanya

for x in range(1,150):
    if x%3==0 : print("tik")
    elif x%5==0: print("boom")
    elif x%3==0 and x%5==0: print("tik boom")
    else: print(x)