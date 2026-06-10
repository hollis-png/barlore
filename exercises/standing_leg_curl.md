---
id: standing_leg_curl
name: Standing Leg Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: semimembranosus
    role: primary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# No peer-reviewed EMG data found for the standing leg curl.
# Hip at ~0° (similar to prone variation). Unilateral format is the key differentiator.
muscle_activation_studies: []

joint_rom_required:
  knee_flexion_deg: 130
  hip_flexion_deg: 0
  source: "biomechanical inference"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Descending; hardest at the start (knee extended, greatest gravity moment arm for the pad); gets easier as the knee flexes and the moment arm shortens"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: low
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight, unilateral_compensation]
  contraindications:
    - acute_proximal_hamstring_tendinopathy

variations: []
progressions: []
alternatives: [lying_leg_curls, seated_leg_curl]

sources: []
---

# Standing Leg Curl

The standing leg curl is a unilateral hamstring isolation exercise performed one leg at a time on a dedicated standing leg curl machine. The torso leans forward approximately 30–45° against a support pad, and the free leg curls the resistance pad toward the glutes. The unilateral format makes bilateral compensation impossible and allows direct left-right strength comparison.

## Execution

1. Adjust the machine so the pad rests just above the ankle of the working leg; the front of the knee is supported by the machine's upper pad
2. Lean forward into the support pad; hold the handles
3. Curl the working leg toward the glutes as high as possible
4. Hold briefly at peak contraction, then lower under control
5. Complete all reps for one leg before switching

## Mechanical Characteristics

The standing position places the hip at approximately 0° flexion (neutral), similar to the prone leg curl. The key difference from the lying version is the unilateral loading:
- Prevents the stronger leg from compensating
- Allows left/right activation comparison
- Adds minor postural demand from standing on one leg

No EMG data is available for this variation. Based on mechanical equivalence to the prone leg curl (schoenfeld_2014: biceps femoris 80% MVIC), similar activation is expected.

## When to Use

Most useful as a unilateral accessory or when bilateral leg curl machines are unavailable. For maximum hamstring hypertrophy stimulus, the seated leg curl (hip 90°) remains the first-choice variation.

> For system-specific training applications, see each system's lens entry.
