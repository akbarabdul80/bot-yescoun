import asyncio

from utils.logger import logger
from yescoin import YesCoin


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    yes = YesCoin(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'
    logger.success(f"Thread {thread} | {account} | Login")

    if await yes.login():
        logger.success(f"Thread {thread} | {account} | Login")

        error_cnt = 0
        update = False
        balance = await yes.get_balance()
        print(balance)

    await yes.logout()


asyncio.run(start(1, 'session', 'phone_number', 'proxy'))