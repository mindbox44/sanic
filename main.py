def on_a_pressed():
    if sanic.vy == 0:
        sanic.vy = -200
        animation.run_image_animation(sanic,
            [img("""
                    . . . . . 8 8 8 8 8 . . . . . . 
                                . . . . . . 8 8 8 8 8 . . . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 . . . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 . . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 . . . 
                                8 8 8 8 8 8 8 8 1 1 8 8 8 . . . 
                                . . . 8 8 8 8 1 1 f 1 8 8 . . . 
                                . . . 8 8 8 8 8 1 1 8 8 . . . . 
                                . 8 8 8 8 d d d d d d f . . . . 
                                8 8 8 8 8 8 d d d d d . . . . . 
                                8 8 8 . 8 8 8 8 8 8 . . . . . . 
                                . . . 8 8 8 8 8 8 d . . . . . . 
                                . . . . . . . . 8 d . . . . 2 . 
                                . . . . . . . . . 1 . . . 2 . . 
                                . . . . . . . . . 8 . 2 2 . . . 
                                . . . . . . . . 2 2 2 . . . . .
                """),
                img("""
                    . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . . . 8 8 8 8 8 8 . . . . .
                """),
                img("""
                    . . . . . 8 8 . . . 8 . . . . . 
                                . . . . . 8 8 8 . . 8 8 8 . . . 
                                . . . . . 8 8 8 . . 8 8 8 8 . . 
                                . . . . 8 . 8 8 8 8 8 8 8 8 . . 
                                . . . . 8 8 8 8 8 8 8 8 8 8 . . 
                                . . . . 8 8 8 d 8 8 8 8 8 8 . 8 
                                . . . . 8 8 d d 8 8 8 8 8 8 8 8 
                                . . . . 8 8 d d 8 1 8 8 8 8 8 8 
                                2 . . 8 8 8 d d 1 1 1 8 8 8 8 8 
                                2 8 1 d d 8 d d 1 f 1 8 8 8 8 8 
                                2 . . . . . d d 8 1 8 8 8 8 8 . 
                                . 2 . . . . . f 8 8 8 8 8 8 . . 
                                . 2 . . . . . . . 8 8 8 8 . . . 
                                . . 2 . . . . . . . . . . . . . 
                                . . . 2 . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . . . 8 8 8 8 8 8 . . . . .
                """),
                img("""
                    . . . . . 2 2 2 . . . . . . . . 
                                . . . 2 2 . 8 . . . . . . . . . 
                                . . 2 . . . 1 . . . . . . . . . 
                                . 2 . . . . d 8 . . . . . . . . 
                                . . . . . . d 8 8 8 8 8 8 . . . 
                                . . . . . . 8 8 8 8 8 8 . 8 8 8 
                                . . . . . d d d d d 8 8 8 8 8 8 
                                . . . . f d d d d d d 8 8 8 8 . 
                                . . . . 8 8 1 1 8 8 8 8 8 . . . 
                                . . . 8 8 1 f 1 1 8 8 8 8 . . . 
                                . . . 8 8 8 1 1 8 8 8 8 8 8 8 8 
                                . . . 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . . 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . . . 8 8 8 8 8 8 8 8 8 8 . . 
                                . . . . . 8 8 8 8 8 . . . . . . 
                                . . . . . . 8 8 8 8 8 . . . . .
                """),
                img("""
                    . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . . . 8 8 8 8 8 8 . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . 2 . . . 
                                . . . . . . . . . . . . . 2 . . 
                                . . . 8 8 8 8 . . . . . . . 2 . 
                                . . 8 8 8 8 8 8 f . . . . . 2 . 
                                . 8 8 8 8 8 1 8 d d . . . . . 2 
                                8 8 8 8 8 1 f 1 d d 8 d d 1 8 2 
                                8 8 8 8 8 1 1 1 d d 8 8 8 . . 2 
                                8 8 8 8 8 8 1 8 d d 8 8 . . . . 
                                8 8 8 8 8 8 8 8 d d 8 8 . . . . 
                                8 . 8 8 8 8 8 8 d 8 8 8 . . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 . . . . 
                                . . 8 8 8 8 8 8 8 8 . 8 . . . . 
                                . . 8 8 8 8 . . 8 8 8 . . . . . 
                                . . . 8 8 8 . . 8 8 8 . . . . . 
                                . . . . . 8 . . . 8 8 . . . . .
                """),
                img("""
                    . . . . . 8 8 8 8 8 8 . . . . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                                . . . 8 8 8 8 8 8 8 8 8 8 . . . 
                                . . . . . 8 8 8 8 8 8 . . . . .
                """),
                img("""
                    . . . . . 8 8 8 8 8 . . . . . . 
                                . . . . . . 8 8 8 8 8 . . . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 . . . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 . . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 . . . 
                                8 8 8 8 8 8 8 8 1 1 8 8 8 . . . 
                                . . . 8 8 8 8 1 1 f 1 8 8 . . . 
                                . . . 8 8 8 8 8 1 1 8 8 . . . . 
                                . 8 8 8 8 d d d d d d f . . . . 
                                8 8 8 8 8 8 d d d d d . . . . . 
                                8 8 8 . 8 8 8 8 8 8 . . . . . . 
                                . . . 8 8 8 8 8 8 d . . . . . . 
                                . . . . . . . . 8 d . . . . 2 . 
                                . . . . . . . . . 1 . . . 2 . . 
                                . . . . . . . . . 8 . 2 2 . . . 
                                . . . . . . . . 2 2 2 . . . . .
                """),
                img("""
                    . . . . . 8 8 8 8 8 . . . . . . 
                                . . . . . . 8 8 8 8 8 . . . . . 
                                . . 8 8 8 8 8 8 8 8 8 8 . . . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 . . . 
                                . 8 8 8 8 8 8 8 8 8 8 8 8 . . . 
                                8 8 8 8 8 8 8 8 1 1 8 8 8 . . . 
                                . . . 8 8 8 8 1 1 f 1 8 8 . . . 
                                . . . 8 8 8 8 8 1 1 8 8 . . . . 
                                . 8 8 8 8 d d d d d d f . . . . 
                                8 8 8 8 8 8 d d d d d . . . . . 
                                8 8 8 . 8 8 8 8 8 8 . . . . . . 
                                . . . 8 8 8 8 8 8 d . . . . . . 
                                . . . . . . . . 8 d . . . . 2 . 
                                . . . . . . . . . 1 . . . 2 . . 
                                . . . . . . . . . 8 . 2 2 . . . 
                                . . . . . . . . 2 2 2 . . . . .
                """),
                img("""
                    . . 8 8 8 8 8 8 8 . . . . . . . 
                                . . . . . . 8 8 8 8 8 . . . . . 
                                . . . . 8 8 8 1 8 1 8 8 . . . . 
                                . 8 8 8 8 8 1 f 1 f 1 8 . . . . 
                                . 8 8 8 8 8 8 1 8 1 8 8 . . . . 
                                . . . . . 8 f d d f d 8 . . . . 
                                . . . . 8 8 d f d d d 8 . . . . 
                                . . . 8 8 8 8 8 8 8 8 . . . . . 
                                . . 8 8 8 . 8 d d d 8 8 . . . . 
                                . . . . . 8 8 d d d 8 8 8 . . . 
                                . . . . . 8 8 8 d 8 8 . 8 8 . . 
                                . . . . 8 . . 8 8 8 . . . 8 . . 
                                . . . 1 1 . 8 8 . 8 . . . 1 1 . 
                                . . . 1 1 . 8 . . 8 8 . . 1 1 . 
                                . . . . . . 8 . . . 8 . . . . . 
                                . . . . . . 2 2 2 . 2 2 2 . . .
                """)],
            100,
            False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(sanic,
        [img("""
                . . . . . . . 8 8 8 8 8 8 8 . . 
                        . . . . . 8 8 8 8 8 . . . . . . 
                        . . . . 8 8 1 8 1 8 8 8 . . . . 
                        . . . . 8 1 f 1 f 1 8 8 8 8 8 . 
                        . . . . 8 8 1 8 1 8 8 8 8 8 8 . 
                        . . . . 8 d f d d f 8 . . . . . 
                        . . . . 8 d d d f d 8 8 . . . . 
                        . . . . . 8 8 8 8 8 8 8 8 . . . 
                        . . . . 8 8 d d d 8 . 8 8 8 . . 
                        . . . 8 8 8 d d d 8 8 . . . . . 
                        . . 8 8 . 8 8 d 8 8 8 . . . . . 
                        . . 8 . . . 8 8 8 . . 8 . . . . 
                        . 1 1 . 2 2 2 . 2 2 2 1 1 . . . 
                        . 1 1 2 2 . . 2 . . 2 1 1 . . . 
                        . . . . 2 . . 2 . . 2 . . . . . 
                        . . . . . 2 2 . 2 2 . . . . . .
            """),
            img("""
                . . . . . . . 8 8 8 8 8 8 8 . . 
                        . . . . . 8 8 8 8 8 . . . . . . 
                        . . . . 8 8 1 8 1 8 8 8 . . . . 
                        . . . . 8 1 f 1 f 1 8 8 8 8 8 . 
                        . . . . 8 8 1 8 1 8 8 8 8 8 8 . 
                        . . . . 8 d f d d f 8 . . . . . 
                        . . . . 8 d d d f d 8 8 . . . . 
                        . . . . . 8 8 8 8 8 8 8 8 . . . 
                        . . . . 8 8 d d d 8 . 8 8 8 . . 
                        . . . 8 8 8 d d d 8 8 . . . . . 
                        . . 8 8 . 8 8 d 8 8 8 . . . . . 
                        . . 8 . . . 8 8 8 . . 8 . . . . 
                        . 1 1 . 2 2 2 2 2 2 2 1 1 . . . 
                        . 1 1 2 2 . . . . . 2 1 1 . . . 
                        . . . . 2 . . . . . 2 . . . . . 
                        . . . . . 2 2 2 2 2 . . . . . .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, sanic)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, sanic)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    animation.run_image_animation(sanic,
        [img("""
                . . 8 8 8 8 8 8 8 . . . . . . . 
                        . . . . . . 8 8 8 8 8 . . . . . 
                        . . . . 8 8 8 1 8 1 8 8 . . . . 
                        . 8 8 8 8 8 1 f 1 f 1 8 . . . . 
                        . 8 8 8 8 8 8 1 8 1 8 8 . . . . 
                        . . . . . 8 f d d f d 8 . . . . 
                        . . . . 8 8 d f d d d 8 . . . . 
                        . . . 8 8 8 8 8 8 8 8 . . . . . 
                        . . 8 8 8 . 8 d d d 8 8 . . . . 
                        . . . . . 8 8 d d d 8 8 8 . . . 
                        . . . . . 8 8 8 d 8 8 . 8 8 . . 
                        . . . . 8 . . 8 8 8 . . . 8 . . 
                        . . . 1 1 2 2 2 . 2 2 2 . 1 1 . 
                        . . . 1 1 2 . . 2 . . 2 2 1 1 . 
                        . . . . . 2 . . 2 . . 2 . . . . 
                        . . . . . . 2 2 . 2 2 . . . . .
            """),
            img("""
                . . 8 8 8 8 8 8 8 . . . . . . . 
                        . . . . . . 8 8 8 8 8 . . . . . 
                        . . . . 8 8 8 1 8 1 8 8 . . . . 
                        . 8 8 8 8 8 1 f 1 f 1 8 . . . . 
                        . 8 8 8 8 8 8 1 8 1 8 8 . . . . 
                        . . . . . 8 f d d f d 8 . . . . 
                        . . . . 8 8 d f d d d 8 . . . . 
                        . . . 8 8 8 8 8 8 8 8 . . . . . 
                        . . 8 8 8 . 8 d d d 8 8 . . . . 
                        . . . . . 8 8 d d d 8 8 8 . . . 
                        . . . . . 8 8 8 d 8 8 . 8 8 . . 
                        . . . . 8 . . 8 8 8 . . . 8 . . 
                        . . . 1 1 2 2 2 2 2 2 2 . 1 1 . 
                        . . . 1 1 2 . . . . . 2 2 1 1 . 
                        . . . . . 2 . . . . . 2 . . . . 
                        . . . . . . 2 2 2 2 2 . . . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    global robuttnik_health
    robuttnik_health += -1
    if robuttnik_health <= 0:
        animation.run_image_animation(robuttnik,
            [img("""
            ................................
                        ................................
                        ...........f.....f..............
                        ............fdddf...............
                        111........ddfdfdd..............
                        111........dfdfdfd..............
                        111........f8fff8f..............
                        222........eeeedfd..............
                        2222.eeeee.eeeeeeeee.ee.........
                        .2222.eeeee.dddddeeee.e.........
                        .22222...22222112222............
                        .222222.22222211222222222.......
                        ..222222222222112222222222......
                        ....222222222211222222.22222....
                        .....222222222112222222..2222...
                        .....222222222112222222...2222..
                        ....2222222222112222222....222..
                        ....1111111111111111111....111..
                        .bbbbbbbbbbbbbbbbbbbbbbbbbb111..
                        .bbbbbbbbbbbbbbbbbbbbbbbbbb111..
                        .bbbbbbbbbbb55555bbbbbbbbbb.....
                        .bbbbbbbbbb5555555bbbbbbbbb.....
                        ..bbbbbbbbb5555555bbbbbbbbb.....
                        ..bbbbbbbbb5555555bbbbbbbbb.....
                        ..bbbbbbbbb5555555bbbbbbbb......
                        ...bbbbbbbb5555555bbbbbbbb......
                        ...bbbbbbbbb55555bbbbbbbb.......
                        ....bbbbbbbbbbbbbbbbbbb.........
                        ......bbbbbbbbbbbbbbb...........
                        ................................
                        ................................
                        ................................
            """)],
            500,
            False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

laser: Sprite = None
robuttnik_health = 0
robuttnik: Sprite = None
sanic: Sprite = None
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999991111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999991111111111111999999999999999111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999111111111111111199999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999991111111111111111199999911111111111111111199999999999999999999999999999999999999999999999999999911111111111111199999999999999999999999999999999999999
        9999999999111111111111111111199111111111111111111111199999999999999999999999999999999999999999999999999991111111111111111111999999999999999999999999999999999999
        9999999911111111111111111111111111111111111111111111199999999999999999999999999999999999999999999999991111111111111111111111111999999999999999999999999999999999
        9999999111111111111111111111111111111111111111111111199999999999999999999999999999999999999999999999911111111111111111111111111111199999999999999999999999999999
        9999999911111111111111111111111111111111111111111111999999999999999999999999999999999999999999999999111111111111111111111111111111199999999999999999999999999999
        9999999111111111111111111111111111111111111111111999999999999999999999999999999999999999999999999991111111111111111111111111111111119999999999999999999999999999
        9999911111111111111111111111111111111111111119999999999999999999999999999999999999999999999999999911111111111111111111111111111111119999999999999999999999999999
        9999111111111111111111111111111111111111119999999999999999999999999999999999999999999999999999999911111111111111111111111111111111119999999999999999999999999999
        9999111111111111111111111111111111111111119999999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999999999999999999999999
        9999911111111111111111111111111111111111119999999999999999999999999999999999999999999999999999991111111111111111111111111111111111111111111999999999999999999999
        9999911111111111111111111111111111111111119999999999999999999999999999999999999999999999999999991111111111111111111111111111111111111111111111199999999999999999
        9999991111111111111111111111111111111111119999999999999999999999999999999999999999999999999999991111111111111111111111111111111111111111111111111999999999999999
        99999991111111111111111111111111111111111199999999999999e9999999999999999999999999999999999999911111111111111111111111111111111111111111111111111199999999999999
        9999999911111111111111111111111111111111199999999999999ee9999999999999999999999999999999999999911111111111111111111111111111111111111111111111111119999999999999
        9999999911111111111111111111111111111111999999999999999eee999999999999999999999999999999999999111111111111111111111111111111111111111111111111111111999999999999
        9999999911111111111111111111111111111119999999999999999eee999999999999999999999999999999999999911111111111111111111111111111111111111111111111111111999999999999
        999999991111111111111111111111111111119999999999999999eeeee99999999999999999999999999999999999991111111111111111111111111111111111111111111111111111999999999999
        999999991111111111119999991111111119999999999999999999eeeee99999999999999999999999999999999999991111111111111111111111111111111111111111111111111111999999999999
        999999999111111119999999999999999999999999999999999999eeeeee999999999999999999999999999ee99999999111111111111111111111111111111111111111111111111111999999999999
        999999999911111999999999999999999999999999999999999999eeeeee99999999999999999999999999eeee9999999991111111111111111111111111111111111111111111111111199999999999
        99999999999999999999999999999999999999999999999999999eeeeeeee9999999999999999999999999eeee9999999999911111111111111111111111111111111111111111111111199999999999
        99999999999999999999999999999999999999999999999999999eeeeeeee999999999999999999999999eeeeee999999999911111111111111111111111111111111111111111111111199999999999
        99999999999999999999999999999999999999999999999999999eeeeeeeee9999999999999999999999eeeeeee999999999111111111111111111111111111111111111111111111111199999999999
        9999999999999999999999999999999999999999999999999999eeeeeeeeee999999999999999999999eeeeeeeee99999999111111111111111111111111111111111111111111111111199999999999
        9999999999999999999999999999999999999999999999999999eeeeeeeeeee9999999999999999999eeeeeeeeee99999999911111111111111111111111111111111111111111111111999999999999
        9999999999999999999999999999999999999999999999999999eeeeeeeeeee9999999999999999999eeeeeeeeeee9999999911111111111111111111111111111111111111111111119999999999999
        999999999999999999999999999999999999999999999999999eeeeeeeeeeee9999999999999999999eeeeeeeeeee9999999999911111111111111111111111111111111111111111199999999999999
        999999999999999999999999999999999999999999999999999eeeeeeeeeeee9999999999999999999eeeeeeeeeeee999999999999111111111111111111111111111111111111111199999999999999
        99999999999999999999999999999999999999999999999999eeeeeeeeeeeeee99999999999999999eeeeeeeeeeeee999999999999999991111111111111111111111111111111119999999999999999
        99999999999999999999999999999999999999999999999999eeeeeeeeeeeeee99999999999999999eeeeeeeeeeeeee99999999999999911111111111111111111111111119999999999999999999999
        9999999999999999999999999999999999999999999999999eeeeeeeeeeeeeee9999999999999999eeeeeeeeeeeeeee99999999999999911111111111111111111111111199999999999999999999999
        99999999999999999999999999999e9999999999999999999eeeeeeeeeeeeeee9999999999999999eeeeeeeeeeeeeeee9999999999999911111111111111111111111111999999999999999999999999
        9999999999999999999999999999ee999999999999999999eeeeeeeeeeeeeeeee999999999999999eeeeeeeeeeeeeeee9999999999999911111111111111111111111119999999999999999999999999
        9999999999999999999999999999eee99999999999999999eeeeeeeeeeeeeeeee99999999999999eeeeeeeeeeeeeeeeee999999999999911111111111111111111111999999999999999999999999999
        9999999999999999999999999999eeee9999999999999999eeeeeeeeeeeeeeeee99999999999999eeeeeeeeeeeeeeeeee999999999999991111111111111111111199999999999999999999999999999
        999999999999999999999999999eeeee999999999999999eeeeeeeeeeeeeeeeee99999999999999eeeeeeeeeeeeeeeeeee99999999999999911111111111111999999999999999999999999999999999
        999999999999999999999999999eeeee999999999999999eeeeeeeeeeeeeeeeeee999999999999eeeeeeeeeeeeeeeeeeee99999999999999999911111199999999999999999999999999999999999999
        999999999999999999999999999eeeeee99999999999999eeeeeeeeeeeeeeeeeee999999999999eeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999eeeeeee99999999999999eeeeeeeeeeeeeeeeeee999999999999eeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999eeeeeeee999999999999eeeeeeeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999999999999999999999999
        99999999999999999999999999eeeeeeee999999999999eeeeeeeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999eeeeeeeee999999999999eeeeeeeeeeeeeeeeeeee9999999999eeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999eeeeeeeeee9999999999eeeeeeeeeeeeeeeeeeeee9999999999eeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999eeeeeeeeee9999999999eeeeeeeeeeeeeeeeeeeeee999999999eeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999999999999999999999
        999999999999999999999999eeeeeeeeeeee999999999eeeeeeeeeeeeeeeeeeeeee99999999eeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999999999999999999999
        999999999999999999999999eeeeeeeeeeee999999999eeeeeeeeeeeeeeeeeeeeee99999999eeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999999999999999999
        999999999999999999999999eeeeeeeeeeee99999999eeeeeeeeeeeeeeeeeeeeeeee9999999eeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999999999999999999
        99999999999999999999999eeeeeeeeeeeeee9999999eeeeeeeeeeeeeeeeeeeeeeee999999eeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999999999999999999
        99999999999999999999999eeeeeeeeeeeeeee99999eeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999e999999999999999999999999999999999999
        9999999999999999999999eeeeeeeeeeeeeeee99999eeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999e999999999999999999999999999999999999
        9999999999999999999999eeeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999ee999999999999999999999999999999999999
        9999999999999999999999eeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999eeee99999999999999999999999999999999999
        999999999999999999999eeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999eeeee99999999999999999999999999999999999
        999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999eeeeee9999999999999999999999999999999999
        999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999eeeeeee999999999999999999999999999999999
        999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777eeeeeeeeeee99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999eeeeeeee999999999999999999999999999999999
        99999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777eeeeeeeeeee9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999eeeeeeeee99999999999999999999999999999999
        9999999e999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeee9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999eeeeeeeeee99999999999999999999999999999999
        999999ee999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999eeeeeeeeee99999999999999999999999999999999
        999999ee999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999eeeeeeeeeeee9999999999999999999999999999999
        999999eee99999999999eeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999eeeeeeeeeeee9999999999999999999999999999999
        99999eeeee999999999eeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999eeeeeeeeeeeee9999999999999999999999999999999
        99999eeeee999999999eeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999eeeeeeeeeeeee9999999999999999999999999999999
        99999eeeeee99999999eeeeeeee77777777777eeeeeeee777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999eeeeeeeeeeeeeee999999999999999e99999999999999
        99999eeeeee9999999eeeeeeee77777777777777eeeee777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999eeeeeeeeeeeeeee99999999999999ee99999999999999
        9999eeeeeeee999999eeeeee7777777777777777777ee7777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999eeeeeeeeeeeeeeee9999999999999eee99999999999999
        9999eeeeeeee999999eeeeee7777777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999eeeeeeeeeeeeeeeee999999999999eee99999999999999
        9999eeeeeeeee99999eeeeee77777777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeeeeeeeeee99999999999eeee99999999999999
        999eeeeeeeeeee999eeeeeee77777777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeeeeeeeeee99999999999eeeee9999999999999
        999eeeeeeeeeee999eeeeeee77777777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999eeeeeeeeeeeeeeeeeee99999999999eeeee9999999999999
        999eeeeeeeeeeee99eeeeeeee777777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeee999999999eeeeee9999999999999
        999eeeeeeeeeeee99eeeeeeee77777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeeeeeeeee999999999eeeeeee999999999999
        99eeeeeeeeeeeee99eeeeeeeee777777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeeeeeeee999999999eeeeeee999999999999
        99eeeeeeeeeeeee9eeeeeeeeeee777777777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeeeeeeeee99999999eeeeeee999999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999eeeeeeeee99999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999eeeeeeeee99999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777ee77777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999eeeeeeeee99999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999eeeeeeeeee9999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeee9999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeee9999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee7777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeeee999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999eeeeeeeeeeee999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999eeeeeeeeeeeee999999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeee99999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999eeeeeeeeeeeeee99999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeee99999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeee9999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99eeeeeeeeeeeeeeee9999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9eeeeeeeeeeeeeeee9999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999e
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999e
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999e
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999e
        99eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99ee
        9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99ee
        9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9eee
        9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""))
tiles.set_tilemap(tilemap("""
    level1
"""))
sanic = sprites.create(img("""
        . . 8 8 8 8 8 8 8 . . . . . . . 
            . . . . . . 8 8 8 8 8 . . . . . 
            . . . . 8 8 8 1 8 1 8 8 . . . . 
            . 8 8 8 8 8 1 f 1 f 1 8 . . . . 
            . 8 8 8 8 8 8 1 8 1 8 8 . . . . 
            . . . . . 8 f d d f d 8 . . . . 
            . . . . 8 8 d f d d d 8 . . . . 
            . . . 8 8 8 8 8 8 8 8 . . . . . 
            . . 8 8 8 . 8 d d d 8 8 . . . . 
            . . . . . 8 8 d d d 8 8 8 . . . 
            . . . . . 8 8 8 d 8 8 . 8 8 . . 
            . . . . 8 . . 8 8 8 . . . 8 . . 
            . . . 1 1 . 8 8 . 8 . . . 1 1 . 
            . . . 1 1 . 8 . . 8 8 . . 1 1 . 
            . . . . . . 8 . . . 8 . . . . . 
            . . . . . . 2 2 2 . 2 2 2 . . .
    """),
    SpriteKind.player)
controller.move_sprite(sanic, 200, 0)
scene.camera_follow_sprite(sanic)
sanic.ay = 400
robuttnik = sprites.create(img("""
        ................................
            ................................
            ...........f.....f..............
            ............fdddf...............
            111........ddfdfdd..............
            111........dfdfdfd..............
            111........f8fff8f..............
            222........eeeedfd..............
            2222.eeeee.eeeeeeeee.ee.........
            .2222.eeeee.dddddeeee.e.........
            .22222...22222112222............
            .222222.22222211222222222.......
            ..222222222222112222222222......
            ....222222222211222222.22222....
            .....222222222112222222..2222...
            .....222222222112222222...2222..
            ....2222222222112222222....222..
            ....1111111111111111111....111..
            .bbbbbbbbbbbbbbbbbbbbbbbbbb111..
            .bbbbbbbbbbbbbbbbbbbbbbbbbb111..
            .bbbbbbbbbbb55555bbbbbbbbbb.....
            .bbbbbbbbbb5555555bbbbbbbbb.....
            ..bbbbbbbbb5555555bbbbbbbbb.....
            ..bbbbbbbbb5555555bbbbbbbbb.....
            ..bbbbbbbbb5555555bbbbbbbb......
            ...bbbbbbbb5555555bbbbbbbb......
            ...bbbbbbbbb55555bbbbbbbb.......
            ....bbbbbbbbbbbbbbbbbbb.........
            ......bbbbbbbbbbbbbbb...........
            ................................
            ................................
            ................................
    """),
    SpriteKind.enemy)
robuttnik.set_position(944, 144)
robuttnik_health = 8

def on_update_interval():
    global laser
    if robuttnik_health > 0:
        laser = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            robuttnik,
            -300,
            25)
        music.pew_pew.play()
game.on_update_interval(1000, on_update_interval)
