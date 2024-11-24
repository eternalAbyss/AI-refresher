from openai import OpenAI

class openai_service:

    def __init__(self):
        self.client = OpenAI()
        

    def create_assistant(self, instrcutions: str)->object:
        """
        Creates an assistant using the OpenAI API with the given instructions.
        Args:
            instrcutions (str): The instructions to be provided to the assistant.
        Returns:
            object: The created assistant object.
        """
        assistant = self.client.beta.assistants.create(
            name="Zenith Sama",
            instructions=instrcutions,
            model="gpt-4o-mini",
            )
        
        return assistant
    
    def create_thread(self)->object:

        thread = self.client.beta.threads.create()
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

        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions=prompt
        )

        if run.status == 'completed': 
            messages = self.client.beta.threads.messages.list(
                thread_id=thread.id
            )
        
        return messages