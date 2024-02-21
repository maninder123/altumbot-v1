from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from flask_cors import CORS
import uuid

# calling the agent response here
from sql_agent.agent import api_response


app = Flask(__name__)
CORS(app)

@app.route('/sqlagent/api', methods=['POST'])
def get_response():
    """this function is use to chat with the redshift database to provide the response"""
    try:
        request_data = request.form.to_dict()

        source_id = str(uuid.uuid4())

        if not request_data:
            raise BadRequest('Invalid request. Missing form data.')

        user_input = request_data.get('user_input')
        source_name = request_data.get('source_name')

        if not user_input or not source_name:
            raise BadRequest('Invalid request. Missing source_name or user_input fields.')

        response, status = api_response(user_input,source_name)
        print('api res:',response)

        response_json = {
            'source_id': source_id,
            'user_input': user_input,
            'source_name' : source_name,
            'response': response,
            'status': status
        }

        return jsonify(response_json)

    except BadRequest as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 400
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500
if __name__ == '__main__':
    app.run(debug=False)

