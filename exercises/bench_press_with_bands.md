---
id: bench_press_with_bands
name: Bench Press with Bands
status: complete
category: exercise
pattern: [horizontal press]
equipment: [barbell, bench, rack, resistance_bands]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: latissimus_dorsi
    role: stabilizer

# No peer-reviewed EMG %MVIC study specific to banded bench press found.
# Muscle activation distribution mirrors the standard bench press (saeterbakken_2017,
# marcos_pardo_2020). Bands shift load distribution without fundamentally changing
# which muscles are involved — they change the resistance profile, not the neural
# recruitment pattern. Triceps activation at lockout is amplified because band tension
# peaks where triceps contribute most to the ascending strength curve.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 79.5
  notes: "Identical ROM to the standard bench press. Bands do not restrict ROM; they modify the load at each position within the same full range."
  source: "Muyor et al. 2022 (standard bench press ROM reference)"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: "The natural ascending bench press strength curve is preserved. Bands add a proportional resistance overlay: minimal tension at the chest, maximal tension at lockout. This creates a load-matched strength curve — the bar becomes progressively heavier precisely where the lifter is progressively stronger — forcing near-maximal effort throughout the full range rather than only at the sticking point. The result is that the lift becomes equally demanding at lockout as at the sticking point."
  source: "Anderson et al. 2008; Simmons (Westside) practitioner description"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
    wrist: low
  common_injuries:
    - structure: glenohumeral_joint
      mechanism: anterior_impingement
      risk_factors: [band_tension_pulling_bar_toward_rack_on_descent, excessive_band_load_relative_to_bar_weight]
    - structure: pectoralis_major_tendon
      mechanism: eccentric_overload_at_stretch
      risk_factors: [band_tension_too_high_relative_to_bar_weight, elastic_rebound_at_bottom]
  notes: "Band tension at lockout should not exceed ~25–30% of the total load, or the band tension at the chest becomes so light that the effective load is almost purely barbell. The correct ratio ensures tension is meaningful throughout the range, not only at the top."
  contraindications:
    - acute_pectoralis_major_tear
    - acute_shoulder_impingement

variations: [bench_press, board_press]
progressions: []
alternatives: [bench_press, close_grip_barbell_bench_press]

sources:
  - source_id: simmons_westside
    title: "Westside Barbell Book of Methods"
    author: "Louie Simmons"
    year: null
    doi: null
    credibility: practitioner
  - source_id: anderson_2008
    title: "Effect of Load on Peak Power of the Bar, Body, and System During the Deadlift"
    author: "Anderson, C. E. et al."
    year: 2008
    doi: "10.1519/JSC.0b013e31816a6f7d"
    credibility: rct
  - source_id: saeterbakken_2017
    title: "Effects of grip width on muscle strength and activation in the bench press"
    author: "Saeterbakken, A. H. et al."
    year: 2017
    doi: null
    credibility: rct
---

# Bench Press with Bands

The bench press with bands is a bench press performed with resistance bands anchored to the base of the rack and looped over the bar ends, adding accommodating resistance — load that increases proportionally as the bar rises toward lockout. At the chest, band tension is minimal; at full lockout, band tension is at maximum. This modification matches the resistance curve more closely to the human strength curve, eliminating the "easy lockout" of standard free-weight pressing and demanding maximal effort throughout the full range of motion. It is the primary Dynamic Effort (DE) pressing exercise in the Westside Conjugate system.

## Setup

1. Loop each band securely around the base of the rack (or anchored to a loaded bar on the floor), one band per side
2. Stretch the bands over the bar ends and position them inside the collars; ensure bands are symmetric
3. Load the barbell to the target working weight — for Westside DE work, approximately 50–55% of 1RM barbell plus band tension
4. Verify that the bands do not contact the rack uprights during the press — they should hang free

**Band tension target**: Aim for bands that add approximately 20–25% of total load at lockout. At the chest, band tension should be minimal but the bands should remain taut (not slack).

## Execution

1. Set up with the standard bench press arch, scapular retraction, and foot drive
2. Unrack and lower the bar under control — the bands will reduce effective load during descent but do not use the bands as a "bounce assist" at the bottom
3. At the bottom, the bar feels lighter (minimal band tension); press immediately and accelerate the bar throughout the full range
4. As the bar rises, band tension increases — the load continues climbing toward lockout; drive through completion
5. Lock out against the full band tension; do not slow down approaching lockout

## The Accommodating Resistance Effect

Standard free weights are heaviest at the bottom (worst leverage, most stretched muscle) and effectively lighter at lockout (best leverage, strongest position). This creates a mismatch: the lifter has unused capacity at the top and is maximally challenged only at the sticking point.

Bands invert this asymmetry:

| Position | Bar load | Band tension | Total load |
|----------|----------|--------------|------------|
| Chest (bottom) | 100% | ~0% | ~100% |
| Midrange | 100% | ~12% | ~112% |
| Lockout | 100% | ~25% | ~125% |

The lifter's muscular capacity also increases from bottom to top (ascending strength curve). Bands apply more load precisely where the lifter is stronger — creating a closer match between load demand and force capacity at every joint angle.

## Westside DE Protocol

Dynamic Effort work uses submaximal loads with maximal intentional velocity. For the bench press with bands:

- **Load**: 50–55% 1RM barbell + bands (total ≈ 75–80% at lockout)
- **Sets/reps**: 8–9 sets of 3 reps
- **Rest**: 45–60 seconds between sets
- **Intent**: Every rep is pressed with absolute maximal acceleration; bar speed is the training variable, not the weight

The short rest and speed focus train rate of force development and bar acceleration — qualities that carry over to the maximal effort press by improving the initial drive off the chest, which determines whether the lifter clears the sticking point.

## Why Bands, Not Just Heavy Weights

Heavy free weights slow due to decelerative demand near lockout — the lifter must decelerate the bar before it flies out of the hands. With bands, the increasing resistance takes care of deceleration naturally, allowing the lifter to press with maximal speed through the complete range without a deliberate slowdown phase. This is critical for training bar acceleration as a motor skill.

> For system-specific training applications, see each system's lens entry.
