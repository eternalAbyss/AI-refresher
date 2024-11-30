from openai import OpenAI
import os

client = OpenAI()
user_thread_map = {}
assistant = client.beta.assistants.retrieve(os.getenv('ASSISTANT_ID'))