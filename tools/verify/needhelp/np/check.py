"""P / NP / NP-completeness course.

  arith      : numbers recomputed
  graph-red  : f given as 'G,k[,t]' expressions; brute force on random small graphs that it is a reduction from -> to
               (exactly one option may be a valid reduction)
  graph-cex  : candidate inputs; the keyed one is a counterexample to f (x in from XOR f(x) in to), the others are not
  sat-graph  : build the 3SAT->IS / 3SAT->CLIQUE graph of the printed formula and count edges / max independent set
  rules      : rule table
Plus a global sanity block: the textbook reductions preserve yes/no on hundreds of random instances."""
import itertools, random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common import *
from rules import *

rep = Report("np")
levels = load_levels("np")


# ----------------------------------------------------------------------------- graphs
def mk(n, edges):
    return (n, frozenset(frozenset(e) for e in edges))


def comp(G):
    n, E = G
    return (n, frozenset(frozenset(p) for p in itertools.combinations(range(n), 2)) - E)


def has_clique(G, k):
    n, E = G
    if k == 0:
        return True
    return any(all(frozenset(p) in E for p in itertools.combinations(S, 2)) for S in itertools.combinations(range(n), k))


def has_is(G, k):
    return has_clique(comp(G), k)


def has_vc(G, k):
    n, E = G
    return any(all(any(v in e for v in S) for e in E) for S in itertools.combinations(range(n), min(k, n)))


def dbl(G):
    n, E = G
    return (2 * n, E | frozenset(frozenset(v + n for v in e) for e in E))


def disjoint_cliques(G, k):
    n, E = G
    cl = [S for S in itertools.combinations(range(n), k) if all(frozenset(p) in E for p in itertools.combinations(S, 2))]
    return any(not set(a) & set(b) for a, b in itertools.combinations(cl, 2))


def addi(G):
    return (G[0] + 1, G[1])


def fixpar(G):
    return addi(G) if G[0] % 2 else G


def addu(G):
    n, E = G
    return (n + 1, E | frozenset(frozenset((v, n)) for v in range(n)))


LANG = {
    "CLIQUE": lambda G, k, *t: has_clique(G, k),
    "IS": lambda G, k, *t: has_is(G, k),
    "VC": lambda G, k, *t: has_vc(G, k),
    "CLIS": lambda G, k, t: has_clique(G, k) and has_is(G, t),
    "2CLIQUE": lambda G, k: disjoint_cliques(G, k),
    "ECLQ": lambda G, k: G[0] % 2 == 0 and has_clique(G, k),
}


def rand_graph(rng, nmax=6):
    n = rng.randint(1, nmax)
    return mk(n, [p for p in itertools.combinations(range(n), 2) if rng.random() < 0.5])


def instances(rng, count=250):
    for _ in range(count):
        G = rand_graph(rng)
        yield G, rng.randint(1, max(1, G[0]))


def f_eval(expr, G, k):
    n = G[0]
    return eval("(" + expr + ",)", {}, dict(G=G, k=k, n=n, comp=comp, dbl=dbl, addi=addi, fixpar=fixpar, addu=addu))


def is_reduction(src, dst, expr, rng):
    for G, k in instances(rng):
        out = f_eval(expr, G, k)
        if LANG[src](G, k) != LANG[dst](*out):
            return False
    return True


# ----------------------------------------------------------------------------- 3SAT graphs
def sat_graphs(phi):
    V = [(i, j) for i, c in enumerate(phi) for j in range(len(c))]
    isE, clE = set(), set()
    for (i, j), (k, l) in itertools.combinations(V, 2):
        a, b = phi[i][j], phi[k][l]
        if i == k or a == -b:
            isE.add(frozenset(((i, j), (k, l))))
        if i != k and a != -b:
            clE.add(frozenset(((i, j), (k, l))))
    return V, isE, clE


def max_is(V, E):
    for r in range(len(V), 0, -1):
        for S in itertools.combinations(V, r):
            if not any(frozenset(p) in E for p in itertools.combinations(S, 2)):
                return r
    return 0


def satisfiable(phi):
    vs = sorted({abs(l) for c in phi for l in c})
    return any(all(any((a[abs(l)] if l > 0 else not a[abs(l)]) for l in c) for c in phi)
               for a in (dict(zip(vs, bits)) for bits in itertools.product([False, True], repeat=len(vs))))


# ----------------------------------------------------------------------------- global sanity of the textbook reductions
rng = random.Random(7)
for t in range(300):
    m = rng.randint(1, 4)
    nv = rng.randint(1, 3)
    phi = [[rng.choice([-1, 1]) * rng.randint(1, nv) for _ in range(rng.randint(2, 3))] for _ in range(m)]
    V, isE, clE = sat_graphs(phi)
    sat = satisfiable(phi)
    rep.ok((max_is(V, isE) >= m) == sat, f"3SAT->IS wrong on {phi}")
    clique_exists = max_is(V, {frozenset(p) for p in itertools.combinations(V, 2)} - clE) >= m
    rep.ok(clique_exists == sat, f"3SAT->CLIQUE wrong on {phi}")
for G, k in instances(rng, 400):
    rep.ok(has_clique(G, k) == has_is(comp(G), k), "CLIQUE<=IS via complement wrong")
    rep.ok(has_is(G, k) == has_vc(G, G[0] - k), "IS<=VC via n-k wrong")

# ----------------------------------------------------------------------------- the questions
for L, q in questions(levels):
    c, k = q["chk"], q["chk"]["kind"]
    if k == "rules":
        exactly_one(rep, q, [rule(r) for r in c["opts"]], "rules")
    elif k == "graph-red":
        truths = [is_reduction(c["from"], c["to"], e, random.Random(3)) for e in c["opts"]]
        exactly_one(rep, q, truths, f"graph-red {c['from']}<={c['to']}")
    elif k == "graph-cex":
        truths = []
        for n, edges, kk in c["cands"]:
            G = mk(n, edges)
            out = f_eval(c["f"], G, kk)
            truths.append(LANG[c["from"]](G, kk) != LANG[c["to"]](*out))
        exactly_one(rep, q, truths, "graph-cex")
    elif k == "sat-graph":
        V, isE, clE = sat_graphs(c["phi"])
        got = {"IS-edges": len(isE), "CLIQUE-edges": len(clE), "IS-max": max_is(V, isE)}[c["ask"]]
        exactly_one(rep, q, [o == str(got) for o in c["opts"]], f"{c['ask']}={got}")
        for i, o in enumerate(q["options"]):
            rep.ok(plain(o) == str(c["opts"][i]), f"{q['id']}: option text {plain(o)} != annotation {c['opts'][i]}")
    elif not check_common(rep, q):
        rep.ok(False, f"{q['id']}: unknown chk kind {k}")
rep.done()
