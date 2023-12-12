from math import *


#   Voileib
soov=input("Kas tahad suua?")
if soov.lower() == "jah" or soov=="yes" or soov=="да":
    valik=int(input("1-juustuga voileib\n2-vorstiga voileib\n"))
    if valik in [1,2]:
        if valik==1:
            print("Palun Juustuga voileib")
        else:
            print("Palun vorstiga voileib")
    else:
        print("Vale valik!")
else:
    print("Ei taha, siis ei taha")



# R = input("Введите радиус круга"))
# A = input("Введите сторону квадрата"))
# B = pi*R*R
# C = A*A*A*A
# if B>C:
#     print("Площадь квадрата больше")
# else:
#     print("Площадь круга меньше")
    


# grupp=input("Ruhma nimetus: ")
# if grupp=="TARgv23":
#    puudumised=int(input("Mitu pudumist sul on"))
#    if puudumised<15:
#        hinne=float(input("Введите свою среднюю оценуку"))
#        if hinne > 3.8:
#            print("Toetus")
#        else:
#            print("Liiga madaal kesknime hinne. Toestus ei ole")
#    else:
#        print("Toetus ei Maaratakse")
# else:
#     print("Не подходит название группы")


# grupp=input("Ruhma nimetus: ")
# puudumised=int(input("Mitu pudumist sul on"))
# hinne=float(input("Введите свою среднюю оценуку"))
# if grupp=="Targv23" and puudumised < 15 and hinne> 3.8:
#     print("Toetus")
# else:
#     print("toetus ei ole!")

# try:
#     a=float(input("Esimene arv: "))
#     try:
#         b=float(input("Teine arv: "))
#         t=input("Tehe: ")
#         if t in['=' ,'-' ,'/' ,'*' ,'**' ,'%' ,'//']: # ""=''
#             if t=='+':
#                 v = a + b
#             elif t=='-':
#                 v = a - b
#             elif t=='*':
#                 v = a * b
#             elif t=='**':
#                 v = a ** b
#             elif t=='/':
#                 if b==0:
#                     v="DIV/0"
#                 else:
#                     v = a / b
#             elif t=='%':
#                 v = a % b
#             else:
#                 v = a // b
#             print("{0}{1}{2}={3}".format(a,t,b,v))
#         else:   
#             print("Tundmatu arv ")
#     except:
#         print("Vale b arvu sndmetup ")
# except:
#     print("Vale a arvu andmetup ")



# a=float(input("Alpha: "))
# b=float(input("Betta: "))
# c=float(input("Gamma: "))
# if a>0 and b>0 and c>0:
#     if a+b+c==180:
#         print("Треугольник")
#     else:
#         print("Не треугольник")
# else:
#     print("Не правильные данные")




