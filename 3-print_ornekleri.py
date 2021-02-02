#!/usr/bin/python3

#Ekrana herhangi bir string değer yazdırmak için:
print("Merhaba Dünya!")


#Yazdırılacak değer, integer tipinde de olabilir:
print(1928)


#Değişkenlerin yazdırılması:
takim = "Bucaspor"
print(takim)
#Ekrana "Bucaspor" yazar.


#Yazdırma işleminde tek tırnak ('), çift tırnak (") ya da 3 tırnak (""") kullanabilirsiniz:
print('Deneme')
print("Deneme")
print("""Deneme""")


#Ekrana çift tırnak işareti yazmak isterseniz, ifadenizi tek tırnaklar arasına alabilirsiniz:
print('Dinlenecek müzisyen "Hayko Cepkin"dir.')


#Benzer şekilde tek tırnak işareti yazmak isterseniz, çift tırnak işaretleri yardımınıza koşar:
print("Bucaspor 11 Mart 1928'de kuruldu.")


#Benim cümlem iki işareti de içeriyor diyorsanız:
print("""Hayko Cepkin'in "brutal" vokallerini duymayan kaldı mı?""")


#3 tırnak işaretini, çok satırlı çıktılar verebilmek için de kullanabilirsiniz:
print("""
                     ._.
__  _  ________  _  _| |
\ \/ \/ /  _ \ \/ \/ / |
 \     (  <_> )     / \|
  \/\_/ \____/ \/\_/  __
                      \/
""")


#Çok satırlı çıktılar için \n de kullanabiliriz:
print("Birinci satır\nİkinci satır\nÜçüncü satır")


#print kullanırken, string'leri uç uca ekleyebilirsiniz:
degisken1="Buca"
degisken2="spor"
print(degisken1+degisken2)


#Ancak integer ve string değerleri, yukarıda mantıkla ekleyemezsiniz:
sayi=29
yazi="Ekim"
#Aşağıdaki satır, hata vereceği için yorum olarak bırakılmıştır:
#print(sayi+yazi)
#Hata: TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Bu durumdan kaçabilmek için virgül (,) karakteri kullanabiliriz.
#Virgül ile ayrılan kelimeler arasında otomatik olarak boşluk bırakılır:
print(degisken1,degisken2)
print(sayi,yazi)


#Boşluk bırakmak istemiyorum fakat integer ve string'i birlikte yazdırmak istiyorum diyorsanız; casting yapabilirsiniz:
print(str(sayi)+yazi)


#Aslında virgül karakteri, araya boşluklar koymak zorunda değil.
#Print çalıştırırken, ayraç olarak boşluk karakteri kullanılır. Bu, varsayılan ayardır ve tabii ki değiştirilebilir.
#sep için herhangi bir değer vermediğimizde, print aşağıdaki gibi davranır:
print("Bu", "cümlenin", "kelimeleri", "arasında", "boşluk", "var.", sep=" ")


#sep değerini değiştirebilirsiniz:
print("Bu", "cümlenin", "kelimeleri", "arasında", "boşluk", "yok", sep="*")
print("Bu", "cümlenin", "kelimeleri", "arasında", "boşluk", "yok.", sep="_-_ ")



#print fonksiyonu, yine varsayılan bir davranış olarak, yazma işlemini bitirince  alt satıra geçer.
#Tıpkı ayraç için sep kullanıldığı gibi, satır sonu için de end parametresi vardır.
#Esasında print fonksiyonu, end parametresinde varsayılan değer olarak "\n" kullanır.
#Yani yazdığı her şeyi yeni satır karakteriyle bitirir.

#Varsayılan print davranışı:
print("Cümle bitince alt satıra geç.", end="\n")


#Bu davranışı değiştirmek için:
print("Bu satırlar",end="==")
print("alt alta yazılmaz",end="==")
print("eşittir karakterleri ile biter",end="==")



#Yeni bir satıra geçmek için:
print()


#print fonksiyonunun bir de "file" parametresi vardır.
#print, varsayılan olarak bütün çıktılarını standart çıktıya (standart output, stdout) verir.
#file parametresini, bu davranışı değiştirmek için kullanırız.
#Aşağıdaki örnekte, script'ile aynı dizinde bulunacak "deneme.txt" isimli bir dosya açılıyor.
#print çıktısı, bu dosyaya yazılıyor:
#deneme.txt dosyasını yazma modunda aç (Dosya yoksa, oluşturulur):
dosya=open("deneme.txt", "w")
#Metni dosya içine yaz:
print("To the file!", file=dosya)
#Yazma işlemini tamamla ve dosyayı kapat.
dosya.close()


#Yukarıdaki örnekte, dosya.close() çalışana kadar dosyada hiçbir değişiklik olmayacaktır.
#Her print sonrasında, içeriğin dosyaya yazılmasını istersek "flush" kullanabiliriz.
#flush, varsayılan olacak False değerdedir.
#flush True yapıldığında ise, her print sonrasında değişiklikler dosyaya yazılacaktır:
dosya2=open("deneme2.txt", "w")
print("Dosyaya close'dan önce yaz.", file=dosya2, flush=True)
dosya2.close()



