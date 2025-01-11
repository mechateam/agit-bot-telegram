from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 21290570
api_hash = 'ca6fab0c87af950ae1b6490faf6e6512'

client = TelegramClient('MeldiBotSendingToAgit1', api_id, api_hash)
client.start()

print(client.get_me().stringify())


@client.on(events.NewMessage(chats='infolokerdrg2020'))
async def my_event_handler(event):
    pesan = event.raw_text
    print(event.raw_text)
    print(type(event.raw_text))
    if "jakarta timur" in pesan:
        await client.send_message('Agritadr', "Ayankkk, ini ada lowongan di\n"+pesan)

client.start()
client.run_until_disconnected()