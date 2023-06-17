import pyttsx3


class KaiVoice:
  def __init__(self):
    self.__engine = pyttsx3.init()
    self.__voice = pyttsx3.voice.Voice()

    self.__initSettings()

  def __initSettings(self):
    voice1, voice2 = self.__engine.getProperty('voices')
    self.__engine.setProperty('voice', voice2.id)
    self.__engine.setProperty('rate', 130)

    print(self.__voice.age)

  def speak(self, speache: str) -> None:
    if self.isBusy():
      self.__engine.say(speache)
      self.__engine.runAndWait()

  def isBusy(self) -> bool:
    return self.__engine.isBusy()
