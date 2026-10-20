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

for obj in pg_list:
    if obj.rent < 4000:
        print(f"PG Name : {obj.name} --> PG Rent : {obj.rent}")
