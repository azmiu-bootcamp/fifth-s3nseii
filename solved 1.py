#Verilmis 3 edededen bir birine beraber olanlarin sayini tapin
num1 = int(input('Brinici ededi daxil edin'))
num2 = int(input('Ikinici ededi daxil edin'))
num3 = int(input('Ucnuncu ededi daxil edin'))

if num1==num2 and num2==num3:
    print(num1,'=',num2,'=',num3)
    print('3 beraber eded var')

elif num1 == num2:
    print(num1,'=',num2)
    print('2 beraber eded var')
elif num2==num3:
    print(num2,'=',num3)
    print('2 beraber eded var')
elif num1==num3:
    print(num1,'=',num3)
    print('2 beraber eded var')
