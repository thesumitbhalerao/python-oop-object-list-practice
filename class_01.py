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

for obj in bus_list:
    if obj.b_no > 200:
        print(f"Bus number : {obj.b_no} --> Bus route : {obj.bus_route}.")

