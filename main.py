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
        
        self.play(Write(Text("HOLA, SOY INVISIBLE").set_opacity(0)), time = 0.1)
        self.next_slide()

        # -----------------------------------------------
        #                  TITLE SCREEN
        # -----------------------------------------------
        
        title = Tex("Chien-Shiung Wu")
        subtitle = Tex("La mujer que rompió la simetría").scale(0.85)
        authors = Tex("Antonio Sojo López").scale(0.7)

        # Logos 'n' stuff
        logo_us = ImageMobject("./assets/logos/logo_us.png").scale_to_fit_width(3)
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
        ).arrange(RIGHT, buff = 0.5).scale_to_fit_width(13)

        title_screen = VGroup(
            title,
            subtitle,
            authors,
        ).arrange(DOWN, buff=0.5).shift(1.2*UP)
        banners.to_edge(DOWN, buff = 1)

        self.play(
            Write(title), Write(subtitle)
        )
        self.play(
            Write(authors),
            FadeIn(banners, shift = UP)
        )

        # -----------------------------------------------
        #                   SYMMETRY
        # -----------------------------------------------

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

        self.fadeout_all()
        # -----------------------------------------------
        #              ROTATING 3D SPHERE
        # -----------------------------------------------

        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light

        self.next_slide()
        # Move camera to view from above
        self.set_camera_orientation(phi=-25*DEGREES)
        sphere = Sphere(radius=1, resolution=(12, 12))\
            .set_fill(blue_color, opacity=1).set_stroke(black_color, width=1)
        sphere.rotate_about_origin(PI/2, RIGHT)

        self.play(FadeIn(sphere))

        self.next_slide(loop = True)
        self.play(Rotate(sphere, angle=TAU, axis=UP), run_time=2, rate_func=linear)

        self.next_slide()
        self.play(
            sphere.animate.shift(screen_witdth/4*LEFT)
        )

        # Axis indicator: vertical dashed line with an arrow at the top
        axis_start = sphere.get_center() - UP * 1.6
        axis_end = sphere.get_center() + UP * 1.6
        axis_line = DashedLine(axis_start, axis_end, dash_length=0.08).set_stroke(black_color, width=2)
        axis_arrow = Arrow(start=sphere.get_center() + UP * 1.1, end=sphere.get_center() + UP * 1.6, buff=0, tip_length=0.2)\
            .set_fill(black_color).set_stroke(width=0)
        
        self.play(Create(Line(10*UP, 10*DOWN)))

        # Create 3D coordinate axes on the left side of the white line
        left_axes = ThreeDAxes(
            x_length=1,
            y_length=1,
            z_length=1,
            x_range=[0, 1],
            y_range=[0, 1],
            z_range=[0, 1],
            axis_config={"color": black_color, "stroke_width": 2},
            tips=False
        ).scale(0.4)
        left_axes.move_to(1.2*LEFT)

        self.play(Create(left_axes), run_time = 0.3)

        self.next_slide()
        sphere2 = Sphere(radius=1, resolution=(12, 12))\
            .set_fill(blue_color, opacity=1).set_stroke(black_color, width=1)
        sphere2.rotate_about_origin(PI/2, RIGHT).shift(screen_witdth/4*RIGHT)

        axis_start = sphere2.get_center() - UP * 1.6
        axis_end = sphere2.get_center() + UP * 1.6
        axis_line2 = DashedLine(axis_start, axis_end, dash_length=0.08).set_stroke(black_color, width=2)
        axis_arrow2 = Arrow(start=sphere2.get_center() + DOWN * 1.1, end=sphere2.get_center() + DOWN * 1.6, buff=0, tip_length=0.2)\
            .set_fill(black_color).set_stroke(width=0)

        self.play(
            FadeIn(sphere2)
        )

        # Create 3D coordinate axes on the right side (mirror image reflected on y-z plane)
        right_axes = ThreeDAxes(
            x_length=1,
            y_length=1,
            z_length=1,
            x_range=[-1, 0],
            y_range=[0, 1],
            z_range=[0, 1],
            axis_config={"color": black_color, "stroke_width": 2},
            tips=False
        ).scale(0.4)
        right_axes.move_to(1.2*RIGHT)


        self.play(Create(right_axes), run_time = 0.3)

        self.next_slide(loop = True)
        self.play(
            Rotate(sphere, angle=TAU, axis=UP),
            Rotate(sphere2, angle=-TAU, axis=UP), run_time=2, rate_func=linear
        )

        self.next_slide()
        self.play(FadeIn(axis_line, run_time=0.2), FadeIn(axis_arrow, run_time=0.2))
        self.next_slide()
        self.play(FadeIn(axis_line2, run_time=0.2), FadeIn(axis_arrow2, run_time=0.2))
        self.next_slide()

        self.next_slide()
        self.play(
            sphere2.animate.rotate(PI, RIGHT, about_point=sphere2.get_center()),
            axis_line2.animate.rotate(PI, RIGHT, about_point=sphere2.get_center()),
            axis_arrow2.animate.rotate(PI, RIGHT, about_point=sphere2.get_center())
        )

        self.next_slide()
        self.play(FadeOut(sphere2), FadeOut(axis_line2), FadeOut(axis_arrow2))

        self.next_slide()
