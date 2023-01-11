# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2023/1/10
# The Lizard Leap Game


# Importing ugame and stage to be able to
# create the game
import stage
import ugame


def game_scene():
    # Allowing the background image to be accessed
    image_bank_background = stage.Bank.from_bmp16("lizard_background.bmp")
    # Allowing the sprite image to be accessed
    image_bank_sprites = stage.Bank.from_bmp16("lizard.bmp")
    # Copying the image multiple times to make a grid
    background = stage.Grid(image_bank_background, 10, 8)
    # Adding the lizard and placing it at point ()5, 66)
    lizard = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Displaying and rendering the background which updates at 60fps
    game = stage.Stage(ugame.display, 60)
    # Layers on the screen
    game.layers = [lizard] + [background]
    # Renders everything on the screen
    game.render_block()

    # Will be used later
    while True:

        # To render and redraw the sprites
        game.render_sprites([lizard])
        game.tick()


if __name__ == "__main__":
    game_scene()
