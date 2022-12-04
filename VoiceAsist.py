



from selenium import webdriver
import time
import speech_recognition as sr
import os
from os import system as komut
from selenium.webdriver.common.keys import Keys
from win32api import GetKeyState


buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoçprsştuüvyz"
def lower(text:str):
    newText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)            
            newText += kucukAlfabe(index)          
            
            
        else:
            newText +=i
    return newText


def Tıklama(tus):
    state = GetKeyState(tus)
    if (state !=0) and (state !=1):        
        return True



while True:
    

    if Tıklama(0x2C) == True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            komut("cls")
            r.adjust_for_ambient_noise(source=source)             
            audio = r.listen(source)


        try:
            text = r.recognize_google(audio,language = "tr")
            text = lower(text)
            if "müzik uygulamasını aç" in text:
                                          
               os.startfile('Spotify')                                    
               
            elif "sosyal medya" in text:
                
                os.startfile('instagram.py')

            
                
                
            elif "film listesi" in text:
                
                os.startfile('FİLM LİSTESİ.docx')


            elif  "google'da ara" in text :
                time.sleep(1)
                
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source=source)
                    audio2 = r.listen(source)
                    searchInput = r.recognize_google(audio2,language = "tr")
                    browser = webdriver.Chrome()
                    browser.get("https://www.google.com/")
                    search = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
                    search.click()
                    search.send_keys(searchInput,Keys.ENTER)

            elif "bilgisayarı kapalı konuma getir" in text:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source=source)
		
		
                    audio3 = r.listen(source)
                    veri = r.recognize_google(audio3,language = "tr")
                    time = veri.replace("saniye sonra","")

                command = "shutdown -s -f -t"
                gap = " "
                shutdown = command + gap + time
                os.system(shutdown)

            elif "bilgisayarı kapatma" in text:
                

                os.system('shutdown -a')
                
                
                

                
                
            else:
                print("Söylediğinizi \" ", text, "\" olarak algıladım ve maalesef ki söylediğinle ilgili bir fonksiyonum yok .... :( ")
                
                




            
        except sr.UnknownValueError:
            print("Herhangi bir konuşma tanımlayamadım, tekrar deneyiniz...")
        except sr.RequestError as e:
            print("Şu anda GOOGLE sunucuları ile bağlantı kurulamadı, daha sonra tekrar deneyiniz...; {0}".format(e))
        time.sleep(15)

    else:
        pass
