from flask import Flask, request, Response
from flask_cors import CORS
from services.number_api_service import NumberAPIService
import json

app = Flask(__name__)
CORS(app)

number_service = NumberAPIService()


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')

    try:
        number = int(number_str)

        response = number_service.analyze_number(number)
        return Response(json.dumps(response), mimetype='application/json', status=200)

    except (ValueError, TypeError):
        error_response = {
            "number": request.args.get('number'),
            "error": True
        }
        return Response(json.dumps(error_response), mimetype='application/json', status=400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)