# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2023/1/10
# The Lizard Leap Game


import random
import time

import constants

# Importing ugame and stage to be able to
# create the game
import stage
import ugame
import supervisor


# The splash scene function
def splash_scene():

    # Getting the sound ready to play
    splash_sound = open("splash_scene.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Playing the sound effect
    sound.play(splash_sound)

    # Allowing the background image to be accessed
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Background grid
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Puts the mt_game_studio image back together, since it is split up into tiles
    # First number is x coordinate, second is y, third is image index
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white
    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white
    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white
    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # Displaying and rendering the background which updates at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Background with text
    game.layers = [background]
    # Renders everything on the screen
    game.render_block()

    while True:
        # Wait for 2 seconds then switch to the menu scene
        time.sleep(2.0)
        menu_scene()


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
    text1.text("Happy Tree Games presents:")
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

    # Initializing the score
    score = 0

    # Text dimensions, colour, etc
    score_text = stage.Text(width=29, height=14, palette=constants.RED_PALETTE)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score = {0}".format(score))

    # Takes an alien from offscreen and moves to the screen
    def show_raptor():
        for raptor_number in range(len(raptors)):
            if raptors[raptor_number].x < 0:
                raptors[raptor_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_SIZE_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # Allowing the background image to be accessed
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Allowing the sprite image to be accessed
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # Copying the image multiple times to make a grid
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # To randomize the tiles
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            # Choose a random tile and place a random image
            tile_picked = random.randint(0, 3)
            background.tile(x_location, y_location, tile_picked)

    # Adding the lizard and placing it at point (5, 66)
    lizard = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_SIZE_Y - (2 * constants.SPRITE_SIZE)
    )

    # Adding the raptors to the game, stored in a list.
    raptors = []
    for raptor_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_raptor = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        raptors.append(a_single_raptor)
    # Display 1 raptor on the screen
    show_raptor()
    # Adding the lasers to the game; they are stored in a list
    # 5 at a time
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # Displaying and rendering the background which updates at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Layers on the screen
    game.layers = [score_text] + raptors + lasers + [lizard] + [background]
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

    # Adding in the screech sound effect
    screech = open("raptor.wav", "rb")
    sound = ugame.audio
    # Stop sound from happening in case something happens
    sound.stop()
    sound.mute(False)

    # Adding in the crash sound effect
    screech = open("crash.wav", "rb")
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
            # Fire a laser if we have not used up all lasers
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(lizard.x, lizard.y)
                    # Play the laser sound
                    sound.play(pew_sound)
                    break
        # Checks each laser to see if it is on the screen.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                # If the laser is on the screen, move it up the screen
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                # If the laser if off the screen, move it back to the holding area
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # Checks each raptor to see if it is on the screen.
        for raptor_number in range(len(raptors)):
            if raptors[raptor_number].x > 0:
                # If the raptor is on the screen, move it down the screen
                raptors[raptor_number].move(
                    raptors[raptor_number].x,
                    raptors[raptor_number].y + constants.ALIEN_SPEED,
                )
                # If the raptor if off the screen, move it back to the holding area
                if raptors[raptor_number].y > constants.SCREEN_SIZE_Y:
                    raptors[raptor_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_raptor()
                    # Take away 1 from the score
                    score -= 1
                    # To make sure there are no negative scores
                    if score < 0:
                        score = 0
                    # Reprinting the text
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score = {0}".format(score))

        # Determining the collision detection.
        # Putting in the coordinates for the laser and alien to
        # determine whether they are colliding.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for raptor_number in range(len(raptors)):
                    if raptors[raptor_number].x > 0:
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 12,
                            lasers[laser_number].y + 1,
                            raptors[raptor_number].x + 1,
                            raptors[raptor_number].y,
                            raptors[raptor_number].x + 16,
                            raptors[raptor_number].y + 16,
                        ):
                            # If you hit an alien, remove both objects from the screen
                            raptors[raptor_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()
                            sound.play(screech)
                            # show two more aliens
                            show_raptor()
                            show_raptor()
                            # Update the score
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score = {0}".format(score))

        # If the alien hits the ship
        for raptor_number in range(len(raptors)):
            if raptors[raptor_number].x > 0:
                if stage.collide(
                    raptors[raptor_number].x + 1,
                    raptors[raptor_number].y + 2,
                    raptors[raptor_number].x + 16,
                    raptors[raptor_number].y + 16,
                    lizard.x,
                    lizard.y,
                    lizard.x + 16,
                    lizard.y + 16,
                ):
                    sound.stop()
                    sound.play(crash)
                    time.sleep(3.0)
                    # Switches to the game over scene
                    game_over_scene(score)

        # If you score 50 points
        if score == 50:
            sound.stop()
            time.sleep(3.0)
            game_win_scene()

        # To render and redraw the sprites
        game.render_sprites(lasers + raptors + [lizard])
        # Wait until the refresh rate is done
        game.tick()


def game_over_scene(final_score):
    # To turn off the sound
    sound = ugame.audio
    sound.stop()

    # Image banks
    image_bank_2 = stage.Bank.from_pmb16("mt_game_studio.bmp")

    # Set the background to the image at index 0
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Game over text
    text = []
    text1 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Moving the text
    text1.move(5, 20)
    text1.text("GAME OVER!")
    text.append(text1)
    text2 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Moving the text
    text2.move(5, 40)
    text2.text("Final Score: {:0>2d}".format(final_score))
    text.append(text2)

    text3 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(5, 100)
    text3.text("Press SELECT to restart!")
    text.append(text3)

    # Stage for the background, framerate at 60FPS
    game = stage.Stage(ugame.display, constants.FPS)
    # Layers for the screen
    game.layers = text + [background]
    # Rendering the background
    game.render_block()

    while True:
        # If the select button is selected
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
        # Update the game logic
        game.tick()


def game_win_scene():
    # To turn off the sound
    sound = ugame.audio
    sound.stop()

    # Image banks
    image_bank_2 = stage.Bank.from_pmb16("mt_game_studio.bmp")

    # Set the background to the image at index 0
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Game over text
    text = []
    text1 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Moving the text
    text1.move(5, 20)
    text1.text("YOU WIN! THE LIZARD IS SAVED!")
    text.append(text1)

    text2 = stage.Text(
        width=17, height=11, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Moving the text
    text2.move(5, 40)
    text2.text("Press SELECT to restart!")
    text.append(text2)

    # Stage for the background, framerate at 60FPS
    game = stage.Stage(ugame.display, constants.FPS)
    # Layers for the screen
    game.layers = text + [background]
    # Rendering the background
    game.render_block()

    while True:
        # If the select button is selected
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
        # Update the game logic
        game.tick()


if __name__ == "__main__":
    splash_scene()
