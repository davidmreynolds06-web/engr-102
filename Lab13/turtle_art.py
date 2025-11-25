# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 13
# Date: 25 11 2025

from fractions import Fraction
import math
import turtle as t

def _min_iterations_for_angle(angle):
    """Return smallest positive integer n such that n * angle is an integer multiple of 360."""
    # represent angle as a Fraction to handle rational degrees correctly
    frac = Fraction(angle).limit_denominator()
    num, den = frac.numerator, frac.denominator
    # smallest n satisfying n * num/den = m * 360  -> n = (360*den) / gcd(num,360*den)
    g = math.gcd(num, 360 * den)
    n = (360 * den) // g
    return n

def parta(angle, forward=200):
    """Part A: given a turn angle (degrees) determine minimal iterations to return to start and draw."""
    t.title(f"parta: angle={angle}°, steps={_min_iterations_for_angle(angle)}")
    t.speed(0)
    t.hideturtle()
    start = t.position()
    t.dot(6, "red")
    n = _min_iterations_for_angle(angle)
    for _ in range(n):
        t.left(angle)
        t.forward(forward)
    # leave turtle at end (caller can reset or input to pause)
    return n

def _simulate_sequence_once(seq, angle_map, forward):
    """Simulate sequence once (mathematically) starting heading=0 and return (net_disp_complex, delta_heading_degrees)."""
    heading = 0.0
    disp = 0+0j
    for ch in seq:
        heading += angle_map[ch]
        rad = math.radians(heading)
        disp += forward * complex(math.cos(rad), math.sin(rad))
    return disp, heading  # heading is the net change in degrees after one sequence

def partb(seq, forward=150, angle0=30, angle1=-114, max_iters=2000, tol=1e-6):
    """Part B: given a binary sequence (string of '0' and '1'), find smallest number of iterations
    repeating the sequence that returns the turtle to the start; then draw that repeated figure.
    Default angles: '0' -> 30°, '1' -> -114° per problem statement.
    Returns the number of iterations found (or None if not found within max_iters).
    """
    t.title(f"partb: seq='{seq}'")
    t.speed(0)
    t.hideturtle()
    angle_map = {'0': angle0, '1': angle1}
    # compute net displacement and heading change for one sequence (starting heading=0)
    net_disp_one, delta_heading = _simulate_sequence_once(seq, angle_map, forward)
    # if net_disp_one is (0,0) and delta_heading % 360 == 0 then 1 iteration closes
    # brute-force repeating up to max_iters, accumulating displacement and heading
    total_disp = 0+0j
    heading_offset = 0.0
    for k in range(1, max_iters+1):
        # apply one sequence rotated by current heading_offset
        rot = math.radians(heading_offset)
        rotated_disp = complex(math.cos(rot), math.sin(rot)) * net_disp_one
        total_disp += rotated_disp
        heading_offset = (heading_offset + delta_heading) % 360.0
        if abs(total_disp.real) < tol and abs(total_disp.imag) < tol and abs(heading_offset) < 1e-7:
            # draw the figure by actually moving the turtle
            t.dot(6, "red")
            for _ in range(k):
                for ch in seq:
                    t.left(angle_map[ch])
                    t.forward(forward)
            return k
    return None

def partc(seq, angle0, angle1, base_forward=None):
    """Part C: draw a single pass of the provided sequence (string of '0' and '1').
    angle0 and angle1 are the turn angles (degrees) for '0' and '1', respectively.
    base_forward controls the forward step length; if None a reasonable size is chosen based on sequence length.
    """
    n = len(seq)
    if base_forward is None:
        base_forward = max(2, 300 // max(1, n))
    t.title(f"partc: len={n}, angles=({angle0},{angle1}), step={base_forward}")
    t.speed(0)
    t.hideturtle()
    t.dot(6, "red")
    for ch in seq:
        if ch == '0':
            t.left(angle0)
        else:
            t.left(angle1)
        t.forward(base_forward)

def make_spiral_sequence(num_ones):
    """Generate spiral sequence described in prompt: '1' followed by 0 zeros, then '1' + 1 zero, then '1' + 2 zeros, ..."""
    parts = []
    for i in range(num_ones):
        parts.append('1' + ('0' * i))
    return ''.join(parts)

if __name__ == "__main__":
    # main code as required by the lab
    t.reset()
    t.speed(0)
    # Part A
    parta(160)
    input("press Enter to continue...")   # pause
    t.reset()
    parta(141)
    # Part B
    input("press Enter to continue to part B...")
    t.reset()
    k1 = partb("01001")
    print("partb('01001') iterations:", k1)
    input("press Enter to continue...")
    t.reset()
    k2 = partb("01001011")
    print("partb('01001011') iterations:", k2)
    # Part C
    input("press Enter to continue to part C...")
    t.reset()
    seq1 = make_spiral_sequence(20)
    partc(seq1, 0, 90)
    input("press Enter to continue...")
    t.reset()
    partc(seq1, 0, 30)
    input("press Enter to continue...")
    t.reset()
    seq2 = make_spiral_sequence(50)
    partc(seq2, 0, 150)
    input("press Enter to continue...")
    t.reset()
    partc(seq2, 5, 108)
    t.done()
