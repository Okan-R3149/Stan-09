password = 12345

sifre = int(input("Lutfen sifrenizi giriniz: "))
count = 0

while count < 3:
    if sifre == password:
        print("Giris Yaptiniz")
        break
    elif sifre != password:
        print("Yanlıs sifrer girdiniz! Lütfen tekrar deneyiniz")
        sifre = input("Lütfen sifrenizi giriniz: ")
    count += 1
else:
     print("Sifre hakkinizi doldurdunuz. Bankayla iletisime geciniz!!")