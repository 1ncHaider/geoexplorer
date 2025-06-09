from flask import Flask, render_template, jsonify, request
import json
import os
import random

app = Flask(__name__)

# Sample data - in a real app, you'd load this from files
POPULATION_DATA = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "United States",
                "density": 36,
                "population": 331000000,
                "gdp": 21433225,
                "gdpPerCapita": 64767,
                "region": "namerica"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-95.7129, 37.0902]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Brazil",
                "density": 25,
                "population": 212600000,
                "gdp": 1839758,
                "gdpPerCapita": 8659,
                "region": "samerica"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-51.9253, -14.2350]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "China",
                "density": 153,
                "population": 1402000000,
                "gdp": 14342903,
                "gdpPerCapita": 10216,
                "region": "asia"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [104.1954, 35.8617]
            }
        }
    ]
}

# Function to process geographic data
def process_geo_data(dataset_name, year=2023, region="all"):
    """
    Process geographic data based on dataset name, year and region
    """
    # In a real app, you'd load from files
    if dataset_name == "population":
        data = POPULATION_DATA
    elif dataset_name == "gdp":
        # Create GDP data from population data
        data = json.loads(json.dumps(POPULATION_DATA))
        for feature in data["features"]:
            feature["properties"]["value"] = feature["properties"]["gdpPerCapita"]
    elif dataset_name == "climate":
        # Create climate data from population data
        data = json.loads(json.dumps(POPULATION_DATA))
        for feature in data["features"]:
            feature["properties"]["temperature"] = random.randint(-10, 30)
            feature["properties"]["precipitation"] = random.randint(0, 2000)
            feature["properties"]["value"] = feature["properties"]["temperature"]
    else:
        data = {"type": "FeatureCollection", "features": []}
    
    # Filter by region if specified
    if region != "all":
        data["features"] = [f for f in data["features"] 
                           if f["properties"].get("region") == region]
    
    # Calculate statistics
    stats = {
        "count": len(data["features"])
    }
    
    return data, stats

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/data/<dataset>/<year>/<region>')
def get_data(dataset, year, region):
    """API endpoint to serve data"""
    geo_data, stats = process_geo_data(dataset, year, region)
    return jsonify({
        'geo_data': geo_data,
        'statistics': stats
    })

if __name__ == '__main__':
    app.run(debug=True)
