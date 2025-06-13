# Geometric Visualisations with Manim

This project is available in:
- [Русский] https://github.com/GranZoy/FullAndPointVideos/blob/master/Readme.ru.md

This repository contains visual proofs of two geometric problems implemented using the Manim animation library.

## Problem 1: Trapezoid Inscribed in a Circle

**Statement**:  
A trapezoid $ABCD (AB \parallel CD)$ is inscribed in a circle $\Omega$. 
Consider all possible circles $\Gamma$ that are tangent to segment $CD$ and to the arc $CD$ of $\Omega$ not containing points $A$ and $B$. 
When $\Gamma$ is tangent to the sides of angle $\angle 𝐴𝑃𝐵$ at points $K$ and $L$ respectively, prove that the sum $AK + BL$ is constant (independent of the choice of $\Gamma$).

## Problem 2: Two Externally Tangent Circles

**Statement**:  
Given two externally tangent circles $\Omega_1$ and $\Omega_2$ and an angle $\alpha$. 
Tangent $l_1$ to $\Omega_1$ at point $X$ and tangent $l_2$ to $\Omega_2$ at point $Y$ are drawn such that $\angle XPY = \alpha$, 
both circles lie inside $\angle XPY$, $P$ is above the line connecting the centers of $\Omega_1$ and $\Omega_2$ (where $P$ is the intersection of $l_1$ and $l_2$). 
Prove that the angle bisector of ∠𝑋𝑃𝑌 is tangent to a fixed circle.

## Technical Implementation

### Dependencies
- Python 3.7+
- Manim Community Edition (`pip install manim`)
- SymPy (`pip install sympy`)
- Additional custom modules:
  - `changing_point_representation.py`
  - `geometry_tools.py`

### File Structure

├── 01_smt_kozhevnikov.py # Contains Problem 1 animations

├── 02_sharygin_kuharchuk.py # Contains Problem 2 animations

├── geometry_tools.py # Custom geometric calculations

├── changing_point_representation.py # Coordinate conversion utilities

├── media/ # Rendered animations (ignored by git)

├── README.md # This file

└── README.ru.md # This file in Russian language

## How to run
- manim -pqh 01_smt_kozhevnikov.py SMTKozhevnikovProblem  # For Problem 1
- manim -pqh 02_sharygin_kuharchuk.py SharyginKuharchukProblem  # For Problem 2
