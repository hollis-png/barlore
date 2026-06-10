---
id: power_snatch
name: Power Snatch
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 3
  mobility_prerequisite: 5

muscles:
  - id: erector_spinae
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
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
  - id: triceps_brachii
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023: Hang Power Snatch (HPS) across three expertise levels and two loads.
# Phase: pull_and_catch — ES values include both pull and overhead catch demands.
# The catch is responsible for the majority of the ES elevation vs the snatch pull.
# At elite level, catch-phase ES significantly exceeds snatch pull (p < 0.05).
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
    measurements:
      - {muscle: trap_upper,     mean_pct_mvc: 71.69, sd: 23.21}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 175.69, sd: 134.95}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 294.28, sd: 152.77}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 215.68, sd: 321.69}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 371.62, sd: 271.60}

joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 90
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: "Setup: 120° hip flexion. Overhead catch: 180° shoulder flexion, 90°/70° ER/IR required for stable lockout"
  source: "nasm_2020 / setpt_2020"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Wider snatch grip shortens effective pull height vs clean grip, requiring greater
    barbell velocity to achieve a successful catch. Peak power at 45–65% 1RM.
    Under repeated fatiguing reps, athletes increase spinal stiffness (L5-S1 extension
    decreases significantly, p=0.03) to protect passive lumbar tissues — a healthy
    protective neural strategy.
    Catch-phase ES at elite level (372% MVIC at 90% 1RM) is ~76% greater than the
    snatch pull (212% MVIC) — the overhead eccentric stabilisation is the defining demand.
  source: "geisler_2023 / jsc_2013"

injury_risk:
  joint_stress:
    shoulder: high
    wrist: high
    lower_back: high
  common_injuries:
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_catch
      risk_factors: [insufficient_shoulder_flexion, restricted_thoracic_extension]
    - structure: lumbar_disc
      mechanism: hyperextension_during_catch
      risk_factors: [excessive_lordosis, poor_bracing]
  contraindications:
    - acute_shoulder_injury
    - lumbar_herniation

variations: [snatch_pull]
progressions: [overhead_squat]
alternatives: []

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
  - source_id: setpt_2020
    title: "Weightlifting Series Part I: Improving Overhead Mobility"
    author: "Set Physical Therapy"
    year: 2020
    credibility: practitioner
---

# Power Snatch

The power snatch is the snatch family's catching derivative. The barbell is pulled from the floor with a wide (snatch) grip and received overhead in a partial squat (≥90° knee flexion). It is the highest-mobility-demand movement in standard strength training, requiring 180° of shoulder flexion and stable overhead control throughout the catch.

## Execution

1. **Setup:** Feet hip-width, bar over mid-foot, wide snatch grip (roughly 1.5× shoulder width). 120° hip flexion, neutral spine. Shins and torso roughly parallel to each other.
2. **First pull (floor to knee):** Drive hips and knees; maintain back angle. Bar stays against the shins.
3. **Transition (double-knee bend):** As bar passes the knees, knees re-bend and hips push forward.
4. **Second pull (triple extension):** Explosive hip, knee, and ankle extension; shrug at peak. Wider grip requires higher peak barbell velocity than the clean grip to achieve the catch position.
5. **Catch:** Arms press out and up, receiving the bar locked overhead with elbows fully extended. Hips and knees flex to ≥90°. Requires 180° shoulder flexion to keep the bar over the midfoot.
6. **Recovery:** Stand by extending hips and knees while maintaining the overhead bar position.

## What the EMG Data Shows

The defining feature of the power snatch versus the snatch pull is the massive erector spinae demand at the catch. Elite athletes at 90% 1RM show ES activation of 372% MVIC during the power snatch versus 212% MVIC during the snatch pull (p < 0.05, Geisler 2023). This ~76% difference represents the eccentric stabilisation cost of arresting a high-velocity barbell overhead — the spinal erectors must decelerate trunk extension through the catch.

Under repeated fatiguing repetitions, athletes adopt a protective neural strategy: L5-S1 intervertebral extension decreases significantly (p = 0.03) as fatigue accumulates, reflecting increased spinal stiffness to protect passive lumbar tissue. Technical failure in this protective mechanism is the injury pathway.

Upper trapezius (beginners, 50% 1RM: 72% MVIC) elevates the shoulder girdle during the shrug and assists in pulling the body under the bar.

## Overhead Catch Mobility Requirements

These are the strictest mobility demands in strength training. Restrictions force a forward bar displacement that cannot be recovered mid-lift:

- Shoulder flexion: ≥180°
- Shoulder external rotation: ≥90°; internal rotation: ≥70°
- Thoracic extension to maintain bar over the midfoot

Shoulder flexibility correlates significantly with trunk angle at the bottom position (r = −0.67, p = 0.003): restricted shoulders force a compensatory forward trunk lean that shifts the bar forward and destabilises the catch.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Snatch pull | No catch phase | Overload training (100–140% snatch 1RM); reduced shoulder demand |
| Snatch (full) | Catch in full squat | Maximising load; competitive weightlifting |
| Overhead squat | No pull; static overhead | Mobility screening; catch-position conditioning |

> For system-specific training applications, see each system's lens entry.
