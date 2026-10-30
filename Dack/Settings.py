import pygame
from os import walk
from os.path import join
from pytmx.util_pygame import load_pygame

def load_settings():
    try:
        with open('settings.txt', 'r') as f:
            settings = f.read().splitlines()
            width = int(settings[0]) if len(settings) > 0 else 1280
            height = int(settings[1]) if len(settings) > 1 else 720
            volume = float(settings[2]) if len(settings) > 2 else 0.5
            return width, height, volume
    except FileNotFoundError:
        return 1280, 720, 0.5 

def save_settings(width, height, volume):
    with open('settings.txt', 'w') as f:
        f.write(f"{width}\n{height}\n{volume}")

WW, WH, VOLUME = load_settings()
SIZE = 64
FPS = 60
BG = '#393939'
BULLET_BUFFER = 1000