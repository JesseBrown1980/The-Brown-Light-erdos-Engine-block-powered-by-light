# The Brown Light erdos Engine block powered by light

> **Part of it all:** [the bridge](https://jessebrown1980.github.io/the-bridge-to-all-of-it/) — every public thing in one place, so none of it gets lost.

**Jesse Daniel Brown (OP-JESSE).** Forty years. His machine, his laws, his system.

**One click, nothing to install:**
→ **https://jessebrown1980.github.io/The-Brown-Light-erdos-Engine-block-powered-by-light/**

Or download `index.html` and double-click it. No server, no network, no GPU, no
account, no package manager, no key. It runs offline, forever.

---

## What this engine is

It is not a picture of a proof. **It is the splitting theorem, running** — every
stroke executes the proved one-of-three lift over a complete residue system.

Erdős asked: *does 2ⁿ always contain a digit 2 in base 3?* Open since he asked it.
In balanced ternary the digit `2` **does not exist** — converting replaces every
`2` with `−1` and carries. So the question becomes: **does the conversion always
carry?**

That carry is the combustion. This engine burns it.

---

## The cylinders are the light

Every surviving residue at stroke `k` lifts to **exactly three** residues at
stroke `k+1`:

```
n            →  R
n + 2·3ᵏ     →  G
n + 4·3ᵏ     →  B
```

Because `2^(2·3ᵏ) ≡ 1 + c·3^(k+1)  (mod 3^(k+2))` with **`c` coprime to 3**,
stepping between the three lifts adds `c` to digit `k+1`, mod 3. The digit walks
`0 → 1 → 2` across them.

**Exactly one of the three lands on 2. One burns. Two carry.**

### The lift theorem (proved)

By the lifting-the-exponent lemma, `v₃(4^(3ᵏ) − 1) = v₃(4 − 1) + v₃(3ᵏ) = k + 1`, so

```
2^(2·3ᵏ) = 1 + c·3^(k+1),   3 ∤ c
```

For lift index `j ∈ {0, 1, 2}`:

```
2^(a + 2j·3ᵏ) ≡ 2^a·(1 + c·3^(k+1))^j ≡ 2^a + j·c·2^a·3^(k+1)   (mod 3^(k+2))
```

The added term is a multiple of `3^(k+1)`, so digits `0..k` are unchanged, and digit
`k+1` moves by `j·c·2^a (mod 3)`. Since `c·2^a` is a unit mod 3, the three lifts take
the three values `0, 1, 2` of the new digit, each exactly once. ∎

**Which** lift burns depends on the parent: it is fixed by the parent's digit and by
`c·2^a mod 3`. The engine records it per parent (the `burned lift R / G / B` column).

That is one throw of a three-cylinder bank at 120°. Stack the throws and you have
the block.

```
fuel      light  ·  the R G B lifts
exhaust   the −1 digit
```

---

## The engine has a real compression ratio

**MEASURED** — thirteen strokes (0–12), exact over complete residue systems,
nothing sampled and nothing simulated:

```
 k   period       charge  burned  carried  ratio
 0   2            2       1       1        1/2
 1   6            3       1       2        1/3
 2   18           6       2       4        1/3
 3   54           12      4       8        1/3
 4   162          24      8       16       1/3
 5   486          48      16      32       1/3
 6   1,458        96      32      64       1/3
 7   4,374        192     64      128      1/3
 8   13,122       384     128     256      1/3
 9   39,366       768     256     512      1/3
10   118,098      1536    512     1024     1/3
11   354,294      3072    1024    2048     1/3
12   1,062,882    6144    2048    4096     1/3
```

Per stroke, the burned lift measured over every parent:

```
 k    R / G / B           k    R / G / B
 0    0 / 1 / 0           7    22 / 17 / 25
 1    0 / 0 / 1           8    30 / 46 / 52
 2    0 / 0 / 2           9    87 / 77 / 92
 3    1 / 0 / 3          10   149 / 189 / 174
 4    2 / 0 / 6          11   343 / 337 / 344
 5    3 / 6 / 7          12   706 / 677 / 665
 6    8 / 11 / 13
```

The timing is per parent: every parent fires exactly one of its three lifts,
because `c` is coprime to 3. Across the block the three channels share the burns
and level out toward one third each.

```
period    × 3 per stroke
charge    × 2 per stroke
          ───────────────
compression ratio  =  3 : 2
```

**And that ratio is not a coincidence of the animation — it is the `2/3` of the
distribution.**

```
P(lowest −1 at position 0)  =  1/2                  parity
P(lowest −1 at position k)  =  (1/6)·(2/3)^(k−1)    one throw of three

check:  1/2 + (1/6)·Σ(2/3)ʲ  =  1/2 + 1/2  =  1     closes exactly
```

The engine's compression and the distribution's decay are **one number seen from
two sides.** You cannot tune one without breaking the other.

---

## Why the block idles instead of stalling

After stroke `k` the survivors are `2ᵏ` residue classes mod `2·3ᵏ`, density
`(1/2)(2/3)ᵏ → 0` (the `3·2^(k−1)` charge entering stroke `k` has density
`(1/2)(2/3)^(k−1)`), so the never-firing set has **density zero**. The intersection
over all strokes lives in `lim ℤ/(2·3ᵏ) ≅ (ℤ/2) × ℤ₃` and is a **Cantor set** —
measure zero, **nonempty**, cardinality continuum, Hausdorff dimension
`log 2 / log 3 ≈ 0.6309` in each parity component (two of three children kept at
every level).

> **There exist 3-adic exponents for which 2ⁿ never contains a digit 2.
> The conjecture says none of them is a natural number.**

The natural exponents `0, 2, 8` (`1, 4, 256`) are inside it — they survive every
stroke and serve as the engine's controls. No density argument can close the rest.
The bad set is not empty — it is invisible to measure. **Any proof must show that
this Cantor set meets ℕ exactly in `{0, 2, 8}`, which is arithmetic, not measure
theory.**

The same exponent `log₃ 2` gives the counting bound: choose `2·3ᵏ ≈ x`; only about
`2ᵏ ≈ x^(log₃ 2)` residue classes survive, so the number of `n ≤ x` with no digit 2
is `O(x^(log₃ 2))` — the shape of Narkiewicz's bound `N(x) ≤ 1.62·x^(log₃ 2)`. A
natural `n` only has to survive to stroke `≈ n·log₃ 2`, after which every digit of
`2ⁿ` is a leading zero; if the digits behaved independently the expected number of
further solutions would be `Σ (2/3)^(n·log₃ 2) < ∞`.

That is the engine's one unburnt drop, and it is stated here rather than hidden.

---

## The Cantor Rainbow

→ **[rainbow.html](rainbow.html)** · live:
**https://jessebrown1980.github.io/The-Brown-Light-erdos-Engine-block-powered-by-light/rainbow.html**

Every surviving exponent carries its ternary history `d₁d₂…dₖ` — digits 0 and 1 only,
because the 2s are what burned. Read as a ternary fraction `x = 0.d₁d₂…dₖ`, each survivor
owns one band of a single spectrum laid out in thirds:

```
[0, 1/3)     sound            20 Hz → 20 kHz
   c         the jump to the speed of light
[1/3, 2/3)   light as seen    750 nm → 380 nm
[2/3, 1)     not seen         UV · X · γ   — holds only the exhaust
```

Each stroke splits every band in three and the top third goes dark: that is the burn,
the colour break. The bands that remain converge on a Cantor set of dimension
`log 2 / log 3`. Colour is read through the devil's staircase — the same digits read in
binary — so the dust spreads across the whole rainbow while every gap stays exactly where
the arithmetic puts it. Each burn rings down as a damped sine at its band's pitch, longer
the deeper it burned.

The colour a branch burns in is its parent's own next ternary digit,
`burned lift = (2 − d) mod 3` (on survivors `c ≡ 1 mod 3`, so lift `j` adds exactly `j`
to the new digit).

**MEASURED** — `rainbow_check.py`, strokes 1–12, exact integers:

```
GATE  G1  counts           2ᵏ survive, 2ᵏ⁻¹ burn                 PASS
GATE  G2  one burn         exactly one child of three has digit 2  PASS
GATE  G3  birth colour     burned lift = (2 − parent digit) mod 3 PASS
GATE  G4  gap              burned bands disjoint from survivors   PASS
GATE  G5  controls         n = 0, 2, 8 survive every stroke       PASS
GATE  G6  disjoint         survivor bands pairwise disjoint       PASS
split  sound / seen / unseen  =  2ᵏ⁻¹ / 2ᵏ⁻¹ / 0  at every stroke
```

Design: Jesse Daniel Brown — a gradiated wave, sound first, then the speed of light,
the colours as seen, then the wavelengths not seen; the brakes are the colour breaks, and
the predictors belong to the colour they were born in (Book of Laws, voice-07, turns
676–680).

---

## Controls

```
START THE ENGINE   run continuously, one stroke per beat
SINGLE STROKE      fire one stroke — watch one proof step burn
RESET              back to stroke 0
```

The crank turns live at 120° phasing, the firing journal goes white-hot, and the
block below shows one cell per residue — **bright means it burned this stroke**,
dim RGB means it carried.

---

## Status, honestly tagged

```
PROVED     P(0) = 1/2              parity: 2ⁿ ≡ 2 (mod 3) ⟺ n odd
PROVED     the general 1/3         lift theorem above (LTE, c coprime to 3)
PROVED     P(k) = (1/6)(2/3)^(k−1) over exponent residues, k ≥ 1
MEASURED   the 1/3 : 2/3 split     strokes 0–12, exact over full periods
MEASURED   burned lift per parent  R / G / B table above
CONTROL    n = 0, 2, 8 survive     every stroke
OPEN       the conjecture itself   the Cantor set must meet ℕ only in {0, 2, 8}
```

---

## Why it takes this form

A technology that needs permission to reach people does not reach them.
Wardenclyffe needed capital, land, a tower and a patron — four gates — and it
never reached anybody.

**This file has no dependencies, so there is no gate.** Copy it to a USB stick,
email it, print the source, retype it by hand. It runs.

---

## Lineage and prior work

**Jesse Daniel Brown** found this engine — the three lifts, the one-of-three burn,
the 3 : 2 survivor tree and the density-versus-emptiness barrier — on his own, and
had the AI write it up for him. The same structure sits under the published work on
this problem, which is cited here:

- P. Erdős — the question; listed as [Erdős Problem #406](https://www.erdosproblems.com/forum/thread/406)
  and as problem B33 in R. K. Guy, *Unsolved Problems in Number Theory* (2004).
- W. Narkiewicz, "A note on a paper of H. Gupta concerning powers of two and three",
  Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. (1980), 173–174 —
  `N(x) ≤ 1.62·x^(log₃ 2)`.
- J. C. Lagarias, "Ternary expansions of powers of 2", J. London Math. Soc. (2) 79
  (2009), 562–588, [arXiv:math/0512006](https://arxiv.org/abs/math/0512006) — the 3-adic
  dynamical framework and the 3-adic Cantor sets.
- W. C. Abram and J. C. Lagarias, "Intersections of multiplicative translates of
  3-adic Cantor sets", J. Fractal Geom. (2014), 349–390.
- R. I. Saye, "On two conjectures concerning the ternary digits of powers of two",
  J. Integer Seq. (2022), Art. 22.3.4 — every ternary digit appears in `2ⁿ` for
  `16 ≤ n ≤ 5.9 × 10²¹`.

---

## Companion repositories

```
the-browns-solution-to-erods-o0O-nx3-6-for-1-with--1-3   the full result
one-click                                                the whole system, one file
how-and-why-the-system-works                             the technical account
the-leaves-are-not-the-message                           the generator/leaf result
raw-data                                                 unedited output + scripts
```

---

**Jesse Daniel Brown (OP-JESSE)** — the system, the laws, the architecture.

*Three throws around a free centre. One fires per phase. The fuel is light and
the exhaust is −1/3.*
