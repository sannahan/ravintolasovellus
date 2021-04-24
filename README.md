# ravintolasovellus

Tavoitteena toteuttaa ravintolasovellus:

- käyttäjä on peruskäyttäjä tai ylläpitäjä
- käyttäjä voi kirjautua sisään ja ulos
- käyttäjä voi rekisteröityä
- käyttäjä näkee ravintolat kartalla ja näkee ravintolasta lisätietoa (kuvaus, aukioloajat) sitä klikatessaan
- käyttäjä voi antaa ja lukea arvioita (tähdet, kommentti)
- ylläpitäjä voi lisätä ja poistaa ravintoloita
- ylläpitäjä voi muokata ravintolasta näytettäviä tietoja
- käyttäjä voi etsiä ravintoloita hakusanalla
- käyttäjä näkee listan ravintoloista parhaimmasta huonompaan
- ylläpitäjä voi poistaa ravintolasta jätetyn arvion
- ylläpitäjä voi luoda ryhmiä ravintoloille (esimerkiksi kasvisruokaa tarjoavat ravintolat)

Välipalautus 1:

- sovellusta voi testata Herokussa [täällä](https://tsoha-raflasovellus.herokuapp.com/)
- kirjautumis- ja rekisteröitymistoiminto on valmis
- pääsivulta löytyy kolme toimintoa: ravintolan lisäys, ravintolalistaus ja ravintolan etsiminen kartalta
- käyttäjärooleja ei ole vielä eriytetty, eli kuka tahansa voi lisätä ravintolan
- ravintolalistaus näyttää ravintolat lisäysjärjestyksessä. Ravintolaa klikatessa pääsee tarkastelemaan ravintolan tietoja ja jättämään ravintolasta arvostelun.
- ravintolaa voi hakea kartalta ravintolan nimellä (karttanäkymä käyttää Googlen rajapintaa ilman API-avainta, joten kartassa näkyy for development only -teksti). Karttanäkymää on tarkoitus muokata siten, että kaikki lisätyt ravintolat näkyvät kartalla yhtäaikaisesti
- virhetilanteita ei vielä juurikaan käsitellä (käsittely on toistaiseksi lisätty vain kirjautumis- ja rekisteröitymistoimintoon)

Välipalautus 2:

- sovellusta voi testata Herokussa [täällä](https://tsoha-raflasovellus.herokuapp.com/)
- pääsivulta löytyy seuraavat toiminnot: ravintolalistaus, ravintolalistaus kartalla ja ravintolahaku (ylläpitäjä voi lisäksi lisätä ja poistaa ravintolan)
- kartta näyttää kaikki ravintolat yhtäaikaisesti, ja klikkauksesta avautuu infoikkuna, jossa on kuvaus ja linkki ravintolan sivulle
- virhetilanteiden käsittelyä on lisätty (käyttäjä ei voi antaa tyhjää syötettä rekisteröityessään tai ravintolaa lisätessään; salasana toistetaan rekisteröitymisvaiheessa kahdesti; osoite varmennetaan oikeaksi ennen sen lisäystä tietokantaan; virheviestit näkyvät samalla sivulla)
- tietokantaa on laajennettu parempaa aukioloaikatoiminnallisuutta varten (toiminnallisuutta on tarkoitus muokata siten, että jokaisella päivällä voi olla eri aukioloaika)
- toteutettavana vielä ravintolan tietojen muokkaus ja arvioiden poisto ylläpitäjänä, ravintolalistaus parhaimmasta huonoimpaan sekä ryhmät ravintoloille 
