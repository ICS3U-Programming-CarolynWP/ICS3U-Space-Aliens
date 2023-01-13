# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2023/1/10
# The Lizard Leap Game


import constants

# Importing ugame and stage to be able to
# create the game
import stage
import ugame


def menu_scene():
    # Allowing the background image to be accessed
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Menu Scene text
    # Text variable
    text = []
    # Colour, font, etc
    text1 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Moving the text
    text1.move(5, 20)
    text1.text("Pine Tree Studiospresents:")
    text.append(text1)
    text2 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Moving the text
    text2.move(5, 40)
    text2.text("Lizard Leap")
    text.append(text2)

    text3 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(5, 100)
    text3.text("Press START to         begin!")
    text.append(text3)

    # Background grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # Displaying and rendering the background which updates at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Background with text
    game.layers = text + [background]
    # Renders everything on the screen
    game.render_block()

    while True:
        # if someone presses the start button, start the game_scene
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START:
            game_scene()


# The game scene (main game)
def game_scene():
    # Allowing the background image to be accessed
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Allowing the sprite image to be accessed
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # Copying the image multiple times to make a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # Adding the lizard and placing it at point (5, 66)
    lizard = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_SIZE_Y - (2 * constants.SPRITE_SIZE)
    )

    # Adding the raptor sprite
    raptor = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_SIZE_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # Displaying and rendering the background which updates at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Layers on the screen
    game.layers = [lizard] + [raptor] + [background]
    # Renders everything on the screen
    game.render_block()

    # Buttons you do not want to repeat 60fps
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Adding in the pew sound effect
    pew_sound = open("lizard.wav", "rb")
    sound = ugame.audio
    # Stop sound from happening in case something happens
    sound.stop()
    sound.mute(False)

    # Everything is happening 60 times a second
    while True:
        # All the buttons for the game
        keys = ugame.buttons.get_pressed()

        # A button; line of code to make sure nothing happens until
        # The button was pressed then released.
        if keys & ugame.K_X:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button
        if keys & ugame.K_O:
            pass
        # Start button
        if keys & ugame.K_START:
            pass
        # Select button
        if keys & ugame.K_SELECT:
            pass
        # Movement buttons
        if keys & ugame.K_RIGHT:
            # If the lizard goes off the screen
            if lizard.x <= constants.SCREEN_SIZE_X - constants.SPRITE_SIZE:
                lizard.move(lizard.x + constants.SPRITE_MOVEMENT_SPEED, lizard.y)
            else:
                lizard.move(0, lizard.y)
        if keys & ugame.K_LEFT:
            # If the lizard goes off the screen
            if lizard.x >= 0:
                lizard.move(lizard.x - constants.SPRITE_MOVEMENT_SPEED, lizard.y)
            else:
                lizard.move(constants.SCREEN_SIZE_X, lizard.y)
        # Up and down will not be used
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # Once the A button is button_just_pressed, play the sound.
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # To render and redraw the lizard sprites
        game.render_sprites([lizard] + [raptor])
        game.tick()


if __name__ == "__main__":
    menu_scene()
