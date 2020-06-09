from mycroft import MycroftSkill, intent_file_handler


class Estadollu(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('estadollu.intent')
    def handle_estadollu(self, message):
        self.speak_dialog('estadollu')


def create_skill():
    return Estadollu()

