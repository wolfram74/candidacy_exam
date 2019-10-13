import sympy

def eq1_stuff():
    cos = sympy.cos
    sin = sympy.sin
    pi = sympy.pi
    xp, xp1, yp, yp1, p, n = sympy.symbols(
        'x_p x_p+1 y_p y_p+1 p n'
        ,real=True
        )
    gam = sympy.symbols('gamma')
    simple = (
        (xp1-xp)*cos((p-1)*gam)+
        (yp1-yp)*sin((p-1)*gam)
        )**2
    # simple = (
    #     (xp1-xp)*cos((p-1)*2*pi/n)+
    #     (yp1-yp)*sin((p-1)*2*pi/n)
    #     )**2
    # simple = simple.subs(2*pi/n, gam)
    sympy.pprint(simple)
    print('expanded')
    sympy.pprint(simple.expand())
    print('reduced')
    sympy.pprint(simple.expand().simplify())

eq1_stuff()
