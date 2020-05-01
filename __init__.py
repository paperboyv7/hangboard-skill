from mycroft import MycroftSkill, intent_file_handler


class hangboard(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hangboard.intent')
    def handle_hangboard(self, message):
        try:
            number = int(message.data.get("number"))
            response = {'number': message.data.get("number")}
            self.speak_dialog("hangboard_start", data=response)
            for i in range(number, 0, -1):
                self.speak("hang" + " .")
            for i in range(number, 0, -1):
                self.speak("rest" + " .")
            self.speak_dialog("hangboard_stop")
            pass
        except:
            self.speak_dialog("hangboard_error")

def create_skill():
    return hangboard()

