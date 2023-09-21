from googletrans import Translator
from playsound import playsound
from gtts import gTTS
import os
from pytube import YouTube
import pywhatkit
import speech_recognition as sr
import pyjokes
import wikipedia
import datetime

def lan_eng(task):
    translator = Translator()
    translation = translator.translate(task, dest='en')
    task=translation.text
    return task
    
def trans(txt):    
    translator = Translator()
    translation = translator.translate(txt, dest=lan)
    x=translation.text
    speak = gTTS(text=x, lang=lan, slow=False)
    speak.save("captured_voice.mp3")
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')


def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        
        #audio=r.adjust_for_ambient_noise(source)
        audio=r.listen(source,phrase_time_limit=7)
        try:
           text=r.recognize_google(audio,language=lan)
           print("USER :",text)
        except: 
            trans("Sorry you are not audible..try again")
            text=listen()
    return text        
           #tell("Sorry you are not audible..try again")
           #listen()



def run(task):
    print("In English : ",task)
    task=task.upper()
    
    if 'PLAY' in task:
        pywhatkit.playonyt(task)  
   
    elif 'GOOGLE' in task:
        task=task.replace('SEARCH','')
        task=task.replace('ON GOOGLE','')
        trans("Searching on google")
        pywhatkit.search(task)
  
    elif 'YOUTUBE' in task:
        task=task.replace('SEARCH','')
        task=task.replace('ON YOUTUBE','')
        trans("Searching on Youtube")
        pywhatkit.playonyt(task)
          
   
    elif 'JOKE' in task:
        trans(pyjokes.get_joke())   
     
    elif "TRANSLATE" in task:
        trans("In which language you want to translate")
        sea=listen()
        sea=lan_eng(sea)
        for key,value in LANGUAGES.items():
            if(value.capitalize()==lan):
                sea=key
                break  
        trans("Say the line or  the word") 
        txt=listen()
        txt=lan_eng(txt)   
        translator = Translator()
        translation = translator.translate(txt, dest=sea)
        x=translation.text
        print('Translated word/line: ',x)
        speak = gTTS(text=x, lang=lan, slow=False)
        speak.save("captured_voice.mp3")
        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')

    elif "TIME" in task and "NOW" in task:
        current_time = datetime.datetime.now()
        trans("Right now it is "+str(current_time.hour)+"Hour"+str(current_time.minute)+"minute")
    #DateTime
    elif "DATE" in task:
        current_time = datetime.datetime.now()
        trans("today's date is"+str(current_time.date()))

    else:
        try:
            x=wikipedia.summary(task,sentences=2) 
            trans(x)  
        except:
            trans("There is no such topic in wikipedia")     

    trans("Sir do you need any other help") 
    print("================================================================================================")
    te=listen()
    te=lan_eng(te)
    te=te.upper()
    if "YES" in te:
        trans("waiting for your command")
           
        task=listen()
        task=lan_eng(task)
        run(task)
    else:
        trans("goodbye")


LANGUAGES = {
    'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian','az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bangla','bs': 'bosnian','bg': 'bulgarian','ca': 'catalan',
    'ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)','zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish','nl': 'dutch','en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'}

lan='en'
print("-----------------------------------------Welcome--------------------------------------------------------------")
trans("Hello Sir.I am your search assistant..I am here to help you..Choose Your language ")

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    
    audio=r.listen(source,phrase_time_limit=3)
    try:
        text=r.recognize_google(audio)
        lan=text
        
    except:
        trans("Sorry you are not audible.try again")
        trans("I am setting the language as English")

    for key,value in LANGUAGES.items():
        if(value.capitalize()==lan):
            lan=key
            break    
     
trans("Waiting for your command")

command=listen() 
command=lan_eng(command) 

run(command)



     
