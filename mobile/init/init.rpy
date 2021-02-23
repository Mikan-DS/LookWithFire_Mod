# -*- coding: utf-8 -*-
init:


    transform zoom_mobile: #Адаптируем под андрюху
        zoom 0.66666666666666 # Чем больше шестерок, тем лучше

    python:
        import os

        mods["fl_start"] =  u"{font=mods/ognenyi_vzglyad/fonts/ov_font.ttf}{size=40}ОГНЕННЫЙ ВЗГЛЯД{/size}{/font}"

		def adapt_hotspot(*points):
            for i, p in enumerate(points):
                points[i] = int(p*0.66666666)
            return *points

        for file in renpy.list_files(): # Что, новомодное объявление файлов хотите? Ну смотрите, даже разьясню что это за бублик
            if "ognenyi_vzglyad" in file: # Проверяет от нашего ли мода этот файл
                file_name = os.path.splitext(os.path.basename(file))[0] # Достаем имя файла

                if file.endswith((".png", ".jpg", ".webp")): # Фильтр на изображения

                    if "sprites" in file and  not "composite" in file: # Если он в директории спрайтов, то по красоте с матрицой добавляет спрайт # За исключением компонентных спрайтов, они будут обьявлены дальше
                        renpy.image( # По факту, так же обьявляет изображение, но реализуемо подругому. Не забудьте использовать bg cg и подобную херотеть в названии папок
                            file_name.replace("_", " "), # имя по которому будем обращаться
                            At( #Портировка под телефоньку
                                ConditionSwitch(
                                    "persistent.sprite_time == 'sunset'",
                                    im.MatrixColor(
                                        file,
                                        im.matrix.tint(0.94, 0.82, 1.0) # При свете дня...
                                    ),
                                    "persistent.sprite_time == 'night'",
                                    im.MatrixColor(
                                        file,
                                        im.matrix.tint(0.63, 0.78, 0.82) # Во тьме ночной...
                                    ),
                                    True,
                                    file # Но на случаи когда ни туда ни сюда, выходит обычный спрайт
                                ),
                                zoom_mobile)#At
                        )
                    elif not "gui" in file: # Компоненты меню обьявляются в самом меню
                        renpy.image(file.split("/")[-2]+" "+file_name,  # Ну а обычные ваши фончики фоточки обьявляются вот так
                            At(
                            file,
                            zoom_mobile)
                            )
                elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")): # Если хотите потусить под музычку
                    globals()[file_name] = file # Разьяснения нужны?

        ###Переходики всякие
        fla = Fade(.25,  .75, .75, color="#FFF")
        bol = Fade(.25,   .5, .75, color="#F00")
        boo = Fade(.25,   .5, .75)
        blt = Fade(.75,  1.0, .75)

        ov_trise = Dissolve(1.5)

    ### Особое исключение, так как не был найден спрайт в оригинале, вернее, спрайта в купальнике, пришлось сделать этого мутанта из мода и ванилы

    image dv sad swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_3_sad.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_3_sad.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_3_sad.png")) )

    image dv shy swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_3_shy.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_3_shy.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_3_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_3_shy.png")) )

    image dv angry swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_5_body.png"),(0,0),(0,0), get_image("sprites/normal/dv/dv_5_angry.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_5_body.png"),(0,0),(0,0), get_image("sprites/normal/dv/dv_5_angry.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900, 1080), (0,0), get_image("sprites/normal/dv/dv_5_body.png"), (0,0),(0,0), get_image("sprites/normal/dv/dv_5_angry.png")) )

    ### Трансформация бега
    transform running():
        zoom 1.01 align (0.5, 0.5)
        ease 0.35 xalign 0.35 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        ease 0.35 xalign 0.65 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        repeat
