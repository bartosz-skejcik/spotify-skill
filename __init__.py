from mycroft import MycroftSkill, intent_file_handler


class Spotify(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spotify.intent')
    def handle_spotify(self, message):
        song = message.data.get('song')

        self.speak_dialog('spotify', data={
            'song': song
        })


def create_skill():
    return Spotify()

