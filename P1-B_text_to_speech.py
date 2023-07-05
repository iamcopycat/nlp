# pip install gtts
# pip install playsound 
from playsound import playsound
# import required for text to speech conversion 
from gtts import gTTS
mytext = "Hello!! i am sneha kadam"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("myfile.mp3")
playsound("myfile.mp3") 
