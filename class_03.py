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

for obj in shop_list:
    if obj.price == 15:
        print(f"Name : {obj.name} --> Price : {obj.price}.")
