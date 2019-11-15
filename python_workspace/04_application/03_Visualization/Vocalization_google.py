from gtts import gTTS

default_str="""안녕하세요. 홍길동입니다. 스마트홈 네트워크를 구동시키겠씁니다."""

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("test.mp3")

    open("test.mp3")

speaker(default_str)
