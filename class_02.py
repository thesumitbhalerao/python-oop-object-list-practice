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

for obj in mess_list:
    if obj.type == "veg":
        print(f"Mess Name : {obj.m_name} --> {obj.type}.")


