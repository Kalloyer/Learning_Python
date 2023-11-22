# Faça um programa de python que abre e reproduza um arquivo de audio mp3
import pygame
pygame.init()
pygame.mixer.music.load('Connor Price & bbno$ - Not A Beanie.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()