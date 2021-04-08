from plugin import plugin
from colorama import Fore
import string
import random


@plugin("quotes")
def jarvis_quotes(jarvis, s):
    quotes = ['As always sir, a great pleasure watching you work', 'Sir, take a deep breath', 'Sir, we will lose power before we penetrate that shell.']
    quote = random.choice(quotes)
    jarvis.say(quote)