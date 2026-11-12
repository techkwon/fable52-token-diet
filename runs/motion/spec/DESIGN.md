# DESIGN — "ONE DOT" (15 s, seamless loop)

## Concept
One vermilion dot is the protagonist: it falls, multiplies, floods the screen, completes a pun, anchors a 3D gyroscope and lands as the full stop of the sign-off. It impresses because every scene is born from the previous shape while proving weight, rhythm, typography and depth.

## Canvas
- Stage 1600×900 units (u), scaled uniformly to fit the window (contain), centred. All numbers are u, origin top-left.
- Scene background colour fills the whole window.
- One master clock, t = elapsed mod 15000 ms; every state is a pure function of t. "@" = start time (delay from t=0).

## Palette
Ink #0B0B0F, Bone #F2EEE6, Vermilion #FF4A1C, Blue #2B4BFF, Acid #D6FF3D

## Type
- Display: "Helvetica Neue", Helvetica, Arial, sans-serif; 700; uppercase.
- Mono: Menlo, Consolas, monospace; 400; 14u; letter-spacing 0.2em; uppercase.

## Easings (cubic-bezier)
OUT (0.16,1,0.3,1); IN (0.7,0,0.84,0); INOUT (0.87,0,0.13,1); BACK (0.34,1.56,0.64,1); UP (0.33,1,0.68,1); DOWN (0.32,0,0.67,0); LIN linear

## HUD (topmost, 48u inset, Mono, 60% opacity)
Bone; Ink between @5750 and @8900.
- Top-left "REEL 2026". Top-right timecode SS:FF at 30 fps.
- Bottom-right bar 160×2: scaleX 0→1, 15000ms, LIN, origin left.
- Bottom-left scene label. Swap: old translateY 0→−16, opacity→0, 200ms IN; new translateY 16→0, opacity 0→1, 300ms OUT.

## Timeline
| s | On screen (label) | What moves |
|---|---|---|
| 0–2.5 | Ink; dot, shock rings (01 — WEIGHT) | Drop, two bounces, split into nine |
| 2.5–5.45 | Nine dots (02 — RHYTHM) | Travelling sine wave, collapse |
| 5.45–5.95 | Iris | Dot floods window Vermilion |
| 5.95–8.5 | MOTION→EMOTION (03 — VOICE) | Letter reveal, E shove, underline |
| 8.5–9.4 | Blue tiles | Diagonal 3D flip |
| 9.4–11.9 | Blue; gyroscope (04 — DEPTH) | Rings spin, flatten |
| 11.9–14.4 | Ink; rule, title, period (05 — SIGNATURE) | Reveal, dot lands, type ripples |
| 14.4–15 | Outro | All exits; dot launches up |

## Element specs

**Scene 1.** Dot D: ø48 Vermilion, centre x=800; squash origin bottom-centre.
- Fall: cy −60→450, 450ms, @0, IN.
- Bounce 1: cy 450→300, 300ms, @520, UP; back 300ms, DOWN. Bounce 2: 450→400, 200ms, @1190, UP; back 200ms, DOWN.
- Squash @450, @1120, @1590: scaleX/scaleY 1→1.45/0.55, then 1.25/0.75, then 1.1/0.9; 70ms OUT, return 110ms BACK.
- Shock ring per landing: Bone stroke 2, centre (800,474), ø48→240/140/80, opacity 0.8→0, 600ms OUT.
- Split: eight Bone clones leave D; dot i (0–8, D is 4) cx 800→320+120i, 600ms, @1800, OUT, stagger 30ms×|i−4|.

**Scene 2.**
- Wave: each dot cy 450±140, true sine, period 1000ms, two periods, upward first, @2500, stagger 75ms left→right.
- Collapse: every cx→800, 350ms, @5100, IN; clones removed @5450.

**Transition A (iris).** D scale 1→0.6, 100ms, @5450, IN; 0.6→64, 400ms, @5550, INOUT. @5950 window = Vermilion, D hidden.

**Scene 3.** Row "EMOTION": Display 260u, letter-spacing −0.04em, Ink, centred on (800,450); each letter in its own overflow-hidden box. "E" is Bone; its box width starts at 0, so "MOTION" sits centred.
- M-O-T-I-O-N: translateY 110%→0, 500ms, @5950, OUT, stagger 35ms.
- E shove: box width 0→natural, glyph translateX −100%→0, 550ms, @7000, BACK. Row stays centred, so MOTION is pushed right, overshooting.
- Underline: Bone bar 12u thick, 24u below, word width, scaleX 0→1, origin left, 600ms, @7500, INOUT.

**Transition B (tiles).** 8 columns × 4 rows of Blue tiles covering the window, above scene 3, below HUD; perspective 1200. Each: rotateX −90°→0°, origin top edge, 500ms, OUT, @8500+40ms×(col+row). @9400 window = Blue; scene 3 and tiles removed.

**Scene 4.** Gyro group at (800,450), perspective 1400, preserve-3d.
- Rings, stroke 3, no fill: R1 ø220 Bone, R2 ø340 Bone, R3 ø460 Acid; each carries a ø14 Vermilion satellite on its rim.
- Entry: scale 0→1, 700ms, @9400, BACK, stagger 100ms inner→outer.
- Spin from @9400, LIN: R1 rotateX 360°/1800ms; R2 rotateY 360°/2400ms; R3 rotateZ 45° then rotateX −360°/3000ms.
- D ø48 at centre: scale 0→1, 400ms, @9500, BACK.
- Flatten: group scaleY 1→0.01, 400ms, @11500, IN.

**Scene 5.** Hard cut @11900: window = Ink; flattened gyro becomes the Rule.
- Rule: Bone, centred x=800; width 460→1120, thickness 3→2, y 450→560, 500ms, @11900, INOUT.
- Title "MADE TO MOVE": Display 150u, −0.03em, Bone, left x=240, box bottom y=545; letters in overflow-hidden boxes, translateY 110%→0, 600ms, @12200, OUT, stagger 30ms.
- Period P (D, ø36): rests on the baseline, 14u right of the last E. cy −60→rest, 450ms, @12900, IN; squash 1.4/0.6, 70ms OUT, return 110ms BACK; one 60u bounce (150ms UP, 150ms DOWN).
- Type ripple: each letter translateY 0→−14→0, 150ms UP + 150ms DOWN, @13350, stagger 25ms right→left.
- Subline, Mono 16u, "MOTION DESIGN REEL — AVAILABLE NOW" at (240,590): opacity 0→0.6, translateY 12→0, 500ms, @13600, OUT.

**Outro and loop.** Letters translateY 0→110%, 300ms, @14400, IN, stagger 15ms left→right. Subline opacity→0, 200ms, @14400. Rule scaleX 1→0, origin right, 400ms, @14450, INOUT. P squash 1.3/0.7, 100ms, @14500, OUT; then scale 0.85/1.2, cy→−60, 350ms, @14600, IN. At 15000 the stage is empty Ink, dot above frame — identical to t=0; loops forever.

## Signature moments — do not simplify
1. **E shove**: real layout push with overshoot, not a crossfade.
2. **Tile flip into gyroscope**: diagonal-staggered 3D tiles, then three rings on different axes in true perspective.
3. **Full stop**: the dot lands with squash, ripples the title right-to-left, then launches out, restarting the loop.
