---
id: bent_over_barbell_row
name: Bent Over Barbell Row
status: complete
category: exercise
pattern: [horizontal_pull]
equipment: [barbell]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 2
  mobility_prerequisite: 3

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: rhomboids
    role: primary
  - id: trap_middle
    role: primary
  - id: erector_spinae
    role: primary
  - id: biceps_brachii
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: rectus_femoris
    role: stabilizer

# ssd_2026 is a literature compilation. The BOR study reports erector spinae subdivisions
# (LUES = left upper/thoracic ES; RLES/LLES = right/left lumbar ES) and rectus femoris
# with numeric values, but reports latissimus dorsi and biceps brachii as qualitative only
# ("high activation"). Do NOT fabricate %MVIC values for LD or biceps.
# Values are %MVC (not %MVIC — different normalization; directly comparable within study only).
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: wide
      phase: concentric
      notes: "Bilateral bent-over barbell row"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 72.8, sd: null, notes: "Left upper thoracic erector spinae (LUES); concentric phase"}
      - {muscle: latissimus_dorsi, mean_pct_mvc: null, sd: null, notes: "High activation — quantitative %MVIC not reported in source; increases significantly vs narrow grip (p<0.01)"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: wide
      phase: eccentric
      notes: "Bilateral bent-over barbell row"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 54.1, sd: null, notes: "Left upper thoracic erector spinae (LUES); eccentric phase"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: wide
      phase: isometric
      notes: "Postural stabilization during bilateral BOR"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 42.9, sd: null, notes: "Lumbar erector spinae; average of RLES 42.5% and LLES 43.3% MVC"}
      - {muscle: rectus_femoris, mean_pct_mvc: 8.2,  sd: null, notes: "Right rectus femoris isometric stabilization"}

joint_rom_required:
  hip_flexion_deg: 75
  elbow_flexion_deg: 110
  shoulder_extension_deg: 90
  notes: >
    Hip hinge to bring torso approximately parallel to the floor (requiring ~75° hip
    flexion and adequate hamstring flexibility). Elbow flexes through 90–110° during
    the concentric phase. Shoulder initiates at ~90° flexion and extends through
    neutral during the pull.
  source: "ssd_2026"

strength_curve:
  type: ascending_descending
  sticking_point: terminal_lockout
  peak_force_position: mid_range
  notes: >
    Peak mechanical force is generated at mid-range — elbow flexed ~90° and shoulder
    near neutral extension. The sticking point is at terminal concentric lockout where
    the bar contacts the torso, because the horizontal lever arm of the humerus
    relative to the shoulder requires maximum force to complete final scapular retraction.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    lower_back: high
    shoulder: low
    elbow: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: compressive_and_shear_forces_during_forward_flexion
      risk_factors: [heavy_loads, spinal_rounding, fatigue, rapid_load_increase]
    - structure: biceps_brachii_tendon
      mechanism: eccentric_overload
      risk_factors: [supinated_grip_at_heavy_loads, high_frequency, inadequate_recovery]
  contraindications:
    - acute_lumbar_disc_herniation
    - proximal_hamstring_tendinopathy

variations: []
progressions: []
alternatives: [inverted_row]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Bent Over Barbell Row

The bent-over barbell row (BOR) is a compound barbell exercise performed with the torso near horizontal. It is the primary standing horizontal pulling movement in strength training and the most direct barbell developer of the upper and mid back musculature. Because no anterior support is provided, the lumbar spine and posterior chain must sustain the forward-flexed posture under heavy load throughout every repetition — making the BOR simultaneously one of the most effective back builders and one of the most spinal-loading exercises in training.

## Execution

1. Stand over a loaded barbell; set feet hip-width, hinge to grip the bar with a pronated double-overhand grip slightly wider than shoulder-width
2. Deadlift the bar to the standing position, then hinge forward until the torso is 10–30° above parallel to the floor; maintain a neutral lumbar spine with a hard brace
3. Begin each rep with the bar hanging at arm's length; pull the bar toward the lower sternum by driving the elbows upward and backward
4. Squeeze the scapulae together at the top; pause briefly with the bar contacting the torso
5. Lower under control through a full 2-second eccentric; do not let the bar drop

## What the EMG Data Shows

The quantitative EMG data from the ssd_2026 literature compilation documents the BOR's erector spinae and stabilizer demands directly, but reports the primary pulling muscles (latissimus dorsi, biceps brachii) in qualitative terms only — "high activation." This is a genuine limitation of the available data, not an omission from this entry.

**Erector spinae demand is substantial and phase-asymmetric**: The left upper thoracic erector spinae (LUES) — representative of the thoracic spinal extensors — activates at 72.8% MVC during the concentric pull and 54.1% MVC during the eccentric descent. The lumbar erector spinae (averaging 42.9% MVC) contracts isometrically throughout both phases to resist spinal flexion under the barbell's moment arm. These are not incidental activation values — they represent the primary mechanical cost of performing the BOR: the spine is loaded continuously and heavily throughout each set.

**Rectus femoris (8.2% MVC isometric)** contributes lower-body postural stability against backward toppling, confirming that the BOR is not an isolated upper-body exercise — the entire kinetic chain is engaged to maintain the forward-flexed posture.

## Technical Modifications and Their Effects

The BOR's neuromuscular stimulus is highly sensitive to grip width and hand orientation:

**Grip width**: Wide grip significantly increases latissimus dorsi sEMG amplitude vs narrow grip (p < 0.01), with wide-grip BOR showing superior RMS peaks even under accumulated fatigue. The abducted elbow path of a wide grip increases shoulder horizontal abduction, loading the mid and upper trapezius and posterior deltoid more than a narrow grip.

**Hand orientation (supinated grip)**: A supinated underhand grip increases biceps brachii and latissimus dorsi activation by improving the mechanical alignment of the humerus during sagittal shoulder extension. The supinated Yates row and supinated Pendlay row exploit this principle.

**Unilateral vs bilateral**: A direct comparison at 80% 1RM (n=30) found no statistically significant differences in latissimus dorsi, posterior deltoid, or biceps brachii activation between bilateral barbell rows and unilateral dumbbell rows. Neural drive to the primary back muscles is conserved across execution formats — unilateral execution adds lateral instability demand without compromising back muscle recruitment.

## Spinal Loading Tradeoff

The standing BOR places among the highest lumbar loads of any upper-body exercise. The inverted row produces equivalent latissimus dorsi (99.3% MVIC) and middle trapezius (98.6% MVIC) activation while reducing lumbar erector spinae demand to ~29% MVC (vs ~43% in the BOR) and rectus femoris to 2.7% MVC. For athletes with lower back pathology or fatigue accumulation from heavy deadlift training, the inverted row is the appropriate substitute.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Pendlay row | Bar returned to floor each rep; strict horizontal torso | Maximum force production per rep; minimizes momentum |
| Barbell Yates row | 70° torso angle; supinated grip | Mid-back emphasis; reduced lumbar load |
| Inverted row | Bodyweight; supine; no spinal compression | Low-back injury management; scapular retraction isolation |

> For system-specific training applications, see each system's lens entry.
