import pyttsx3


class KaiVoice:
  def __init__(self):
    self.__engine = pyttsx3.init()

    voices = self.__engine.getProperty('voice')
    print(voices)
    # self.__engine.setProperty('voice', voices[1].id)

  def speak(self, speache):
    self.__engine.say(speache)
    self.__engine.runAndWait()
