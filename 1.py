from datetime import date
d1=date.today()
ds=str(d1)
print("Системная дата ",ds)
yyyy=ds[0:4]
mm=ds[5:7]
dd=ds[8:10]

date=dd+"/"+mm+"/"+yyyy
print ("Российский формат",date)
