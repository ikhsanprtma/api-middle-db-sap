# Flask Application

This project is a Flask application that connects to a SQL Server database and provides endpoints for testing database connections and retrieving stock data.

## Project Structure

```
flask-app
├── app.py                  # Main application file containing Flask routes
├── requirements.txt        # Python dependencies for the application
├── Dockerfile              # Instructions for building the Docker image
├── .dockerignore           # Files and directories to ignore when building the Docker image
└── README.md               # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. **Install dependencies**:
   You can install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   You can run the Flask application locally with:
   ```
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Docker Instructions

To build and run the application using Docker, follow these steps:

1. **Build the Docker image**:
   ```
   docker build -t flask-app .
   ```

2. **Run the Docker container**:
   ```
   docker run -p 5000:5000 flask-app
   ```
   The application will be accessible at `http://localhost:5000`.

## Usage

- **Test Database Connection**:
  Access the endpoint to test the database connection:
  ```
  GET /test-db
  ```

- **Get Stock Data**:
  Retrieve stock data by providing the date range:
  ```
  GET /get-data-stock-opname-penerimaan-bahan-baku?from=YYYYMMDD&to=YYYYMMDD
  ```

Replace `YYYYMMDD` with the desired date format.