def on_button_pressed():
    controller.move_sprite(idk)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_on_overlap(sprite, otherSprite):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

err: Sprite = None
ghost: Sprite = None
idk: Sprite = None
if ("") == ("dontchangethis"):
    idk = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . 2 2 2 2 2 2 2 2 . . . 
                    . . . . 2 2 2 2 2 2 2 2 2 . . . 
                    . . . . 2 2 2 2 2 2 2 2 2 . . . 
                    . . . . 8 8 8 8 8 8 8 8 8 . . . 
                    . . . 8 8 8 8 8 8 8 8 8 8 8 . . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                    . . . 8 8 8 8 8 8 8 8 8 8 8 . . 
                    . . . . 8 8 8 8 8 8 8 8 8 . . . 
                    . . . . . 8 8 8 8 8 8 8 . . . .
        """),
        SpriteKind.player)
    ghost = sprites.create(img("""
            f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f 2 2 2 2 f f 2 2 2 2 f f f 
                    f f f 2 2 2 2 f f 2 2 2 2 f f f 
                    f f f 2 2 2 2 f f 2 2 2 2 f f f 
                    f f f 2 2 2 2 f f 2 2 2 2 f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f
        """),
        SpriteKind.enemy)
    ghost.set_position(9, 14)
    ghost.follow(idk, 30)
    scene.set_background_color(7)
else:
    scene.set_background_color(4)
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.IN_BACKGROUND)
    pause(2000)
    err = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 . . . . . . . . . . . . . . 8 
                    8 . . . . . . . . . . . . . . 8 
                    8 . 1 1 1 . . 1 1 1 . 1 1 1 . 8 
                    8 . 1 . . . . 1 . 1 . 1 . 1 . 8 
                    8 . 1 1 1 . . 1 1 1 . 1 1 1 . 8 
                    8 . 1 . . . . 1 1 . . 1 1 . . 8 
                    8 . 1 1 1 . . 1 . 1 . 1 . 1 . 8 
                    8 . . . . . . . . . . . . . . 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)

def on_update_interval():
    pass
game.on_update_interval(5000, on_update_interval)
