#İkincisi de elinde bir çember var ve bir de nokta bu nokta bu çemberin içinde mi dışında mı algoritması
#cemberde kontrolu sadece yarıcao ve noktanın cemberın merkezınde olan uzaklıkta yapıyoruz elipste tek bir yarı cap yok cıft yarıcap var ayrıca elıpsın yonu de var 
#yanı cemberı ne kadar dondurusen dondur merkezı etrafında aynı gorunum olur ama elıpste olmaz 
#dolayısıyla oradakı zorluk 2 yarıcap ve rotasyon olması
import math
print("Cizgiye ait katsayalari giriniz:")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("daireye ait katsayalar2 giriniz:")
x = int(input("x:"))
y = int(input("y:"))
r= int(input("r:"))

d= abs(a*x + b*y+ c ) / math.sqrt (a*2 + b*2 )
print("nokta uzaklıgı  " , d , "yarıcapı " , r )
if d>r:
    print("cemberın dısında")
elif d==r:
    print("cembere deget")
else:
    print("kesıyor")