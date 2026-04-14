# print ("Calculator")
#
# def add(x,y):
#     return  x + y
#
# print (add(156,659))
#
# def subtract(x,y):
#     return x - y
#
# def multiply(x,y):
#     return x * y
#
# def divide(x,y):
#     return x / y
#
# print (subtract(156,659))
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# num3 = add (num1,num2)
# num4= subtract(num1,num2)
# num5= multiply(num1,num2)
# num6= divide(num1,num2)
#
# print ("Sonlar yig'indisi: " + str(num3))
# print ("Sonlar ayirmasi: " + str(num4))
# print ("Sonlar ko'paytmasi: " + str(num5))
# print ("Sonlar bo'linmasi: " + str(num6))
#
# print (2**4) #2ni 4chi darajasi
from operator import truediv

# help('keywords')
#
# print("\U0001F600")
#
# ism="Rashid"
# familiya="Mirzaakhmedov"
# print(f"Sening isming nima? {ism} {familiya}" )

# print ("Hello, World")
# print ("Hello, \tWorld")
# print ("Hello, \nWorld")
#
# ism="Rashid"
# familiya="Mirzaakhmedov"
# ism_sharif=f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# #
# meva = "        olma          "
# # print(meva)
# # print(f"Men {meva.lstrip()} yaxshi ko'raman")
# # print("Men "+meva.lstrip()+ " yaxshi ko'raman")
# # print(f"Men {meva.rstrip()} yaxshi ko'raman")
# # print("Men "+meva.rstrip()+ " yaxshi ko'raman")
# # print(f"Men {meva.strip()} yaxshi ko'raman")
# # print("Men "+meva.strip()+ " yaxshi ko'raman")
# # print(f"Men {meva} yaxshi ko'raman")
# # print("Men "+ meva + " yaxshi ko'raman")
#
# # ism = input ("Ismingiz nima?\n")
# # print ("Assalomu Alaykum, " + ism.capitalize())
#
# print("\U00000021")
#
# print(type(meva))
#
# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2026-t_yil
# print(f"Siz {yosh}, yoshda ekansiz")

# temp = float(36.6)
# print(type(temp))
# print(temp)

# x = int(input("Istalgan son kiriting:\n>>>"))
# print(x, " ning kvadrati ", x**2, " ga teng")
# print(x, " ning kubi ", x**3, " ga teng")

# narxlar = "12000, 18000, 190000, 25000, 6.2, -56.3"
# print(narxlar)
# print(type(narxlar))

# yosh = int(input("Yoshingiz nechida? \n>>>"))
# t_yil = 2026-yosh
# print("Siz ", t_yil, " da tug'ilgansiz")

# ismlar = ["Otabek", "Sherzod", "Shoxrux"]
# print (f"Salom {ismlar[0]}, bugun choyxona bormi?")
# print (f"Salom {ismlar[1]}, bugun choyxona bormi?")
# print (f"Salom {ismlar[2]}, bugun choyxona bormi?")
# print(type(ismlar))

# sonlar = [10.5, 52, 68, -98, -0.258, 0.56, 0.788]
# print(sonlar[2])
# print(sonlar[2]+sonlar[3])
# print(sonlar[2]+sonlar[3]*sonlar[4])
# sonlar.append (55)
# print(sonlar[2]+sonlar[3]*sonlar[5])
# sonlar.insert (2,5)
# print(sonlar[2])
# print(sonlar[2]+sonlar[3])
# sonlar.remove (10.5)
# print(sonlar)
# del sonlar [2]
# print(sonlar)
#
# kasrlar = []
# kasrlar.append(float(sonlar.pop(3)))
# kasrlar.append(float(sonlar.pop(4)))
# print(kasrlar)
#
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)
#
#
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
#
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
#
# print(sorted(mehmonlar, reverse=True))
#
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
#
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)
#
# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
# print(len(fruits))
#
#
# sonlar = list(range(0,10)) #
# print(sonlar)
#
# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)
#
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
#
#
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars)
#
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
#
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)
#
#
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)
#
#
# tomonlar = (20, 30, 55.2)
# print(tomonlar)
#
# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# print(type(toys))
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

# cars =["bmw", "mercedes benz", "audi"]
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
#
# print(sorted(cars))
# print(sorted(cars, reverse=True))
# print(cars)
#
# sonlar = [12, 64, 68, -12, -14.6]
# print(sorted(sonlar))
# print(sorted(sonlar, reverse=True))


# sonlar = list(range(1,11))
# print(sonlar)
# len(sonlar)
# print(len(sonlar))
#
# toq_sonlar = list(range(1,11,2))
# print(toq_sonlar)
# print(len(toq_sonlar))
#
# juft_sonlar = list(range(0,11,2))
# print(juft_sonlar)
# print(len(juft_sonlar))
#
# print(max(toq_sonlar))
# print(min(toq_sonlar))
# print(sum(toq_sonlar))
#
# arzon = min(sonlar)
# qimmat = max(sonlar)
# summa =sum(sonlar)
#
# print(f"past narx {arzon}, eng qimmat {qimmat}, hammasi {summa}")

# cars =["bmw", "mercedes benz", "audi", "lacetti"]
# print(cars[0:3])
# my_cars = cars[:]
# print(my_cars[3])
#
#
# print(my_cars[0])


# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Sardor"]
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print("Hayr,", mehmon)

# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Sardor"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 dekabrdagi nahorgi oshga taklif qilamiz")
#     print (f"Hurmat bilan palonchievlar oilasi")

# sonlar = list(range(1,11))
# print(sonlar)
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2}ga teng")

# sonlar = list(range(11))
# sonlar_kavdrati = []
# for son in sonlar:
#     sonlar_kavdrati.append(son**2)
# print(sonlar)
# print(sonlar_kavdrati)
#
# dostlar = []
# print("5 ta eng yaqin do'stingiz kim? ")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingiz kim?"))
# print(dostlar)


# ismlar = ["Ali", "Vali", "Jahon", "Tursun", "Iqbol"]
# for ism in ismlar:
#     print(f"Salom, {ism}")
# print(f"Kod {len(ismlar)} marta takrorlandi.")
#
# sonlar = list(range(11,100,2))
# print(sonlar)
# for son in sonlar:
#     print(son**3)

# filmlar = []
# print(input(f"5 ta sevimli kinongiz nima?"))
# for film in range(5):
#     filmlar.append(input(f"{film+1} kino"))
# print (filmlar)
#

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
# print(ismlar)

# a = 10
# print(a)
# print(a == 10)
# print(a == 5)
#
# avtolar = ["audi", "bmw", "volvo", "kia", "hyundai"]
# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())
#
# avto = "audi"
# print(avto == "audi")

# ism = "Ali"
# print(ism == "ali")
# print(ism.lower() == "ali")
#
# ism = input("Ismingiz nima?\n>>>")
# if ism.lower() != "ali":
#     print(f"Uzr, {ism.title()} biz Alini kutvommiz.")
# else:
#     print("Salom. Ali")
#
# javob = float(input("12*6 nechiga teng?>>>"))
# if javob !=72:
#     print("Javob xato!")
#
# yosh = int(input("Yoshingiz nechida?"))
# if yosh >=18:
#     print("Xush Kelibsiz!")
# else:
#     print("Kirish mumkin emas!")

# login = input("Yangi login tanlang: ")
# if len(login)<=5:
#     print("Login 5 harfdan ko'proq bo'lishi kerak")
#
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2026-yil<=18:
#     print(f'Yoshingiz {2026-yil}da ekan')
#     print('Kirish mumkin emas')
# else:
#     print('Xush kelibsiz')

# x,y = 20,30
# print("x>y") if x>y else print('x<y')

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
#
# login = input('Loginizni kiriting: ')
# if login.lower() == 'admin':
#     print(f"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# son_1 = input("Birinchi sonni kiriting: ")
# son_2 = input("Ikkinchi sonni kiriting: ")
# if son_1 == son_2:
#     print(f'Sonlar teng')
# else:
#     print(f'Sonlar farq qiladi')

# son_3 = float(input("Istalgan sonni kiriting: "))
# if son_3 <0: print(f"Manfiy son")

# son_4 = float(input("Istalgan sonni kiriting: "))
# print(son_4**(1/2)) if son_4>0 else print('Musbat sonni kiriting')

# yosh = int(input('Yoshingiz nechchida?>>>'))
# narxlar = [5000, 8000, 10000, 5000]
# if yosh<=3:
#     narx=narxlar[0]
# elif yosh<=12:
#     narx=narxlar[1]
# elif yosh<=65:
#     narx=narxlar[2]
# else:
#     yosh>65
#     narx=narxlar[3]
#
# print(f'Sizga bilet {narx} s\'om')


# kun = input('bugun nima kun?')
# if kun.lower() =='shanba' or kun.lower()=='yakshanba' :
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun dam olish kuni emas.')

# kun = input('bugun nima kun?')
# harorat = float(input('harorat qanday?'))
# if kun.lower() == 'shanba' and 'yakshanba' and harorat>30:
#     print('bugun cho\'milamiz.')
# elif kun.lower() != 'shanba' and 'yakshanba' or harorat<30:
#     print('bugun cho\'milmaymiz.')

# narh=15000
# choy=True
# salat=False
#
# if choy and salat:
#     narh=15000+10000
# elif choy or salat:
#     narh=15000+5000
#
# print(f'Jami {narh} s\'om')

# narh=15000
# choy=True #1
# salat=False #0
# non=True #1
# kompot=True #1
# assorti=False #0
#
# if choy:
#     narh=15000+3000
#     print('Mijoz choy oldi.')
# if salat:
#     print('Mijoz salat oldi.')
#     narh = narh +5000
# if non:
#     print('Mijoz non oldi.')
#     narh = narh +2000
# if kompot:
#     print('Mijoz kompot oldi.')
#     narh = narh +1500
# if assorti:
#     print('Mijoz assorti oldi.')
#     narh = narh +7500
#
#
# print(f'Jami {narh} s\'om')


# menu = ['osh', 'qozonkabob', 'shashlik']
# ovqat = input('Nima ovqat yeysiz?>>>')
# # print("osh" in menu)
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Bunday ovqat yo'q.")
#
# menu = ['osh', 'qozonkabob', 'shashlik']
# ovqat = input('Nima ovqat yeysiz?>>>')
# # print("osh" in menu)
# if ovqat.lower() not in menu:
#     print("Bunday ovqat yo'q.")
# else:
#     print("Buyurtma qabul qilindi.")

# menu = ['osh', 'qozonkabob', 'shashlik']
# buyurtmalar= ['osh', 'somsa', 'shashlik']
#
# if buyurtmalar:
#     print(len(buyurtmalar)>0)
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f'Menuda {taom} bor')
#         else:
#             print(f'Kechirasiz, menuda {taom} yo\'q')
#

# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")



# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
#
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
#
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ['alisher','aziza','yasina','umar']
#
# login = input("Yangi login tanlang: ")
#
# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# son = int(input("Istalgan butun son kiriting: "))
#
# for n in range(2,son+1):
#     if not (son%n):
#     if (son%n) ==0:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# son = float(input("Juft son kiriting: "))
#
# if son%2!=0:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")
#

# yosh = int(input("Yoshingiz nechida?"))
#
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
#
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do\'konimizda {mahsulot} bor")
#         else:
#             print(f"Do\'konimizda {mahsulot} yo\'q")
# else:
#     print("Savatingiz bo'sh")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n + 1}-mahsulotni qo\'shing: '))
#
# bor_mahsulotlar = []
# mavjud_emas = []
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# users = ['alisher1983','aziza','yasina', 'umar']
# print(users)
#
# login = input('Yangi login tanlang: ' )
#
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print(f"Xush kelibsiz! {login.title()}")

# git config --global user.name "pm14p009"
# git config --global user.email ("rashid@iuj.ac.jp")

git status