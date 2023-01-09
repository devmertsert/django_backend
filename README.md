# Django Case Study
## _Full Stack Developer Task_

## Tanım
Uygulama ve Proje Detayları:
- Django Projesi olmali.
- Kullanici giris sayfasi olmali.
- Film detaylari admin'den girilecek.
- Uygulama ekteki tasarımlara uygun şekilde “listeleme ve detay sayfası” olmak uzere 2 sayfadan oluşmalı.
- Listeleme sayfasında arama çubuğunda yapılan sorguya göre tasarımdaki şekilde filmler listelenmeli
- Arama çubuğunda auto complete olmalı
- Bir filmde [+] butonuna tıklandığında kullanicinin Watch List listesine kaydedilmeli ve bu filmler listelemede Watch List tabında gösterilmeli
- Uygulama Github, Bitbucket veya Gitlab uzerinden paylasilmali.
- Arayüz icin herhangi bir hazir arayuz frameworku (Bootstrap vb.) kullanabilirsin.
- Uygulamayi herhangi bir client side framework (Backbone, Angular, React) kullanarak gelistirebilirsin.
- Gerekli komutların yer aldığı README dosyasını da eklemelisin.

## Kurulum
Projeyi çalıştırabilmek için aşağıdaki adımları uygulayınız.

```sh
git clone django_backend
```
```sh
cd django_backend
```
```sh
pipenv install
```

(eğer bulunamayan modul olursa aşağıdaki formatta o modulu indirin)

```sh
pip install <modul_adı>
```
```sh
cd backend
```
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
```sh
python manage.py createsuperuser
```
```sh
python manage.py runserver
```