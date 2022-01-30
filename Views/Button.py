import pygame
from consts import *


def inverted(img, color):
    inv = pygame.Surface(img.get_rect().size, pygame.SRCALPHA)
    inv.fill(color)
    inv.blit(img, (0, 0), None, pygame.BLEND_RGB_SUB)
    return inv


class Button:
    def __init__(self, gv, text, x, y, image, width, func=None):
        scale = 0.8
        self.gv = gv
        height = image.get_height()
        self.text = text
        self.func = func
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.selected = False
        self.font = pygame.font.Font("assets/DejaVuSans.ttf", 50)

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.clicked = not self.clicked
            if pygame.mouse.get_pressed()[0] and self.func:
                self.func()
                self.image = inverted(self.image, INV_COLOR)
                self.selected = not self.selected
                action = True

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        text = self.font.render(self.text, False, WHITE)
        surface.blit(text, (self.rect.x + BUTTON_PADDING, self.rect.y + 18))

        return action
