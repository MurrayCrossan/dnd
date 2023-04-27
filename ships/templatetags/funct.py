from django import template
import random

register = template.Library()

@register.filter
def getAtr(obj, atr):
    return getattr(obj, atr)

@register.filter
def getCrewVars(obj):
    print(obj.getVars())
    return obj.getVars()

@register.filter
def formatShipName(obj):
    return obj.replace(" ", "_")

@register.filter
def getFlag(obj=""):
    lst = ["ra-beetle","ra-bird-claw","ra-butterfly","ra-cat","ra-dinosaur","ra-dragon","ra-dragonfly","ra-eye-monster","ra-fairy","ra-fish","ra-fox","ra-gecko","ra-hydra","ra-insect-jaws","ra-lion","ra-love-howl","ra-maggot","ra-octopus","ra-rabbit","ra-raven","ra-sea-serpent","ra-seagull","ra-shark","ra-sheep","ra-snail","ra-snake","ra-spider-face","ra-spiked-tentacle","ra-spiral-shell","ra-suckered-tentacle","ra-tentacle","ra-two-dragons","ra-venomous-snake","ra-wyvern","ra-wolf-head","ra-wolf-howl"]
    choice = random.choice(lst)
    return choice