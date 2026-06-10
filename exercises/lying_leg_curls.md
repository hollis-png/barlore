---
id: lying_leg_curls
name: Lying Leg Curls
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

# schoenfeld_2014 (n=13): prone position.
# biceps_femoris 80% MVIC, semitendinosus 65% MVIC.
# Hip neutral (0° flexion) → hamstring heads in mid-range length.
# Bell-shaped strength curve: hardest at ~90° knee flexion.
muscle_activation_studies:
  - source_id: schoenfeld_2014
    doi: null
    n: 13
    population: "healthy males, prone leg curl machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Prone (lying face-down) position; hip at 0°"
    measurements:
      - {muscle: biceps_femoris, mean_pct_mvc: 80.0, sd: null}
      - {muscle: semitendinosus, mean_pct_mvc: 65.0, sd: null}

joint_rom_required:
  knee_flexion_deg: 130
  hip_flexion_deg: 0
  source: "schoenfeld_2014"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; peak hamstring force at ~90° knee flexion; prone hip position places hamstrings in mid-length"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: low
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, pre_existing_proximal_tendinopathy]
  contraindications:
    - acute_proximal_hamstring_tendinopathy
    - acute_posterior_knee_injury

variations: []
progressions: []
alternatives: [seated_leg_curl, glute_ham_raise]

sources:
  - source_id: schoenfeld_2014
    title: "Effects of Different Volume-Equated Resistance Training Loading Strategies on Muscular Adaptations in Well-Trained Men"
    author: "Schoenfeld, Brad J. et al."
    year: 2014
    doi: null
    credibility: rct
---

# Lying Leg Curls

The lying leg curl is the standard prone isolation exercise for the hamstrings. Performed face-down on a leg curl machine, the knee flexion movement loads the biceps femoris, semitendinosus, and semimembranosus against pad resistance. The prone (hip neutral) position places all three hamstring heads in their natural mid-range length, producing a bell-shaped resistance curve with peak load at approximately 90° knee flexion.

## Execution

1. Adjust the leg curl machine pad so it sits just above the ankle and lie face-down
2. Keep the hips flat on the pad throughout — do not allow the hips to lift as the legs curl up
3. Curl the legs toward the glutes as far as the machine allows; hold briefly at the contracted position
4. Lower under control through the full eccentric — do not let the weight drop

## What the EMG Data Shows

Schoenfeld 2014 (n=13, prone):

| Muscle | Activation |
|--------|-----------|
| Biceps femoris | 80% MVIC |
| Semitendinosus | 65% MVIC |

The biceps femoris generates significantly higher activation than the semitendinosus in the prone position. This biceps femoris dominance is a consistent finding in prone leg curl research.

## Prone vs Seated: Hip Position Matters

The key mechanical difference between lying and seated leg curls is hip angle:
- **Prone (lying)**: Hip at 0° — hamstrings in mid-range length
- **Seated**: Hip at ~90° flexion — hamstrings pre-stretched at proximal end

The seated position places the hamstrings in a more lengthened overall configuration. Both machines train knee flexion, but through different muscle length conditions — making them complementary rather than interchangeable.

## Foot Positioning

Toe rotation affects medial vs lateral hamstring emphasis:
- **Toes forward**: Balanced biceps femoris and semitendinosus
- **Toes in (internal rotation)**: Slightly greater biceps femoris emphasis
- **Toes out (external rotation)**: Slightly greater semitendinosus/semimembranosus emphasis

> For system-specific training applications, see each system's lens entry.
