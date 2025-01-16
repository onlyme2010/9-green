"""funksiya"""
# print("Hi")

# def salom_ber():
#     print("Salom")
# salom_ber()

# def yosh_top():
#     ism = input("Ismingiz: ")
#     t_yil = int(input("tug'ilgan yilingiz: "))
#     print(2024-t_yil)

# yosh_top()

# def yosh_top(t_yil):# t_yil - parametr
#     """ Tug'ilgan yilni qabul qilib olib yoshni hisoblovchi funksiya
    
#     t_yil --> int
#     """
#     print(f"Sizning yoshingiz {2024-t_yil} da")

# yosh_top(2012)
# yosh_top(2020)
# x = int(input("T yil kiriting: "))
# yosh_top(x)



# print(print.__doc__)# double under  score --> dunder metod
# print(max.__doc__)
# print(len.__doc__)
# # print(yosh_top.__doc__)

# """ Prametrni key_word bilan birga berish """
# def yosh_top(ism,t_yil):
#     print(f"Salom {ism.title()}, siz {t_yil}-yilda tug'ilgan siz va yoshingiz {2024-{t_yil}} da")

# yosh_top("Ali",t_yil=2012)

# """ Standart qiymat"""
# def yosh_top(ism,t_yil=2000):
#     print(f"Salom {ism.title()}, siz {t_yil}-yilda tug'ilgan siz va yoshingiz {2024-{t_yil}} da")

# yosh_top("Ali",t_yil=2012)


"""1"""
# print(len.__doc__)
# print(max.__doc__)
# print(sum.__doc__)
# print(range.__doc__)
# print(list.__doc__)

"""2"""
# def ball_top(ball):
    # """balinga baho beraman"""
#     if 0 <= ball <= 50:
#         print("qo'niqarsiz") 
#     elif 51 <= ball <= 70:
#         print("qo'niqarli") 
#     elif 71 <= ball <= 90:
#         print("yaxshi") 
#     elif 91 <= ball <= 100:
#         print("a'lo") 

# ball_top(10)

"""3"""
# def t_tburchak(r,s):
#     """ yuzini va perimetrini topamiz"""
#     print(f"Tomanlari {r} va {s} bo'lgan to'g'ri to'rtburchakning yuzi {r*s}ga parimetri esa {(r+s)*2}")

# t_tburchak(2,5)

"""4"""

# sonlar = [0,-5,9,-12,99]

# def tartibla(qiymat):
#     qiymat.sort()
#     print(qiymat)
# tartibla()

"""Funksiyadan qiymat qaytarish """
# def yosh_top(t_yil):
#     """Tug'ilgan yilni qabul qilib olib yoshini qaytaradigan funksiya"""
#     yosh = 2024-t_yil
#     return yosh

# malikaning_yoshi = yosh_top(2010)
# print(f"Maklikaning yoshi {malikaning_yoshi} da")

# def yosh_top(t_yil: int) -> int:
#     """Tug'ilgan yilni qabul qilib olib yoshini qaytaradigan funksiya"""
#     yosh = 2024-t_yil
#     return yosh# Return qaytarish

# malikaning_yoshi = yosh_top(2010)
# print(f"Maklikaning yoshi {malikaning_yoshi} da")
# yangi_royhat = list(range)

# def person(name:str,surname:str,age:int,email:str,phone:int) ->dict:
#     """Hamma ma'lumotlaringizni bitta lu'atda chiqarib beramiz"""
#     new_person = {
#         "name":name,
#         "surname":surname,
#         "age":age,
#         "email":email,
#         "phone":phone
#     }

#     return new_person

# person2 = person("JK","Jeon",27,"jeonkookjung@gmail.com",987654321)
# person3 = person("V","Kim",27,"thv@gmail.com",123456789)

# print(person2)
# print(person3)


# def person(dad:str,mom:str) ->list:
#     """Hamma ma'lumotlaringizni bitta lu'atda chiqarib beramiz"""
#     new_person = [dad,mom]

#     return new_person

# person2 = person("JK","Jeon",27,"jeonkookjung@gmail.com",987654321)
# person3 = person("V","Kim",27,"thv@gmail.com",123456789)

# print(person2)
# print(person3)

# def bahola(ismlar):
#     baholash={}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
#         baholash[ism] = baho
#         return baholash
# talabalar = ["ghsghhd","dfdbgf","CFhdjhn","tghj"]
# baholar = bahola(talabalar)
# print(baholar)



# def info(name:str,age:int,sinf="9 Green") ->str:
#     """siz haqingizdagi ma'lumotlarni chiroyli qilib cgiqarib beradi"""
#     return f"{name.title()} your age {age}, your class {sinf}"

# student1 = info(sinf= "10 Green", age=15,name="Abbos")
# print(student1)

"""mashq"""
# def juft(son:int) ->list:
#     """karochi bu funksiya sizga sizga juftsonli ro'yhat tuzib chiqarib beradi"""
#     return list(range(0,son,2))
# s = juft(50)
# print(s)


"""   Takrorlash   """
def full_name(ism:str,surname:str) ->str:
    """ism va familia ni olib hammasini chiqaradi"""
    full = f"{ism} {surname}"
    return full
abror = full_name("Abror","Ahmedov")
# print(abror)

def yosh_top(ism:str,t_yil:int,h_yil=2024) -> str:
    """ """
    natija = f"{ism.title()}ning yoshi {h_yil-t_yil}"
    return natija

lola = yosh_top("Lola",2006)
# print(lola)

""" max"""
def the_biggest1(*numbers):
    """ bla bla bla"""
    x = sorted(numbers)
    return x[-1]
numbers1 =the_biggest1(12,898,-5,2154,-445578,54654)
# print(numbers1)

"""1"""
def the_biggest1(*numbers):
    """ bla bla bla"""
    x = sorted(numbers)
    return x[0]
numbers1 =the_biggest1(12,898,-5,2154,-445578,54654)
# print(numbers1)

def the_biggest1(*numbers: int) ->int:
    """ bla bla bla"""
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum 
# numbers2 = the_biggest1(214,56456,-654654,654564541654)
# print(numbers2)

def a(*n):
    x = 0
    for smth in n:
        x += 1
    return x
# numbers2 = a(214,56456,-654654,654564541654)

"""mashq(range)"""
def ranges(x:int,y:int)->list:
    """range yasaymiz"""
    son = [x]

    for s in son:
        if s < y - 1:
            son.append(s+1)
            
    return son

# num = ranges(14,54)
# print(num)

"""sqrt"""
def my_sqrt(son):
    """sqrt ni aysayman"""
    return son ** 0.5
son = float(input("son kiriting: "))
# print(f"{son} sonning kv ildizi -> {my_sqrt(son)}")

"""unli,undosh"""
def unli(letter:str):
    """unlisi """
    l = ["a","e","i","u","o"]
    if letter in l:
        return "unli harf"
    else:
        return "undosh harf"
# print(unli(input("harf kiriting:")))

"""unli yoki undosh"""
# unli = []
# undosh = []
# def harf(letter:str) -> str:
#     """  """
#     lu = ["a","e","i","u","o"]
#     for l in letter:
#         if l == " ":
#             continue
#         elif l in lu:
#             unli.append(l)
#         elif l not in lu:
#             undosh.append(l)
#     return f"{unli} shu matindagi unli harflar, {undosh} shu matindagi undosh harflar"

# print(harf(input("matn kiring: ")))

""" o'rta arifmetik """
# def middle(*numbers:int)->int:
#     """ """
#     summa = 0
#     count = 0
#     for number in numbers:
#         summa += number
#         count += 1
#     return summa/count

# print(middle(12,0,9,52))
# print(middle(23,45))
# print(middle(9,6))


# print("Siz son kiriting kompyuter bilan birhil topsayz yutasiz")
# import random
# son = (random.randrange(0,10))
# siz = int(input("Son kiriting: "))
# if siz == son:
#     print(f"to'g'ri topdingis o'ylangan son {son} da teng edi ✔")
# elif siz != son :
#     print(f"hato kompyuter o'ylagan son {son} ga teng edi❌")




