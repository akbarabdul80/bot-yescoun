# config.py
API_ID = 25577737  # Replace with your Telegram API ID
API_HASH = "b291315db388c8cc41cd879393458548"  # Replace with your Telegram API Hash
WORKDIR = "./sessions"  # Directory for session files

# Proxy Configuration
PROXY = {
    'TYPE': {
        'REQUESTS': 'http',  # HTTP/HTTPS/SOCKS5 for requests
        'TG': 'socks5',  # Type of proxy for Telegram client
    }
}

# Delay Configuration
DELAYS = {
    'ACCOUNT': (1, 3),  # Random delay range in seconds for account actions
}

# Referral Code
REF_CODE = "your_referral_code"  # Replace with your referral code
