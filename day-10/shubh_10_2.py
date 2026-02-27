# part 2 is a bit more complex
import sympy as sp
import numpy as np
import math

cache = {}

debug = False
with open(f"input/d10{"s" if debug else ""}.in") as f:
    lines = [x.strip() for x in f.readlines()]


def apply(state, buttonVal):
    for id in buttonVal:
        state[id] += 1

def over(target, curr):
    return any(c > t for c,t in zip(curr, target))

mins = []

tot = len(lines)
for i, lne in enumerate(lines):
    print(f"{i+1}/{tot}", end = " ")
    lne = lne.split()
    target = tuple(int(x) for x in lne[-1][1:-1].split(','))
    buttons = []
    for x in lne[1:-1]:
        buttons.append(tuple(map(int, x[1:-1].split(","))))
    print(target, end = " ")
    print(buttons, end = " ")
    print()

    # build matrix
    mat: list[list[int]] = [[0 for _ in range(len(buttons)+1)] for _ in range(len(target))]
    for col,b in enumerate(buttons):
        for r in b:
            if r is None: continue
            mat[r][col] = 1
    for i, l in enumerate(target):
        mat[i][-1] = l
    M: sp.Matrix = sp.Matrix(mat)
    M, pivots = M.rref()
    r, c = M.shape
    # print(M.shape)
    if debug:
        sp.pprint(M)
    # print(pivots)
    # sum all the rows
    summed = list(sp.ones(1, r) * M)
    # print(summed)
    if len(pivots) == c-1 and all(_ == 0 or _ == 1 for _ in summed[:-1]):
        # easy
        # check cols
        constant_column = M.col(-1)
        if any(_ < 0 for _ in constant_column):
            print("CONSTANT COL HAS NEGATIVE PLEASE ADDRESS")
            print(constant_column)
        print("easy min", summed[-1])
        mins.append(summed[-1])
    else:
        # free vars :(
        print("not easy :(")
        const_col: list[int] = list(M.col(-1))
        # we need to use these to find a bounds
        free_cols: list[list[int]] = []
        # -1 = fixed
        lowerbds = [0] * len(buttons)
        upbounds = [float('inf')] * len(buttons)
        # we look at any pos vals in the pivot row and find that to be the bounds
        free_col_numers = list(sorted(set(range(len(buttons))) - set(pivots)))
        for c_i in free_col_numers:
            ourcol = M.col(c_i)
            free_cols.append([-_ for _ in ourcol])
            for r_i, val in enumerate(ourcol):
                # this method only works if there is only one free var in the row
                # if there is more than one we hope and pray that it works
                crow = M.row(r_i)
                crow[c_i] = 0
                cntofstuff = len([_ for _ in crow[:-1] if _ != 0])
                if cntofstuff > 1:
                    # only cases for valid are
                    # 1) nothing except for this free var
                    #    (this would only occur if val > 1)
                    # 2) there's one 1 in the pivot
                    # if anything else then there's smth else in the row
                    # then we can't do this trick for bounds
                    continue
                const = const_col[r_i]
                if val > 0:
                    upbounds[c_i] = min(upbounds[c_i], const/val)
                elif val < 0:
                    lowerbds[c_i] = max(lowerbds[c_i], const/val)
        # cut down bounds
        # this makes the indices of the bounds match the indices of the free cols
        # 
        lowerbds = [_ for i,_ in enumerate(lowerbds) if i in set(free_col_numers)]
        upbounds = [(400 if _ == float('inf') else _) for i,_ in enumerate(upbounds) if i in set(free_col_numers)]
        bounds = [(a,b) for a,b in zip(lowerbds, upbounds)]
        
        # now we can build a matrix of (# buttons)x(# free cols + 1)
        M2 = sp.Matrix([const_col] + free_cols).transpose()
        rm2, cm2 = M2.shape
        
        # we gotta insert rows for every button that is a free var
        for i,fci in enumerate(free_col_numers):
            row = [0] * cm2
            row[i+1] = 1
            M2 = M2.row_insert(fci, sp.Matrix([row]))
        
        # NOW our matrix is proper.
        
        # convert M2 to a NumPy float array
        M2_np = np.array(M2.tolist(), dtype=np.float32)
        
        # now we can multiply by [1 c1 c2 ... cN] (col vector) to get the  
        # counts of the buttons, where c1 -> cN is the coeffs of the free vars
        
        # we can also multiply by a matrix representing all the combos we want to try
        
        print("bounds", bounds)
        if (tupled:=tuple(bounds)) in cache:
            A1_np = cache[tupled]
        else:
            axes = [np.arange(math.ceil(a), math.floor(b)+1, dtype=np.int16) 
                    for a,b in bounds]
            grids = np.meshgrid(*axes, indexing='ij')
            # stack all grids into shape (n_free_vars, n_combos)
            A1_np = np.vstack([g.ravel() for g in grids])
            row_ones = np.ones((1, A1_np.shape[1]), dtype=np.int16)
            A1_np = np.vstack((row_ones, A1_np.astype(np.float32)))
            cache[tupled] = A1_np
        
        
        print("M2")
        if debug:
            sp.pprint(M2)
        print("A1")
        # sp.pprint(A1)
        # multiplied
        print("M3 = M2 * A1")
        # just overwrite m2 bc we don't need it anymore (may save on memory?)
        M2_np = M2_np @ A1_np
        # sp.pprint(M3)
        
        # filter cols w/negatives
        print("M3 Cleaned")
        is_positive = np.all(M2_np >= -1e-5, axis=0)
        is_integer = np.all(np.abs(M2_np - np.round(M2_np)) < 1e-5, axis = 0)
        
        valid_mask = is_positive & is_integer
        valid_results = M2_np[:, valid_mask]
        # sp.pprint(M3)
        
        if valid_results.shape[1] > 0:
            sums = np.sum(valid_results, axis=0)
            minsummed = int(np.round(np.min(sums)))
            print("min", minsummed)
            mins.append(minsummed)
            best_idx = np.argmin(sums)
            print("best combo", valid_results[:len(buttons), best_idx])
        else:
            print("no valid combos found in bounds")
    print()

print()
print(mins)
print(len(mins))
print(sum(mins))