#!/usr/bin/env python2
# coding: utf-8

from hermes_python.hermes import Hermes
import requests
import time

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

  if intent_message.intent.intent_name == 'amartinez35:joke':
    
    #if intent_message.slots.subject:
    #  r = requests.get('https://chucknorrisfacts.fr/api/get?data=nb:1;type:txt;tri:alea')
    #  joke = r.json()[0].get('fact')
    #else:
    r = requests.get('https://blague.xyz/joke/random')
    question = r.json().get('joke').get('question').replace('?', '    ')
    answer = r.json().get('joke').get('answer')
    hermes.publish_continue_session(intent_message.session_id, question)
    time.sleep(0.5)
    hermes.publish_end_session(intent_message.session_id, answer)


with Hermes(MQTT_ADDR) as h:
  h.subscribe_intents(intent_received).start()
