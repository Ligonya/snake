"""
    Fichier regroupant toutes les variables utilisées par le jeu.

    Pour modifier la vitesse du serpent, il faut diminuer ou augmenter
    la distance_travelled et / ou le refresh_rate.
"""

title = 'Snake'
version = '1.0.0'

width = 384
height = 384
dimensions = (width, height)
snake_width = 12
snake_height = 12
fruit_width = snake_width * 1.5
fruit_height = snake_height * 1.5

background_color = (30, 41, 59)
snake_color = (22, 163, 74)
fruit_color = (225, 29, 72)

# La fenêtre est redessinée toutes les 40 ms.
refresh_rate = .04
distance_travelled = snake_width * 0.5
