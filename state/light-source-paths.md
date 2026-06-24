# Light source (광원) — generation-path survey

Pillar 1 of the lumen research hub. How EUV / shorter-wavelength photons are
generated, and which path has a route to a **stable sub-13.5 nm source** (the
central lumen target). Numbers below are well-established public facts; anything
uncertain is marked `?` and should be verified before use.

## Path comparison

| Path | Mechanism | Wavelength | Maturity | Stability / throughput | Sub-13.5 nm prospect |
|---|---|---|---|---|---|
| **LPP** (Laser-Produced Plasma) | High-power CO₂ laser pulses vaporize falling Sn micro-droplets → 13.5 nm plasma | 13.5 nm | Production (ASML NXE/EXE) | Incumbent; ~250 W+ source power, droplet-rate limited | Scaling to higher power hard; different target element needed for shorter λ |
| **DPP** (Discharge-Produced Plasma) | Electrical discharge through Sn/Xe vapor creates pinch plasma | 13.5 nm | Largely superseded by LPP for HVM | Heat/electrode erosion limited power | Limited |
| **LDP** (Laser-induced Discharge Plasma) | Laser triggers a discharge plasma (hybrid of LPP+DPP) | 13.5 nm | Path ASML dropped; revisited by China | Lower throughput today | Open / nationally funded R&D |
| **Synchrotron** (storage ring) | Bending-magnet / undulator radiation from relativistic electrons | Broadband, tunable incl. EUV & shorter | Science facilities; lithography use experimental | Extremely stable beam, but huge facility, low wafer throughput | Strong in principle (tunable to 6.5 nm), throughput is the wall |
| **FEL** (Free-Electron Laser) | Undulator + electron bunching → coherent, high brightness | Tunable, can reach sub-13.5 nm | Research | Very high brightness; facility-scale, cost/availability unproven for HVM | Promising on physics, unproven on economics `?` |

## The 6.5 nm ("Beyond-EUV" / BEUV) wall

- Shorter wavelength → higher resolution at fixed NA, but **no clear stable-source path** (this is the stated central dilemma).
- Emitter element changes: 6.x nm bands are associated with Gd / Tb plasmas (not Sn) `?` — verify.
- Mirror multilayers must change too (see `optics.md`): Mo/Si works at 13.5 nm; ~6.5 nm needs La/B-based multilayers with lower reflectivity → more mirrors, more loss.

## Open questions

- Which path is *least blocked* for a stable sub-13.5 nm source: LPP power-scaling, FEL, or synchrotron-throughput engineering?
- Source power vs droplet/repetition-rate ceiling for LPP — where is the real wall?
- Is the China LDP + synchrotron bet a throughput dead-end or a post-EUV variable?
