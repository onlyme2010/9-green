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
print(car1.get_info())
print(car2.get_info())
print(car1.get_c_m())
"""trt20100207
gansura"""
# git config --global user.name "Your Name"
# git config --global user.email "youremail@domain.com"


