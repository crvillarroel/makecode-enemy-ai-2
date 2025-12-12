def on_up_pressed():
    mySprite.vy = -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    starkNextLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile4
        """),
    on_overlap_tile)

def on_left_pressed():
    mySprite.set_image(assets.image("""
        MyCat
        """))
    animation.run_image_animation(mySprite,
        assets.animation("""
            CatWalkBack
            """),
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    mySprite.set_image(assets.image("""
        MyCatBack
        """))
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    mySprite.set_image(assets.image("""
        MyCat
        """))
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def starkNextLevel():
    global currentLevel, mySprite, myEnemy
    for value in sprites.all_of_kind(SpriteKind.enemy):
        value.destroy(effects.hearts, 500)
    currentLevel += 1
    if currentLevel == 1:
        tiles.set_tilemap(tilemap("""
            level0
            """))
        mySprite = sprites.create(assets.image("""
            MyCatBack
            """), SpriteKind.player)
        controller.move_sprite(mySprite, 100, 0)
        mySprite.ay = 500
        scene.camera_follow_sprite(mySprite)
        tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 0))
        for value2 in tiles.get_tiles_by_type(assets.tile("""
            tile5
            """)):
            myEnemy = sprites.create(img("""
                    . . f f f . . . . . . . . . . .
                    f f f c c . . . . . . . . f f f
                    f f c c c . c c . . . f c b b c
                    f f c 3 c c 3 c c f f b b b c .
                    f f c 3 b c 3 b c f b b c c c .
                    f c b b b b b b c f b c b c c .
                    c c 1 b b b 1 b c b b c b b c .
                    c b b b b b b b b b c c c b c .
                    c b 1 f f 1 c b b c c c c c . .
                    c f 1 f f 1 f b b b b f c . . .
                    f f f f f f f b b b b f c . . .
                    f f 2 2 2 2 f b b b b f c c . .
                    . f 2 2 2 2 2 b b b c f . . . .
                    . . f 2 2 2 b b b c f . . . . .
                    . . . f f f f f f f . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                SpriteKind.enemy)
            tiles.place_on_tile(myEnemy, value2)
            myEnemy.follow(mySprite, 30)
    elif currentLevel == 2:
        tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 0))
        scene.set_background_color(6)
        tiles.set_tilemap(tilemap("""
            level02
            """))
    else:
        game.over(True)

def on_right_pressed():
    mySprite.set_image(assets.image("""
        MyCatBack
        """))
    animation.run_image_animation(mySprite,
        assets.animation("""
            CatWalk
            """),
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile2(sprite2, location2):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile2
        """),
    on_overlap_tile2)

def on_on_overlap(sprite3, otherSprite):
    otherSprite.destroy()
    if mySprite.bottom < otherSprite.y:
        sprite3.vy = -100
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

myEnemy: Sprite = None
mySprite: Sprite = None
currentLevel = 0
scene.set_background_color(9)
currentLevel = 0
starkNextLevel()

def on_on_update():
    for value3 in sprites.all_of_kind(SpriteKind.enemy):
        if value3.is_hitting_tile(CollisionDirection.BOTTOM):
            if value3.tile_kind_at(TileDirection.LEFT, assets.tile("""
                tile1
                """)) and value3.vx < 100:
                value3.vy = -150
            elif value3.tile_kind_at(TileDirection.RIGHT, assets.tile("""
                tile1
                """)) and value3.vx < 100:
                value3.vy = -150
        elif value3.is_hitting_tile(CollisionDirection.LEFT):
            value3.vx = 30
        elif value3.is_hitting_tile(CollisionDirection.RIGHT):
            value3.vx = -30
game.on_update(on_on_update)
