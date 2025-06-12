from manim import *
from math import sqrt
from geometry_tools import TwoPointsTangsIntersection


class SharyginKuharchukProblem(Scene):
    """Main animation sequence for Sharygin-Kuharchuk geometric problem."""
    def construct(self):
        self._setup_parameters()
        self._create_circles()
        self._create_arcs()
        self._create_dynamic_objects()
        self.SetupUpdaters()
        self.RunAnimations()

    def _setup_parameters(self):
        """
        Initializes geometric parameters and scene configuration.
        Note: According to solution we have r_gamma as (r1 - r2) / 2.
        """
        self.r1 = 1
        self.r2 = 2
        self.r_gamma = (self.r2 - self.r1) / sqrt(2)
        self.alpha = PI * 5 / 7
        self.phi = PI / 3
        self.common_shift = DOWN
        self.omega1_center = LEFT * 1.5 * self.r1 + self.common_shift
        self.omega2_center = RIGHT * 2 * self.r1
        self.gamma_center = LEFT * 1.5 * self.r1 + DOWN + (RIGHT + self.common_shift) * (self.r1 + self.r2) / 2

    def _create_circles(self):
        """Creates and positions all circle objects in the scene."""
        self.omega1 = Circle(radius=self.r1, color=WHITE).shift(self.omega1_center)
        self.omega2 = Circle(radius=self.r2, color=WHITE)\
            .align_to(self.omega1.copy().shift(self.omega2_center), LEFT)\
            .shift(self.common_shift)
        self.gamma = DashedVMobject(Circle(radius=self.r_gamma, color=WHITE).shift(self.gamma_center))
        self.add(self.omega1, self.omega2, self.gamma)

    def _create_arcs(self):
        """
        Creates animation paths for tangent points

        Initializes:
        - Primary arcs (arc1, arc2, arc_gamma) for forward motion
        - Reverse arcs (arc1_rev, etc.) for return motion
        """
        self.arc1 = Arc(start_angle=self.alpha,
                        angle=self.phi,
                        arc_center=self.omega1.get_center(),
                        radius=self.r1)
        self.arc2 = Arc(start_angle=self.alpha - PI / 2,
                        angle=self.phi,
                        arc_center=self.omega2.get_center(),
                        radius=self.r2)
        self.arc_gamma = Arc(start_angle=self.alpha - PI * 3 / 4,
                             angle=self.phi,
                             arc_center=self.gamma.get_center(),
                             radius=self.r_gamma)

        self.arc1_rev = Arc(start_angle=self.alpha + self.phi,
                            angle=-self.phi,
                            arc_center=self.omega1.get_center(),
                            radius=self.r1)
        self.arc2_rev = Arc(start_angle=self.alpha - PI / 2 + self.phi,
                            angle=-self.phi,
                            arc_center=self.omega2.get_center(),
                            radius=self.r2)
        self.arc_gamma_rev = Arc(start_angle=self.alpha - PI * 3 / 4 + self.phi,
                                 angle=-self.phi, arc_center=self.gamma.get_center(),
                                 radius=self.r_gamma)

    def _create_dynamic_objects(self):
        """
        Initializes animated objects

        - The first 3 will follow arc paths
        - The rest will depend on them
        """
        self.tangent_point1 = Dot(radius=0)
        self.tangent_point2 = Dot(radius=0)
        self.tangent_point_gamma = Dot(radius=0)

        self.tangent1 = VMobject()
        self.tangent2 = VMobject()
        self.bisector = VMobject()
        self.tangents_intersection_point = VMobject()
        self.angle1 = VMobject()
        self.angle2 = VMobject()

    def SetupUpdaters(self):
        """Configures object updaters for dynamic animations"""

        def GetTangentIntersectionPoint():
            """Helper: Calculates current tangent lines intersection"""
            return TwoPointsTangsIntersection(self.tangent_point1, self.tangent_point2, self.omega1, self.omega2)

        self.tangent1.add_updater(lambda x: x.become(
            Line(self.tangent_point1.get_center(), GetTangentIntersectionPoint())
        ))
        self.tangent2.add_updater(lambda x: x.become(
            Line(self.tangent_point2.get_center(), GetTangentIntersectionPoint())
        ))
        self.bisector.add_updater(lambda x: x.become(
            Line(self.tangent_point_gamma.get_center(), GetTangentIntersectionPoint())
        ))
        self.tangents_intersection_point.add_updater(lambda x: x.become(
            Dot(GetTangentIntersectionPoint())
        ))

        self.angle1.add_updater(lambda x: x.become(
            Angle(
                Line(self.tangent_point1.get_center(), GetTangentIntersectionPoint()),
                Line(self.tangent_point_gamma.get_center(), GetTangentIntersectionPoint()),
                quadrant=(-1, -1),
                radius=0.4
            )))

        self.angle2.add_updater(lambda x: x.become(
            Angle(
                Line(self.tangent_point_gamma.get_center(), GetTangentIntersectionPoint()),
                Line(self.tangent_point2.get_center(), GetTangentIntersectionPoint()),
                quadrant=(-1, -1),
                radius=0.5
            )))

    def RunAnimations(self):
        """
        Executes the animation sequence

        Plays:
        1. Forward motion along arcs (4 seconds)
        2. Reverse motion back along arcs (4 seconds)
        """

        self.add(
            self.tangent1, self.tangent2,
            self.bisector, self.tangents_intersection_point,
            self.angle1, self.angle2
        )

        self.play(MoveAlongPath(self.tangent_point1, self.arc1),
                  MoveAlongPath(self.tangent_point2, self.arc2),
                  MoveAlongPath(self.tangent_point_gamma, self.arc_gamma),
                  run_time=4,
                  rate_func=linear)
        self.play(MoveAlongPath(self.tangent_point1, self.arc1_rev),
                  MoveAlongPath(self.tangent_point2, self.arc2_rev),
                  MoveAlongPath(self.tangent_point_gamma, self.arc_gamma_rev),
                  run_time=4,
                  rate_func=linear)
