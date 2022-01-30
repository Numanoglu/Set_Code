import pygame
from GameController import GameController
from consts import *
from Views.CardView import CardView
from Views.Button import Button
from util import get_pos

gc = GameController


# Source https://stackoverflow.com/questions/65059267/how-do-i-implement-option-buttons-and-change-the-button-color
# -in-pygame
# Source https://stackoverflow.com/questions/49345616/highlighting-buttons-in-pygame
# Source https://stackoverflow.com/questions/47639826/pygame-button-single-click
# https://github.com/russs123/pygame_tutorials
class GameView:
    def __init__(self, gc: GameController):
        self.gc = gc
        self.card_slots = []
        self.buttons = []
        self.info_text = "Let's go"
        self.skip_button_text = "Skip >>"
        pygame.init()

        # Window options
        pygame.display.set_caption('Set of 3 | Set Game')
        window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background.fill(pygame.Color('#000000'))

        self.generate_card_views()

        clock = pygame.time.Clock()
        is_running = True

        # Draw once
        window_surface.blit(background, (0, 0))
        self.generate_buttons()
        # button_img = pygame.image.load('assets/btn.png').convert_alpha()
        # self.buttons.append(Button(self, self.gc.cards_in_play[0], 10, 410, button_img, 0.8))

        while is_running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    is_running = False

                window_surface.blit(background, (0, 0))
                # Button handling
                for b in self.buttons:
                    if b.draw(window_surface):
                        if b.selected:
                            self.buttons = []
                            if len(gc.deck) == 0:
                                self.skip_button_text = 'Final cards'
                            self.generate_buttons()

                # CardView handling
                for c in self.card_slots:
                    if c.draw(window_surface):
                        if c.selected:
                            selected_cards = [s.card for s in self.card_slots if s.selected]
                            if len(selected_cards) == 3:
                                if gc.remove_set(selected_cards):
                                    self.card_slots = []
                                    self.generate_card_views()

                                    # refresh buttons to show the info
                                    self.info_text = 'Its a SET!'
                                    # Take out, use inline for loop (list comprehension)
                                    for card_slot in self.card_slots:
                                        card_slot.selected = False
                                        card_slot.clicked = False
                                else:
                                    # refresh buttons to show the info
                                    self.info_text = 'No SET!'

                                if len(gc.deck) == 0:
                                    self.info_text = 'Final cards'
                                self.generate_buttons()

            pygame.display.update()
        pygame.quit()

    # Button options
    def generate_buttons(self):
        skip = self.skip_and_redraw
        button_img = pygame.image.load('assets/btn.png').convert_alpha()
        info_button = Button(self, self.info_text, PADDING, 350, button_img, 450, None)
        skip_button = Button(self, self.skip_button_text, PADDING * 3 + 350, 350, button_img, 450, skip)
        self.buttons.append(info_button)
        self.buttons.append(skip_button)

    def generate_card_views(self):
        img = pygame.image.load('assets/btn.png').convert_alpha()
        for i, card in enumerate(self.gc.cards_in_play):
            pos_x, pos_y = get_pos(i)
            self.card_slots.append(
                CardView(self, card, PADDING + pos_x * CARD_WIDTH, PADDING + pos_y * CARD_HEIGHT, img, 0.8))

    def less_than_max_cards_selected(self):
        return len([s.card for s in self.card_slots if s.selected]) < SET_SIZE

    def skip_and_redraw(self):
        self.gc.skip()
        self.card_slots = []
        self.generate_card_views()
        self.info_text = 'Cheater'
        self.generate_buttons()
