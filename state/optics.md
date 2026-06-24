# Optics (광학계) — focusing and imaging the source

Pillar 3 of the lumen research hub. The projection optics that shrink and focus the
source onto the wafer. This is where the NA / depth-of-focus trade-off originates,
which then drives the resist (`photochemistry.md`) and source (`light-source-paths.md`)
constraints. Items marked `?` need verification before use.

## The NA ↔ depth-of-focus trade

- **Resolution** (half-pitch) ≈ k₁ · λ / NA — smaller with shorter λ or higher NA.
- **Depth-of-focus** ≈ k₂ · λ / NA² — falls with NA², so raising NA for resolution
  collapses the focus window → ultra-thin resist + tighter focus control.

```
NA ↑   →  해상도 ↑  (좋음)
NA ↑   →  DoF ↓ (NA² 로)  →  레지스트 극박막·초점 제어 난도 ↑  (나쁨)
```

- Current EUV: NA ≈ **0.33** (ASML NXE). High-NA: NA ≈ **0.55** (ASML EXE / "High-NA EUV").
- High-NA uses **anamorphic** optics (different magnification in x/y, 4×/8×) → half-field
  imaging, stitching, throughput implications `?`.

## Mirror / multilayer challenge

- EUV is absorbed by everything → all-reflective optics with **multilayer mirrors**.
- 13.5 nm: **Mo/Si** multilayers, ~70% reflectivity per mirror; with ~10+ mirrors the
  total throughput budget is already tight.
- ~6.5 nm ("BEUV"): needs **La/B-based** multilayers with **lower** reflectivity →
  more loss per mirror → demands far more source power (ties back to the source wall).

## Open questions

- Throughput math: per-mirror reflectivity × mirror count × source power — where is the
  6.5 nm system-level wall?
- Does High-NA (0.55) buy enough nodes to bridge to whatever comes after EUV, or is it a
  stopgap before the source problem must be solved?
