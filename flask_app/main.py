from flask import Flask, request
from flask import jsonify
from controllers.assistant_handler import assistant_handler
from controllers.user_handler import user_handler
from controllers.response_handler import response_handler
import logging

app = Flask(__name__)

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/aicoach/chat', methods=['POST'])
def aicoach_chat():
    messages = []
    data = request.get_json()
    user = data['user']
    query = data['query']
    assistant = assistant_handler().create_assistant()
    thread = user_handler().get_thread(user)
    messages = assistant_handler().run_thread(assistant, thread, query)
    responses = response_handler().get_response(messages)
    response = {
        "user": user,
        "message": responses
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)