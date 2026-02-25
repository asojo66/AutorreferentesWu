from manim import * 
from manim.mobject.svg.svg_mobject import SVGMobject
import numpy as np
from manim_slides import ThreeDSlide

screen_witdth = 16/9 * 8

config.background_color = "#edebda"
black_color = "#323030"
blue_color = "#6883FB"
red_color = "#F1534D"
head_color = "#fcad63"

Text.set_default(color = black_color)
Tex.set_default(color = black_color)
MathTex.set_default(color = black_color)
Dot.set_default(color = black_color)

class Wu(ThreeDSlide):

    def fadeout_all(self, **kwargs):
        """Fade out all the currents objects from screen"""

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def remove_all(self, **kwargs):
        """Remove all the currents objects from screen"""

        self.remove(*self.mobjects)

    

    def construct(self):

        # Add an empty slide to avoid automatic start

        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r"\usepackage{physics, amsmath, amssymb}")
        
        invisible = Text("HOLA, SOY INVISIBLE").set_opacity(0)

        self.play(Write(invisible), time = 0.1)
        self.next_slide()

        # -----------------------------------------------
        #                  TITLE SCREEN
        # -----------------------------------------------
        
        title = Tex(r"Chien-Shiung Wu")
        subtitle = Tex(r"La mujer que rompió la simetría").scale(0.85)
        authors = Tex(r"Antonio Sojo López").scale(0.7)

        # Logos 'n' stuff
        logo_us = ImageMobject("./assets/logos/logo_us.png").scale_to_fit_height(1)
        banner_min = ImageMobject("./assets/logos/min_banner.jpg").scale_to_fit_height(1)
        banners = Group(
            ImageMobject("./assets/logos/autorreferentes_full.png").scale_to_fit_height(1)\
            .to_edge(UP, buff = 0.35),
            Group(
                logo_us,
                Tex("PIF VII Plan Propio").scale_to_fit_width(logo_us.width)\
                    .next_to(logo_us, DOWN, buff=0.1)
            ),
            Group(
                banner_min,
                Tex("PID2022-136228NB-C22").scale_to_fit_width(banner_min.width)\
                    .next_to(banner_min, DOWN, buff=0.1)
            )
        ).arrange(RIGHT, buff = 0.5).scale_to_fit_width(9)
        logo_fisica = Group(
            SVGMobject("./assets/logos/fisica.svg").scale_to_fit_height(1),
            ImageMobject("./assets/logos/divulgaus.png").scale_to_fit_height(1)
        ).arrange(RIGHT, buff=2).to_edge(UP, buff = 1)


        title_screen = VGroup(
            title,
            subtitle,
            authors,
        ).arrange(DOWN, buff=0.35)
        authors.shift(0.15*DOWN)
        banners.to_edge(DOWN, buff = 1)

        self.play(
            Write(title), Write(subtitle)
        )
        self.play(
            Write(authors),
            FadeIn(banners, shift = UP),
            FadeIn(logo_fisica, shift = DOWN)
        )

        # -----------------------------------------------
        #                  EARLY LIFE: MAP
        # -----------------------------------------------

        title = Title("China, 1912")
        title.underline.set_color(black_color)

        self.next_slide()
        self.fadeout_all()

        worldmap = SVGMobject("./assets/world_taicang.svg").scale_to_fit_height(8)
        self.play(FadeIn(worldmap))

        self.next_slide()

        target_point = worldmap.get_center() + RIGHT * (screen_witdth / 4) + UP * (1.8)
        scale_factor = 3
        shift_vec = ORIGIN - target_point
        self.play(
            worldmap.animate.scale(scale_factor, about_point=target_point).shift(shift_vec),
            Write(title),
            run_time=2
        )

        self.next_slide()
        self.remove_all()

        # -----------------------------------------------
        #               EARLY LIFE: FAMILY
        # -----------------------------------------------

        title = Title("Familia")
        title.underline.set_color(black_color)
        self.add(title)

        father_name = Tex("Wu Zhong-Yi").scale(0.8)
        mother_name = Tex("Fan Fu-Hua").scale(0.8)
        older_brother_name = Tex("Chien-Ying").scale(0.8)
        younger_brother_name = Tex("Chien-Hao").scale(0.8)
        main_person = Tex("Chien-Shiung Wu").scale(1.0)

        fathers = VGroup(father_name, mother_name).arrange(RIGHT, buff=2.5)
        siblings = VGroup(older_brother_name, main_person, younger_brother_name).arrange(RIGHT, buff=1.5)
        main_person.shift(0.25*DOWN).set_color(red_color)

        family = VGroup(fathers, siblings).arrange(DOWN, buff=2)

        line1 = Line(father_name.get_right()+0.25*RIGHT, mother_name.get_left()+0.25*LEFT, color=black_color, stroke_width=2)
        line2 = Line(line1.get_center(), line1.get_center()+2*DOWN, color=black_color, stroke_width=2)
        line3 = Line(older_brother_name.get_top()+0.25*UP, younger_brother_name.get_top()+0.25*UP, color=black_color, stroke_width=2)
        line4 = Line(older_brother_name.get_top()+0.25*UP, older_brother_name.get_top(), color=black_color, stroke_width=2)
        line5 = Line(line1.get_center()+2*DOWN, main_person.get_top(), color=black_color, stroke_width=2)
        line6 = Line(younger_brother_name.get_top()+0.25*UP, younger_brother_name.get_top(), color=black_color, stroke_width=2)

        lines = VGroup(line1, line2, line3, line4, line5, line6)

        self.play(Write(fathers))
        self.next_slide()
        self.play(Create(lines), Write(siblings))

        fatherlist = BulletedList(
            " Ingeniero",
            r" Animaba a Wu a \\ interesarse por la ciencia",
            dot_scale_factor=3
        ).scale(0.6).next_to(father_name, DOWN, buff=0.25)

        motherlist = BulletedList(
            " Profesora",
            r" Apoyaba la \\ educación igualitaria",
            dot_scale_factor=3
        ).scale(0.6).next_to(mother_name, DOWN, buff=0.25)

        self.next_slide()
        self.play(Create(fatherlist))
        self.wait(0.3)

        self.next_slide()
        self.play(Create(motherlist))
        self.wait(0.3)

        self.next_slide()
        everything = Group(title, family, lines, fatherlist, motherlist)
        family_pic = ImageMobject("./assets/family.png").scale_to_fit_height(5).next_to(everything, DOWN, buff=1)
        everything.add(family_pic)
        self.play(FadeIn(family_pic), everything.animate.shift(0.75*DOWN-family_pic.get_center()))
        arrow = Arrow(start = 5*DOWN, end = UP).scale(3.5).next_to(family_pic, DOWN, buff = 0).set_color(red_color).shift(0.5*LEFT)
        self.play(Create(arrow))

        # -----------------------------------------------
        #               EARLY LIFE: SCHOOL AND HIGH SCHOOL
        # -----------------------------------------------

        self.next_slide()

        school_img = ImageMobject("./assets/school.png").scale_to_fit_height(4.5)
        school = Group(
            school_img,
            Tex("Escuela de niñas Ming De. Fundada por su padre.").next_to(school_img, DOWN, buff=0.25)
        )

        more_data = BulletedList(
            " Escuchaba a su padre leer artículos de ciencia en voz alta",
            " Prefería escuchar la radio a jugar con otros niños"
        ).next_to(school, DOWN, buff=0.5)

        schoolslide = Group(school, more_data).next_to(fatherlist, LEFT, buff = 4)
        everything.add(schoolslide)

        self.remove(arrow)
        self.add(school)
        self.play(everything.animate.move_to(-schoolslide.get_center()/2))

        # -----------------------------------------------
        #                   High school
        # -----------------------------------------------

        self.next_slide()

        text1 = Tex(r"Con solo \textbf{11 años}:")
        text12 = Tex(r"Se matricula en la Escuela de mujeres de Suzhou ($80$ km)").scale(0.8)
        text2 = Tex(r"Se gradua con el mejor expediente en 1929").scale(0.8)
        text3 = Tex(r"Aquí descubre la ciencia de primera mano").scale(0.8)
        text4 = Tex(r"Fue admitida en la Universidad Nacional Central").scale(1.1)

        texts = VGroup(text1, text12, text2, text3, text4).arrange(DOWN, buff=0.5)
        text1.to_edge(LEFT, buff=0.5)
        text12.to_edge(LEFT, buff=2)
        text2.to_edge(LEFT, buff=2)
        text3.to_edge(LEFT, buff=2)
        text4.shift(0.25*DOWN)

        texts.next_to(more_data, DOWN, buff=1.5)

        line1 = Line(more_data.get_bottom()+0.25*DOWN, texts.get_top()+0.25*UP, color=black_color, stroke_width=4)

        everything.add(texts, line1)

        self.play(Create(line1), Write(texts), everything.animate.shift(schoolslide.get_center()-texts.get_center()))

        self.next_slide()
        self.fadeout_all()

        question1 = Tex(r"¿Qué opinais sobre la educación que recibió Wu?").scale_to_fit_width(10)

        self.play(Write(question1))

        # -----------------------------------------------
        #                 University
        # -----------------------------------------------

        self.next_slide()
        self.fadeout_all()

        title = Title("Universidad Nacional Central")
        title.underline.set_color(black_color)
        university_img = ImageMobject("./assets/universidad_build.jpg").scale_to_fit_height(3.5).next_to(title, DOWN, buff=0.5)

        math_symbol = MathTex(r"\pi").scale_to_fit_height(0.5)
        physics_symbol = MathTex("F = ma").scale_to_fit_height(0.5)

        subjects = VGroup(
            math_symbol,
            physics_symbol
        ).arrange(RIGHT, buff=2).next_to(university_img, DOWN, buff = 0.5)

        arrow = Arrow(math_symbol.get_right()+0.25*RIGHT, physics_symbol.get_left()+0.25*LEFT).set_color(black_color)

        text1 = Tex(r"Fue líder politica en la universidad").to_edge(DOWN, buff=0.25)

        self.play(Write(title), FadeIn(university_img))
        self.next_slide()
        self.play(Create(subjects), Create(arrow))
        self.next_slide()
        self.play(Write(text1))

        self.next_slide()
        self.fadeout_all()

        university_img2 = ImageMobject("./assets/universidad.jpg").scale_to_fit_width(12).center()
        self.play(FadeIn(university_img2))

        self.next_slide()
        self.fadeout_all()

        title = Title("Universidad de Zhejiang y Academia Sinica")
        title.underline.set_color(black_color)
        self.play(Write(title))

        text1 = Tex(r"1. Se traslada a la Universidad de Zhejiang en 1934 como profesora").scale(0.8)
        text2 = Tex(r"2. Trabaja en el Instituto de Física de la Academia Sinica").scale(0.8)
        text3 = Tex(r"Su supervisora Gu Jien-Wei, \\ le recomienda doctorarse en \textbf{Michigan}").scale(0.8)

        VGroup(text1, text2, text3).arrange(DOWN, buff=0.5).center()
        text1.to_edge(LEFT, buff=0.5)
        text2.to_edge(LEFT, buff=0.5)

        self.next_slide()
        self.play(Write(text1))
        self.next_slide()
        self.play(Write(text2))
        self.next_slide()
        self.play(Write(text3))


        # -----------------------------------------------
        #                    Viaje a Usa
        # -----------------------------------------------

        title = Title("Viaje a USA, 1936")
        title.underline.set_color(black_color)

        self.next_slide()
        self.fadeout_all()

        worldmap = SVGMobject("./assets/world_usa.svg").scale_to_fit_height(8)
        self.play(FadeIn(worldmap))

        self.next_slide()
        tio = ImageMobject("./assets/tio.png").scale_to_fit_height(3).to_edge(DOWN, buff=0.5).shift(2*LEFT)
        amigas = ImageMobject("./assets/amigas.png").scale_to_fit_height(3).to_edge(DOWN, buff=0.5).shift(2*RIGHT)

        self.play(FadeIn(tio))

        self.next_slide()
        self.play(FadeIn(amigas))

        self.next_slide()
        self.remove_all()

        self.next_slide()
        text1 = Tex("¿Cuál es la impresión que se lleva al llegar?").scale_to_fit_width(12)
        self.play(Write(text1))
        text2 = Tex(r"Wu se sorprendió por el sexismo en la sociedad estadounidense.").scale(0.8).next_to(text1, DOWN, buff=0.5)
        text3 = Tex(r"Dejó Michigan y volvió a Berkeley").scale(0.8).next_to(text1, DOWN, buff=0.5)
        self.next_slide()
        self.play(Write(text2))
        self.next_slide()
        self.play(ReplacementTransform(text2, text3))

        self.next_slide()
        self.remove_all()

        # -----------------------------------------------
        #                 RESEARCH CAREER
        # -----------------------------------------------

        title = Title("Carrera investigadora")
        title.underline.set_color(black_color)

        text1 = Tex(r"1. \textbf{Berkeley} - Ernest O. Lawrence y Emilio Segrè (\textbf{Nobel 1939 y 1959})")
        text2 = Tex(r"a. Radiación de frenado (bremsstrahlung)").scale(0.8)
        text3 = Tex(r"b. Producción de isótopos radiactivos Xe").scale(0.8)

        text4 = Tex(r"Tras problemas por su raza y género").scale(0.9)

        text5 = Tex(r"2. \textbf{Princeton y Proyecto Manhatan}")
        text6 = Tex(r"a. Se casa con Yuan Jialiu (Sin familia por WWII)").scale(0.8)
        text7 = Tex(r"b. Descubre el envenenamiento por Xe-$135$").scale(0.8)

        text8 = Tex(r"Le ofrecen un puesto de profesora asociada").scale(0.9)

        text9 = Tex(r"3. \textbf{Columbia} (NY) - Primera profesora titular mujer")
        text10 = Tex(r"a. Pionera del entrelazamiento cuántico").scale(0.8)
        text11 = Tex(r"b. Acaba la WWII pero comienza la guerra civil China").scale(0.8)

        VGroup(title, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=0.5).scale_to_fit_height(7.5)
        text1.to_edge(LEFT, buff=0.5)
        text2.to_edge(LEFT, buff=1.5)
        text3.to_edge(LEFT, buff=1.5)
        text5.to_edge(LEFT, buff=0.5)
        text6.to_edge(LEFT, buff=1.5)
        text7.to_edge(LEFT, buff=1.5)
        text9.to_edge(LEFT, buff=0.5)
        text10.to_edge(LEFT, buff=1.5)
        text11.to_edge(LEFT, buff=1.5)

        title.shift(title.get_center()[0]*LEFT)

        self.play(Write(title))
        self.play(Write(text1), Write(text2), Write(text3))
        self.next_slide()
        self.play(Write(text4))
        self.next_slide()
        self.play(Write(text5), Write(text6), Write(text7))
        self.next_slide()
        self.play(Write(text8), Write(text9), Write(text10), Write(text11))

        # -----------------------------------------------
        #               Comienza su fama
        # -----------------------------------------------

        self.next_slide()
        self.fadeout_all()

        title = Title("Comienza su fama")
        title.underline.set_color(black_color)
        

        text1 = Tex(r"Fermi (1934) propone su teoría para la $\beta^-$")
        betam = MathTex(r"n \rightarrow p + e^- + \bar{\nu}_e")
        text2 = Tex(r"Luis W. Álvarez (Nobel 1968) obtiene resultados que no encajan")
        text3 = Tex(r"Wu se interesa en la $\beta^-$ desde Berkeley")
        text4 = Tex(r"En 1949 realiza confirmaciones empíricas que:")
        text5 = Tex(r"1. Confirma la teoría de Fermi").scale(0.8)
        text6 = Tex(r"2. Descubre errores en los cálculos de Álvarez").scale(0.8)
        text7 = Tex(r"Se posiciona como la \# 1 en $\beta^-$").scale(1.2)

        VGroup(title, text1, betam, text2, text3, text4, text5, text6, text7).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=0.5).scale_to_fit_height(7.5)
        text1.to_edge(LEFT, buff=0.5)
        text2.to_edge(LEFT, buff=0.5)
        text3.to_edge(LEFT, buff=0.5)
        text4.to_edge(LEFT, buff=0.5)
        text5.to_edge(LEFT, buff=1.5)
        text6.to_edge(LEFT, buff=1.5)

        title.shift(title.get_center()[0]*LEFT)

        self.play(Write(title))
        self.play(Write(text1))
        self.next_slide()
        self.play(Write(betam), Write(text2))
        self.next_slide()
        self.play(Write(text3), Write(text4))
        self.next_slide()
        self.play(Write(text5), Write(text6))
        self.next_slide()
        self.play(Write(text7))

        # -----------------------------------------------
        #       Teoría Tsung-Dao Lee y Chen-Ning Yang
        # -----------------------------------------------

        self.next_slide()
        self.fadeout_all()

        title = Title("Teoría de Lee y Yang")
        title.underline.set_color(black_color)
        lee = ImageMobject("./assets/lee.jpg").scale_to_fit_height(3)
        yang = ImageMobject("./assets/yang.jpg").scale_to_fit_height(3)
        text1 = Tex(r"La paridad se conserva en las fuerzas fuertes y electromagnéticas").scale(0.8)
        text2 = Tex(r"Pero no en la débil...").scale(0.8)
        text3 = Tex(r"Proponen un experimento a Wu, a la que ya le precede la fama").scale(0.8)

        photos = Group(lee, yang).arrange(RIGHT, buff=2.5)

        Group(
            photos,
            text1,
            text2,
            text3
        ).arrange(DOWN, buff = 0.5).shift(0.5*DOWN)
        
        self.play(Write(title))
        self.next_slide()
        self.play(FadeIn(photos))
        self.next_slide()
        self.play(Write(text1))
        self.next_slide()
        self.play(Write(text2))
        self.next_slide()
        self.play(Write(text3))

        # -----------------------------------------------
        #                   SYMMETRY
        # -----------------------------------------------

        self.next_slide()
        self.fadeout_all()

        text1 = Tex(r"¿Qué es la paridad?").scale_to_fit_width(10)
        text2 = Tex(r"Primero necesitamos entender qué es una simetría").next_to(text1, DOWN, buff=0.5)

        self.play(Write(text1))
        self.next_slide()
        self.play(Write(text2))

        self.next_slide()
        self.fadeout_all()

        square = Square(side_length=2, color = black_color, fill_color = blue_color, fill_opacity = 1)
        triangl = Triangle(color = black_color, fill_color = blue_color, fill_opacity = 1).scale_to_fit_width(2)
        circl = Circle(radius=1, color = black_color, fill_color = blue_color, fill_opacity = 1)

        objs = VGroup(circl, square, triangl).arrange(RIGHT, buff = 1.5)

        self.play(Create(objs))
        self.next_slide()

        def make_ccw_arrow(center_point, radius=0.6, start_angle=-PI/4, angle=PI*1.7):
            arc = Arc(radius=radius, start_angle=start_angle, angle=angle)
            arc.set_stroke(black_color, width=3)
            # center the arc at the target center
            arc.move_to(center_point)
            # compute tangent at end to place arrow tip
            p_end = arc.get_end()
            p_before = arc.point_from_proportion(0.98)
            direction = p_end - p_before
            ang = np.arctan2(direction[1], direction[0])
            tip = Triangle().scale(0.12).set_fill(black_color, opacity=1).set_stroke(width=0)
            tip.move_to(p_end)
            tip.set_angle(ang)
            tip.shift(direction / np.linalg.norm(direction) * 0.05)
            return VGroup(arc, tip)

        arrow1 = make_ccw_arrow(square.get_center(), radius=0.3)
        arrow2 = make_ccw_arrow(circl.get_center(), radius=0.3)
        arrow3 = make_ccw_arrow(triangl.get_center_of_mass(), radius=0.3)

        self.play(FadeIn(arrow1, run_time=0.18), FadeIn(arrow2, run_time=0.18), FadeIn(arrow3, run_time=0.18))
        self.play(Rotate(square, PI / 2),
                  Rotate(triangl, PI / 2, about_point=triangl.get_center_of_mass()),
                  Rotate(circl, PI / 2))
        self.play(FadeOut(arrow1, run_time=0.18), FadeOut(arrow2, run_time=0.18), FadeOut(arrow3, run_time=0.18))

        self.next_slide()
        # Dashed horizontal axis (x-axis) through each object's center for reflection
        dash1 = DashedLine(square.get_center() + LEFT * 1.5, square.get_center() + RIGHT * 1.5, dash_length=0.08)
        dash2 = DashedLine(circl.get_center() + LEFT * 1.5, circl.get_center() + RIGHT * 1.5, dash_length=0.08)
        dash3 = DashedLine(triangl.get_center_of_mass() + LEFT * 1.5, triangl.get_center_of_mass() + RIGHT * 1.5, dash_length=0.08)
        for d in (dash1, dash2, dash3):
            d.set_stroke(black_color, width=2)

        self.play(FadeIn(dash1, run_time=0.12), FadeIn(dash2, run_time=0.12), FadeIn(dash3, run_time=0.12))
        self.play(square.animate.apply_matrix(np.array([[1, 0], [0, -1]])),
                  triangl.animate.apply_matrix(np.array([[1, 0], [0, -1]]), about_point=triangl.get_center_of_mass()),
                  circl.animate.apply_matrix(np.array([[1, 0], [0, -1]])))
        self.play(FadeOut(dash1, run_time=0.12), FadeOut(dash2, run_time=0.12), FadeOut(dash3, run_time=0.12))

        self.next_slide()
        # Dashed diagonal axis (y = x) through each object's center for reflection
        diag_vec = (RIGHT + UP)
        diag1 = DashedLine(square.get_center() - diag_vec * 1.5, square.get_center() + diag_vec * 1.5, dash_length=0.08)
        diag2 = DashedLine(circl.get_center() - diag_vec * 1.5, circl.get_center() + diag_vec * 1.5, dash_length=0.08)
        diag3 = DashedLine(triangl.get_center_of_mass() - diag_vec * 1.5, triangl.get_center_of_mass() + diag_vec * 1.5, dash_length=0.08)
        for d in (diag1, diag2, diag3):
            d.set_stroke(black_color, width=2)

        self.play(FadeIn(diag1, run_time=0.12), FadeIn(diag2, run_time=0.12), FadeIn(diag3, run_time=0.12))
        self.play(square.animate.apply_matrix(np.array([[0, 1], [1, 0]]), about_point=square.get_center()),
                  triangl.animate.apply_matrix(np.array([[0, 1], [1, 0]]), about_point=triangl.get_center_of_mass()),
                  circl.animate.apply_matrix(np.array([[0, 1], [1, 0]]), about_point=circl.get_center()))
        self.play(FadeOut(diag1, run_time=0.12), FadeOut(diag2, run_time=0.12), FadeOut(diag3, run_time=0.12))

        self.next_slide()
        self.fadeout_all()

        # -----------------------------------------------
        #              Paridad en la física
        # -----------------------------------------------

        self.set_camera_orientation(phi=-25*DEGREES)

        left_axes = ThreeDAxes(
            x_length=3,
            y_length=3,
            z_length=3,
            x_range=[0, 3],
            y_range=[0, 3],
            z_range=[0, 3],
            axis_config={"stroke_width": 2},
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE}
        ).shift(3*LEFT)

        right_axes = ThreeDAxes(
            x_length=3,
            y_length=3,
            z_length=3,
            x_range=[0, 3],
            y_range=[0, 3],
            z_range=[0, 3],
            axis_config={"stroke_width": 2},
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE}
        ).shift(3 *RIGHT)

        self.play(Create(left_axes), Create(right_axes))

        self.next_slide()
        self.play(right_axes.animate.apply_matrix(np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]), about_point=right_axes.get_center()))

        self.next_slide()
        self.remove(right_axes)
        right_axes = ThreeDAxes(
            x_length=3,
            y_length=3,
            z_length=3,
            x_range=[0, 3],
            y_range=[0, 3],
            z_range=[0, 3],
            axis_config={"stroke_width": 2},
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE}
        ).shift(3 *RIGHT)

        self.add(right_axes)

        self.next_slide()
        self.wait(0.1)
        self.next_slide()
        self.play(right_axes.animate.apply_matrix(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]), about_point=right_axes.get_center()))
        self.next_slide()
        self.play(Rotate(right_axes, angle=PI, axis=RIGHT))

        self.next_slide()
        self.fadeout_all()

        # -----------------------------------------------
        #            El experimento 
        # -----------------------------------------------

        title = Title("El experimento de Wu")
        title.underline.set_color(black_color)

        reaction = MathTex(r"{}^{60}_{27} Co", r"\rightarrow ",r"{}^{60}_{28} Ni",r"+ ",r"e^-",r" + \bar{\nu}_e").next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.next_slide()
        self.play(Write(reaction))

        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light

        # Move camera to view from above
        self.set_camera_orientation(phi=-25*DEGREES)
        sphere = Sphere(radius=1, resolution=(12, 12))\
            .set_fill(blue_color, opacity=1).set_stroke(black_color, width=1)
        sphere.rotate_about_origin(PI/2, RIGHT).shift(1.5*DOWN)

        self.play(FadeIn(sphere))

        self.next_slide(loop = True)
        self.play(Rotate(sphere, angle=TAU, axis=UP), run_time=2, rate_func=linear)

        econe = Cone(base_radius=1/2, height=1.5, direction=DOWN, fill_color=red_color, )\
            .rotate(PI, RIGHT).move_to(sphere.get_bottom()).shift(-0.8*Y_AXIS-0.5*X_AXIS).set_opacity(0.5)
        
        econe2 = Cone(base_radius=1/2, height=1.5, direction=UP, fill_color=red_color, )\
            .rotate(PI, RIGHT).move_to(sphere.get_top()).shift(0.8*Y_AXIS-0.5*X_AXIS).set_opacity(0.5)
        
        self.next_slide(loop = True)

        self.add(econe, econe2)
        reaction[0].set_color(blue_color)
        reaction[2].set_color(blue_color)
        reaction[4].set_color(red_color)

        self.play(Rotate(sphere, angle=TAU, axis=UP), run_time=2, rate_func=linear)

        self.next_slide()

        self.play(
            FadeOut(title), FadeOut(reaction), FadeOut(econe), FadeOut(econe2),
            sphere.animate.move_to(screen_witdth/4*LEFT)
        )

        # Axis indicator: vertical dashed line with an arrow at the top
        axis_start = sphere.get_center() - UP * 1.6
        axis_end = sphere.get_center() + UP * 1.6
        axis_line = DashedLine(axis_start, axis_end, dash_length=0.08).set_stroke(black_color, width=2)
        axis_arrow = Arrow(start=sphere.get_center() + UP * 1.1, end=sphere.get_center() + UP * 1.6, buff=0, tip_length=0.2)\
            .set_fill(black_color).set_stroke(width=0)
        
        self.play(Create(Line(10*UP, 10*DOWN).set_color(black_color)))

        # Create 3D coordinate axes on the left side of the white line
        left_axes = ThreeDAxes(
            x_length=1,
            y_length=1,
            z_length=1,
            x_range=[0, 1],
            y_range=[0, 1],
            z_range=[0, 1],
            axis_config={"stroke_width": 2},
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
            tips=False
        ).scale(0.4)
        left_axes.move_to(1.2*LEFT)

        self.play(Create(left_axes), run_time = 0.3)

        sphere2 = Sphere(radius=1, resolution=(12, 12))\
            .set_fill(blue_color, opacity=1).set_stroke(black_color, width=1)
        sphere2.rotate_about_origin(PI/2, RIGHT).shift(screen_witdth/4*RIGHT)

        axis_start = sphere2.get_center() - UP * 1.6
        axis_end = sphere2.get_center() + UP * 1.6
        axis_line2 = DashedLine(axis_start, axis_end, dash_length=0.08).set_stroke(black_color, width=2)
        axis_arrow2 = Arrow(start=sphere2.get_center() + DOWN * 1.1, end=sphere2.get_center() + DOWN * 1.6, buff=0, tip_length=0.2)\
            .set_fill(black_color).set_stroke(width=0)

        # Create 3D coordinate axes on the right side (mirror image reflected on y-z plane)
        right_axes = ThreeDAxes(
            x_length=1,
            y_length=1,
            z_length=1,
            x_range=[-1, 0],
            y_range=[0, 1],
            z_range=[0, 1],
            axis_config={"stroke_width": 2},
            x_axis_config={"color": RED},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": BLUE},
            tips=False
        ).scale(0.4)
        right_axes.move_to(1.2*RIGHT)

        self.play(FadeIn(sphere2),
                  Create(right_axes), run_time = 0.3)

        self.next_slide(loop = True)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=-TAU, axis=UP), run_time=2, rate_func=linear
        )

        self.next_slide(loop = True)
        self.add(axis_line, axis_arrow)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=-TAU, axis=UP), run_time=2, rate_func=linear
        )

        self.next_slide(loop = True)
        self.add(axis_line2, axis_arrow2)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=-TAU, axis=UP), run_time=2, rate_func=linear
        )
        

        self.next_slide()
        self.play(
            Rotate(sphere2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center()),
            Rotate(axis_line2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center()),
            Rotate(axis_arrow2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center())
        )

        self.next_slide(loop = True)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=TAU, axis=UP), run_time=2, rate_func=linear
        )

        self.next_slide()
        self.play(FadeOut(sphere2), FadeOut(axis_line2), FadeOut(axis_arrow2))

        self.next_slide(loop = True)
        
        econe = Cone(base_radius=1, height=3, direction=DOWN, fill_color=red_color, )\
            .rotate(PI, RIGHT).move_to(sphere.get_bottom()).shift(-Y_AXIS-X_AXIS).set_opacity(0.5)
        
        econe2 = Cone(base_radius=1, height=3, direction=DOWN, fill_color=red_color)\
            .rotate(PI, RIGHT).move_to(sphere2.get_bottom()).shift(-Y_AXIS-X_AXIS).set_opacity(0.5)
        
        self.add(econe)
        self.play(Rotate(sphere, angle=TAU, axis=UP), run_time=2, rate_func=linear)

        self.next_slide(loop = True)

        axis_line2 = DashedLine(axis_start, axis_end, dash_length=0.08).set_stroke(black_color, width=2)
        axis_arrow2 = Arrow(start=sphere2.get_center() + DOWN * 1.1, end=sphere2.get_center() + DOWN * 1.6, buff=0, tip_length=0.2)\
            .set_fill(black_color).set_stroke(width=0)
        
        self.add(sphere2, axis_arrow2, axis_line2)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=-TAU, axis=UP), run_time=2, rate_func=linear)
        
        self.next_slide(loop = True)
        self.add(econe2)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=-TAU, axis=UP), run_time=2, rate_func=linear
        )

        self.next_slide()
        self.play(
            Rotate(sphere2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center()),
            Rotate(econe2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center()),
            Rotate(axis_arrow2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center()),
            Rotate(axis_line2, angle=-PI, axis=RIGHT, about_point=sphere2.get_center()),
        )

        self.next_slide(loop = True)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=TAU, axis=UP),
            run_time=2, rate_func=linear
        )

        self.next_slide()
        self.fadeout_all()

        # -----------------------------------------------
        #               El experimento 2
        # -----------------------------------------------

        self.set_camera_orientation(phi=0)

        title = Title("El experimento de Wu")
        title.underline.set_color(black_color)

        text1 = Tex(r"¿Cómo se realizó el experimento?").scale_to_fit_width(10)
        text2 = Tex(r"1. Se enfría el Co-$60$ a $0.01$ K").scale(0.8)
        text3 = Tex(r"2. Se aplica un campo magnético $1$ T para alinear los espines").scale(0.8)
        text4 = Tex(r"3. Se mide la dirección de emisión de los electrones").scale(0.8)
        text5 = Tex(r"4. Se repite el experimento con el campo magnético invertido").scale(0.8)

        VGroup(title, text1, text2, text3, text4, text5).arrange(DOWN, buff=0.5)
        text2.to_edge(LEFT, buff=1.5)
        text3.to_edge(LEFT, buff=1.5)
        text4.to_edge(LEFT, buff=1.5)
        text5.to_edge(LEFT, buff=1.5)

        self.play(Write(title))
        self.next_slide()
        self.play(Write(text1))
        self.next_slide()
        self.play(Write(text2))
        self.next_slide()
        self.play(Write(text3))
        self.next_slide()
        self.play(Write(text4))
        self.next_slide()
        self.play(Write(text5))
        self.next_slide()
        self.fadeout_all()

        # -----------------------------------------------
        #               Resultados y consecuencias
        # -----------------------------------------------

        title = Title("Premio Nobel")
        title.underline.set_color(black_color)
        text1 = Tex(r"El experimento es premiado con un \textbf{premio Nobel} en 1957")
        text2 = Tex(r"Solo dos de los autores son premiados").scale(0.8)
        text3 = Tex(r"Más tarde se reconoce a Wu con el premio Wolf en 1978").scale(0.8).to_edge(DOWN, buff=0.5)

        VGroup(text1, text2).arrange(DOWN, buff=0.5)

        self.play(Write(title), Write(text1))
        self.next_slide()
        self.play(Write(text2))
        self.next_slide()
        self.play(Write(text3))

        self.next_slide()
        self.fadeout_all()

        # -----------------------------------------------
        #        Fotos
        # -----------------------------------------------
        
        img1 = ImageMobject("./assets/wu.jpg").scale_to_fit_height(6)
        img3 = ImageMobject("./assets/wu3.jpg").scale_to_fit_height(6)
        img2 = ImageMobject("./assets/wu2.png").scale_to_fit_height(3.5)

        Group(img1, img3).arrange(RIGHT, buff=0)
        img2.to_corner(DR, buff=1)

        self.add(img1, img3, img2)
        self.wait(0.1)


        # -----------------------------------------------
        #        Fotos
        # -----------------------------------------------
        
        img1 = ImageMobject("./assets/wu.jpg").scale_to_fit_height(6)
        img3 = ImageMobject("./assets/wu3.jpg").scale_to_fit_height(6)
        img2 = ImageMobject("./assets/wu2.png").scale_to_fit_height(3.5)

        Group(img1, img3).arrange(RIGHT, buff=0)
        img2.to_corner(DR, buff=1)

        self.add(img1, img3, img2)
        self.wait(0.1)

        self.next_slide()
        self.remove_all()


        # -----------------------------------------------
        #        Despedida y QR
        # -----------------------------------------------

        text1 = Tex("Gracias por vuestra atención")
        
        qr = ImageMobject("./assets/qr.png").scale_to_fit_height(4.5)
        logo = ImageMobject("./assets/logos/autorreferentes_full.png").scale_to_fit_width(qr.width)

        Group(
            text1, 
            Group(
                logo,
                qr
            ).arrange(DOWN, buff=0)
        ).arrange(DOWN, buff=0.5)

        self.add(text1, logo, qr)
        self.wait(0.1)