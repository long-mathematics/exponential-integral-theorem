# Paper V density and front-matter closeout — 6 October 2026

## Trigger and scope

A post-merge audit of Paper V at commit `32fc761b84137ed2a229bd3c0db4ab05cf0101d3` found no mathematical defect in the integrated theorem but identified an expository gap: the continuation hypothesis and saddle proof used a phase-density germ and a chain multiplicity that were no longer defined after the earlier compression. It also noted scalar-field bookkeeping and front-matter residue from the archived "polynomial flags" presentation.

This closeout makes only those bounded repairs. It does not alter the class-(W) hypotheses, weaken (Q), enlarge the boundary field, change either example, or restore any withdrawn formal-completeness claim.

## Density and multiplicity

The manuscript now defines a polynomial two-chain once, including its oriented polynomial faces. For a point outside the boundary image it defines the chain multiplicity by the coefficient-weighted Brouwer degrees of the square parametrizations. This is locally constant and automatically handles non-injective parametrizations.

A new phase-density lemma proves the exact facts used later:

- polynomial-amplitude chain integrals are bilateral Laplace transforms of compactly supported L1 densities;
- at regular values the density is given by the coarea formula with the chain multiplicity;
- away from interior critical values, face critical values, and vertex values, the density has a real-analytic representative and hence a holomorphic germ;
- one-variable face moments have algebraic inverse-Laplace densities, written as finite sums over algebraic inverse branches;
- endpoint exponentials and the constant function are point masses.

Hypothesis (S) now writes its nonzero coefficient as `w := m_D(P_0)`; hypothesis (S*) explicitly refers to the density `rho_{D,1}` from the lemma. The saddle proof cites the lemma instead of assuming this machinery.

## Scalar-field bookkeeping

Part (iii) now says explicitly that independence over the complexified boundary field `K_partial` from part (ii) implies independence over `K_partial,0`. Hence, if `d = trdeg_{k(z)} K_partial,0`, the combined field has degree `d + mu` over `k(z)` before Beukers is applied separately to the boundary and combined E-function vectors. No theorem statement changes.

## Front matter

The current title is changed from

> Relative Exponential Periods on Polynomial Flags: Algebraic Independence over Fixed Boundary Fields

to

> Relative Exponential Periods on Polynomial Chains: Algebraic Independence over Fixed Boundary Fields.

The PDF metadata is updated accordingly. The obsolete keyword "Stokes matrix" and the no-longer-relevant MSC entries 14D07 and 14H40 are removed. The historical archive and prior provenance records keep their original titles.

## Citation rechecks

Two citations mentioned by the post-merge audit were independently checked against the cited sources.

- **Sabbah, Proposition 9.1:** the proposition represents the algebraic direct image by the stated differential-form complex and says its cohomology modules are holonomic (regular even at infinity). The subsequent standing assumption of cohomological tameness begins only after that proposition, at Proposition 9.2. The current general-finiteness use is therefore correctly scoped.
- **Milne, Proposition 15.15 and Corollary 22.43:** Proposition 15.15 does state that an algebraic group is linearly reductive iff H^1(G,V)=0 for every finite-dimensional representation. Corollary 22.43 states that all finite-dimensional representations are semisimple iff the identity component is reductive. Both current pinpoints are correct. An earlier AI comment suggesting that Proposition 15.15 concerned parabolic subgroups was itself incorrect; the manuscript citation is retained.

The source checks do not replace specialist refereeing. The two already disclosed unnumbered geometric source passages and the OCR limitation on the AGV excerpt remain part of the review boundary.

## Validation boundary

The existing exact elliptic, rank-six, and formal-recursion certificates remain unchanged. A regression test is added for the new density/multiplicity definitions, title/metadata cleanup, scalar-field sentence, and the retained Milne pinpoints. The normal PR workflow must pass before merge, including the committed-PDF/manifest check.

No previous archive is rewritten by this closeout.
