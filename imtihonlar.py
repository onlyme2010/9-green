"""9G001"""
"""Bir vaqtni o’zida 4 ta o’zgaruvchi yarating(Bu ishni bir qatorda bajarish zarur !).
Hamda o’zgaruvchilarni konsulga chiqaring"""
# 1
# a,b,c,d = "a","b","c","d"
# print(a,b,c,d)
# 2
"""Ushbu matinni konsulga chiqaring:
“Ahmadning “yuvvosh” mushugi meni ko’rsa, doim yugurib keladi.”"""
# print(f'Ahmadning "yuvosh" mushugi meni ko\'rsa, doim yugurib keladi.')
# 3
"""Misolni pyhtonda bajaring:
93434 ga 94903 ni qoshing, hosil bo’lgan natijadaan 22344 ni ayring 
va unga 7363 ni qo’shing
"""
# print((93434+94903)-22344+7363)

"""Ism, yosh, manzil, maktab, sinf deb nomlangan o’zgaruvchilar yarating 
va ularni konsulga f”” yordamida chiqaring."""
# ism = "JK"
# yosh = 27
# manzil = "Korea"
# maktab = "Seul maktabi"
# sinf = "hammasini o'qib tugatgan"
# print(f"{ism},{yosh},{manzil},{maktab},{sinf}")

"""Name, surname deb nomlangan o’zgaruvchilar yarating va 
ularni yangi full_name deb nomlangan o’zgaruvida jamlang. 
Hamda full_name deb nomlangan o’zgaruvchining qiymatini ba’zi 
metodlar ishlatgan holda barcha hariflarini kichhik qilib konsulga chiqaring."""

"""---------------------------------5----------------------------------"""
# 1
"""4 dan 873 gacha bo’lgan toq sonli ro’yhat yarating va ro’yhatdagi 
har bir sonning ildizini chiqaring."""
# from math import sqrt
# sonlar = list(range(3,873,2))
# for s in sonlar:
#     print(sqrt(s))

# 2
"""Foydalanuvchidan uning ismini so’rang va unga quida keltirilgan javoblardan mosini qaytaring.
Dasturni tuzishda or operatoridan foydalanig !
Muslima  – Salom Muslima. Davramizda hush ko’rdik.
Zilola/Sevara  – Assalomu aleykum. Zilola/Sevara sizga qanday yordam berishim mumkin?
Anvar/Aziz  – Salom Anvar/Aziz . Bugun Qayerga boramiz ?
"""
# ism = input("Ism kiriting: ").title()
# if ism == "Muslima":
#     print(f" Salom {ism}. Davramizda hush ko’rdik.")
# elif ism == "Zilola" or ism == "Servara":
#     print(f"Assalomu aleykum. {ism} sizga qanday yordam berishim mumkin?")
# elif ism == "Anvar" or ism == "Aziz":
#     print(f"Salom {ism}.Bugun Qayerga boramiz?")


# 3
"""102 dan 2020 gacha bo’lgan sonladan iborat ro’yhat yarating va ro’yhatdagi:
1000 gacha bo’lgan sonning 3-darajasini toping.
1500 dan katta barcha sonlarning o’zidan 4 taga kichik sonni toping.
Ro’yhatdagi 7 ga qoldiqsiz bo’linadigan sonlarning ildizini toping.
"""
from math import sqrt
# sonlar = list(range(102,2020))
# for s in sonlar:
#     if s < 1000:
#         print(s**3)
#     elif s > 1500:
#         print(s-4)
#     if s % 7 == 0:
#         print(sqrt(s))

# 4
"""| -322 dan -2 gacha bo’lgan barcha toq sonlarning:
1) 5 chi va 7 chi darajasini toping;
2) Ro’yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro’yhatning uzunligini o’lchang;
4) Ro’yhatdagi har bir sonning ildizini toping;
5) Ro’yhatni avval o’sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
"""
# sonlar = list(range(-322,-2,3))
# # for s in sonlar:
#     # print(f"{s**5} va {s**7}")
#     # print(s-4)
#     # print(len(sonlar))

# sonlar.sort()
# print(sonlar)

# 5
"""a = float(input("1-sonni kirirting:"))
b = int(input("2-sonni kirirting:"))
if a<b:
print(f"{a}>{b}")
elif a<b:
print(f"{a}<{b}")
elif a != :
print(f"{a}={b}")
"""
# a = float(input("1-sonni kirirting:"))
# b = int(input("2-sonni kirirting:"))
# if a<b:
#     print(f"{a}<{b}")
# elif a>b:
#     print(f"{a}>{b}")
# elif a == b:
#     print(f"{a}={b}")

"""------------------------6------------------------"""
# 1
"""Quidagicha sonli ro’yhatlar yarating:
200 dan 400 gacha toq sonli;
301 dan 500 gacha juft sonli;
10 dan 600 gacha 25 ga bo’linadigan sonlardan iborat;
"""
# s1 = list(range(200,400,3))
# print(s1)

# s2 = list(range(301,500,3))
# print(s2)

# s3 = list(range(10,600,25))
# print(s3)

# 2
"""O’zingizga ma’lum 7 ta davlat nomini qo’shgan holatda 
davlatlar deb nomlangan ro’yhat tuzing. 
3 ta elementni 3 hil usulda o’chirib tashlang. 
Yangi 2 ta davlat nomini 2 xil usulda qo’shing.
"""
# davlatlar = ["USA","Ukrain","India","United States"]
# davlatlar.remove("USA")
# del davlatlar[1]
# davlatlar.pop(-1)
# davlatlar.append("UZB")
# davlatlar.insert(0,"China")
# print(davlatlar)

# 3
"""Names deb nomlangan ro’yhat yararing unda o’zingiz bilgan 3, 4 ta ism bo’lsin. 
Keyin esa foydalanuvchidan uning ismini ham so’rang agar uning ismi sizning 
ro’yhatingizda bo’lsa, “Kechirasiz sizning ismingiz mening ro’yhatimda bor ekan” degan 
habarni agar ro’yhatda bo’lmasa “Guruhga hush kelibsiz” degan habarni konsulga chiqaring.
"""
# names = ["Lola","Munisa","Qobil"]
# ism = input("Ism kiriting: ")
# if ism in names:
#     print("Kechirasiz sizning ismingiz mening ro’yhatimda bor ekan")
# elif ism not in names:
#     print("Guruhga hush kelibsiz")

# 4
"""O’quv qurollari nomlaridan iborat ro’yhat tuzing. Foydalanuvchiga ro’yhatdagi 
mahsulotlar nomini ko’rsating va undan nechta mahsulot va nimalar olmoqchiligini so’rang. 
Keyin esa foydalanuvchi olmoqchi bo’lgan ,do’koningizda bor va yo’q mahsulotlarni ko’rsatib 
o’ting.
"""
# bor = []
# yoq = []
# oquv_qurollar = ["ruchk","qalam","penal","daftar"]
# print(oquv_qurollar)
# nechta = int(input("Nechta o'quv qurol olasiz: "))
# narsa = input("Nima olasiz: ")
# if narsa in oquv_qurollar:
#     for i in range(nechta):
#         mahsulot = input(f"{narsa} {i+1}-chini mahsulot kiriting: ")
#         if mahsulot in bor:
#             yoq.append(mahsulot)
#         else:
#             bor.append(mahsulot)

"""-----------------------------7----------------------------------------"""
# 1
"""Foydalanuvchidan 7 ta shahar nomini so’rang va shaharlar deb nomlangan ro’yhat tuzing. 
3 ta elementni 3 hil usulda o’chirib tashlang. Yangi 2 ta davlat nomini 2 xil usulda qo’shing.
Ro’yhatni alifbo bo’yicha va alifboga teskari tartibda doimiy qilib tartiblang. Ro’yhatni tozalab yuboring, so’ngra uni o’chirib tashlang.
"""
# shaharlar = []
# for s in range(7):
#     shahar = input(f"{s+1} - shahar nomini kiriting: ")
#     shaharlar.append(shahar)
# shaharlar.remove("UZB")
# del shaharlar[2]
# shaharlar.pop(-1)
# print(shaharlar)

# 2
"""Foydalanuvchidan uning yaqin do’sti haqidagi ma’lumotlarni so’ragan holda friend nomli 
lug’at yarating. Lug’atda quidagi ma’lumotlar bo’lsin; ism, familiya,  yosh, manzil, 
telefon raqam hamda email. Keyin lug’atdagi barcha ma’lumotlarni konsulga bir gap 
ko’rinishida chiqaring.
"""
# friend = {
#     "ism",input("Ism: "),
#     "familiya", input("Familiya: "),
#     "yosh", int(input("Yosh: ")),
#     "manzil", input("Manzil: "),
#     "telefon", input("Telefon raqam: "),
#     "email", input("Email: ")
# }
# print(friend)

# 3
"""Ingliz-O’zbek lug’atini yarating. Key o’rnida ingliz tilidagi so’z, 
value o’rnida o’zbekcha so’z bo’lsin. Foydalanuvchidan biror so’z so’rang agar u 
lug’atda bor so’zni kiritsa unga u so’zning tarjimasini qaytaring, agar bo’lmasa 
“Bizda bu so’z haqida ma’lumot yo’q” degan javobni qaytaring."""



# pythonl = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}


# k = input("Kalit so'z kiriting:").lower()
# tarjima = pythonl.get(k)
# if tarjima == None:
#     print("Bunday so'z mavjud emas") 
# else:
#     print(f"{k.title()} so'zi {tarjima} deb tarjima qilinadi")
    
# 4
"""books deb nomlangan lug’at yarating{“key”:”kitob nomi”}. 
Ichida 2 ta element bo’lsin. Yana yangi 2 ta elementni 2 xil usulda 
qo’shing, 2 ta elementni 2 xil usulda yangilang, 3 ta elementni 3 xil 
usulda o’chiring va so’ngra lug’atni tozalab tashlang."""
























