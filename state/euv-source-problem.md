# EUV source problem — reference note

First research artifact for `lumen`. Frames the next-generation lithography
light-source problem and its three reference fields. Source is a Korean YouTube
analysis featuring Prof. Kwon Seok-jun (Sungkyunkwan Univ.) on the state of EUV.

## Reference fields (scope pillars)

- **Light source (광원)** — how the EUV/shorter-wavelength photons are generated.
- **Photochemistry (광화학)** — the photoresist that records the projected image.
- **Optics (광학계)** — the projection optics (NA, depth-of-focus, mirrors).

## Core dilemma (next-gen wall)

1. **Roadmap gap beyond 3rd-gen** — current EUV lithography has a roadmap through
   the 3rd generation, but no clear technical alternative for the step after that
   (post-2040s). Video ref: 14:38–14:55, 17:15–17:25.
2. **NA vs depth-of-focus** — raising NA (numerical aperture) for higher physical
   resolution shrinks the focus depth, forcing the resist to be controlled extremely
   thin. That control raises process difficulty steeply and increases error
   probability. Video ref: 15:52–16:40.
3. **Shorter-wavelength source** — using a shorter wavelength (e.g. 6.5 nm) is
   theoretically possible, but there is no clear engineering path to securing a
   STABLE source for it. Video ref: 17:26–18:01. **← lumen's central target.**

## Industry context (from the source)

- **EUV capex & ramp** (01:37–05:59) — Samsung and SK hynix bought 2nd-gen EUV tools
  at ~KRW 520B each in volume; ~1.5–2 yr of process optimization / R&D before real
  mass production; maintenance runs ~1/3 of tool price.
- **ASML monopoly** (06:53–10:20) — the LPP (Laser-Produced Plasma) approach is a
  ~30-year ASML + partner ecosystem moat; very hard for others to enter short-term.
- **China's indigenous push** (10:31–14:37) — blocked from buying EUV by US export
  controls, China invests nationally in the LDP (Laser-induced Discharge Plasma)
  path ASML abandoned, plus synchrotron (storage-ring) lithography. Low yield today,
  but heavy basic-science investment is a post-EUV-era variable.
- **EUV shelf-life & outlook** (14:38–19:58) — no clear alternative beyond 3rd-gen
  (post-2040s); Japan and others have largely exited the frontier; China is the lone
  rising challenger; Korea must move from operating tools to owning the broader
  technology ecosystem.

## Open questions for lumen

- Which lumen form fits — research hub (organize approaches/devices/patents),
  simulator (model LPP/LDP/synchrotron source physics), or a design tool/calculator?
- For a sub-13.5 nm stable source: which generation path (LPP scaling, LDP,
  synchrotron, FEL, other) is least blocked, and by what?
