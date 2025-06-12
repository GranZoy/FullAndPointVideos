from manim import *
import sympy as sy
from changing_point_representation import MakeSympyView
from geometry_tools import CircleTangentToCircleAndPointOnLine, CorrectTangentFromPoint


class SMTKozhevnikovProblem(Scene):
    """Main animation sequence for SMT Kozhevnikov geometric problem."""

    def construct(self):
        self._setup_parameters()
        self._create_circles_and_points()
        self._create_lines_and_arcs()
        self._create_dynamic_objects()
        self._add_problem_text()
        self.SetupUpdaters()
        self.RunAnimations()

    def _setup_parameters(self):
        """Initializes geometric parameters."""
        self.r = 2.5
        self.delta = PI / 6
        self.beta = PI / 4
        self.circle_shift = UP * 0.5

    def _create_circles_and_points(self):
        """Creates and positions all circle and point objects."""
        self.omega = Circle(radius=self.r, color=WHITE).shift(self.circle_shift)

        # Create points on the circle
        self.a = Dot(self.omega.point_at_angle(PI + self.beta))
        self.b = Dot(self.omega.point_at_angle(-self.beta))
        self.c = Dot(self.omega.point_at_angle(PI - self.delta))
        self.d = Dot(self.omega.point_at_angle(self.delta))

    def _create_lines_and_arcs(self):
        """Creates lines and arcs for animation paths."""
        # Create sympy line for calculations
        self.line_cd_sy = sy.Line(MakeSympyView(self.c), MakeSympyView(self.d))

        # Create arcs for circle_tangent_point movement
        self.arc_dc = Arc(
            start_angle=self.delta,
            angle=PI - 2 * self.delta,
            arc_center=self.omega.get_center(),
            radius=self.r
        )
        self.arc_cd = Arc(
            start_angle=PI - self.delta,
            angle=-(PI - 2 * self.delta),
            arc_center=self.omega.get_center(),
            radius=self.r
        )

        # Create lines for line_tangent_point movement
        self.line_dc = Line(self.d.get_center(), self.c.get_center())
        self.line_cd = Line(self.c.get_center(), self.d.get_center(), color=BLUE)
        self.line_ab = Line(self.a.get_center(), self.b.get_center(), color=BLUE)

    def _create_dynamic_objects(self):
        """Initializes animated objects that will be updated."""
        self.circle_tangent_point = Dot(radius=0)
        self.line_tangent_point = Dot(radius=0)
        self.gamma = VMobject()
        self.tangent_a = VMobject()
        self.tangent_b = VMobject()

    def _add_problem_text(self):
        """Creates and positions the problem statement text."""
        self.texts = VGroup(
            Text('Blue segments are parallel', color=WHITE, font="Arial Black").scale(0.6),
            Text('Prove that the sum of the red ones is constant', color=WHITE, font="Arial Black").scale(0.6)
        )
        self.texts.arrange_in_grid(cols=1, rows=2, buff=0.2)
        self.texts.to_edge(DOWN)

    def SetupUpdaters(self):
        """Configures object updaters for dynamic animations."""

        def UpdateGamma(x):
            center, radius = CircleTangentToCircleAndPointOnLine(
                self.circle_tangent_point,
                self.line_tangent_point,
                self.line_cd_sy
            )
            x.become(Circle(radius=radius, color=WHITE).shift(center))

        def UpdateTangentA(x):
            center, radius = CircleTangentToCircleAndPointOnLine(
                self.circle_tangent_point,
                self.line_tangent_point,
                self.line_cd_sy
            )
            tangent_point = CorrectTangentFromPoint(center, radius, self.a)
            x.become(Line(self.a.get_center(), tangent_point, color=RED))

        def UpdateTangentB(x):
            center, radius = CircleTangentToCircleAndPointOnLine(
                self.circle_tangent_point,
                self.line_tangent_point,
                self.line_cd_sy
            )
            tangent_point = CorrectTangentFromPoint(center, radius, self.b)
            x.become(Line(self.b.get_center(), tangent_point, color=RED))

        self.gamma.add_updater(UpdateGamma)
        self.tangent_a.add_updater(UpdateTangentA)
        self.tangent_b.add_updater(UpdateTangentB)

    def RunAnimations(self):
        """Executes the animation sequence."""
        self.add(
            self.line_cd, self.line_ab,
            self.tangent_a, self.tangent_b,
            self.omega, self.gamma,
            self.a, self.b, self.c, self.d,
            self.texts
        )

        # First animation: move along arc_dc and line_dc
        self.play(
            MoveAlongPath(self.circle_tangent_point, self.arc_dc),
            MoveAlongPath(self.line_tangent_point, self.line_dc),
            run_time=4,
            rate_func=linear
        )

        # Second animation: move along arc_cd and line_cd
        self.play(
            MoveAlongPath(self.circle_tangent_point, self.arc_cd),
            MoveAlongPath(self.line_tangent_point, self.line_cd),
            run_time=4,
            rate_func=linear
        )
