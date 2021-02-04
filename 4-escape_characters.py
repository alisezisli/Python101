#! /usr/bin/python3

#Kaçış karakterleri (Escape characters)

#Kaçış karakterleri sayesinde, karakterleri esas amacından farklı şekilde kullanabilme şansımız vardır.
#Kaçış karakteri ile bir araya gelerek yeni bir anlam kazanan ifadelere ise "kaçış dizileri" diyoruz.

#Daha önce tek tırnak ve çift tırnak işaretlerinin print'teki öneminden bahsetmiştik.
#İfade içinde tek tırnak geçiyorsa; tüm ifadeyi çift tırnak ya da üç tırnak arasına alabiliyorduk.
#İfade içinde çift tırnak geçiyorsa; tüm ifadeyi tek tırnak ya da üç tırnak arasına alabiliyorduk.
#Bunların haricinde, kaçış karakterlerini kullanarak, bu işaretlerin yorumlanma şeklini değiştirebiliriz:


#Bu örnek hata verir. Çünkü tırnak işaretleri doğru kapatılmadı:
#print("Hep bir ağızdan "Buraya kadar!" diye bağırdılar.")
#SyntaxError: invalid syntax

#Bu şekilde yazabilirdik:
print('Hep bir ağızdan "Buraya kadar!" diye bağırdılar.')



#Kaçış karakterlerini kullanmak istersek de "\" yardımımıza koşuyor.
#Burada anlatmak istediğimiz durum: İki çift tırnak arasını string göreceksin, fakat başında \ olan çift tırnak
#işaretlerini dikkate alma. String ifade orada bitmiyor, devamı gelecek.
#En başta ve en sonda kullandığımız ", print fonksiyonu için gerekli.
#Başında \ olan " işaretleri ise, gerçek anlamda " yazmak istediğimizi gösteriyor:
print("Hep bir ağızdan \"Buraya kadar!\" diye bağırdılar.")



#Kaçış karakterlerinin tek görevi bu değil.
#Örneğin, yeni satıra geçmek istediğimiz belirtmek için \n kullanabiliriz:
print("Birinci\nİkinci\nÜçüncü")



#Peki gerçekten \ karakteri yazmak istersek ne yapacağız? \ karakterinin özel bir anlamı var.
#Bu anlamı ezebilmek için \ karakterinden de kaçacağız. Yani aslında \\ kullanacağız:
print("\\_/\\_/\\_/")



#Bir sekme (tab) eklemek için ise \t ifadesini kullanabiliriz:
print("Sütun - 1\tSütun - 2")
print("Satır - 1.1\tSatır - 1.2")



#Dikkat etmemiz gereken başka bir kaçış dizisi \a
#Bu karakteri kullanarak Windows 10 üzerinde uyarı sesini alabildim. Fakat GNU/Linux ortamında ses gelmedi.
#Neredeyse hiçbir zaman kullanmayacaksınız muhtemelen. Fakat bilmekte fayda var.
#Çünkü fark etmeden kendi string ifadeniz içinde bu ifadenin geçmesi muhtemel:
print("\a")



#Bir başka kaçış dizisi olarak \r örneğine bakalım.
#\n yeni bir satıra geçerken, \r ise aynı satırın başına gider.
#İfadenizde \r görülene kadarki ifade yazdırılır, \r'den sonrası ise en başa dönülerek tekrar yazılır:
print("Ali\rSezişli")
#Ali yazdı. Başa döndü. Sezişli yazdı. Önceki yazılanlar silindi.
#Başka bir örnek:
print("Sezişli\rAli")
#Sezişli yazdı. Başa döndü. S'nin yerine A, e'nin yerine l, z'nin yerine i yazdı ve ifade bitti.
#Çıktı "Aliişli" şeklinde olacaktır.
#Insert tuşu açık kalmış gibi...



#Bir alt satırda tab'lamak... Yeni bir satıra geçip (\n) bir de yeni bir sekme açmak (\t) isterseniz \v kullanabilirsiniz.
#Önemli bir nokta. Göreceğiniz üzere çıktılar birebir aynı değil.
#Yani aslında tam olarak \n\t değil. "Düşey sekme" diyorlar bu olaya.
#Ek olarak, bu kaçış dizisinin davranışı OS'e göre değişkenlik gösterebilir.
print("Düşey\n\tsekme")
print("Düşey\vsekme")



#\r bizi satır başına götürüyordu. \b ise bir karakter önceye götürüyor:
print("Son karakter\be")
#Son karakter yazar. \b ile bir sola kayar ve r'nin üzerine gelir. İfade devam eder. r silinir, e yazılır.
#Farklı bir örnek:
#\b kullanmadan boşluklar bırakılır:
gun = 5
print(gun,".","günün şafağında doğuya bakın.")
#Varsayılan olarak gelen boşluklardan birini istemiyoruz. O yüzden tam o noktada bir sola kayıp oradan yazmaya devam edelim:
print(gun,"\b.","günün şafağında doğuya bakın.")



#Kısa ve uzun unicode gösterimleri için sırasıyla \u ve \U kullanabiliriz:
print("\u00B6")
print("\u00D1")
print("\U000000C6")



#Benzer şekilde, karakterleri unicode adı ile çağırmak için de \N kullanılır:
print("\N{LATIN CAPITAL LETTER S WITH CEDILLA}")



#Onaltılık (Hexadecimal) sistemdeki bir ifadenin karakter karşılığını çağırmak için \x kullanılır:
print("\x42")



#Kaçış karakterlerinden tümden kaçabilmenizi sağlayacak başka bir karakter var, r:
#Aşağıdaki ifadede \n, \t, \a, \U gibi birçok kaçış dizisi var.
#print("C:\Users\ali\tablolar\nisan")
#Yukarıdaki ifade hata verecektir.
#Her bir ifadeden tekrar \ kullanarak kaçabilirsiniz:
print("C:\\Users\\ali\\tablolar\\nisan")
#Ya da şöyle yapabiliriz:
print(r"C:\Users\ali\tablolar\nisan")



#Son olarak \f'den bahsedelim. Çıktının yeni bir sayfaya geçmesini söyleyen bir kaçış dizisi.
#Eski tip yazıcılara "burası bitti, yeni sayfaya geç" demek için kullanılsa da günümüzde pek bir önemi kalmadı.
#Bir dosyaya yazma işlemi yaparak deneyelim:
f = open("yenisayfa.txt", "w")
print("Sayfa-1\fSayfa-2", file=f)
f.close()
