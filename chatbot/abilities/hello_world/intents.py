from pyttman.core.containers import Reply, ReplyStream, Message
from pyttman.core.intent import Intent


# Created by Pyttman

class PrintHelloWorld(Intent):
    lead = ('Hello', 'Hi')

    def respond(self, message: Message) -> Reply | ReplyStream:
        return Reply(f'Hello World')
