import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from openai import OpenAI
client = OpenAI(
    api_key="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"
)

token = '6527142271:AAHPj-712vqa_C3UMIMAbpxuiQN8cTq2xIo'
updater = Updater(token=token, use_context= True)
dispatcher = updater.dispatcher
updater.start_polling()
chat_id = 6893588310
bot = telegram.Bot(token=token)
public_chat_name = -1002111713064

def chatGPT(update, context):
    message = update.channel_post
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.text + " json"}
        ],
        response_format={"type": "json_object"}
    )

    message = bot.send_message(chat_id=public_chat_name, text=completion.choices[0].message.content)
    print(message.chat_id)    
echo_handler = MessageHandler(Filters.chat(public_chat_name), chatGPT)
dispatcher.add_handler(echo_handler)


