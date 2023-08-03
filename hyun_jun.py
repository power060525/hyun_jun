import pyttsx3


#한글 TTS 엔진을 설정하자!!
engine = pyttsx3.init()
engine.setProperty(name='rate',value=150) #말하는속도??
# 텍스트를 읽어주는 함수를 정의하자!!
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 텍스트를 입력받아 TTS로 변환합니다
text = "이루현 바보"
speak(text)
