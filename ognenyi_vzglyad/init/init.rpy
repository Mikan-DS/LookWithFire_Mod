# -*- coding: utf-8 -*-
init:
    python:
        import os

        mods["fl_start"] =  u"{font=mods/ognenyi_vzglyad/fonts/ov_font.ttf}{size=40}ОГНЕННЫЙ ВЗГЛЯД{/size}{/font}"


        for file in renpy.list_files(): # Что, новомодное объявление файлов хотите? Ну смотрите, даже разьясню что это за бублик
            if "ognenyi_vzglyad" in file: # Проверяет от нашего ли мода этот файл
                file_name = os.path.splitext(os.path.basename(file))[0] # Достаем имя файла

                if file.endswith((".png", ".jpg", ".webp")): # Фильтр на изображения
                    if "sprites" in file: # Если он в директории спрайтов, то по красоте с матрицой добавляет спрайт
                        renpy.image( # По факту, так же обьявляет изображение, но реализуемо подругому. Не забудьте использовать bg cg и подобную херотеть в названии папок
                            file_name.replace("_", " "), # имя по которому будем обращаться
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
                            )
                        )
                    elif not "gui" in file: # Компоненты меню обьявляются в самом меню
                        renpy.image(file.split("/")[-2]+" "+file_name, file) # Ну а обычные ваши фончики фоточки обьявляются вот так
                elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")): # Если хотите потусить под музычку
                    globals()[file_name] = file # Разьяснения нужны?

        ###Переходики всякие
        fla = Fade(0.25, 0.75, .75, color="#FFFFFF")
        bol = Fade(.25, 0.5, .75, color="#FF0000")
        boo = Fade(.25, 0.5, .75, color="#000000")

        ov_trise = Dissolve(1.5)

    transform running():
        zoom 1.01 align (0.5, 0.5)
        ease 0.35 xalign 0.35 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        ease 0.35 xalign 0.65 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        repeat
