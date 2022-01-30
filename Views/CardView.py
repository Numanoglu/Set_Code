import pygame
from consts import *

# https://github.com/russs123/pygame_tutorials/blob/main/Button/button.py
class CardView:
    def __init__(self, gv, card, x, y, image, scale):
        self.card = card
        self.gv = gv
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.selected = False        
        self.font = pygame.font.Font("assets/DejaVuSans.ttf", 50)

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.clicked = not self.clicked
            if pygame.mouse.get_pressed()[0]:
                # if there are 3 selected cards, only allow deselecting
                if self.gv.less_than_max_cards_selected() or self.selected:
                    self.image = self.inverted(self.image, INV_COLOR)
                    self.selected = not self.selected
                    action = True

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        text = self.font.render(self.card.pretty_print(), 0, self.card.get_color())
        surface.blit(text, (self.rect.x + self.get_padding(), self.rect.y + 18))

        return action

    def inverted(self, img, color):
        inv = pygame.Surface(img.get_rect().size, pygame.SRCALPHA)
        inv.fill(color)
        inv.blit(img, (0,0), None, pygame.BLEND_RGB_SUB)
        return inv

    def get_padding(self):
        return 25 * (3 - int(self.card.quantity)) + 40