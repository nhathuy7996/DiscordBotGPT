from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response


load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_read(self):
        print("Successfully logged in ass: ", self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message=None,None

        

        if "<@1115512161096175628>" in message.content: 
            user_message=message.content.replace("<@1115512161096175628>",'')
            print(command, user_message) 
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)