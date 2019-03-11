f = False
a = int(input('a ya vermek istediyiniz qiymeti daxil edin: '))
b = int(input('b ye vermek istediyiniz qiymeti daxil edin: '))
if a==6 or b==6:
    f = True
    print(f)
elif a - b == 6 or a + b ==6:
    f = True
    print(f)
else:
    print(f)
