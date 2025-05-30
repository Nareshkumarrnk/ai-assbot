from pyrogram import Client,filters
from pyrogram.types import Message
from openai import OpenAI
from config import OPENAI_KEY

openrouter= OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENAI_KEY,
)

def register_handlers(app: Client):
  @app.on_message(filters.private & filters.text)
  async def chat_handler(client_tg: Client,message: Message):
    user_input = message.text
    await
message.chat.action.send_chat_action("typing")
    try:
      completion = openrouter.chat.completions.create(
  
  model="openai/gpt-4.1",
  messages=[
    {
      "role": "user",
      "content":user_input}
  ]
      )
      reply=completion.choices[0].message.content
    except Exception as e:
      reply= f"Error:{str(e)}"
    await message.reply_text(reply)

      

