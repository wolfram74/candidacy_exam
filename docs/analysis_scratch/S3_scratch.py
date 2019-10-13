'''
elements of S3
e d r rr dr drr
cayley table

e       d       r       rr      dr      drr
d   e   dr  drr   r         rr
r   drr rr  e       d       dr
rr  dr  e   r       drr     d
dr  e   drr d
drr rr

abstract
E1, A1, A2, A3, A4,A5

'''

def D(tri):
    return [tri[0], tri[2], tri[1]]

def R(tri):
    return [tri[1], tri[2], tri[0]]

def E1(tri):
    return tri

def A1(tri):
    return D(tri)
def A2(tri):
    return R(tri)
def A3(tri):
    return R(R(tri))
def A4(tri):
    return D(R(tri))
def A5(tri):
    return D(R(R(tri)))

def cayley_table():
    base = ['A','B','C']
    ops = [E1,A1, A2, A3, A4,A5]
    keyset = None
    for opl in ops:
        print(opl.__name__)
        row = []
        for opr in ops:
            res = opl(opr(base))
            row.append(res)
        results = [''.join(ele) for ele in row]
        # print(results)
        if keyset == None:
            keyset = results
        display = []
        for indr in range(len(results)):
            for indk in range(len(keyset)):
                if results[indr]==keyset[indk]:
                    display.append(ops[indk].__name__)
        print(display)

def test_subgroup():
    base = ['A','B','C']
    ops = [E1,A1, A2, A3, A4,A5]
    Nsub = [A2, A3]
    leftovers = [A1, A4,A5]
    for opm in Nsub:
        for opo in leftovers:
            print(opo(opm(opo(base))), opm(base))


test_subgroup()
