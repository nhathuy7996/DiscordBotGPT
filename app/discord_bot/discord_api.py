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

        print(f"<@{self.user.id}>")

        if f"<@{self.user.id}>" in message.content: 
            user_message=message.content.replace(f"<@{self.user.id}>",'') 
            if(user_message):
                print(user_message)
                bot_response = chatgpt_response(prompt=user_message)
                await message.channel.send(bot_response)
                return

        if message.content.startswith('/tarotVI'): 
            user_message= "chọn giúp tôi 3 lá bài tarot ngẫu nhiên, giải thích ý nghĩa dựa theo câu hỏi " + message.content.replace('/tarotVI','')
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")

        if message.content.startswith('/tarotEN'): 
            user_message= "pick for me 3 random tarot card and explain it as my question "+ message.content.replace('/tarotEN','')
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)