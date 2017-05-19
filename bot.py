import asyncio
import discord
import queue
import threading
import os

DISCORD_KEY = os.environ['DISCORD_KEY']
DISCORD_CHANNEL = os.environ['DISCORD_CHANNEL']

class Bot:

    def __init__(self, token, vc_channel):
        self.client = discord.Client()
        self.queue = queue.Queue(maxsize=10)
        self.channel_id = vc_channel
        self.token = token
        self.ready = False

    def run(self):
        self.cons_loop = asyncio.new_event_loop()
        self.cons_loop.create_task(self.consume())
        threading.Thread(target=self.cons_loop.run_forever).start()

        self.client.event(self.on_message)
        self.client.event(self.on_ready)
        self.client.run(self.token)


    async def on_ready(self):
        chan = self.client.get_channel(self.channel_id)
        self.vc = await self.client.join_voice_channel(chan)
        self.ready = True
        print("Bot is ready.")
        
    async def on_message(self, message):
        print('Message recived: {}'.format(message.content))
        if not self.ready:
            print('Ignoring message')
            return
        tok = message.content.split(' ')
        if tok[0] == ']]':
            if tok[1] == 'skip':
                if self.player:
                    self.player.stop()
            else:
                try:
                    self.queue.put(tok[1], block=False)
                    print("Added {} to queue.".format(tok[1]))
                except queue.Full:
                    await self.client.send_message(message.channel, 'Sorry the queue is already full.')

    async def consume(self):
        asyncio.set_event_loop(self.cons_loop)
        try:
            while True:
                it = self.queue.get()
                print("Playing " + it)
                self.player = self.vc.create_ytdl_player(it)
                print("player started for {}".format(it))
                self.player.start()
                self.player.join()
                print("player ended for {}".format(it))
        except Exception as e:
            print(e)



if __name__ == '__main__':
    b = Bot(DISCORD_KEY, DISCORD_CHANNEL)
    b.run()

