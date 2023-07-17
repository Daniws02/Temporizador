import pygame
import datetime
import time

def som():    
    # Inicializar o mixer de áudio do pygame
    pygame.mixer.init()

    # Carregar o arquivo de som desejado
    sound_file = "./Som.wav"
    pygame.mixer.music.load(sound_file)

    # Tocar o som uma vez
    pygame.mixer.music.play()

        # Aguardar até que o som termine de tocar
    while pygame.mixer.music.get_busy():
        pass

while True:
    agora = datetime.datetime.now()
    horas = agora.hour
    minutos = agora.minute
    segundos = agora.second
    
    shoras = str(horas)
    sminutos = str(minutos)
    ssegundos = str(segundos)
    
    #print(minutos)

    if(minutos%2==0):
        if(segundos == 0):
            print("foi")
            som()
        else:
            pass
    else:
        pass
    
    time.sleep(1)