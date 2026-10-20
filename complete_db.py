# Class 01 :
 
class Pmpml:                                #Class

    def __init__(self,b_no,b_route):        #Constructor
        self.b_no=b_no
        self.bus_route= b_route

bus1=Pmpml(98,"Wagholi")                    #Object
bus2=Pmpml(43,"Katraj")
bus3=Pmpml(276,"ChinchwadGaon")
bus4=Pmpml(228,"Vadgaon Mawal")
bus5=Pmpml(281,"Ganpati Matha")

bus_list=[]
print(bus_list)
bus_list.append(bus1)
bus_list.append(bus2)
bus_list.append(bus3)
bus_list.append(bus4)
bus_list.append(bus5)

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

# for obj in perfume_list:
#     if obj.price > 500:
#         print(f"Perfume Brand : {obj.brand} --> Perfume Price : {obj.price}.")


# Class 02 :

class Mess:
    
    def __init__(self,mess_name,type):
        self.m_name=mess_name
        self.type=type

mess1=Mess("Shiv_Samarth_Bhojnalaya","veg")
mess2=Mess("Khandesh_katta","veg")
mess3=Mess("Ganesh_Hotel","not-veg")
mess4=Mess("Sai_mess","veg")
mess5=Mess("chilapi_mess","non-veg")

mess_list=[]
mess_list.append(mess1)
mess_list.append(mess2)
mess_list.append(mess3)
mess_list.append(mess4)
mess_list.append(mess5)

# for obj in mess_list:
#     if obj.type == "veg":
#         print(f"Mess Name : {obj.m_name} --> {obj.type}.")


#Class 03

class TeaHouse:

    def __init__(self,n,p):
        self.name=n
        self.price=p
    
tea=TeaHouse("Tea",15)
tea1=TeaHouse("Black_tea",25)
tea2=TeaHouse("Green_tea",30)
coffee=TeaHouse("Coffee",20)
coffee2=TeaHouse("Cappuccino",120)

shop_list=[]
shop_list.append(tea)
shop_list.append(tea1)
shop_list.append(tea2)
shop_list.append(coffee)
shop_list.append(coffee2)

# for obj in shop_list:
#     if obj.price == 15:
#         print(f"Name : {obj.name} --> Price : {obj.price}.")


# class 04 

class PG:

    def __init__(self,n,r):
        self.name=n
        self.rent=r

Pg1=PG("Janki PG",2800)
Pg2=PG("Sai Boys PG",5000)
Pg3=PG("Shree PG", 3500)
Pg4=PG("Om PG",4500)
Pg5=PG("Ganesh PG", 3000)

pg_list=[]
pg_list.append(Pg1)
pg_list.append(Pg2)
pg_list.append(Pg3)
pg_list.append(Pg4)
pg_list.append(Pg5)

# for obj in pg_list:
#     if obj.rent < 4000:
#         print(f"PG Name : {obj.name} --> PG Rent : {obj.rent}")


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

# for obj in perfume_list:
#     if obj.price > 500:
#         print(f"Perfume Brand : {obj.brand} --> Perfume Price : {obj.price}.")


# Complete DataBase

complete_db=[]
complete_db.extend(bus_list)
complete_db.extend(mess_list)
complete_db.extend(shop_list)
complete_db.extend(pg_list)
complete_db.extend(perfume_list)

print("Complete Database")

print("Total_objects",len(complete_db))