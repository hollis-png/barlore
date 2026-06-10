---
id: power_clean
name: Power Clean
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 3
  mobility_prerequisite: 4

muscles:
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer
  - id: rhomboids
    role: stabilizer

# Geisler 2023: Hang Power Clean (HPC) across three expertise levels and three loads.
# %MVIC values are for the pull phase only; catch phase adds eccentric stabilisation demand.
# Do NOT average across expertise levels — motor unit synchronisation differs substantially.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 163.82, sd: 64.41}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 124.91, sd: 76.67}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 208.20, sd: 113.02}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 99.50,  sd: 56.46}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 203.96, sd: 119.85}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 247.70, sd: 259.48}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 97.20,  sd: 37.72}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 321.09, sd: 367.87}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 107.70, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 307.97, sd: 288.30}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 324.41, sd: 305.15}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 298.74, sd: 195.54}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 248.37, sd: 221.22}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 186.84, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 249.30, sd: 213.53}

joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 90
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 173
  shoulder_external_rotation_deg: 107
  shoulder_internal_rotation_deg: 89
  notes: "Setup: 120° hip flexion. Front-rack catch: 90° knee flexion, 173° shoulder flexion, 107°/89° ER/IR"
  source: "nasm_2020 / crossfit_2022"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    GRF profile: first pull ~1.5×BW, unweighting (double-knee bend) ~1.0×BW,
    second pull peak 2.0–2.5×BW. Floor-start: peak GRF 2306±388 N,
    instantaneous RFD 8840±2940 N/s (Kawamori 2005).
    VL and GM activation is statistically equivalent between power clean and clean pull
    at loads ≥70% 1RM — the catch adds eccentric demand, not additional concentric power.
  source: "kawamori_2005 / geisler_2023"

injury_risk:
  joint_stress:
    wrist: high
    elbow: moderate
    lower_back: moderate
  common_injuries:
    - structure: wrist_extensors
      mechanism: forced_extension_on_catch
      risk_factors: [insufficient_shoulder_er, poor_front_rack_mobility]
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_away_from_body, poor_bracing]
  contraindications:
    - acute_wrist_injury
    - acute_shoulder_impingement

variations: [clean_and_jerk, clean_pull]
progressions: [clean_pull]
alternatives: []

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: kawamori_2005
    title: "Comparisons of Peak Ground Reaction Force and Rate of Force Development During Variations of the Power Clean"
    author: "Kawamori N et al."
    year: 2005
    doi: "10.1519/00124278-200508000-00011"
    credibility: rct
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
---

# Power Clean

The power clean is an Olympic weightlifting derivative in which the barbell is pulled from the floor and caught on the anterior shoulders in a partial squat (≥90° knee flexion). It is the most widely programmed catching derivative in athletic conditioning, training explosive triple extension — simultaneous hip, knee, and ankle extension at peak velocity.

## Execution

1. **Setup:** Feet hip-width, bar over mid-foot. Hips below shoulders, shoulders over or slightly in front of bar. Neutral spine, 120° hip flexion, elbows fully extended, pronated hook grip just outside the knees.
2. **First pull (floor to knee):** Drive hips and knees simultaneously; maintain constant back angle. Bar stays against the shins.
3. **Transition (double-knee bend):** As bar passes the knees, knees re-bend and hips push forward; torso angle becomes more upright.
4. **Second pull (triple extension):** Forceful simultaneous extension of hips, knees, and ankles; shrug at full extension.
5. **Catch:** Elbows rotate rapidly under the bar; receive in front-rack position — elbows high and parallel to floor, bar resting on anterior deltoids, ≥90° knee flexion.
6. **Recovery:** Extend hips and knees to standing; lower bar under control.

## What the EMG Data Shows

The pull phase is dominated by vastus lateralis (VL) and gluteus maximus (GM). Beginners at 50% 1RM: VL 164% MVIC, GM 125% MVIC. Elite athletes at the same relative load: VL 324% MVIC, GM 299% MVIC — reflecting superior motor unit synchronisation rather than greater absolute force.

Critically, VL and GM activation is statistically equivalent between the power clean and the clean pull at loads ≥70% 1RM (Geisler 2023). The pulling phase produces an identical concentric extension stimulus whether or not a catch follows. The catch adds eccentric stabilisation demand on the wrist, elbow, and shoulder girdle — not additional triple-extension power.

VL activation at elite level does not increase monotonically from 70% to 90% 1RM (248 → 249% MVIC), suggesting motor efficiency plateaus at high expertise and that load increases beyond ~70% produce diminishing neuromuscular returns for the pull.

## Front-Rack Mobility Requirements

The catch position requires specific mobility cut-points that are frequently under-screened. Deficits force the bar onto the anterior deltoid or clavicle, creating wrist and elbow torque and causing the fingers to release:

- Shoulder flexion: ≥173°
- Shoulder external rotation: ≥107°; internal rotation: ≥89°
- Elbow flexion: ≥135°; pronation: ≥90°
- Wrist extension: ≥90°

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Hang power clean | Starts from mid-thigh or knee | Learning the second pull; reduced first-pull complexity |
| Clean (full) | Catch in full squat | Maximising load; competitive weightlifting |
| Clean pull | No catch phase | Overload training; athletes with restricted front-rack mobility |

> For system-specific training applications, see each system's lens entry.
