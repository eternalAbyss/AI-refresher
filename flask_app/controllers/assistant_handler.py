from services.openai_service import openai_service
from prompts import prompts

class assistant_handler:
    def __init__(self):
        self.openai_service = openai_service()

    def create_assistant(self)->object:
        """
        Creates an assistant using the OpenAI API with the given instructions.
        Args:
            instructions (str): The instructions to be provided to the assistant.
        Returns:
            object: The created assistant object.
        """

        sys_prompt = prompts().get_prompt('system_instructions')
        assistant = self.openai_service.create_assistant(sys_prompt)
        return assistant

    def create_thread(self)->object:
        """
        Creates a thread using the OpenAI API.
        Returns:
            object: The created thread object.
        """
        thread = self.openai_service.create_thread()
        return thread
    
    def run_thread(self, assistant, thread, prompt: str)->object:
        """
        Executes a thread run with the given assistant and prompt, and retrieves the messages 
        if the run is completed.
        Args:
            assistant: The assistant object containing the assistant ID.
            thread: The thread object containing the thread ID.
            prompt (str): The instructions or prompt to be used for the thread run.
        Returns:
            object: The list of messages from the thread if the run is completed.
        """
        messages = self.openai_service.run_thread(assistant, thread, prompt)
        return messages