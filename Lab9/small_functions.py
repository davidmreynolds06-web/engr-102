# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 9
# Date: 27 10 2025

def parta(nums):
    if not nums:
        raise ValueError("nums must contain at least one number")
    s = sorted(nums)
    n = len(s)
    min_num = s[0]
    max_num = s[-1]
    mid = n // 2
    if n % 2 == 1:
        med = s[mid]
    else:
        med = (s[mid - 1] + s[mid]) / 2
    return (min_num, med, max_num)

def partb(times, dists):
    """Return list of velocities between consecutive time measurements.
    times must be strictly increasing and times and dists must have the same length.
    """
    if len(times) != len(dists):
        raise ValueError("times and dists must have the same length")
    if len(times) < 2:
        return []
    vels = []
    for i in range(1, len(times)):
        dt = times[i] - times[i - 1]
        if dt <= 0:
            raise ValueError("times must be strictly increasing (no zero or negative intervals)")
        vels.append((dists[i] - dists[i - 1]) / dt)
    return vels

def partc(nums):
    """Return the product of two numbers in nums that sum to 2029, or False if none exist."""
    seen = set()
    for num in nums:
        target = 2029 - num
        if target in seen:
            return num * target
        seen.add(num)
    return False

def partd(n):
    """Return a list of 2+ consecutive positive even integers that sum to n, or False."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # max L satisfies L*(L+1) <= n  ->  L <= (sqrt(1+4n)-1)/2
    max_L = int(((1 + 4 * n) ** 0.5 - 1) // 2)
    for L in range(2, max_L + 1):
        numerator = n - L * (L - 1)
        denom = 2 * L
        if numerator <= 0:
            continue
        if numerator % denom == 0:
            m = numerator // denom
            if m >= 1:
                return [2 * (m + i) for i in range(L)]
    return False

def parte(radius_sphere, radius_hole):
    """Return volume of the napkin-ring (sphere with a cylindrical hole).
    radius_sphere = R, radius_hole = r. Raises ValueError for invalid inputs.
    Uses V = (pi * h^3) / 6 where h = 2*sqrt(R^2 - r^2).
    """
    import math
    R = float(radius_sphere)
    r = float(radius_hole)
    if R <= 0 or r < 0:
        raise ValueError("sphere radius must be > 0 and hole radius must be >= 0")
    if r > R:
        raise ValueError("hole radius cannot exceed sphere radius")
    h = 2.0 * math.sqrt(R * R - r * r)
    return math.pi * h**3 / 6.0

def partf(border_char, name, company, email):
    """Return a digital business card string using border_char and 2-space padding."""
    if not border_char:
        raise ValueError("border character must be a non-empty string")
    padding = 2
    entries = [str(name), str(company), str(email)]
    max_len = max(len(e) for e in entries)
    inner_width = max_len + padding * 2
    top = border_char * (inner_width + 2)
    lines = [top]
    for e in entries:
        lines.append(
            f"{border_char}{' ' * padding}{e}{' ' * (max_len - len(e))}{' ' * padding}{border_char}"
        )
    lines.append(top)
    return "\n".join(lines)

def partg(x, tol):
    """Return sum of series ln((1+x)/(1-x)) = sum_{n=1}^\infty 2/(2n-1) * x^(2n-1)
    Continue until absolute value of term is less than tol.
    """
    if not (-1 < x < 1):
        raise ValueError("x must be between -1 and 1 (exclusive)")
    if tol <= 0:
        raise ValueError("tolerance must be positive")
    total = 0.0
    power = float(x)  # x^(2n-1) with n starting at 1
    n = 1
    while True:
        term = 2.0 * power / (2 * n - 1)
        if abs(term) < tol:
            break
        total += term
        power *= x * x  # increase exponent by 2 for next term
        n += 1
    return total

