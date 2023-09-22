from pyttman.core.ability import Ability
from .intents import PrintHelloWorld


# Created by Pyttman

class HelloWorld(Ability):
    intents = (
        PrintHelloWorld,
    )
