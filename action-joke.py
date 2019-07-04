#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import requests
from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

  print()
  print(intent_message.intent.intent_name)
  print ()

  if intent_message.intent.intent_name == 'amartinez35:joke':

    r = requests.get('https://blague.xyz/joke/random')
    joke = r.json().get('joke')

    hermes.publish_end_session(intent_message.session_id, joke)


with Hermes(MQTT_ADDR) as h:
  h.subscribe_intents(intent_received).start()