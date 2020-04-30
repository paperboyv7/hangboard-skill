from mycroft import MycroftSkill, intent_file_handler


class Hangboard(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hangboard.intent')
    def handle_hangboard(self, message):
        self.speak_dialog('hangboard')


def create_skill():
    return Hangboard()

