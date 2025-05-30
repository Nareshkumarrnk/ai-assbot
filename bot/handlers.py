from pyrogram import Client,filters
from pyrogram.types import Message
from pyrogram import enums
from openai import OpenAI
from config import OPENAI_KEY

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= OPENAI_KEY,
)

def register_handlers(app: Client):
    @app.on_message(filters.private&filters.text)
    async def chat_handler(client_app, message):
      user_input=message.text
      await message.reply_text("Thinking")
      try:
        completion = client.chat.completions.create(
  
        model="mistralai/mistral-7b-instruct",
        messages=[
        {
        "role": "user",
        "content":user_input
        }
        ]
        )
        reply=completion.choices[0].message.content
        await message.reply_text(reply)

      except Exception as e:
        await message.reply_text("failed to reply")
        print("error in AI",e)

      

