---
id: board_press
name: Board Press
status: complete
category: exercise
pattern: [horizontal press]
equipment: [barbell, bench, rack, boards]

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

# No peer-reviewed EMG study with %MVIC found for the board press specifically.
# Muscle activation pattern is inferred from bench press EMG literature (saeterbakken_2017,
# marcos_pardo_2020) with the following modification: the bottom-range pectoralis stretch
# contribution (the dominant driver in the lowest third of the standard bench press) is
# absent. Board height shifts emphasis progressively toward triceps as ROM shortens.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 30
  notes: "ROM depends on board height. 1 board (~50mm): removes only the deepest 10–15° of elbow flexion. 5 boards (~125mm): removes the bottom ~50–60° of elbow flexion. The exercise begins from lockout and ends at the board contact angle; no bottom-stretch position is reached."
  source: "Biomechanical inference from bench press ROM literature (Muyor et al. 2022)"

strength_curve:
  type: ascending
  sticking_point: board_contact_point
  peak_force_position: lockout
  notes: "The standard bench press sticking point (2–3 inches off the chest) is bypassed at 2+ boards — the exercise begins above it. At 3–5 boards, the lift starts in the strong mid-range and finishes at lockout, allowing supramaximal loads (>100% of standard bench 1RM) to be handled because pectoralis major active insufficiency at depth is eliminated. The effective sticking point becomes the board contact point itself."
  source: "Simmons (Westside) practitioner description; bench press sticking point literature"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: moderate
    wrist: low
  common_injuries:
    - structure: triceps_brachii_tendon
      mechanism: overload_at_lockout
      risk_factors: [supramaximal_loading, rapid_load_increase, inadequate_warm_up]
    - structure: glenohumeral_joint
      mechanism: anterior_impingement
      risk_factors: [improper_bar_path_with_boards, elbow_flare_at_high_board_heights]
    - structure: wrist
      mechanism: compressive_and_shear_load
      risk_factors: [cocked_wrist_position, supramaximal_loading]
  notes: "Board stability is a setup safety concern — boards that shift during the lift create an unpredictable surface. Secure boards to the chest with a bungee cord, strapped vest, or dedicated training partner holding them in place."
  contraindications:
    - acute_triceps_tendon_rupture
    - acute_elbow_injury

variations: [bench_press, close_grip_barbell_bench_press]
progressions: []
alternatives: [bench_press, floor_press]

sources:
  - source_id: simmons_westside
    title: "Westside Barbell Book of Methods"
    author: "Louie Simmons"
    year: null
    doi: null
    credibility: practitioner
  - source_id: saeterbakken_2017
    title: "Effects of grip width on muscle strength and activation in the bench press"
    author: "Saeterbakken, A. H. et al."
    year: 2017
    doi: null
    credibility: rct
---

# Board Press

The board press is a range-of-motion restricted barbell bench press in which one to five wooden boards (2×6 lumber, stacked and secured) rest on the lifter's chest, stopping the bar's descent at a fixed height above the chest. The removed bottom ROM eliminates the pectoralis major's weakest position, allowing supramaximal loading and isolating the mid-range and lockout portions of the press. It is a foundational Maximum Effort (ME) exercise in the Westside Conjugate system.

## Execution

1. Set up identically to a standard bench press: arch, retract scapulae, feet planted, eyes under bar
2. Have a training partner place the boards on the chest (or secure them with a bungee cord through the shirt)
3. Unrack and lower the bar under control until it contacts the boards — do not crash into them
4. Pause briefly (or perform a touch-and-go depending on the programming intent), then press with maximal intent
5. Lock out completely before re-racking

## Board Height and Muscle Emphasis

Each board (nominally 38–50 mm thick) cuts approximately 10–15° of elbow flexion from the bottom of the lift. This shifts which muscles bear the primary load:

| Boards | Approximate ROM removed | Primary target |
|--------|------------------------|----------------|
| 1 board (~50 mm) | Deepest chest contact only | Balanced pec/triceps; pausing above chest |
| 2 boards (~100 mm) | First ~25° of elbow flexion | Mid-range; slightly more triceps emphasis |
| 3 boards (~150 mm) | First ~40° | Triceps dominant; above sticking point |
| 4–5 boards (~200–250 mm) | First ~55° | Near-lockout isolation; supramaximal loads |

## Why Boards Allow Supramaximal Loading

In the standard bench press, the sticking point 2–3 inches off the chest is where the pectoralis major operates at maximum stretch and minimum mechanical advantage — simultaneously its weakest and most loaded position. At 3+ boards, the lift begins above this sticking point entirely. The lifter's full lockout strength is now applied through a range where their musculature is mechanically stronger, allowing 10–30% more total load than their standard bench 1RM. This overload stimulus is the primary training rationale.

## Westside Application

The board press is a Max Effort exercise in the Conjugate system, not an accessory. It is rotated with other ME exercises (floor press, close-grip bench, slingshot bench) on a weekly or bi-weekly basis to prevent accommodation. Weekly max-effort rotation prevents the nervous system from adapting to any single movement pattern while continuously driving strength in the primary press ROM.

> For system-specific training applications, see each system's lens entry.
