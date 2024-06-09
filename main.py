import asyncio
from pyngrok import ngrok
from pyrogram import Client, filters
from aiohttp import web

api_id = "21425768"
api_hash = "850a6a60609afe5986a71d85f13cc452"

ngrok.set_auth_token('2hbUMvo6QYBQV5O8pmKlKP0G6Ze_4tZqgcM3DwsWqUsUiCxrG')

app = Client('my_session', api_id, api_hash)

@app.on_message(filters.text)
async def echo(client, message):
    await print(message)

        
if __name__ == '__main__':
    print("bot start")
    asyncio.run(app.run())