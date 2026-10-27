"""THE CANTOR RAINBOW - exact-integer receipt for rainbow.html (json=0).

Every surviving exponent residue carries its ternary history d1 d2 ... dk
(d0 = 1 for every even n, so it is dropped). Read as a ternary fraction

    x = 0.d1 d2 ... dk  (base 3)  =  num / 3^k,   num = sum d_i * 3^(k-i)

each survivor owns the band [num/3^k, (num+1)/3^k). Survivors never carry a
digit 2, so at every stroke each band keeps its lower two thirds and its top
third goes dark: the burned child. The bands converge on the middle-thirds-
style Cantor set with digits {0,1}, Hausdorff dimension log 2 / log 3.

Axis thirds:  [0,1/3) sound  |  [1/3,2/3) light as seen  |  [2/3,1) unseen.

Gates, all exact integers:
  G1  counts           survivors after stroke k = 2^k, burned = 2^(k-1)
  G2  one burn         every parent has exactly one child with digit 2
  G3  birth colour     burned lift j == (2 - parent's own digit k) mod 3
  G4  gap              burned bands are disjoint from every survivor band
  G5  controls         n = 0, 2, 8 survive every stroke at their known positions
  G6  disjoint         survivor bands at each stroke are pairwise disjoint
"""
import hashlib

KMAX = 12
CONTROLS = {0: None, 2: None, 8: None}


def digit(v, i):
    return (v // 3 ** i) % 3


def main():
    gates = {g: True for g in ("G1", "G2", "G3", "G4", "G5", "G6")}
    print("RAINBOWHDR|schema=CANTOR-RAINBOW-V1|kmax=%d|json=0" % KMAX)
    # stroke 0: parity. n=1 burns (2 = "2"), n=0 survives with d0=1
    surv = [(0, 0)]                       # (residue n mod 2*3^k, num over 3^k)
    print("STROKE|k=0|period=2|survivors=1|burned=1|json=0")
    for k in range(1, KMAX + 1):
        p_prev = 2 * 3 ** (k - 1)
        mod = 3 ** (k + 1)
        new, burned, gaps = [], 0, []
        for a, num in surv:
            dpar = digit(pow(2, a, mod), k)
            kids = []
            for j in range(3):
                n = a + j * p_prev
                d = digit(pow(2, n, mod), k)
                kids.append((j, n, d))
            ds = sorted(d for _, _, d in kids)
            if ds != [0, 1, 2]:
                gates["G2"] = False
            for j, n, d in kids:
                if d == 2:
                    burned += 1
                    if j != (2 - dpar) % 3:
                        gates["G3"] = False
                    gaps.append(3 * num + 2)
                else:
                    new.append((n, 3 * num + d))
        surv = new
        if len(surv) != 2 ** k or burned != 2 ** (k - 1):
            gates["G1"] = False
        nums = sorted(num for _, num in surv)
        if any(b <= a for a, b in zip(nums, nums[1:])):
            gates["G6"] = False
        if set(gaps) & set(nums) or len(gaps) != burned:
            gates["G4"] = False
        per = 2 * 3 ** k
        res = {n % per: num for n, num in surv}
        for c in CONTROLS:
            if c % per not in res:
                gates["G5"] = False
            else:
                CONTROLS[c] = res[c % per]
        thirds = [0, 0, 0]
        for num in nums:
            thirds[(3 * num) // 3 ** k] += 1
        h = hashlib.sha256(",".join(map(str, nums)).encode()).hexdigest()[:16]
        print("STROKE|k=%d|period=%d|survivors=%d|burned=%d|sound=%d|seen=%d|unseen=%d|bands_sha=%s|json=0"
              % (k, per, len(surv), burned, thirds[0], thirds[1], thirds[2], h))
    for c, num in CONTROLS.items():
        print("CONTROL|n=%d|num=%s|den=3^%d|json=0" % (c, num, KMAX))
    print("DIMENSION|log2/log3|survivors=2^k|band_width=3^-k|json=0")
    for g, ok in gates.items():
        print("GATE|%s|%s|json=0" % (g, "PASS" if ok else "FAIL"))
    verdict = "PASS" if all(gates.values()) else "FAIL"
    print("RAINBOW_VERDICT|%s|json=0" % verdict)
    raise SystemExit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()
