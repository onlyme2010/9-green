# taomlar = {
#     "Nodir":"lag'mon",
#     "Lola":"manti",
#     "Qodir":"besh barmoq",
#     "Ali":"mampar",
#     "Olim":"khinkalli"
# }
"""Qiymat qo'shish"""
# taomlar["Olim"] = "So'msa"
# taomlar["Lola"] = input("Azamjoning taomi?")
# print(taomlar)

# taomlar.update({"Akramjon":"ramyon"})
# print(taomlar)

""" Qiymatni o'zgartirish / update() """
# taomlar["hasan"] = 'qozon_kabob'
# print(taomlar)

# taomlar.update({"olin":"manti"})
# print(taomlar)

""" Qiymatni o'zgartirish / update() """
# taomlar["hasan"] = 'qozon_kabob'
# print(taomlar)

# taomlar.update({"olin":"manti"})
# print(taomlar)


""" Ro'yhatni tozalash """
# taomlar.clear()
# print(taomlar)

""" Ro'yhatdan nusha olish """
# meals = taomlar.copy()
# print(meals)

# meals2 = dict(taomlar)
# print(meals2)






# otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa"
    }
print(taomlar)
taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")

pythonl = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}


k = input("Kalit so'z kiriting:").lower()
tarjima = pythonl.get(k)
if tarjima == None:
    print("Bunday so'z mavjud emas") 
else:
    print(f"{k.title()} so'zi {tarjima} deb tarjima qilinadi")
    













