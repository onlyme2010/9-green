"""class2"""
"""vorislik"""
class Shaxs():
    def __init__(self,ism,familya,sharif,t_yil,pasport,millat):
        self.ism = ism
        self.familya = familya
        self.sharif = sharif
        self.t_yil = t_yil
        self.pasport = pasport
        self.millat = millat
    def __str__(self):
        return f"{self.ism} {self.familya} {self.sharif}"
    def get_age(self,h_yil):
        """shaxsning yoshini qaytaruvchi funksiya"""
        return h_yil-self.t_yil
    def get_passport(self):
        """shaxsning pasportnomini qaytaruvchi funksiya"""
        return self.pasport
    def get_millat(self):
        """shaxsning millatinini qaytaruvchi funksiya"""
        return self.millat

shaxs1 = Shaxs("John","Doe","Adanson","2000","1234567890","American")

class Student(Shaxs):
    """O'quvchi haqidagi klass"""
    def __init__(self,ism,familya,sharif,t_yil,pasport,millat,maktab,sinf,baholar):
        """Talbaning xsusiyatlari"""
        super().__init__(ism,familya,sharif,t_yil,pasport,millat)
        self.maktab = maktab
        self.sinf = sinf
        self.baholar = baholar
    def get_info(self):
        """talaba haqida full name"""
        return f"{self.ism} {self.familya} {self.sharif}"
    def get_maklab(self):
        """talaba maktabini qaytaruvchi funksiya"""
        return self.maktab
    def change_school(self,new_school):
        """talabaning maktabini o'zgartiruvchi funksiya"""
        self.maktab = new_school
        return self.maktab
    def get_sinf(self):
        """talaba sinflarini qaytaruvchi funksiya"""
        return self.sinf
    def set_sinf(self):
        """talaba sinflarini o'zgartiruvchi funksiya"""
        if self.sinf < 11:
            self.sinf += 1
            return self.sinf
        else:
            return "Siz hozi eng oxirgi sinfda siz"
    def get_baholar(self):
        """talaba baholarlarini qaytaruvchi funksiya"""
        return sum(self.baholar)
    def get_age(self,h_yil):
        """shaxsning yoshini qaytaruvchi funksiya"""
        return f"{self.ism} {h_yil-self.t_yil} yoshda"   
student1 = Student("JK","Jung","Jeon",1997,"AK654656545","Korean","seoul",8,[321,31,321,321])

print(student1.get_age(2025))
# print(student1.get_info())
# print(student1.get_maklab())
# print(student1.change_school("New School"))
# print(student1.get_sinf())
# print(student1.set_sinf())
# print(student1.get_baholar())

class Texnika():
    def __init__(self, model, yil, color,muddat):
        self.model = model
        self.yil = yil
        self.color = color
        self.muddat = muddat
    def get_info(self):
        """sdghj"""
        return f"Texnika haqidagi ma'lumotlar:\nModel: {self.model} \nYil: {self.yil} \nColor: {self.color}"
    def get_model(self):
        """sryj"""
        return self.model
    def get_yil(self):
        """dtg"""
        return self.yil
    def get_color(self):
        """sryj"""
        return self.color
    def change_color(self, new_color):
        """sryj"""
        self.color = new_color
        return self.color
    def get_muddat(self):
        """sryj"""
        return self.muddat
technique = Texnika("Samsung",2013,"purple",11)
print(technique.get_info())
print(technique.get_color())
print(technique.change_color("red"))
print(technique.get_yil)
print(technique.get_model)
print(technique.get_muddat)

class Computer(Texnika):
    def __init__(self, model, yil, color, muddat, company, protsesor):
        super().__init__(model, yil, color, muddat)
        self.company = company
        self.protsesor = protsesor
    def get_info(self):
        """sdghj"""
        return f"Company: {self.company} \nProtsesor: {self.protsesor}"
    def get_company(self):
        """sryj"""
        return self.company
    def get_protsesor(self):
        """sryj"""
        return self.protsesor
    def change_company(self, new_company):
        """sryj"""
        self.company = new_company
        return self.company
comp = Computer("S24",2025,"black",8,"Samsung","Windows")
print(comp.get_info())
print(comp.get_company())
print(comp.get_color())
print(comp.change_color("White"))
print(comp.get_protsesor())

class Phone(Computer):
    def __init__(self, model, yil, color, muddat, company, protsesor,mp):
        super().__init__(model, yil, color, muddat, company, protsesor)
        self.mp = mp
        
    def get_info(self):
        """sdghj"""
        return f"Company: {self.company} \nProtsesor: {self.protsesor} \nMp: {self.mp}"
    def get_mp(self):
        """sryj"""
        return self.mp
    def change_mp(self, new_mp):
        """sryj"""
        self.mp = new_mp
        return self.mp
tel = Phone("S24",2025,"black",8,"Samsung","Android","456-MP")
print()






