"""Rule tables of KNOWN RESULTS, and the closure engine, used by the dec / map / np checkers.

Closure engine (language classes R, RE, coRE).  A claim is "expr is ALWAYS in <class>" or "expr POSSIBLY has
exact class <class>", given premises about the variables.
  - Sound proof:     propagate guaranteed memberships (flags) through the operators with the closure table.
  - Counterexample:  evaluate expr in a small Boolean-algebra MODEL of real languages {empty, Sigma*, X, co-X}
                     (X = A_TM, which is in RE-R, so co-X is in coRE-R) over every assignment that satisfies the
                     premises.  A model counterexample is a genuine counterexample (these four languages exist).
A claim that has neither a proof nor a counterexample is reported as UNPROVEN (the check fails).
"""
import itertools

# ----------------------------------------------------------------------------- classes
CLASSES = ["R", "RE", "coRE", "RE\\R", "coRE\\R", "none"]
FLAGS = {"R": {"R", "RE", "coRE"}, "RE": {"RE"}, "coRE": {"coRE"}, "RE\\R": {"RE"}, "coRE\\R": {"coRE"}, "none": set(),
         "any": set()}
# exact class of the 4 model languages
MODEL = {0b00: "R", 0b11: "R", 0b01: "RE\\R", 0b10: "coRE\\R"}   # empty, Sigma*, X, co-X
MODEL_FLAGS = {k: FLAGS[v] | ({"RE"} if v == "RE\\R" else set()) for k, v in MODEL.items()}
MODEL_FLAGS[0b01] = {"RE"}
MODEL_FLAGS[0b10] = {"coRE"}


def exact_from_flags(fl):
    if "R" in fl or ("RE" in fl and "coRE" in fl):
        return "R"
    if "RE" in fl:
        return "RE\\R"
    if "coRE" in fl:
        return "coRE\\R"
    return "none"


class Sym:
    """guaranteed-membership flags"""
    def __init__(self, fl): self.fl = set(fl)
    def __or__(s, o): return Sym(s.fl & o.fl)
    __and__ = __or__
    def __sub__(s, o): return s & ~o
    def __invert__(s):
        out = set()
        if "R" in s.fl: out |= {"R", "RE", "coRE"}
        if "RE" in s.fl: out.add("coRE")
        if "coRE" in s.fl: out.add("RE")
        return Sym(out)
    def __matmul__(s, o): return Sym(s.fl & o.fl)      # concatenation
    def star(s): return Sym(s.fl)


class Mod:
    """a language of the 4-element model"""
    def __init__(self, bits): self.b = bits
    def __or__(s, o): return Mod(s.b | o.b)
    def __and__(s, o): return Mod(s.b & o.b)
    def __sub__(s, o): return Mod(s.b & ~o.b & 3)
    def __invert__(s): return Mod(~s.b & 3)


PREM = {"R": [0b00, 0b11], "RE": [0b00, 0b11, 0b01], "coRE": [0b00, 0b11, 0b10], "RE\\R": [0b01], "coRE\\R": [0b10],
        "any": [0b00, 0b11, 0b01, 0b10], "none": [0b00, 0b11, 0b01, 0b10]}


def _assignments(prem):
    names = sorted(prem)
    for combo in itertools.product(*[PREM[prem[n]] for n in names]):
        yield dict(zip(names, combo))


def model_classes(expr, prem):
    """set of exact classes the expression takes over all model assignments"""
    return {MODEL[eval(expr, {}, {n: Mod(v) for n, v in a.items()}).b] for a in _assignments(prem)}


def derive(expr, prem):
    return eval(expr, {}, {n: Sym(FLAGS[c]) for n, c in prem.items()}).fl


def claim_truth(expr, prem, claim):
    """claim = 'always:<class>' | 'possible:<class>' ;  returns True/False (raises on UNPROVEN)"""
    mode, cls = claim.split(":", 1)
    fl = derive(expr, prem)
    if mode == "always":
        if cls in ("R", "RE", "coRE"):
            if cls in fl:
                return True
            member = {"R": {0b00, 0b11}, "RE": {0b00, 0b11, 0b01}, "coRE": {0b00, 0b11, 0b10}}[cls]
            if any(eval(expr, {}, {n: Mod(v) for n, v in a.items()}).b not in member for a in _assignments(prem)):
                return False
            raise ValueError(f"UNPROVEN always:{cls} for {expr} given {prem}")
        # strict class: always exactly that class -> false when the model produces anything else
        got = model_classes(expr, prem)
        if got != {cls}:
            return False
        raise ValueError(f"UNPROVEN always:{cls} (model agrees, no proof) for {expr} given {prem}")
    # possible
    if cls in ("RE", "coRE"):    # membership, not an exact class
        want = {"RE": {"R", "RE\R"}, "coRE": {"R", "coRE\R"}}[cls]
        if want & model_classes(expr, prem):
            return True
        raise ValueError(f"UNPROVEN possible:{cls} for {expr} given {prem}")
    if cls in model_classes(expr, prem):
        return True
    ex = exact_from_flags(fl)
    if ex != "none" and cls != ex and not (ex == "R" and cls in ("RE", "coRE")):
        return False           # derived flags already pin the exact class to something else
    if cls == "none" and fl:
        return False
    raise ValueError(f"UNPROVEN possible:{cls} for {expr} given {prem}")


# ----------------------------------------------------------------------------- named languages (course facts)
FACTS = {
    "A_TM": "RE\\R", "H_TM": "RE\\R", "E_TM": "coRE\\R", "notE_TM": "RE\\R",
    "coA_TM": "coRE\\R", "coH_TM": "coRE\\R", "EQ_TM": "none", "ALL_TM": "none", "INF_TM": "none", "FIN_TM": "none",
    "coEQ_TM": "none", "coALL_TM": "none",
    "A_DFA": "R", "E_DFA": "R", "PATH": "R", "SAT": "R", "empty": "R", "Sigma*": "R", "H10": "RE\\R",
}


def complement_class(c):
    return {"R": "R", "RE\\R": "coRE\\R", "coRE\\R": "RE\\R", "none": "none"}[c]


# classification by the SHAPE of a condition on machines (from the course: simulate / exists / for-all)
SHAPES = {
    "bounded": "R",          # a fixed or computable step/cell bound: simulate up to the bound
    "exists": "RE\\R",       # exists w / exists a run that ends well, non-trivial
    "forall": "coRE\\R",     # for all w / never accepts / never halts, non-trivial
    "count_ge": "RE\\R",     # |L(M)| >= k : wait for k accepted words
    "count_le": "coRE\\R",   # |L(M)| <= k : complement is |L(M)| > k
    "specific": "none",      # L(M) = specific language, inclusion, equality, |L(M)| = k
    "trivial": "R",          # a condition every machine satisfies / none does
    "automaton": "R",        # the input is a DFA/CFG, not a Turing machine
}


# ----------------------------------------------------------------------------- yes/no rule table
# id -> (truth, justification).  These are the known results of the course; every question option that is a
# general statement is annotated with one of these ids and the checker compares.
RULES = {
    # inclusion between classes
    "R_sub_RE": (True, "a decider is a recognizer"),
    "RE_sub_R": (False, "A_TM is in RE and not in R"),
    "R_eq_RE": (False, "A_TM"),
    "RE_eq_coRE": (False, "A_TM in RE, not in coRE"),
    "RE_or_coRE_gives_R": (False, "A_TM is in RE; the union RE u coRE is bigger than R"),
    # Post's theorem and its uses
    "post.both_RE": (True, "L and complement in RE  =>  L in R"),
    "post.only_L_RE": (False, "A_TM"),
    "post.only_coL_RE": (False, "complement of A_TM"),
    "post.in_RE_and_coRE": (True, "R = RE cap coRE"),
    "swap.nonhalting": (False, "swapping acc/rej of a machine that loops keeps the loops"),
    "swap.decider": (True, "swapping acc/rej of a halting machine decides the complement"),
    "compl.RE_notR_not_RE": (True, "if L in RE-R then complement not in RE, else Post gives L in R"),
    "compl.RE_closed": (False, "A_TM"),
    "compl.R_closed": (True, "swap acc/rej of a decider"),
    "compl.coRE_closed": (False, "co-A_TM"),
    "sandwich.R": (False, "empty <= A_TM <= Sigma*"),
    "finite.R": (True, "a finite language is decided by a table"),
    "subset_of_RE_in_RE": (False, "empty subset of A_TM; but also subsets of A_TM outside RE exist"),
    "subset_of_R_in_RE": (False, "every language is a subset of Sigma*, which is in R"),
    "L_M_always_RE": (True, "M accepts L(M)"),
    "L_M_always_R": (False, "A_TM = L(U)"),
    "L_M_always_coRE": (False, "A_TM = L(U) is not in coRE"),
    "L_M_always_finite": (False, "a machine accepting everything"),
    "L_M_in_R_implies_M_decides": (False, "M may loop on words outside L(M)"),
    "R_implies_exists_decider": (True, "definition"),
    "NTM_language_RE": (True, "an NTM is simulated by a TM"),
    "union_finite_R_infinite": (False, "every language is an infinite union of singletons"),
    # reductions
    "red.R_down": (True, "A<=B, B in R  =>  A in R"),
    "red.RE_down": (True, "A<=B, B in RE  =>  A in RE"),
    "red.coRE_down": (True, "A<=B, B in coRE  =>  A in coRE"),
    "red.R_up": (False, "A in R, B = A_TM"),
    "red.RE_up": (False, "A = empty in RE, B not in RE"),
    "red.notR_up": (False, "A not in R says nothing about easier... B can be harder only"),
    "red.notR_flows": (True, "A<=B, A not in R  =>  B not in R"),
    "red.notRE_flows": (True, "A<=B, A not in RE  =>  B not in RE"),
    "red.notcoRE_flows": (True, "A<=B, A not in coRE  =>  B not in coRE"),
    "red.B_notR_gives_A_notR": (False, "A = empty"),
    "red.B_notRE_gives_A_notRE": (False, "A = empty is in RE although B may not be"),
    "red.coRE_down_to_RE": (False, "A = A_TM <=m ... B in coRE does not make A in RE (A_TM <=m ALL_TM... or A<=B with B=co-A_TM, A=co-A_TM)"),
    "red.complement_one_side": (False, "A <=m B does not give complement(A) <=m B (A_DFA <=m H_TM but not the complement version, 24A-A-Q11 style)"),
    "red.complement_target_only": (False, "A <=m complement(B) is a different relation from A <=m B"),
    "red.complement_swapped": (False, "complement(B) <=m complement(A) is the converse direction"),
    "red.common_source": (False, "two targets of one source need not reduce to each other"),
    "red.common_target": (False, "two sources of one target need not reduce to each other"),
    "red.equiv_means_equal": (False, "A_TM and H_TM reduce to each other and differ"),
    "red.coRE_up": (False, "A = empty is in coRE although B may not be"),
    "red.RE_down_wrong_class": (False, "B in coRE does not make A decidable"),
    "proof.notRE_from_coATM": (True, "co-A_TM is not in RE and hardness flows right"),
    "proof.ATM_gives_notRE": (False, "L=H_TM is in RE"),
    "proof.L_to_coATM": (False, "L <=m co-A_TM only shows L is in coRE"),
    "proof.L_to_ATM": (False, "L <=m A_TM only shows L is in RE"),
    "proof.ATM_gives_notR_notcoRE": (True, "A_TM not in R, and complement(A_TM) <=m complement(L) with complement(A_TM) not in RE"),
    "proof.ATM_gives_in_RE": (False, "L = EQ_TM"),
    "proof.ATM_gives_in_coRE": (False, "L cannot be in coRE"),
    "x.L_le_coL_RE_in_R": (True, "complement(L) <=m L, L in RE => complement(L) in RE => Post"),
    "x.L_le_coL_RE_in_RE_notR": (False, "it is in R"),
    "x.L_le_coL_RE_coRE_notR": (False, "it is in R"),
    "x.L_le_coL_RE_none": (False, "it is in RE"),
    "red.f_just_writes_code": (True, "f only writes the code of K"),
    "red.f_needs_K_halt": (False, "f does not run K"),
    "red.f_needs_M_halt": (False, "f does not run M"),
    "red.f_needs_H_decidable": (False, "f is a plain text transformation"),
    "np.NP_sub_R": (True, "simulate the nondeterministic tree"),
    "np.NP_undecidable": (False, "NP is inside R"),
    "np.NP_sub_coRE_notR": (False, "NP is inside R"),
    "np.HTM_in_NP": (False, "H_TM is not decidable"),
    "np.P_compl": (True, "course theorem"),
    "np.P_eq_NP_gives_NP_eq_coNP": (True, "course theorem"),
    "np.P_sub_NPcoNP": (True, "course theorem"),
    "np.open_NPcoNP_notP": (True, "course theorem"),
    "np.coSAT_in_NP_gives_NP_eq_coNP": (True, "course theorem"),
    "pr.NP_down": (True, "course theorem"),
    "pr.HTM_hard_notC": (True, "course theorem"),
    "pr.SAT_to_L": (True, "course theorem"),
    "pr.NPC_to_hard": (True, "course theorem"),
    "np2.P_eq_NP": (True, "course theorem"),
    "np2.PATH_NPC_if_PNP": (True, "course theorem"),
    "np2.empty_never_NPC": (True, "course theorem"),
    "np2.SATtoPATH_PNP": (True, "course theorem"),
    "np2.coNP_eq_NP": (True, "course theorem"),
    "np.NP_compl_proved": (False, "does not follow / open problem / contradicts the premise"),
    "np.NP_not_compl_proved": (False, "does not follow / open problem / contradicts the premise"),
    "np.NP_union_not_concat": (False, "does not follow / open problem / contradicts the premise"),
    "np.P_eq_NP_gives_P_ne_coNP": (False, "does not follow / open problem / contradicts the premise"),
    "np.P_eq_NP_gives_NPcoNP_ne_P": (False, "does not follow / open problem / contradicts the premise"),
    "np.P_eq_NP_gives_CLIQUE_notP": (False, "does not follow / open problem / contradicts the premise"),
    "np.proved_NPcoNP_sub_P": (False, "does not follow / open problem / contradicts the premise"),
    "np.proved_NP_sub_coNP": (False, "does not follow / open problem / contradicts the premise"),
    "np.proved_P_eq_NP": (False, "does not follow / open problem / contradicts the premise"),
    "np.SAT_in_NPcoNP_notP": (False, "does not follow / open problem / contradicts the premise"),
    "np.PRIME_example": (False, "does not follow / open problem / contradicts the premise"),
    "np.proved_no_NPcoNP_notP": (False, "does not follow / open problem / contradicts the premise"),
    "np.coSAT_in_NP_gives_SAT_in_P": (False, "does not follow / open problem / contradicts the premise"),
    "np.coSAT_in_NP_gives_P_eq_NP": (False, "does not follow / open problem / contradicts the premise"),
    "np.coSAT_in_NP_gives_SAT_notNP": (False, "does not follow / open problem / contradicts the premise"),
    "pr.NP_up": (False, "does not follow / open problem / contradicts the premise"),
    "pr.hard_down": (False, "does not follow / open problem / contradicts the premise"),
    "pr.P_up": (False, "does not follow / open problem / contradicts the premise"),
    "pr.HTM_C_if_PNP": (False, "does not follow / open problem / contradicts the premise"),
    "pr.HTM_C": (False, "does not follow / open problem / contradicts the premise"),
    "pr.HTM_not_hard": (False, "does not follow / open problem / contradicts the premise"),
    "pr.L_to_SAT": (False, "does not follow / open problem / contradicts the premise"),
    "pr.L_to_PATH": (False, "does not follow / open problem / contradicts the premise"),
    "pr.PATH_to_L": (False, "does not follow / open problem / contradicts the premise"),
    "pr.hard_to_NPC": (False, "does not follow / open problem / contradicts the premise"),
    "pr.NPC_to_NP": (False, "does not follow / open problem / contradicts the premise"),
    "pr.NPC_to_P": (False, "does not follow / open problem / contradicts the premise"),
    "np2.P_ne_NP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.NP_ne_coNP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.SAT_notP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.PATH_notNPC": (False, "does not follow / open problem / contradicts the premise"),
    "np2.PATH_NPC_always": (False, "does not follow / open problem / contradicts the premise"),
    "np2.PATH_notNP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.empty_NPC_if_PNP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.Sigma_NPC_if_PNP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.finite_NPC_always": (False, "does not follow / open problem / contradicts the premise"),
    "np2.SATtoPATH_PneNP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.SATtoPATH_PATHnotP": (False, "does not follow / open problem / contradicts the premise"),
    "np2.SATtoPATH_NPnotclosed": (False, "does not follow / open problem / contradicts the premise"),
    "np2.L_in_P": (False, "does not follow / open problem / contradicts the premise"),
    "np2.P_eq_NP2": (False, "does not follow / open problem / contradicts the premise"),
    "np2.L_notNP": (False, "does not follow / open problem / contradicts the premise"),
    "red.symmetric": (False, "A<=B does not give B<=A (A in R, B = A_TM)"),
    "red.transitive": (True, "compose the two functions"),
    "red.complement_same_f": (True, "A<=B  iff  complement A <= complement B (same f)"),
    "red.R_to_any_nontrivial": (True, "decide x, output a fixed yes or no word"),
    "red.nonR_to_nontrivial_R_not_needed": (False, "needs A in R"),
    "red.RE_RE_to_coRE": (False, "no reduction between RE-R and coRE-R in either direction"),
}


def rule(rid):
    return RULES[rid][0]
