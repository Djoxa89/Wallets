# Wallets

Sistem za upravljanje i distribuciju digitalnih ulaznica.

## Project structure

- `backend/` — backend aplikacije
- `admin/` — administrativni deo sistema
- `scanner/` — komponenta za skeniranje i validaciju ulaznica

## Environments

### Development

Development okruženje se pokreće lokalno.

- PostgreSQL: 18.4
- Host: `localhost`
- Port: `5432`

### Staging

Staging okruženje se nalazi na serveru.

## Secrets

Tajne vrednosti, lozinke i ključevi ne čuvaju se u Git repozitorijumu.

Lokalne tajne se čuvaju u `.env` fajlu, koji nije deo repozitorijuma.

Za deljenje strukture konfiguracije koristi se `.env.example` bez stvarnih tajnih vrednosti.

## Local development

Detaljna uputstva za pokretanje biće dopunjena kada budu postavljene konkretne komponente sistema.

Docker Compose se ne koristi. Development okruženje se pokreće direktno lokalno.
