import urllib.parse
import json
from datetime import datetime
import requests
from telethon.sync import TelegramClient
from telethon import functions, types

# API Telegram Anda
api_id = 25577737  # Ganti dengan API ID Anda
api_hash = 'b291315db388c8cc41cd879393458548'  # Ganti dengan API Hash Anda
name = 'akbar'  # Ganti dengan nama session Anda

with TelegramClient(name, api_id, api_hash) as client:
    # Get chat
    bot = client.get_entity('theYescoin_bot')

    print(bot.stringify())

    result = client(functions.messages.RequestWebViewRequest(
        peer=bot,
        bot=bot,
        platform='android',
        from_bot_menu=True,
        url='https://www.yescoin.gold/',
        start_param='1403435891',
    ))

    webview_url = result.stringify()

    # Decode URL query string
    parsed_url = urllib.parse.urlparse(webview_url)
    query_string = parsed_url.fragment.split('=', 1)[-1]
    params = urllib.parse.parse_qs(urllib.parse.unquote(query_string))

    print(params)

    # Decode `user` JSON data
    user_data = json.loads(urllib.parse.unquote(params['user'][0]))

    # Convert auth_date to readable format
    auth_date_unix = int(params['auth_date'][0])
    auth_date_readable = datetime.utcfromtimestamp(auth_date_unix).strftime('%Y-%m-%d %H:%M:%S UTC')

    print(webview_url)
    # Prepare decoded values
    decoded_data = {
        "code": f"user={json.dumps(user_data)}&chat_type=sender&auth_date={auth_date_unix}&signature={params['signature'][0]}&hash={params['hash'][0]}"
    }

    # Langkah untuk membersihkan string JSON di dalam 'code'
    cleaned_code = decoded_data['code'].replace(': ', ':').replace(', ', ',').replace('": ', '":"').replace('", "','","').replace(': "', ':"').replace('": ', '":')

    # Membuat JSON yang sesuai format permintaan
    result = {
        "code": "user={\"id\":7621724236,\"first_name\":\"Test\",\"last_name\":\"\",\"username\":\"ZERODEV_01\",\"language_code\":\"id\",\"allows_write_to_pm\":true,\"photo_url\":\"https:\\/\\/t.me\\/i\\/userpic\\/320\\/BQ-QSfKW-jzDUs-byoStmcyP_eLvo4TESk1B-l5FPs1_ICg7EmLKKdsGh2kz2Jg7.svg\"}&chat_instance=-145718358148689571&chat_type=sender&auth_date=1734766716&signature=Kywui21H_qn-pUiI7aNjvHK12FLkwV46JemMNv1U6VZY2nVCU_zqYYlGK83MOqJ2eX7rr0uOpPkefTZxfwEnBw&hash=2787591164947fd99552e47c9cadaa37f0592ce9ed10d20e1f5512b4bac58c38"
    }

    print(result)

    # Send POST request
    url = 'https://bi.yescoin.gold/user/login'
    response = requests.post(url, data=result)

    # Output response
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
