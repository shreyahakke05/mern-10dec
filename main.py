import arithmetic as ar
import geometry as geo
from geometry import calc_rec_peri as peri
from geometry import calc_rec_area as area

print("Hello,World!!")

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

ar.add(num1,num2)
ar.sub(num1,num2)
ar.mul(num1,num2)
ar.div(num1,num2)

len=int(input("Enter length:"))
br=int(input("Enter breadth:"))
peri(num1,num2)
area(num1,num2)