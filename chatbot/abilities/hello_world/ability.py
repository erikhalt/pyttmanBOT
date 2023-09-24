from pyttman.core.ability import Ability

from chatbot.abilities.hello_world.intents import PrintHelloWorld

# Created by Pyttman

class HelloWorld(Ability):
    intents = (
        PrintHelloWorld,
    )

    """
    Concept proof of framework
    def before_create(self):
        self.storage['APIKEY'] = 'somthng'
        self.nickname['nickname'] = ''
        self.url['URL'] = 'asdasd'+self.storage['nickname']
    """
