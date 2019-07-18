# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
from telethon import TelegramClient,events
from requests import post
from logging import basicConfig, getLogger, INFO, DEBUG
from flask import Flask, abort, request, jsonify
import json
APP_ID=""
APP_HASH=""
basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=INFO,
)
bot = TelegramClient("selenium-auto-eval", APP_ID, APP_HASH)
bot.start()
URL="http://localhost:1313/"
@bot.on(events.NewMessage(pattern="/eval",incoming=True))
async def evaluate(eval):
    message=eval.text.split(" ")
    if len(message) != 3:
          await eval.respond("Credentials incomplete")
    else:
        await eval.respond("Processing the request...")
        data = {"uname": message[1],
                "passwd": message[2]}
        r = post(url = URL, json = json.dumps(data))
        if r.text == "False":
            await eval.respond("Unable to connect to AUMS/ Credentials incorrect")
        else:
            await eval.respond("Evaluation completed successfully!")
@bot.on(events.NewMessage(pattern="/start",incoming=True))
async def start(tr):
    tr.respond("Ohai! Just gimme your username and password with the command `/eval` in the format `/eval <username> <password>` Built and maintained by: @baalajimaestro and @akashsuper2000")
bot.run_until_disconnected()
