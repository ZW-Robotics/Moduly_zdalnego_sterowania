import speech_recognition as sr
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.OUT)

while True:

    r = sr.Recognizer()
    with sr.Microphone() as źródło_dźwięku:
        r.adjust_for_ambient_noise(źródło_dźwięku)
        try:
            print("Wydaj polecenie")
            wypowiedziane_słowo = r.listen(źródło_dźwięku)
            print("Przetwarzam ...")
            print("Polecenie: \n" + r.recognize_google(wypowiedziane_słowo, language="pl-PL"))
        except sr.UnknownValueError:
            print("Nie rozpoznałem polecenia")
            continue

    polecenie = r.recognize_google(wypowiedziane_słowo, language="pl-PL")
        
    if polecenie == "Włącz lampę":
        GPIO.output(14, GPIO.LOW)
                        
    if polecenie == "Wyłącz lampę":
        GPIO.output(14, GPIO.HIGH)
   
    polecenie = ""















