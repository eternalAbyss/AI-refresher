from prompts.system_prompt import system_instructions

class prompts:
    def __init__(self):
        self.system_instructions = system_instructions

    def get_prompt(self, prompt_name: str)->str:
        """
        Returns the prompt text for the given prompt name.
        Args:
            prompt_name (str): The name of the prompt.
        Returns:
            str: The prompt text.
        """
        if prompt_name == 'system_instructions':
            res_prompt = self.system_instructions
        return res_prompt