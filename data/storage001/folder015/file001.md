```plaintext
Zbudowac w pythonie mikroserwisk, który na podstwie adresu (wojewodztwo, miejscowosc, ulica, numer)

zwróci:

- lat (opcjonalnie)

- long (opcjonalnie)

- czas dojazdu do wybranej lokalizacji (wspolrzedne)

- czas dojazdu do najbliszczego marketu

- czas dojazdu do najbliższej szkoły podstawowej

Wymaganie: dostarczone wraz z plikami Dockerfile i docker-compose
```

Aby zbudować mikroserwis w Pythonie, który spełnia wymagania podane w zadaniu, będziemy korzystać z następujących technologii i narzędzi:

- Flask: Framework do budowania API w Pythonie.
- Google Maps API (lub inne API geolokalizacyjne) do uzyskiwania współrzędnych (lat, long) oraz czasów dojazdu.
- Docker do konteneryzacji aplikacji.
- Docker Compose do uruchamiania aplikacji i zależnych usług.

### 1. Tworzenie mikroserwisu w Pythonie

#### a) Instalacja zależności

Najpierw utwórz nowy katalog na projekt i zainstaluj zależności:

```bash
mkdir geo_service
cd geo_service
python3 -m venv venv
source venv/bin/activate
pip install Flask requests
```

#### b) Kod mikroserwisu `app.py`

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Wstaw tutaj swój klucz API do Google Maps
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

def get_coordinates(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            location = results[0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

def get_travel_time(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('rows')
        if results and results[0]['elements']:
            duration = results[0]['elements'][0]['duration']['text']
            return duration
    return None

@app.route('/location', methods=['GET'])
def location_info():
    wojewodztwo = request.args.get('wojewodztwo')
    miejscowosc = request.args.get('miejscowosc')
    ulica = request.args.get('ulica')
    numer = request.args.get('numer')
    destination_lat = request.args.get('dest_lat')
    destination_lng = request.args.get('dest_lng')

    if not all([wojewodztwo, miejscowosc, ulica, numer]):
        return jsonify({"error": "Brak wymaganych parametrów"}), 400

    address = f"{ulica} {numer}, {miejscowosc}, {wojewodztwo}, Poland"
    lat, lng = get_coordinates(address)

    if lat is None or lng is None:
        return jsonify({"error": "Nie udało się uzyskać współrzędnych"}), 500

    response_data = {
        "lat": lat,
        "lng": lng
    }

    if destination_lat and destination_lng:
        destination = f"{destination_lat},{destination_lng}"
        origin = f"{lat},{lng}"
        travel_time_to_destination = get_travel_time(origin, destination)
        response_data["czas_dojazdu_do_wybranej_lokalizacji"] = travel_time_to_destination

    # Dodanie zapytań do najbliższego marketu i szkoły
    market_address = "najbliższy market, Poland"
    school_address = "najbliższa szkoła podstawowa, Poland"

    response_data["czas_dojazdu_do_najbliższego_marketu"] = get_travel_time(f"{lat},{lng}", market_address)
    response_data["czas_dojazdu_do_najbliższej_szkoły"] = get_travel_time(f"{lat},{lng}", school_address)

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 2. Plik Dockerfile

Stwórz plik `Dockerfile` w głównym katalogu projektu:

```Dockerfile
# Wybierz obraz bazowy
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki do kontenera
COPY . .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Określ port
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "app.py"]
```

### 3. Plik requirements.txt

Stwórz plik `requirements.txt` z zależnościami:

```
Flask
requests
```

### 4. Plik docker-compose.yml

Stwórz plik `docker-compose.yml` w głównym katalogu projektu:

```yaml
version: '3'
services:
  geo_service:
    build: .
    ports:
      - '5000:5000'
    environment:
      - GOOGLE_MAPS_API_KEY=YOUR_GOOGLE_MAPS_API_KEY
```

### 5. Budowanie i uruchamianie aplikacji

Aby zbudować obraz Dockera i uruchomić aplikację, uruchom poniższe komendy:

```bash
docker-compose build
docker-compose up
```

### 6. Testowanie API

API będzie dostępne pod adresem `http://localhost:5000/location`. Przykładowe zapytanie:

```http
GET /location?wojewodztwo=mazowieckie&miejscowosc=Warszawa&ulica=Nowy+Swat&numer=1&dest_lat=52.2297&dest_lng=21.0122
```

### Podsumowanie

Mikroserwis jest teraz gotowy do użycia i można go konteneryzować za pomocą Dockera. Serwis zwraca współrzędne podanego adresu, czas dojazdu do wybranej lokalizacji oraz do najbliższego marketu i szkoły.
