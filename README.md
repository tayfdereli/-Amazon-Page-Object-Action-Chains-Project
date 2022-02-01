# -Amazon-Page-Object-Action-Chains-Project


# Stepler;

>1.  http://www.amazon.com sitesine gidecek ve anasayfanın açıldığını assertion ile onaylayacak,
 
>2. Login ekranını açıp, bir kullanıcı ile login olunacak ( daha önce siteye üyeliği varsa o olabilir )

>3. Ekranin ustundeki Search alanına 'samsung' yazıp ara butonuna tıklanacak,

>4. Gelen sayfada samsung icin sonuc bulunduğunu onaylayacak,

>5. Arama sonuçlarından 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanin şu an gösterimde oldugunu onaylayacak,

>6. Üstten 3. urunun içindeki 'Add to List' butonuna tıklayacak,

>7. Ekranin en üstündeki 'List' linkine tiklayacak içerisinden Wish listi seçecek,

>8. Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak,

>9. Favorilere alinan bu urunun yanindaki 'Delete' butonuna basarak, favorilerimden cikaracak,

>10. Sayfada bu urunun artik favorilere alinmadigini onaylayacak.

# Nasıl Çalışır ? 

> Utils/Locator/LoginPageLocator kısmından mail adresinizi ve parolanızı , kullanıcı girişi için değiştirmeniz gerekiyor.
![image](https://user-images.githubusercontent.com/93590132/151952359-19b1db3c-e7b0-4192-8bb7-b4b6b6b2a617.png)

> Terminale "pytest" yazarak testi koşabiliriz.

> Çalışma videosu -->https://www.loom.com/share/9e71dbdbb58d4704a0d559f1a9e48b5b

# Pages

>- **BasePage**

-Diğer tüm pageler bu classtan miras aldı.

-Pagelerde kullanılan fonksiyonlar bu pagede oluşturulup diğer pagelerde çağırıldı.

>Diğer Pageler;

>- **HomePage,LoginPage,ProductPage,SearchPage,WishListPage**

-Steplerdeki ilgili aksiyonlar pagelerine ayrılarak yazıldı.

# Tests
>- BaseTest --> Testin base kısmı oluşturuldu.

>- Mysteps --> Pagelerde oluşturulan fonksiyonlar bu kısımda çağırılarak test stepleri oluşturuldu.

# Utils

>- Locator >> Tüm sayfalardaki locatorlar sayfa başlıklarına göre bu kısımda tanımlandı.
