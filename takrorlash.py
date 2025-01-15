"""    9b001    """
# 1
# ism = ["JK"]
# fm = ["jeon"]
# yosh = [27]
# kitoblar = ["kitob","men"]
# kasb = ["idol"]
# print(type(ism))
# print(type(fm))
# print(type(yosh))
# print(type(kitoblar))
# print(type(kasb))

# 2
# from math import sqrt
# print(round(sqrt(4364 + 1233)), 2)

# 3
# a = int(input("Son1: "))
# b = int(input("Son2: "))
# print((a**2)/23)
# print((b**2)/23)

# 4
# son = int(input("butun son: "))
# print(float(son))
# print(int(son))
# print(type(son))

# 5
# kitoblar = []
# kitoblar.append(input("kitob1: "))
# kitoblar.append(input("kitob2: "))
# kitoblar.append(input("kitob3: "))
# kitoblar.append(input("kitob4: "))
# kitoblar.append(input("kitob5: "))

# 6
# students = ["Ali","Maruf","Bahrom"]
# students.insert(0,"Vali")
# students.insert(2,"Qobil")
# students.insert(-1,"Olim")
# print(students)
# students[1] = "Me"
# students[1] = "You"

"""   9b002   """
# 1
# import random
# a = int(input("Son1: "))
# b = int(input("Son2: "))
# print(random.randrange(a,b))

# 2
# ism = input("Ismingizni kiriting: ")
# kitob = []
# kitob.append(input("Kitob:"))
# kitob.append(input("Kitob:"))
# kitob.append(input("Kitob:"))
# kitob.append(input("Kitob:"))
# kitob.append(input("Kitob:"))
# kitob.pop(1)
# kitob.insert(2,"Men")
# kitob.insert(3,"Men faqat men")
# print(kitob)

# 3
# yangi = []
# fanlar = ["ICT","Matem"]
# fanlar.append("Ona tili")
# fanlar.insert(2,"EnGLISH")
# fanlar[2] = "Rus tili"
# fanlar[2] = "Nemis tili"
# fanlar.remove("ICT")
# del fanlar[2]
# fanlar.pop(0)
# yangi.append(fanlar)
# fanlar.clear()
# print(yangi)
# print(fanlar)

# 4
# fam = []
# soni = int(input("Soni: "))
# for s in range(soni):
#     fam.append(input("Ismi: "))
#     print(s)
# print(fam)

# 5
# cars = ["BMW","Spark","M5","Kobalt","Matiz"]
# print(cars)
# print(len(cars))
# cars.sort()
# cars.sort(reverse=True)
# cars.reverse()
# print(cars)


"""    9b004    """
# 1
# sonlar = [45,-96,0,63.2,1257,-6752.2,42,3,542]
# sonlar.sort()
# sonlar.sort(reverse=True)
# sonlar.reverse()
# print(sonlar)

# 2
# mevalar = ["olma","o'rik","shaftoli","apelsin","malina","xurmo"]
# for a in mevalar:
#     if a == "olma" and a == "malina":
#         print(a.upper())
    
# 3
# books = {
#     "a":"kitob",
#     "b":"men"
# }
# books.update({"c","aaaaaaa"})
# books["d"] = "bbbbbbbb"
 
# books.pop('a')
# books.popitem()

# books.update({"a","aaaaaaa"})
# books["c"] = "bbbbbbbb"
 
# del books [1]
# books.pop('a')
# books.popitem()

# books.clear()
# print(books)

# 4
# from math import sqrt
# sonlar = list(range(102,2021))
# print(sonlar)
# for son in sonlar:
#     if son < 1000:
#         print(son**3)
#     elif son > 1500:
#         print(son-4)
#     if son % 7:
#         print(sqrt(son))

# 5
# natija = float(input("natijangizni foizini kiriting: "))
# orin = input("o'rin: ")
# if natija < 0 and natija > 100:
#     print("hato")
# elif 0 < natija < 64:
#     print("Siz o'ta olmadingiz!")

# elif 65 <= natija <= 85:
#     print("O'tgansiz")
# elif 85 < natija <= 100:
#     if orin ==1:
#         print("100%")
#     elif orin ==2:
#         print("75%")
#     elif orin ==3:
#         print("50%")
#     elif orin ==4:
#         print("25%")

"""   9b005   """
# 1
# ing_uzb = {
#     "banana":"banan",
#     "apple":"olma",
#     "pen":"ruchka",
#     "pencil":"qalam",
#     "galass":"ko'z oynak"
# }
# print(ing_uzb.get(input("So'z kiriting: "),"hato"))

# 2
# menu = {
#     "osh":10_000,
#     "choy":5_000,
#     "shashli":20_000,
# }
# print("Bizning restoranimizda quyidagi taomlar bor",end=" ")
# for k in menu.keys():
#     print(f"{k}", end=", ")

# print("\n Narxlari: ")
# for k,v in menu.items():
#     print(f"{k.title()} - {v}") 

# 3
# ism = input("Ism: ")
# yosh = int(input("Yosh: "))
# if 1 <= yosh >= 6:
#     print("Boxcha bolasi")
# elif 7 <= yosh >= 17:
#     print("Mkdasiz")
# elif 18 <= yosh >= 30:
#     print("Univer")
# elif 31 <=  yosh >100:
#     print("mkX")
# elif yosh >= 0 or yosh > 100:
#     print("Hato")

# 4



"""     9g001    """
# 1
# a,b,c,d = "a","b","c","d"
# print(a,b,c,d)

# 2
# print("Ahmadning 'yuvvosh' mushigi meni ko'rsa, doim yuguradi")

# 3
# print((93434 - 94903)-22344+7363)

# 4
# ism = "Rahima"
# yosh = 14
# manzil = "Namangan"
# mk = "BM"
# print(f"{ism},{yosh},{manzil},{mk}")

# 5
# ful_name = []
# name = "Me"
# surname = 'Yoo'
# print(ful_name.append(name))
# print(ful_name.append(surname))

# print(ful_name.lower())

# 6
# 😁

"""    9g002   """
# 1


























































































































