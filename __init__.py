from mycroft import MycroftSkill, intent_file_handler
import time

class hangboard(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hangboard.intent')
    def handle_hangboard(self, message):
        try:
            hang = int(message.data.get("hang"))
            response = {'hang': message.data.get("hang")}
            reps = int(message.data.get("reps"))
            repsresponse = {'reps': message.data.get("reps")}
            rest = int(message.data.get("rest"))
            restresponse = {'rest': message.data.get("rest")}
            self.speak_dialog("hangboard_restend")
            for j in range(1, reps+1, +1):
                repno = str(j)
                self.speak_dialog("hangboard_repstart", data={"repno": repno})
                for i in range(hang, 0, -1):
                    self.speak(str(i) + " .")
                    time.sleep(1)
                if j < reps:
                    self.speak_dialog("hangboard_rest", data=restresponse)
                    for i in range(rest, 0, -1):
                        time.sleep(1)
                    self.speak_dialog("hangboard_restend")
            self.speak_dialog("hangboard_finish")
            pass
        except:
            self.speak_dialog("hangboard_error")

def create_skill():
    return hangboard()

