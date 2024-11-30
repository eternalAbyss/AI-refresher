from flask import request
from controllers.user_handler import user_handler
from controllers.assistant_handler import assistant_handler
from controllers.response_handler import response_handler
from config import assistant

class chats_handler:
    def __init__(self):
        self.assistant = assistant

    def chat(self, user: str) -> dict:
        """
        Initiates a chat with the AI coach.
        Args:
            user (str): The user ID.
            messages (list): The list of messages from the user.
        Returns:
            dict: The response from the AI coach.
        """
        data = request.get_json()
        query = data['query']
        # Get the thread for the user
        thread = user_handler().get_thread(user)
        messages = assistant_handler().run_thread(self.assistant, thread, query)
        response = response_handler().get_response(messages)
        return response