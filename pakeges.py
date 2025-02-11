""" tashqi kutibhonalr """
"""datetime"""
# import datetime
# print(datetime.datetime.now())
# hozir = datetime.datetime.now()
# print(hozir.year)
# print(hozir.month)
# print(hozir.weekday())

# print(f"Sana: {hozir.strftime("%A, %d %B %Y year")}")
# print(f"Bugun sana: {hozir.strftime("%d-%m- %Y")}")

# bugun1 = datetime.date.today()
# ramazon1 = datetime.date(2025,3,1,00,00,1)

# print(bugun1)
# print(ramazon1)

# farq = ramazon1-bugun1
# print(farq)
# print(farq.days)

# """         """
# t_sana = datetime.datetime(2001,1,18,3,0,0)
# print(t_sana)
# print(t_sana + datetime.timedelta(days = 20, hours = 8))

import datetime
# def otgan_kunlar(yil:int, oy:int, kun:int):
#     """ Yashab o'tgan vaqtingizni yil va kun hisobida hisoblab beruvchi funksiya.
#     yil - tug'ilgan yil
#     oy - tug'ilgan oy
#     kun - tug'ilgan kun 

#     9 Green sinfi bilan yasalgan funksiyasi(06-02-2025)
#     """
#     t_yil = yil 
#     t_oy = oy
#     t_kun = kun
#     t_sana = datetime.date(yil,oy,kun)
#     bugun = datetime.date.today()

#     if (bugun-t_sana).days <= 365:
#         return f"Siz tug'ilganizga {(bugun-t_sana).days} kun bo'ldi"
#     elif bugun.month > t_oy:
#         yil = bugun.year - t_yil
#         kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
#         return f"Siz tug'ilganizga {yil}-yilu {kun.days} kun bo'ldi"
#     elif bugun.month == t_oy:
#         if bugun.day >= t_kun:
#             yil = bugun.year - t_yil - 1
#             kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
#             return f"Siz tug'ilganizga {yil}-yilu {kun.days} kun bo'ldi"
#         elif bugun.day == t_kun:
#             yil = bugun.year - t_yil
#             return f"Siz tug'ilganizga {yil} yoshga to'ldiz. Tabriklaymiz !"
#         else:
#             yil = bugun.year - t_yil
#             kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
#             return f"Siz tug'ilganizga {yil}-yilu {kun.days} kun bo'ldi"
#     else:
#         yil = bugun.year - t_yil - 1
#         kun = bugun-datetime.date(bugun.year, t_oy, t_kun)
#         return f"Siz tug'ilganizga {yil}-yilu {kun.days} kun bo'ldi"
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# oy = int(input("Tug'ilgan oyingizni kiriting: "))
# kun = int(input("Tug'ilgan kuningizni kiriting: "))


# fodalanuvchi = otgan_kunlar(yil,oy,kun)
# print(fodalanuvchi)

import datetime
yil = 2025
yil1 = 2025 + 1

hozir = datetime.date.today()
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
toy = int(input("Tug'ilgan oyingizni kiriting: "))
tkun = int(input("Tug'ilgan kuningizni kiriting: "))
tsana = datetime.date(tyil, toy, tkun)

if tsana > hozir:
    # a = tsana-hozir
    print(f"{(tsana-hozir).days} kun bor")
elif tsana < hozir:
    print(f"{(hozir-tsana).days} kun o'tdi")
    # a = hozir-tsana


