import logging
from flask import Flask, request
from flask import jsonify
from dotenv import load_dotenv
from controllers.chats.chats_handler import chats_handler
import openai

app = Flask(__name__)

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Load environment variables from .env file
load_dotenv()

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/aicoach/chat', methods=['POST'])
def aicoach_chat():
    data = request.get_json()
    user = data['user']
    responses = chats_handler().chat(user)
    response = {
        "user": user,
        "message": responses
    }
    return jsonify(response)

@app.route('/assistant', methods=['POST'])
def assistant():
    user_message = request.json.get('message', '')

    # Create a new thread
    thread = openai.Thread.create()

    # Add user's message to the thread
    openai.ThreadMessage.create(
        thread_id=thread['id'],
        role='user',
        content=user_message
    )

    # Create a run to get the assistant's response
    run = openai.ThreadRun.create(
        thread_id=thread['id'],
        assistant_id='your-assistant-id'
    )

    # Poll the run status until completion
    while run['status'] in ['queued', 'in_progress']:
        run = openai.ThreadRun.retrieve(
            thread_id=thread['id'],
            run_id=run['id']
        )

    # Retrieve the assistant's message
    messages = openai.ThreadMessage.list(thread_id=thread['id'])
    assistant_message = next(
        (msg for msg in messages if msg['role'] == 'assistant'), None
    )

    return jsonify({'reply': assistant_message['content']})

if __name__ == '__main__':
    app.run(debug=True)