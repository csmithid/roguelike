import libtcodpy as libtcod

SCREEN_WIDTH = 32
SCREEN_HEIGHT = 32

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

libtcod.console_set_custom_font('terminal8x8_gs_ro.png',libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH,SCREEN_HEIGHT,'mines', False)

def handle_keys(key):
    global playerx,playery
    if key.vk == libtcod.KEY_UP:
        playery -= 1
    if key.vk == libtcod.KEY_LEFT:
        playerx -= 1
    if key.vk == libtcod.KEY_DOWN:
        playery += 1
    if key.vk == libtcod.KEY_RIGHT:
        playerx += 1
    if key.vk == libtcod.KEY_ESCAPE:
        return True

while not libtcod.console_is_window_closed():
    exit = handle_keys(libtcod.console_wait_for_keypress(True))
    if exit:
        break
    libtcod.console_clear(0)
    libtcod.console_set_default_foreground(0,libtcod.white)
    libtcod.console_put_char(0,playerx,playery,'@',libtcod.BKGND_NONE)
    libtcod.console_flush()
