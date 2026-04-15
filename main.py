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

# git remote remove origin
# git remote add origin https://github.com/pm14p009/Mohirdev_homeworks.git
# git push -u origin main
# git remote -v
# git config --global http.proxy http://10.130.20.251:2002
# git config --global https.proxy http://10.130.20.251:2002
# git status
# git push -u origin main
# git config --global --list
# git config --global http.sslVerify false
# git push -u origin main



# 14-python

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.


# otam = {'ismi':'mirzali', 'tyil':1946,'viloyat':'toshkent'}
# print(f"Otamning ismi ({otam['ismi'].title()}, {otam['tyil']} - yilda, {otam['viloyat'].title()} shahrida tug\'ilgan")
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")


# ism = input("Otangizni ismini kiriting: ")
# yil = input ("Otangizni tug'ilgan yilini kiriting: ")
# vil = input ("Otangizni tug'ilgan viloyatini kiriting: ")
# otam = {'ismi':'ism', 'tyil':yil,'viloyat':'vil'}
# print(f"Otamning ismi {ism.title()}, {yil}-yilda, {vil.title()} shahrida tug'ilgan")

# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }
#
# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat",
#     'dictionary': "Lug'at"}
#
## print(python_izohli_lugati['tuple'])
#
# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
#
# if tarjima==None:
#     print('Bunday so\'z mavjud emas')
# else:
#     print(f"{kalit.title()} so\'zi {tarjima} deb tarjima qilinadi.")
#
# # print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))
#
# # print(python_izohli_lugati.get(kalit, 'bunday ism mavjud emas.'.title()))


# 15-python

# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
#
# print(talaba_0.items())
#
# for kalit, qiymat in talaba_0.items():
#     print(f'Kalit: {kalit}')
#     print(f'Qiymat: {qiymat} \n')

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
#
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
#
# # print(mahsulotlar.keys())
#
#
# # print('Do\'kondagi mahsulotlar:')
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())
#
# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     # print(mahsulot.title())
#     print(f"{mahsulot.title()}: {mahsulotlar[mahsulot]} so'm")


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
#     }
#
#
# print(telefonlar.items())
# print(telefonlar.keys())
# print(telefonlar.values())
#
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
# # for tel in telefonlar.keys():
# #     print(tel)
# # for tel in telefonlar.items():
# #     print(tel)
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}
#
# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
#
# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
# print('\n')
# print('Davlatlar nomi')
# for poytaxt in sorted(davlatlar.keys()):
#     print(poytaxt.title())
# print('\n')
# print('Davlatlar nomi va poytaxtlari:')
# for key, value in sorted(davlatlar.items()):
#     print(f"{key.title()} - {value.title()}")


# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
#
# poytaxt = input('Qaysi poytaxtning davlatini bilishni istaysiz?: ').lower()
# # Teskari qidirish
# davlat = None
# for kalit, qiymat in davlatlar.items():
#     if qiymat.lower() == poytaxt:
#         davlat = kalit
#
# if davlat is None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#     print(f"{poytaxt.title()} — {davlat.title()} davlatining poytaxti")



# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }
#
# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())
#
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")
#

# NESTING (16-Python)
#
# AMALIYOT
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
#
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
#
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
#
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
#
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.


# Royhat ichida lug'at (1)

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }
#
# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }
#
# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }
#
# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }
#
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
#
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil-tyil} yil umr ko'rgan.")


# Royhat ichida lug'at (2)


# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }
#
# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }
#
# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }
#
# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
#
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
#
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)


# Lug'at ichida ro'yhat


# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }
#
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)




# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }
#
# for key, value in davlatlar.items():
#     if key.lower()=='aqsh':
#         davlat = key.upper()
#     else:
#         davlat = key.capitalize()
#     print(f"\n{davlat}ning poytaxti {value['poytaxt'].title()}"
#           f"\nHududi: {value['maydon']} kv.km"
#           f"\nAholisi: {value['aholi']}"
#           f"\nPul birligi: {value['pul birligi']}")


# lug'at ichida lug'at

#
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }
#
# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")



