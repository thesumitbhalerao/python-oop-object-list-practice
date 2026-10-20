# class 05

class Perfume:

    def __init__(self,b,p):
        self.brand=b
        self.price=p

perfume1=Perfume("Bella Vita",549)
perfume2=Perfume("Wild Stone",499)
perfume3=Perfume("Fogg",350)
perfume4=Perfume("Denver",650)
perfume5=Perfume("Park Avenue",450)

perfume_list=[]
perfume_list.append(perfume1)
perfume_list.append(perfume2)
perfume_list.append(perfume3)
perfume_list.append(perfume4)
perfume_list.append(perfume5)

for obj in perfume_list:
    if obj.price > 500:
        print(f"Perfume Brand : {obj.brand} --> Perfume Price : {obj.price}.")