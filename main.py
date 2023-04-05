import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Liste de couleurs prédéfinies de la librairie Arcade
COLORS = [arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW, arcade.color.GREEN, arcade.color.BLUE, arcade.color.PURPLE, arcade.color.PINK]


class Balle:
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    def update(self):
        # Mise à jour de la position de la balle
        self.x += self.change_x
        self.y += self.change_y

        # Vérification pour éviter que la balle ne sorte de l'écran
        if self.x < self.rayon:
            self.x = self.rayon
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1
        if self.y < self.rayon:
            self.y = self.rayon
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1

    def draw(self):
        # Dessin de la balle à l'écran
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle:
    def __init__(self, x, y, change_x, change_y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle

    def update(self):
        # Mise à jour de la position du rectangle
        self.x += self.change_x
        self.y += self.change_y

        # Vérification pour éviter que le rectangle ne sorte de l'écran
        if self.x < 0:
            self.x = 0
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.change_x *= -1
        if self.y < 0:
            self.y = 0
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.change_y *= -1

    def draw(self):
        # Dessin du rectangle à l'écran
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_balles = []
        self.liste_rectangles = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

