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
git clone https://github.com/devmertsert/django_backend.git
```
```sh
cd django_backend
```
```sh
pip install -r requirements.txt
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

(eğer bulunamayan modul olursa aşağıdaki formatta o modulu indirin ve sunucuyu üstteki komut ile tekrar çalıştırın)

```sh
pip install <modul_adı>
```

Proje çalıştırıldıktan sonra http://localhost:8000/admin/ adresine gidilerek "createsuperuser" metodu ile oluştuurmuş olduğumuz kullanıcı ile giriş yapıyoruz
Ardından alttaki users modeline kullanıcı ekliyoruz.
Movies modeline de filmler ekliyoruz ve kullanmaya hazır hale getiriyoruz

```json
ornek kullanici: {
    Role: 'User',
    Name: 'Ad Soyad',
    Email: 'email@gmail.com',
    Password: '123456789'
}
ornek film: [
    {
        name: "Godzilla vs. Kong",
        description: "In a time when monsters walk the Earth, humanity’s fight for its future sets Godzilla and Kong on a collision course that will see the two most powerful forces of nature on the planet collide in a spectacular battle for the ages.",
        image_url: "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/pgqgaUx1cJb5oZQQ5v0tNARCeBp.jpg",
        language: "En",
        genre: "Action, Fantasy, Science Fiction",
        release_date: "2021-03-26"
        imdb: "7.8"
    },
    {
        name: "Tom & Jerry",
        description: "Tom the cat and Jerry the mouse get kicked out of their home and relocate to a fancy New York hotel, where a scrappy employee named Kayla will lose her job if she can’t evict Jerry before a high-class wedding at the hotel. Her solution? Hiring Tom to get rid of the pesky mouse.",
        image_url: "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8XZI9QZ7Pm3fVkigWJPbrXCMzjq.jpg",
        language: "En",
        genre: "Comedy, Family, Animation",
        release_date: "2021-02-26"
        imdb: "9.8"
    },
    {
        name: "Miraculous World: New York, United HeroeZ",
        description: "Teen Parisian superheroes Ladybug and Chat Noir visit New York on a field trip and discover that superheroes exist in the United States too.",
        image_url: "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/9YbyvcrHmY2SVbdfXpb8mC4Fy0g.jpg",
        language: "En",
        genre: "Animation, TV Movie, Fantasy, Action",
        release_date: "2021-03-26"
        imdb: "8.3"
    },
    {
        name: "Mortal Kombat Legends: Scorpion's Revenge",
        description: "After the vicious slaughter of his family by stone-cold mercenary Sub-Zero, Hanzo Hasashi is exiled to the torturous Netherrealm. There, in exchange for his servitude to the sinister Quan Chi, he’s given a chance to avenge his family – and is resurrected as Scorpion, a lost soul bent on revenge. Back on Earthrealm, Lord Raiden gathers a team of elite warriors – Shaolin monk Liu Kang, Special Forces officer Sonya Blade and action star Johnny Cage – an unlikely band of heroes with one chance to save humanity. To do this, they must defeat Shang Tsung’s horde of Outworld gladiators and reign over the Mortal Kombat tournament.",
        image_url: "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/4VlXER3FImHeFuUjBShFamhIp9M.jpg",
        language: "En",
        genre: "Animation, Action, Fantasy",
        release_date: "2020-04-12"
        imdb: "8.2"
    },
]
```