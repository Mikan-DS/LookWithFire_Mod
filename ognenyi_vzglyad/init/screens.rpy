# -*- coding: utf-8 -*-
init 100:

    python:
        #Трансформы
        def particle_working(trans, st, at):

            try:
                trans.particle["current_angle"] += trans.particle["new_angle"]

                trans.xalign += px2pos(math.cos(trans.particle["current_angle"]), "x")+0.0005
                trans.yalign += px2pos(math.sin(trans.particle["current_angle"]), "y")+0.0001

                if trans.xalign > 1.1 or trans.xalign < -0.1 or trans.xalign > 1.1 or trans.xalign < -0.1:#Тут происходит вылет за экран
                    trans.xalign = renpy.random.randint(0, 350)*0.001
                    trans.yalign = renpy.random.random()
                    trans.zoom = renpy.random.randint(2, 12)*0.1
                    trans.particle = new_particle_profile(trans, st)

                if trans.particle["time2new_profile"] - st < 0: #В мире все не бесконечно, и эти шарики тоже
                    trans.particle = new_particle_profile(trans, st)
                    trans.xalign = renpy.random.randint(0, 350)*0.001
                    trans.yalign = renpy.random.random()
                    trans.zoom = renpy.random.randint(2, 12)*0.1
                    return renpy.random.choice([renpy.random.randint(1, 5)+renpy.random.random(), None])

                elif trans.particle["time2new_profile"] - st < 5: #Мы теряем шарик...
                    if trans.alpha > 0:
                        trans.alpha -= 0.02

                elif trans.alpha < 0.6: #Оно рождается!
                    trans.alpha += 0.005

                return 0.02
            except: #В случае первого появления
                trans.xalign = renpy.random.randint(0, 350)*0.001
                trans.yalign = renpy.random.random()
                trans.zoom = renpy.random.randint(2, 12)*0.1
                trans.particle = new_particle_profile(trans, st)
                return renpy.random.randint(0, 15)+renpy.random.random()

        def gravity_force(trans, st, at):
            #Конечно не понятно зачем, но в прошлом меню пытались сделать ускорение, потому я решил сделать более реалистичное
            trans.yalign -= 0.24 - st*0.4 #ну гравитация типа 0.4~
            if trans.yalign > 5:
                return
            return 0.01

        #########Вспомогательные функции
        def new_particle_profile(trans, st=0): #Создание профиля для шарико-блека


            return {"current_angle": renpy.random.randint(0, 628)*0.01,
                    "new_angle": 0.002-renpy.random.random()*0.004,
                    "time2new_profile": st + renpy.random.randint(15, 40)
                    }

        def px2pos(px, orientation="x"): #align адекватно принимает только проценты, потому приходится конвертировать
            return px/{"x":1920, "y":1080}[orientation]

    transform particle_moves():
        alpha 0
        function particle_working
        pause 5
        repeat

    transform alisas_jump():
        xalign -2.0
        block:
            pause 60
            xalign 0.2
            yalign 4
            function gravity_force
            repeat

    transform DissolveSH(speed = 1):
        on show:
            alpha 0
            linear speed alpha 1
        on hide:
            linear speed alpha 0

label fl_start:

    window hide

    #$config.developer = True
    scene black with dissolve
    $ renpy.pause(3, hard = True)

    show image Text("{size=70}RedHead Team представляет{/size}", slow_cps = 25) at truecenter#text "{size=70}RedHead Team представляет{/size}" at truecenter:

    #with dissolve
    pause 2#1
    hide text
    with dissolve

    $ persistent.sprite_time = "day"
    $ day_time ()

    scene bg ext_house_of_dv_day with dissolve
    pause (1)
    scene bg ext_house_of_dv_day:
        xalign 0.65 yalign 0.5
        linear 5 zoom 10.5

    scene white with dspr
    pause (2)
    jump fl_main_menu

label fl_main_menu:

    window hide

    play music bv_rideon
    scene bg int_house_of_dv_day with dissolve
    call screen fl_main_menu_screen

    return


screen fl_main_menu_screen:

    modal True
    zorder 999

    fixed at DissolveSH:

        add get_image("bg/int_house_of_dv_day.jpg")

        use fl_menu_GUI_screen

        use dinamic_particles


screen fl_menu_GUI_screen:

    tag menu

    imagemap:

        auto "mods/ognenyi_vzglyad/gui/menu/overlay_%s.png"

        hotspot (996, 505, 741, 110) action Jump("fl_enter_game")

        hotspot (912, 615, 834, 110) action ShowMenu("fl_menu_in_progress")

        hotspot (1089, 725, 650, 110) action ShowMenu("fl_menu_in_progress")

        hotspot (1329, 835, 409, 110) action ShowMenu("fl_menu_exit")

        hotspot (183, 806, 196, 196) action ShowMenu("fl_menu_vk")

    text "0.21.2.18 Git": # А вообще вот тут было бы хорошо стирать Git дабы версию указывать точнее
        size 25
        color "#AAA"
        at transform:
            xanchor 1.0
            xpos 0.9
            yoffset 20
            alpha 0.65

screen fl_menu_in_progress:

    tag menu

    imagebutton at DissolveSH:
        idle "mods/ognenyi_vzglyad/gui/menu/in_progress.jpg"
        action Return()


screen fl_menu_exit:

    tag menu

    fixed at DissolveSH:
        add "mods/ognenyi_vzglyad/gui/menu/exit.jpg"
        use fl_menu_ask_user((Hide("fl_main_menu_screen"), Hide("menu"), Jump("fl_true_exit")), Return())


screen fl_menu_vk:

    tag menu

    fixed at DissolveSH:
        add "mods/ognenyi_vzglyad/gui/menu/vk_link.jpg"
        use fl_menu_ask_user(OpenURL("https://vk.com/redhead_team"), Return())


screen fl_menu_ask_user(action_yes, action_no=NullAction()):

    imagebutton xalign 0.59 yalign 0.6:

        auto "mods/ognenyi_vzglyad/gui/ask_user/yes_%s.png"
        action action_yes

    imagebutton xalign 0.8 yalign 0.6:

        auto "mods/ognenyi_vzglyad/gui/ask_user/no_%s.png"
        action action_no



############EXTRA SCREENS####################

screen dinamic_particles:

    for i in range(25):
        add "mods/ognenyi_vzglyad/gui/particle.png" at particle_moves

    add "mods/ognenyi_vzglyad/gui/dv_chibi.png" at alisas_jump

label fl_true_exit:
    stop music fadeout 3
    scene black with dissolve
    pause 1
    $ MainMenu(confirm=False)()

label fl_enter_game:
    stop music fadeout 3
    scene black with dissolve2
    pause 3
    jump fl_prologue
