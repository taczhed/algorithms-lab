def root_bisection(coeffs, a, b, eps):
    def f(x):
        # Evaluate the polynomial at x
        return sum(c * x ** i for i, c in enumerate(coeffs))

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("-- f(a) and f(b) must have opposite signs (root must exist in [a, b]).")

    while (b - a) / 2.0 > eps:
        mid = (a + b) / 2.0
        fmid = f(mid)

        if abs(fmid) < eps:
            return mid

        if fa * fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid

    return (a + b) / 2.0