from plugin import plugin
from colorama import Fore
import random
import string


@plugin("fakehacker")
def fake_hacker(jarvis, s):
    while True:
        rand = ' '.join([random.choice(string.ascii_letters) for x in range(random.randrange(30, 80))])
        jarvis.say(rand, Fore.GREEN)
