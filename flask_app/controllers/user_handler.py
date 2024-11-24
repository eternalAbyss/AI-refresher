from controllers.assistant_handler import assistant_handler
from config import user_thread_map
import logging

class user_handler:
    def __init__(self):
        self.user_id = None
        self.thread_id = None

    def get_thread(self, user_id: str) -> str:
        if user_id in user_thread_map.keys():
            logging.info(f"User {user_id} already has an openai thread.")
            return user_thread_map[user_id]
        else:
            thread = assistant_handler().create_thread()
            user_thread_map[user_id] = thread
            logging.info(f"User {user_id} has been assigned a new openai thread")
            return thread

    def map_user_id_with_openai_thread(self, user_id: str, thread_id: str = None) -> None:
        if user_id not in user_thread_map.keys():
            user_thread_map[user_id] = thread_id
