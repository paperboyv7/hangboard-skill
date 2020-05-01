from mycroft import MycroftSkill, intent_file_handler
import time

class hangboard(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hangboard.intent')
    def handle_hangboard(self, message):
        try:
            number = int(message.data.get("number"))
            response = {'number': message.data.get("number")}
            self.speak_dialog("hangboard_start", data=response)
            for j in range(1, number+1, +1):
                repno = str(j)
                self.speak_dialog("hangboard_repstart", data={"repno": repno})
#                self.speak(str(j) + " .")
                for i in range(number, 0, -1):
                    self.speak("hang" + " .")
                    time.sleep(1)
                if j < number:
                    self.speak_dialog("hangboard_rest", data=response)
                    for i in range(number, 0, -1):
                        time.sleep(1)
                        #self.speak("rest" + " .")
                    self.speak_dialog("hangboard_restend", data=response)
            self.speak_dialog("hangboard_finish", data=response)
            pass
        except:
            self.speak_dialog("hangboard_error")

def create_skill():
    return hangboard()

