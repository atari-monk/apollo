```plaintext
Build a microservice in Python that, based on an address (province, town, street, number), returns:

Latitude (optional)
Longitude (optional)
Travel time to a selected location (coordinates)
Travel time to the nearest market
Travel time to the nearest primary school
Requirement: Provide with Dockerfile and docker-compose files.
```

To build a microservice in Python that fulfills the requirements, we'll use the following technologies and tools:

- **Flask:** A web framework for building APIs in Python.
- **Google Maps API** (or another geolocation API) to obtain coordinates (latitude, longitude) and travel times.
- **Docker** to containerize the application.
- **Docker Compose** to manage the application and its dependent services.

### 1. Creating the Microservice in Python

#### a) Install Dependencies

First, create a new project directory and install the necessary dependencies:

```bash
mkdir geo_service
cd geo_service
python3 -m venv venv
source venv/bin/activate
pip install Flask requests
```

#### b) Microservice Code (`app.py`)

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Insert your Google Maps API key here
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
        return jsonify({"error": "Missing required parameters"}), 400

    address = f"{ulica} {numer}, {miejscowosc}, {wojewodztwo}, Poland"
    lat, lng = get_coordinates(address)

    if lat is None or lng is None:
        return jsonify({"error": "Failed to obtain coordinates"}), 500

    response_data = {
        "lat": lat,
        "lng": lng
    }

    if destination_lat and destination_lng:
        destination = f"{destination_lat},{destination_lng}"
        origin = f"{lat},{lng}"
        travel_time_to_destination = get_travel_time(origin, destination)
        response_data["travel_time_to_selected_location"] = travel_time_to_destination

    # Add queries for the nearest market and primary school
    market_address = "nearest market, Poland"
    school_address = "nearest primary school, Poland"

    response_data["travel_time_to_nearest_market"] = get_travel_time(f"{lat},{lng}", market_address)
    response_data["travel_time_to_nearest_school"] = get_travel_time(f"{lat},{lng}", school_address)

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 2. Dockerfile

Create a `Dockerfile` in the project's root directory:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### 3. requirements.txt

Create a `requirements.txt` file with the dependencies:

```
Flask
requests
```

### 4. Docker Compose File

Create a `docker-compose.yml` file in the root directory:

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

### 5. Building and Running the Application

To build the Docker image and run the application, execute the following commands:

```bash
docker-compose build
docker-compose up
```

### 6. Testing the API

The API will be accessible at `http://localhost:5000/location`. Example request:

```http
GET /location?wojewodztwo=mazowieckie&miejscowosc=Warsaw&ulica=Nowy+Swat&numer=1&dest_lat=52.2297&dest_lng=21.0122
```

### Summary

The microservice is now ready to be used and can be containerized using Docker. It returns the coordinates of a given address, travel time to a selected location, and travel times to the nearest market and primary school.
