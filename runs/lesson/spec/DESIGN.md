# 「1,000 kg의 비밀」 — 광합성 오프너, 15 s

## Concept
A 0.1 g seed erupts into a 1,000 kg tree and the screen asks where that weight came from; we dive into one leaf, where light, water and CO₂ collide inside a chloroplast and the answer slams in: 광합성. It impresses by opening on a real puzzle and answering it in one unbroken camera move.

## Canvas
Full window, background `#04100C`. Stage: centred 16:9, contain-fit. `u` = 1% of stage width (stage 100×56.25u). Positions (x,y) are in u from stage top-left. Text: 6u margins; positions are anchor centres (left-centre if left-aligned).

## Palette
Night `#04100C`, Deep leaf `#0B3D2E`, Chlorophyll `#19E57F`, Sun `#FFD23F`, Water `#3EC5FF`, Carbon `#B8C4C0`, Coral `#FF5A4E`, Paper `#F4FFF8`

## Type
Pretendard (fallback Apple SD Gothic Neo, Noto Sans KR), letter-spacing −0.03em.
Mega 20u/900, Counter 7u/900 tabular, Headline 5u/900, Label 2.6u/700, Caption 1.8u/700.

## Easings
OUT `cubic-bezier(0.16,1,0.3,1)`, IN `cubic-bezier(0.7,0,0.84,0)`, INOUT `cubic-bezier(0.83,0,0.17,1)`, BACK `cubic-bezier(0.34,1.56,0.64,1)`

## Timeline
| s | Screen | Motion |
|---|---|---|
| 0.0–1.0 | Ground, seed, "씨앗 0.1 g" | Seed drops, squashes |
| 1.0–3.2 | Tree, counter | Tree draws; counter rolls up |
| 3.2–5.2 | Question, "흙?" chip | Words rise; chip struck out |
| 5.2–6.2 | Hero leaf | Leaf dive |
| 6.2–10.4 | Chloroplast, three inputs | Streams converge; pulse quickens |
| 10.4–12.2 | 포도당, 산소, equation | Flash, burst, outputs |
| 12.2–14.6 | "광합성" on Chlorophyll | Wipe; glyphs rise |
| 14.6–15.0 | Night | Fade, loop |

## Elements
Spec order: change, duration ms, absolute start t (ms), easing; one clock.

**Scenes 1–2** (stage scales 1→1.05, 0–5200, linear)
- Ground line (14,46)→(50,46), 0.2u, Paper 40%: scaleX 0→1, 500, t=0, OUT.
- Seed, Sun ellipse 1.6×1.1u, lands (32,45.5): translateY −50u→0, 450, t=100, IN; then scaleY 1→0.6→1, 250, BACK.
- "씨앗 0.1 g" Label, Paper, (39,43): opacity 0→1, x −1u→0, 300, t=550, OUT; opacity →0, 200, t=1000.
- Trunk (32,46)→(32,25), 1.4u, Chlorophyll, round caps: stroke draw 0→100%, 900, t=1000, OUT.
- Branches: 6 lines at trunk y=40,37,34,31,28,25, alternating left/right, 45° up, lengths 6,8,9,8,6,5u, 0.8u: draw 500, t=1300, stagger 90, OUT.
- Canopy: 9 circles r 4–6u, alternating Chlorophyll/Deep leaf, centres inside a 26×14u ellipse centred (32,17); centre one is the Chlorophyll **hero leaf**, r 6u: scale 0→1, 500, t=1720, stagger 110 centre-out, BACK.
- Counter, Paper, left (56,17), "0 kg"→"1,000 kg" (integer, comma): value 0→1000, 2000, t=1100, INOUT. At t=3100: scale 1→1.25→1, colour Paper→Sun, 300, BACK.
- Question, Headline, Paper, left at x=56: "이 무게," (y=27), "어디서 왔을까?" (y=33). Each word masked, translateY 110%→0, 500, t=3200, stagger 120, OUT.
- Chip "흙?" Label in Sun-outlined pill, (59,41): scale 0→1, 300, t=4000, BACK. Coral strike line 0.5u: scaleX 0→1, 200, t=4500, OUT; chip shakes x ±0.6u, 3 cycles, 240, linear; opacity 1→0.35, 200.

**Leaf dive**
- Counter, question, chip: opacity 1→0, x 0→4u, 250, t=5100, IN.
- Hero leaf: scale 1→30 about its centre, 900, t=5200, INOUT; fill Chlorophyll→Deep leaf over the last 400. Remove everything it covers.

**Scene 3**
- Cell pattern: brick grid of 10×7u rounded rects (radius 2u), stroke Chlorophyll 12%, 0.15u: scale 1.3→1, opacity 0→1, 800, t=6000, OUT.
- Chloroplast: Chlorophyll ellipse 22×13u at (50,26), 4 Deep-leaf pills 4×1.2u inside: scale 0→1, 600, t=6300, BACK. Then pulses scale 1↔1.04, period 1200→300 ms across t=6900–10280. Blurred Sun glow behind: opacity 0→0.9, same span, linear.
- "엽록체" Caption, Paper, (50,16): opacity 0→1, 300, t=6600, OUT.
- Light: 5 Sun beams 0.5u wide from (0,0), fanned ±6° toward centre: length 0→100%, 400, t=6900, stagger 60, OUT. Label "빛에너지", Sun, (14,12).
- Water: 12 Water dots r 0.6u, (8,56) arcing up to centre: 900 each, t=7700, stagger 80, IN. Label "물", Water, (16,44).
- CO₂: 12 molecules (Carbon dot between two Paper dots, r 0.5u) from (100,20) to centre: 900 each, t=8500, stagger 80, IN. Label "이산화 탄소", Carbon, (82,12).
- Each label: scale 0.6→1, opacity 0→1, 350, at its stream's start, BACK. Particles vanish on arrival.

**Scene 4**
- Chloroplast: scale 1→0.7, 120, t=10280, IN; →1.15→1, 500, t=10400, BACK.
- Flash: full-stage Paper, opacity 0→1 in 80, →0 in 420, t=10400.
- Shock ring: Sun stroke 0.4u, r 6u→60u, opacity 1→0, 800, t=10400, OUT.
- Beams, input labels: opacity →0, 200, t=10400.
- Glucose: hexagon r 4u, Coral stroke 0.6u, Coral 20% fill: centre→(24,26), rotate −180°→0, scale 0→1, 700, t=10450, OUT. Label "포도당", Coral, (24,34).
- Oxygen: 14 Paper ring bubbles r 0.5–1.2u: centre→(76,26) ±6u scatter, 700, t=10450, stagger 30, OUT; then drift up 0.5u/s. Label "산소", Paper, (76,36).
- Equation, Label, centred y=48, terms in label colours, operators Paper: "빛에너지 + 물 + 이산화 탄소 → 포도당 + 산소". Each term masked, translateY 100%→0, 400, t=11000, stagger 70, OUT.

**Scene 5**
- Wipe: Chlorophyll panel skewed −12°, translateX −130%→0, 500, t=12200, INOUT; becomes the background.
- "광합성" Mega, Night, centred (50,27): each glyph masked, translateY 120%→0, rotate 8°→0, 700, t=12550, stagger 90, OUT. Title scale 1→1.04, t=12550–14600, linear.
- Subtitle "식물이 빛으로 양분을 만드는 방법" Label, Night, (50,44): opacity 0→1, y 2u→0, 500, t=13100, OUT.

## Ending
Night overlay opacity 0→1, 400, t=14600, IN. Loops at 15000 from the same frame.

## Signature moments, never simplify
1. **Weigh-in**: canopy and counter finish together at t=3100, then the punch.
2. **Leaf dive**: one continuous scale into the next background, no cross-fade.
3. **Collision**: quickening pulse, compression, flash, shock ring, outputs thrown outward.
