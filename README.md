# Number Classification API

A RESTful API that analyzes numbers and returns their mathematical properties along with interesting facts.

## Project Structure

```
number-classification-api/
├── app.py                  # Application entry point and route
├── services/
│   └── number_api_service.py  # Business logic
├── utils/
│   ├── constants.py          # Configuration constants
│   └── number_properties.py   # Mathematical utilities
├── requirements.txt
└── README.md
```

## Features

- Determines if a number is **prime**
- Checks if a number is **perfect**
- Identifies **Armstrong numbers**
- Calculates **digit sum**
- Classifies numbers as **even/odd**
- Fetches fun facts from the **Numbers API**
- **CORS enabled**
- Handles invalid input gracefully

## Requirements

- Python 3.8+
- Flask
- Flask-CORS
- Requests
- gunicorn

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/EmmyAnieDev/number-classifier-api.git
    cd number-classification-api
    ```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:
```bash
python app.py
```

2. The API will be available at `http://localhost:8000`

## API Documentation

### GET /api/classify-number

Analyzes a number and returns its properties.

#### Query Parameters

- `number` (required): The integer to analyze

#### Success Response (200 OK)

```json
{
    "number": 5,
    "is_prime": true,
    "is_perfect": false,
    "properties": [
        "armstrong",
        "odd"
    ],
    "digit_sum": 5,
    "fun_fact": "5 is the third prime number."
}
```

#### Error Response (400 Bad Request)

```json
{
    "number": "letter",
    "error": true
}
```

#### Occurs when an invalid input (like a letter/alphabet) is provided.


## Deployment

The API is deployed on Railway and can be accessed at:
```
https://number-classifier-api-production.up.railway.app/
```

## 🧪 Quick Test

To test the full URL with the parameter:

```bash
curl "https://number-classifier-api-production.up.railway.app/api/classify-number?number=5"
```