# green_9 = {
#     "olimjonova":"Sarvinoz",
#     "botirova":"Hadicha",
#     "malikova":"Naima",
#     "tohirova":"Rahima"
# }
# print(green_9)

# """Element qo'shish"""
# green_9.update({'mamadova':"Oydina"})
# print(green_9)

# green_9['fazliddinova'] = "Mubona"
# print(green_9)

# green_9[input("Familya kiriting:").lower()] = input("Ism kiriting: ").title()
# print(green_9)

# """Elementni qiymatini yangilash """
# green_9.update({"mamadova":"Muslima"})
# print(green_9)

# green_9["fazliddinova"] = "Masrura"
# print(green_9)

# """ Elementni o'chirish"""
# del green_9 ["botirova"]
# print(green_9)

# green_9.pop("fazliddinova")
# print(green_9)

# green_9.popitem()
# print(green_9)

# """ Lug'atni o'chirish """
# del green_9

# ota = {
#     "ismi":"Ali",
#     "familia":"Olimov",
#     "yosh": 40,
#     "kasb":"biznesmen"
# }
# print(ota)

# print(f"Otamning ismi {ota['ismi']} familiasi {ota['familia']} yoshi {ota['yosh']} kasbi {ota['kasb']}")

# ona = {
#     "ismi":"Anora",
#     "familia":"Olimova",
#     "yosh": 38,
#     "kasb":"o'qituvchi"
# }
# print(ona)

# print(f"Onamning ismi {ona['ismi']} familiasi {ona['familia']} yoshi {ona['yosh']} kasbi {ona['kasb']}")

# aka = {
#     "ismi":"Oqil",
#     "familia":"Naimov",
#     "yosh": 16,
#     "kasb":"o'quvchi"
# }
# print(aka)

# print(f"Akamning ismi {aka['ismi']} familiasi {aka['familia']} yoshi {aka['yosh']} kasbi {aka['kasb']}")

""" Lug'atni tozalash"""
# green_9.clear()
# print(green_9)

""" Nusxa olish """
# math_students = green_9.copy()#1- usuli
# print(math_students)

# math_students2 = dict(green_9)#2 - usuli
# print(math_students2)

""" .get() - metodi """
# print(green_9.get("abdilahad", "bunday ism yoq"))
# print(green_9.get(input("Key kiriting : "), "bunday ism yoq"))
"""1 """
# abc = {
#     'a':"A",
#     'b': 'B'    
# }
# sora = input("Harf kiriting: ")
# if sora in abc:
#     print(abc.get(sora,("so'zning tarjimasi")))
# else:
#     print("None")
"""2"""
# dost = {
#     "ism":"Lola",
#     "familia":"Qosimova",
#     "yoshi":14,
#     "mashgulot":"kitob yozish",
#     "hobbi":"uxlash"
# }
# print(f"do'stim haqidagi ma'lumotlar ",dost)
"""3"""




















