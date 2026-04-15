import asyncio
import os
from backboard import BackboardClient
import dotenv

dotenv.load_dotenv()

async def main():
    client = BackboardClient(api_key=os.getenv("BACKBOARD_API_KEY"))

    # Step 1: Create assistant
    assistant = await client.create_assistant(
        name="My First Assistant",
        system_prompt="You are a helpful assistant that responds concisely."
    )
    print(f"Created assistant: {assistant.assistant_id}")

    # Step 2: Create thread
    thread = await client.create_thread(assistant.assistant_id)
    print(f"Created thread: {thread.thread_id}")

    # Step 3: Send message
    response = await client.add_message(
        thread_id=thread.thread_id,
        content="say Hello World",
        stream=False
    )
    print(f"Assistant: {response.content}")

asyncio.run(main())
