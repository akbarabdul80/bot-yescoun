import asyncio
import random
from urllib.parse import unquote
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestAppWebView
from pyrogram.raw import functions
from pyrogram.raw.types import InputBotAppShortName

# Define variables
API_ID = 25577737
API_HASH = "b291315db388c8cc41cd879393458548"
SESSION_NAME = "akbar1"
CHAT_ID = '@theYescoin_bot'
START_PARAM = "45456"
PLATFORM = 'android'
START_PARAM_WEBVIEW = "77777"

# Client setup
client = Client(
    name=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    lang_code='ru'
)

async def get_tg_web_data():
    try:
        await client.connect()  # Connect to Telegram
        messages = await client.get_chat_history_count(chat_id=CHAT_ID)

        if messages == 0:  # Start the bot if no history found
            peer = await client.resolve_peer(CHAT_ID)
            await client.invoke(
                functions.messages.StartBot(
                    bot=peer,
                    peer=peer,
                    start_param=START_PARAM,
                    random_id=random.randint(1, 9999999),
                )
            )

        # Request the web view
        web_view = await client.invoke(RequestAppWebView(
            peer=await client.resolve_peer(CHAT_ID),
            app=InputBotAppShortName(bot_id=(await client.resolve_peer(CHAT_ID)).user_id, short_name="Yescoin"),
            platform=PLATFORM,
            write_allowed=True,
            start_param=START_PARAM_WEBVIEW
        ))

        # Get and decode the URL
        auth_url = web_view.url
        query = unquote(unquote(auth_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0]))
        print(query)
        return query.replace('"', '\"')

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        await client.disconnect()  # Ensure disconnection


# Run the function
if __name__ == "__main__":
    asyncio.run(get_tg_web_data())
