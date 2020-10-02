# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
from telethon import TelegramClient,events
from requests import post
from logging import basicConfig, getLogger, INFO, DEBUG
from flask import Flask, abort, request, jsonify
import json
import ujson
import aiohttp
import os

APP_ID=os.environ.get(APP_ID,None)
APP_HASH=os.environ.get(APP_HASH,None)

basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=INFO,
)
bot = TelegramClient("selenium-auto-eval", APP_ID, APP_HASH)
bot.start()
print("Bot is running!")
URL="http://localhost:1313/"

@bot.on(events.NewMessage(pattern="/eval",incoming=True))
async def evaluate(eval):
    message=eval.text.split(" ")
    if len(message) != 3:
          await eval.reply("Bruh Moment! Your credentials are missing!")
    else:
        msg=await eval.reply("Processing the request...")
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with await session.post(URL, json={"uname": message[1],"passwd": message[2]}) as response:
                    data = await response.text()
                    if data == "False":
                        await msg.edit("Naniiiiii? Password Incorrect?")
                    else:
                        await msg.edit("Desu! Faculty Feedback Completed!")
                        
@bot.on(events.NewMessage(pattern="/start",incoming=True))
async def start(tr):
    await tr.respond("Onii-Chaan! Just gimme your AUMS username and password `/eval` in the format `/eval <username> <password>`\nI can assure I don't log your passwords ~nya")
bot.run_until_disconnected()
