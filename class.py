""" Class"""
""" OOP - Object oriented programming"""

class Car():
    """Docstring"""
    def __init__(self,company:str,model:str,color:str,price:int,max_speed:int,year:int):# parametr
        self.company = company
        self.model = model
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.year = year
    def get_info(self):
        """Mashina haqidagi ma'lumot beruvchi funksiya"""
        info = f"Mashina haqidagi ma'lumotlar:\nKampaniya: {self.company} \nModel: {self.model} \nColor: {self.color} \nPrice: {self.price} \nYear: {self.year} \nMaxSpeed: {self.max_speed}"
        return info
    
    def get_c_m(self):
        """Chiqaruvchi miqdori qo'shuvchi funksiya"""
        return f"{self.company}  {self.model}"
car1 = Car("Tesla","Model 3","black", 30_000,220,2022)
car2 = Car("BMW","M5","black",50_000,290,2020)
# print(car1.get_info())
# print(car2.get_info())
# print(car1.get_c_m())
"""trt20100207
gansura"""
# git config --global user.name "Your Name"
# git config --global user.email "youremail@domain.com"

"""talaba haqidagi ma'lumotlar 16.01.25"""
class Talaba():
    """ docstring """
    pass
    def __init__(self, familiya:str, ism:str,kurs:int,baholar:list,year:int,friends:list):
        self.ism = ism
        self.familiya = familiya
        self.kurs = kurs
        self.baholar = baholar
        self.year = year
        self.friends = friends
    def get_info(self):
        """talaba haqidagi ma'lumotlar"""
        info = f"Talaba haqidagi ma'lumotlar:\nIsm: {self.ism} \nFamiliya: {self.familiya} \nKurs: {self.kurs} \nBaholar: {self.baholar}"
        return info
    def get_orta_baho(self):
        """talaba baholarining orta qiymatini qaytaruvchi funksiya"""
        baholar_sum = sum(self.baholar)
        baholar_count = len(self.baholar)
        return baholar_sum / baholar_count
    def get_full_name(self):
        """talaba haqida full name"""
        return f"{self.ism} {self.familiya}"
    def get_age(self,now=2025):
        """yoshi"""
        return now - self.year
    def get_friends(self):
        """do'stlari"""
        info = f"{self.ism}ning do'stlari: "
        for i in self.friends:
            info += i + " "
        return info
    def set_kurs(self):
        """kursni o'zgartiruvchi funksiya"""
        if self.kurs < 6:
            self.kurs += 1
        else:
            return "Siz hozi eng oxirgi kursda siz"
    def get_kurs(self):
        """kursni qaytaruvchi funksiya"""
        return self.kurs
# jk = Talaba("Jung","Jk",4,[5,5,5,5],1997,["V","Jimin","Jin","RM","J-hope","Suga"])
# print(jk.get_info())
# print(jk.get_orta_baho())
# print(jk.get_full_name())
# print(jk.get_age())
# print(jk.get_friends())

"""book"""
class Book():
    """Docstring"""
    def __init__(self, name:str, author:str,year:int,publisher:str,price:float):
        self.name = name
        self.author = author
        self.year = year
        self.add_books = 0
        self.price = price
        self.publisher = publisher
    def __str__(self):
        return self.name
    def get_info(self):
        """kutibxonaga ma'lumot beruvchi funksiya"""
        info = f"Kutibxona haqidagi ma'lumotlar:\nNomi: {self.name} \nQo'shiluvchi kitoblar: {self.add_books}\npublishe: {self.publisher}"
        return info
    def get_name(self):
        """namesi chiqadi"""
        return self.name
    def get_price(self):
        """Kutibhonadagi kitoblarni narxi qaytaruvchi funksiya"""
        return self.price

book1 = Book("lool")

"""kutibxona"""
class Library():
    """Docstring"""
    def __init__(self, name:str, adress):
        self.name = name
        self.adress = adress
        self.books = []
        self.add_books = 0
    def __str__(self):
        return self.name
    def get_info(self):
        """kutibxonaga ma'lumot beruvchi funksiya"""
        info = f"Kutibxona haqidagi ma'lumotlar:\nNomi: {self.name} \nKitoblar: {self.books} \nQo'shiluvchi kitoblar: {self.add_books}\nadress: {self.adress}"
        return info
    def add_book(self, book:str):
        """kitobni qo'shuvchi funksiya"""
        self.books.append(book)
        self.add_books += 1
        return f"{self.add_books} kutibxonaga qo'shildi"
    def get_books(self):
        """Kutibhonadagi kitoblarni nomini chiqazib beruvchi kutibxona"""
        info = f"{self.name} kutixonasida quyidagi kitoblar bor: "
        for i in self.books:
            info += i + " "
        return info
a = Library("Nadira","qwert")
# print(a.add_book("meow"))
# print(a.get_books())
# print(a.get_info())

# print(a)

"""obyektning hususiyati va metodlarini ko'ris"""
from pprint import pprint
print(dir(a)) 
print(dir(book1)) 

"""__dict___ metodi"""
pprint(a.__dict__)
