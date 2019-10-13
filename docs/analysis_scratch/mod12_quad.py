
def evaluate_quadratic(coeffs, mod):
    f = lambda x: (coeffs[0]*x**2+coeffs[1]*x+coeffs[2])%mod
    out = tuple([f(x) for x in range(mod)])
    return out

def gen_quadratics(mod):
    possible_coeffs=[]
    for a2 in range(mod):
        for a1 in range(mod):
            for a0 in range(mod):
                possible_coeffs.append((a2,a1,a0))
    return possible_coeffs

def quad_census(mod=12):
    all_quads = gen_quadratics( mod)
    unique_quads = {}
    for quad in all_quads:
        output = evaluate_quadratic(quad, mod)
        if output not in unique_quads.keys():
            unique_quads[output] = []
        unique_quads[output].append(quad)
    # print(unique_quads.keys())
    uniques = unique_quads.keys()
    print(len(uniques), mod**3)
    sorted_keys =sorted(
        uniques, key=lambda tup:','.join(['%02d' % el for el in tup])
        )
    # print(sorted_keys)
    # for unique_output in sorted_keys:
    #     print(unique_output)
    #     print(unique_quads[unique_output])

for N in range(4, 17):
    print(N)
    quad_census(N)
