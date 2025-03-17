import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    
    response = f"Hey How are you , You say : {message.content}"

    await cl.Message(content = response).send()
