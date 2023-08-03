# Python scripti joka lähettää tiedon discrord webhookkiin jos hälytin on lauennut
# Tekijä: Miko Savolainen
# Vuosi: 2022


import RPi.GPIO as GPIO 
from discord_webhook import DiscordWebhook, DiscordEmbed


webhook = DiscordWebhook(url='WEBHOOk TÄHÄN')
embed = DiscordEmbed(title='HÄLYTYS', description='Halytys aktivoitu', color='03b2f8')

webhook.add_embed(embed)

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    if not GPIO.input(10) == GPIO.HIGH:
        print("hälytys lauennut!")
        response = webhook.execute()
        

GPIO.cleanup()