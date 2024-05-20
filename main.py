import pygame as pg
import sys
import easygui


pg.font.init()


BG1 = int(input())
BG2 = int(input())
BG3 = int(input())

CL1 = int(input())
CL2 = int(input())
CL3 = int(input())

r = int(input())
s = int(input())

TC1 = int(input())
TC2 = int(input())
TC3 = int(input())


def add_text(_Text, pos, a, b, c, d):
    f1 = pg.font.Font(None, d)
    text1 = f1.render(_Text, True, ((a, b, c)))
    sc.blit(text1, pos)

def text():
    message = easygui.enterbox("Введите фразу которая появится на месте курсора когда вы нажали Ентер на нампаде.")
    return message

def name():
    message = easygui.enterbox("Введите название вашего файла.")
    return message

def get_color():
    msg = "Введи цвет(rgb)"
    title = "Редактор цвета"
    fieldNames = ["Red", "Green", "Blue"]
    fieldValues = []
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    try:
        return (int(fieldValues[0]), int(fieldValues[1]), int(fieldValues[2]))
    except:
        return False

def get_size():
    msg = "Введи размер кисти и текста"
    title = "Редактор размера"
    fieldNames = ["Кисть", "Текст"]
    fieldValues = []
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    try:
        return (int(fieldValues[0]), int(fieldValues[1]))
    except:
        return False

sc = pg.display.set_mode((1750, 1000))
sc.fill((BG1, BG2, BG3))
pg.display.update()


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()

    if pressed[0]:
        pg.draw.circle(sc, (CL1, CL2, CL3), pos, r)
    if pressed[1]:
        pg.draw.rect(sc, (CL1, CL2, CL3), (pos[0] - r/2, pos[1] - r/2, r, r))
    if pressed[2]:
        pg.draw.circle(sc, (BG1, BG2, BG3), pos, r)

    keys = pg.key.get_pressed()
    if keys[pg.K_KP_ENTER]:
        add_text(text(), pos, TC1, TC2, TC3, s)
    if keys[pg.K_c]:
        sc.fill((BG1, BG2, BG3))
    if keys[pg.K_s]:
        pg.image.save(sc, name() + ".jpeg")
    if keys[pg.K_KP_1]:
        a = get_color()
        if a:
            BG1, BG2, BG3 = a
    if keys[pg.K_KP_2]:
        a = get_color()
        if a:
             CL1, CL2, CL3 = a
    if keys[pg.K_KP_3]:
        a = get_color()
        if a:
            TC1, TC2, TC3 = a
    if keys[pg.K_KP_4]:
        a = get_size()
        if a:
            r, s = a

    pg.draw.rect(sc, (250, 250, 250), (0, 0, 300, 80))

    variables1 = pg.font.Font(None, 25)

    textvariables1 = variables1.render(f"{BG1}, {BG2}, {BG3}, цвет фона", True, (TC1, TC2, TC3))

    sc.blit(textvariables1, (0, 0))


    variables2 = pg.font.Font(None, 25)

    textvariables2 = variables2.render(f"{CL1}, {CL2}, {CL3}, цвет кисточки", True, (TC1, TC2, TC3))

    sc.blit(textvariables2, (0, 20))


    variables3 = pg.font.Font(None, 25)

    textvariables3 = variables3.render(f"{r}, {s}, ширина кисточки и текста", True, (TC1, TC2, TC3))

    sc.blit(textvariables3, (0, 40))


    variables4 = pg.font.Font(None, 25)

    textvariables4 = variables4.render(f" {TC1}, {TC2}, {TC3}, цвет текста", True, (TC1, TC2, TC3))

    sc.blit(textvariables4, (0, 60))


    pg.display.update()

    pg.time.delay(10)
