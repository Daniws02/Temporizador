import pygame

def tocar_som(arquivo_som):
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo_som)
    pygame.mixer.music.play()

# Exemplo de uso
tocar_som("./Som.wav")