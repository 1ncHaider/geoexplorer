# geoexplorer
Interactive Map Visualization Tool
# GeoExplorer - Interactive Map Visualization

An interactive geographic data visualization tool built with Python, Flask, and Leaflet.js.

## Features

- Interactive map with multiple visualization types (choropleth, markers, heatmap)
- Multiple datasets (population density, GDP per capita, climate data)
- Region and year filtering
- Data insights and statistics
- Python backend for data processing

## Installation

1. Clone this repository:

git clone https://github.com/YOUR_USERNAME/geoexplorer.git
cd geoexplorer


2. Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


3. Run the application:

python app.py


4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

geoexplorer/
├── app.py              # Flask application
├── templates/          # HTML templates
│   └── index.html      # Main page template
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation


## Running Without Command Line

If you don't have access to a command line, you can:

1. Download this repository as a ZIP file
2. Install Python from python.org
3. Install the required packages using pip through your IDE
4. Run the app.py file through your Python IDE
