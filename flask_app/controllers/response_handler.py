class response_handler:
    def __init__(self):
        pass

    def get_response(self, messages: list) -> list:
        """
        Retrieves the response from the messages.
        Args:
            messages (list): The list of messages from the thread.
        Returns:
            list: The list of responses from the messages.
        """
        # Check if 'data' exists and is a list
        messages = getattr(messages, 'data', None)
        if not messages or not isinstance(messages, list):
            print("No messages found!")

        responses = []
        # Iterate over each message
        for message in messages:
            content_blocks = getattr(message, 'content', [])

            # Extract and print text from content blocks
            for block in content_blocks:
                if getattr(block, 'type', None) == 'text':
                    text_content = getattr(block.text, 'value', None)
                    if text_content:
                        responses.append(text_content)

        return responses