import libtcodpy as libctod


def render_all(con, entities, screen_width, screen_height):
    # Draw all the entities in the list
    for entity in entities:
        draw_entity(con, entity)

    libctod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    libctod.console_set_default_foreground(con, entity.color)
    libctod.console_put_char(con, entity.x, entity.y, entity.char, libctod.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    libctod.console_put_char(con, entity.x, entity.y, ' ', libctod.BKGND_NONE)
