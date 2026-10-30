import pygame
from Settings import WW, WH, BG, save_settings, VOLUME
from support import audio_importer

class Menu:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WW, WH))
        pygame.display.set_caption('Duck Dack SM - Menu')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, int(WH * 0.1))
        self.small_font = pygame.font.Font(None, int(WH * 0.06))
        self.running = True
        self.state = 'menu'
        self.current_screen = 'main'
        self.volume = VOLUME  

        
        try:
            self.audio = audio_importer('audio')
            self.audio['click'].set_volume(self.volume)
        except FileNotFoundError:
            self.audio = {'click': None}

       
        button_width, button_height = 200, 60
        button_spacing = 12
        start_y = WH//2 - (2 * button_height + 0.15 * button_spacing) + 50
        self.main_buttons = [
            {'text': 'Start', 'rect': pygame.Rect(WW//2 - button_width//2, start_y, button_width, button_height), 'action': 'start'},
            {'text': 'Settings', 'rect': pygame.Rect(WW//2 - button_width//2, start_y + button_height + button_spacing, button_width, button_height), 'action': 'settings'},
            {'text': 'Score', 'rect': pygame.Rect(WW//2 - button_width//2, start_y + 2 * (button_height + button_spacing), button_width, button_height), 'action': 'score'},
            {'text': 'Exit', 'rect': pygame.Rect(WW//2 - button_width//2, start_y + 3 * (button_height + button_spacing), button_width, button_height), 'action': 'exit'}
        ]

        
        settings_start_y = WH//2 - (2.5 * button_height + 2 * button_spacing)
        self.settings_buttons = [
            {'text': '1280x720', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y, button_width, button_height), 'action': (1280, 720)},
            {'text': '800x600', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y + button_height + button_spacing, button_width, button_height), 'action': (800, 600)},
            {'text': '1920x1080', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y + 2 * (button_height + button_spacing), button_width, button_height), 'action': (1920, 1080)},
            {'text': 'Volume Up', 'rect': pygame.Rect(WW//2 - button_width//2 - 110, settings_start_y + 3 * (button_height + button_spacing), button_width, button_height), 'action': 'volume_up'},
            {'text': 'Volume Down', 'rect': pygame.Rect(WW//2 - button_width//2 + 110, settings_start_y + 3 * (button_height + button_spacing), button_width, button_height), 'action': 'volume_down'},
            {'text': 'Back', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y + 4 * (button_height + button_spacing), button_width, button_height), 'action': 'back'}
        ]

       
        self.score_buttons = [
            {'text': 'Back', 'rect': pygame.Rect(WW//2 - button_width//2, WH//2 + 150, button_width, button_height), 'action': 'back'}
        ]

       
        try:
            with open('highest_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0

    def draw(self):
        self.display_surface.fill(BG)
        if self.current_screen == 'main':
            title_text = self.font.render('Duck Dack SM', True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(WW//2, WH//8))
            self.display_surface.blit(title_text, title_rect)

            high_score_text = self.small_font.render(f'Highest Score: {self.high_score}', True, (255, 255, 255))
            high_score_rect = high_score_text.get_rect(center=(WW//2, WH//8 + 60))
            self.display_surface.blit(high_score_text, high_score_rect)

            for button in self.main_buttons:
                color = (150, 150, 150) if button['rect'].collidepoint(pygame.mouse.get_pos()) else (100, 100, 100)
                pygame.draw.rect(self.display_surface, color, button['rect'])
                text = self.small_font.render(button['text'], True, (255, 255, 255))
                text_rect = text.get_rect(center=button['rect'].center)
                self.display_surface.blit(text, text_rect)
        elif self.current_screen == 'settings':
            settings_text = self.font.render('Settings', True, (255, 255, 255))
            settings_rect = settings_text.get_rect(center=(WW//2, WH//8))
            self.display_surface.blit(settings_text, settings_rect)

            current_size_text = self.small_font.render(f'Current: {WW}x{WH}', True, (255, 255, 255))
            current_size_rect = current_size_text.get_rect(center=(WW//2, WH//8 + 60))
            self.display_surface.blit(current_size_text, current_size_rect)

            volume_text = self.small_font.render(f'Volume: {int(self.volume * 100)}%', True, (255, 255, 255))
            volume_rect = volume_text.get_rect(center=(WW//2, WH//8 + 120))
            self.display_surface.blit(volume_text, volume_rect)

            for button in self.settings_buttons:
                color = (150, 150, 150) if button['rect'].collidepoint(pygame.mouse.get_pos()) else (100, 100, 100)
                pygame.draw.rect(self.display_surface, color, button['rect'])
                text = self.small_font.render(button['text'], True, (255, 255, 255))
                text_rect = text.get_rect(center=button['rect'].center)
                self.display_surface.blit(text, text_rect)
        else:
            score_text = self.font.render('Highest Score', True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(WW//2, WH//8))
            self.display_surface.blit(score_text, score_rect)

            high_score_text = self.small_font.render(f'Score: {self.high_score}', True, (255, 255, 255))
            high_score_rect = high_score_text.get_rect(center=(WW//2, WH//2))
            self.display_surface.blit(high_score_text, high_score_rect)

            for button in self.score_buttons:
                color = (150, 150, 150) if button['rect'].collidepoint(pygame.mouse.get_pos()) else (100, 100, 100)
                pygame.draw.rect(self.display_surface, color, button['rect'])
                text = self.small_font.render(button['text'], True, (255, 255, 255))
                text_rect = text.get_rect(center=button['rect'].center)
                self.display_surface.blit(text, text_rect)

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = 'exit'
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.current_screen == 'main':
                    for button in self.main_buttons:
                        if button['rect'].collidepoint(event.pos):
                            if self.audio['click']:
                                self.audio['click'].play()
                            if button['action'] == 'settings':
                                self.current_screen = 'settings'
                            elif button['action'] == 'score':
                                self.current_screen = 'score'
                            else:
                                self.state = button['action']
                                self.running = False
                elif self.current_screen == 'settings':
                    for button in self.settings_buttons:
                        if button['rect'].collidepoint(event.pos):
                            if self.audio['click']:
                                self.audio['click'].play()
                            if button['action'] == 'back':
                                self.current_screen = 'main'
                            elif button['action'] == 'volume_up':
                                self.volume = min(1.0, self.volume + 0.1)
                                if self.audio['click']:
                                    self.audio['click'].set_volume(self.volume)
                            elif button['action'] == 'volume_down':
                                self.volume = max(0.0, self.volume - 0.1)
                                if self.audio['click']:
                                    self.audio['click'].set_volume(self.volume)
                            else:
                                global WW, WH
                                WW, WH = button['action']
                                save_settings(WW, WH, self.volume)
                                self.display_surface = pygame.display.set_mode((WW, WH))
                                button_width, button_height = 200, 60
                                button_spacing = 80
                                start_y = WH//2 - (2 * button_height + 1.5 * button_spacing) + 50
                                settings_start_y = WH//2 - (2.5 * button_height + 2 * button_spacing)
                                self.main_buttons = [
                                    {'text': 'Start', 'rect': pygame.Rect(WW//2 - button_width//2, start_y, button_width, button_height), 'action': 'start'},
                                    {'text': 'Settings', 'rect': pygame.Rect(WW//2 - button_width//2, start_y + button_height + button_spacing, button_width, button_height), 'action': 'settings'},
                                    {'text': 'Score', 'rect': pygame.Rect(WW//2 - button_width//2, start_y + 2 * (button_height + button_spacing), button_width, button_height), 'action': 'score'},
                                    {'text': 'Exit', 'rect': pygame.Rect(WW//2 - button_width//2, start_y + 3 * (button_height + button_spacing), button_width, button_height), 'action': 'exit'}
                                ]
                                self.settings_buttons = [
                                    {'text': '1280x720', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y, button_width, button_height), 'action': (1280, 720)},
                                    {'text': '800x600', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y + button_height + button_spacing, button_width, button_height), 'action': (800, 600)},
                                    {'text': '1920x1080', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y + 2 * (button_height + button_spacing), button_width, button_height), 'action': (1920, 1080)},
                                    {'text': 'Volume Up', 'rect': pygame.Rect(WW//2 - button_width//2 - 110, settings_start_y + 3 * (button_height + button_spacing), button_width, button_height), 'action': 'volume_up'},
                                    {'text': 'Volume Down', 'rect': pygame.Rect(WW//2 - button_width//2 + 110, settings_start_y + 3 * (button_height + button_spacing), button_width, button_height), 'action': 'volume_down'},
                                    {'text': 'Back', 'rect': pygame.Rect(WW//2 - button_width//2, settings_start_y + 4 * (button_height + button_spacing), button_width, button_height), 'action': 'back'}
                                ]
                                self.score_buttons = [
                                    {'text': 'Back', 'rect': pygame.Rect(WW//2 - button_width//2, WH//2 + 150, button_width, button_height), 'action': 'back'}
                                ]
                                self.font = pygame.font.Font(None, int(WH * 0.1))
                                self.small_font = pygame.font.Font(None, int(WH * 0.06))
                else:
                    for button in self.score_buttons:
                        if button['rect'].collidepoint(event.pos):
                            if self.audio['click']:
                                self.audio['click'].play()
                            if button['action'] == 'back':
                                self.current_screen = 'main'

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        return self.state, WW, WH, self.volume

if __name__ == '__main__':
    menu = Menu()
    state, width, height, volume = menu.run()
    print(f"Menu state: {state}, Screen size: {width}x{height}, Volume: {volume}")