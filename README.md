# ravintolasovellus

Lopullinen palautus:
- sovellusta voi testata Herokussa [täällä](https://tsoha-raflasovellus.herokuapp.com/)
- käyttäjä voi rekisteröityä käyttäjän tai ylläpitäjän oikeuksin

- ylläpitäjä voi lisätä ravintolan määrittämällä sille nimen, kuvauksen, osoitteen ja aukioloajat. Nimen ja kuvauksen pituus tarkistetaan. Ravintolaa ei lisätä, jos nimi, kuvaus tai osoite on tyhjä.

![Ravintolan lisääminen](https://github.com/sannahan/ravintolasovellus/blob/main/pictures/lisays.png)

- ylläpitäjä voi poistaa ravintolan. Ylläpitäjä näkee pudotusvalikon, josta voi valita poistettavan ravintolan.
- ylläpitäjä voi lisätä ravintoloille tägejä. Tägejä voi lisätä monelle ravintolalle yhtäaikaisesti, mutta vain yhden tägin kerrallaan. Sovellus antaa virheviestin, jos ylläpitäjä yrittää lisätä sekä itse kirjoittamansa että listasta valitsemansa tägin.

![Ravintolan tagaaminen](https://github.com/sannahan/ravintolasovellus/blob/main/pictures/tagays.png)

- ylläpitäjä ja käyttäjä voivat tarkastella listausta kaikista ravintoloista. Lista esitetään arvostelujen perusteella paremmuusjärjestyksessä (uudet ravintolat, joilla ei ole vielä arvosteluja, näkyvät kuitenkin ensin)
- ylläpitäjä ja käyttäjä voivat tarkastella ravintoloita kartalla (kun ravintolan sijaintia klikataan, avautuu infoikkuna, jossa näkyy ravintolan nimi, kuvaus ja linkki ravintolan sivulle)
- ylläpitäjä ja käyttäjä voivat etsiä ravintoloita hakusanalla ravintoloiden kuvauksista
- ylläpitäjä ja käyttäjä voivat etsiä ravintoloita tägillä. Tägit listataan pudotusvalikkoon, josta käyttäjä voi valita haluamansa

![Ravintolan arvosteleminen](https://github.com/sannahan/ravintolasovellus/blob/main/pictures/arvostelu.png)

- ylläpitäjä ja käyttäjä voivat arvostella ravintolan sen sivulla
- ylläpitäjä voi poistaa arvostelun Poista-painikkeella

Jatkokehitysideoita:

- kartassa näkyy tällä hetkellä for development purposes only -vesileima: tämä on tarkoituksellista. Oikean version käyttöönotto vaatisi karttapalvelun maksullisen version käyttöönoton
- karttanäkymä olisi hyvä saada vastaamaan muun sovelluksen ulkonäköä
- parhausjärjestykseen listaamisessa on jokin bugi, jonka havaitsin vasta viimeisissä testeissä
- routes.py:n metodit ovat turhan pitkiä

Välipalautus 3:

- sovellusta voi testata Herokussa [täällä](https://tsoha-raflasovellus.herokuapp.com/)
- pääsivulta löytyy seuraavat toiminnot: ravintolalistaus, ravintolalistaus kartalla ja ravintolahaku (ylläpitäjä voi lisäksi lisätä ja poistaa ravintolan)
- kartta näyttää kaikki ravintolat yhtäaikaisesti, ja klikkauksesta avautuu infoikkuna, jossa on kuvaus ja linkki ravintolan sivulle
- virhetilanteiden käsittelyä on lisätty (käyttäjä ei voi antaa tyhjää syötettä rekisteröityessään tai ravintolaa lisätessään; salasana toistetaan rekisteröitymisvaiheessa kahdesti; osoite varmennetaan oikeaksi ennen sen lisäystä tietokantaan; virheviestit näkyvät samalla sivulla)
- tietokantaa on laajennettu parempaa aukioloaikatoiminnallisuutta varten (toiminnallisuutta on tarkoitus muokata siten, että jokaisella päivällä voi olla eri aukioloaika)
- toteutettavana vielä ravintolan tietojen muokkaus ja arvioiden poisto ylläpitäjänä, ravintolalistaus parhaimmasta huonoimpaan sekä ryhmät ravintoloille 

Välipalautus 2:

- sovellusta voi testata Herokussa [täällä](https://tsoha-raflasovellus.herokuapp.com/)
- kirjautumis- ja rekisteröitymistoiminto on valmis
- pääsivulta löytyy kolme toimintoa: ravintolan lisäys, ravintolalistaus ja ravintolan etsiminen kartalta
- käyttäjärooleja ei ole vielä eriytetty, eli kuka tahansa voi lisätä ravintolan
- ravintolalistaus näyttää ravintolat lisäysjärjestyksessä. Ravintolaa klikatessa pääsee tarkastelemaan ravintolan tietoja ja jättämään ravintolasta arvostelun.
- ravintolaa voi hakea kartalta ravintolan nimellä (karttanäkymä käyttää Googlen rajapintaa ilman API-avainta, joten kartassa näkyy for development only -teksti). Karttanäkymää on tarkoitus muokata siten, että kaikki lisätyt ravintolat näkyvät kartalla yhtäaikaisesti
- virhetilanteita ei vielä juurikaan käsitellä (käsittely on toistaiseksi lisätty vain kirjautumis- ja rekisteröitymistoimintoon)

Välipalautus 1:

Ravintolasovelluksen toiminnallisuudet:

- käyttäjä on peruskäyttäjä tai ylläpitäjä
- käyttäjä voi kirjautua sisään ja ulos
- käyttäjä voi rekisteröityä
- käyttäjä näkee ravintolat kartalla ja näkee ravintolasta lisätietoa (kuvaus, linkki) sitä klikatessaan
- käyttäjä voi antaa ja lukea arvioita (tähdet, kommentti)
- ylläpitäjä voi lisätä ja poistaa ravintoloita sekä määrittää ravintolasta näytettävät tiedot
- käyttäjä voi etsiä ravintoloita hakusanalla
- käyttäjä näkee listan ravintoloista parhaimmasta huonompaan
- ylläpitäjä voi poistaa ravintolasta jätetyn arvion
- ylläpitäjä voi luoda ryhmiä ravintoloille (esimerkiksi kasvisruokaa tarjoavat ravintolat)
