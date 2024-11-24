from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)

thread = client.beta.threads.create()

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )

# Check if 'data' exists and is a list
messages = getattr(messages, 'data', None)
if not messages or not isinstance(messages, list):
    print("No messages found!")

# Iterate over each message
for message in messages:
    role = getattr(message, 'role', 'unknown').capitalize()
    content_blocks = getattr(message, 'content', [])

    print(f"Role: {role}")

    # Extract and print text from content blocks
    for block in content_blocks:
        if getattr(block, 'type', None) == 'text':
            text_content = getattr(block.text, 'value', None)
            if text_content:
                print(text_content)
    print("-" * 80)