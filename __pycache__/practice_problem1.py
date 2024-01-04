''' import datetime
x=datetime.datetime.now()
print(x)
x=datetime.datetime(2022,2,22)     '''
#problem to take d.o.b as imput
from gettext import find


operators=input("Enterr an operator....")
find=input("Enterr a number....")
find2=input("Enterr a number....")



express=find+operators+find2
print("solution= ",eval(express))