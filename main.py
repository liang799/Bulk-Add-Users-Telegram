import asyncio
import os
import pandas as pd

from telethon import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv


xls = pd.ExcelFile('users.xlsx')
df = pd.read_excel(xls, 'Sheet1')
print(df)

potential_members = df['Users to be Added'].tolist()


async def main():
    load_dotenv()
    api_id = int(os.getenv('CLIENT_API_ID'))
    api_hash = os.getenv('CLIENT_API_HASH')
    session_str = os.getenv('CLIENT_SESSION')
    group_invite_link = os.getenv('GROUP_INVITE_LINK')

    async with TelegramClient(StringSession(session_str), api_id, api_hash) as client:
        for potential_member in potential_members:
            try:
                await client.send_message(potential_member, group_invite_link)
                print(f'Message sent to @{potential_member}')
            except Exception as e:
                print(f'Failed to send message to @{potential_member}: {e}')


# Run the main function
asyncio.run(main())
