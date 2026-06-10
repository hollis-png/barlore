---
id: snatch_pull
name: Snatch Pull
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 3

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
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023: Hang Snatch Pull (HSP) across three expertise levels and two loads.
# %MVIC values, pull phase only (no catch). ES values substantially lower than power snatch
# because catch-phase eccentric stabilisation demand is absent.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: trap_upper,     mean_pct_mvc: 78.58, sd: 27.10}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 101.97, sd: 99.91}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 147.35, sd: 147.64}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 144.53, sd: 185.68}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 211.80, sd: 190.72}

joint_rom_required:
  hip_flexion_deg: 120
  notes: "Setup: 120° hip flexion with snatch-width grip. No catch — terminates at full triple extension with shrug."
  source: "nasm_2020 / geisler_2023"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Wide snatch grip shortens effective pull height, placing greater velocity demand
    on the second pull compared to the clean pull.
    No catch allows loading at 100–140% of snatch 1RM — the primary overload mechanism
    for athletes who cannot increase overhead catch capacity.
    ES pull-phase activation (elite 148–212% MVIC) is ~43–56% lower than the power snatch
    (elite 294–372% MVIC) because catch eccentric demand is absent.
    Lifting straps increase latissimus dorsi and VL activation by removing grip as a limiter.
  source: "geisler_2023 / nsca_2016"

injury_risk:
  joint_stress:
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_forward, poor_bracing]
  contraindications:
    - acute_lumbar_injury

variations: [power_snatch]
progressions: []
alternatives: [clean_pull]

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: nsca_2016
    title: "NSCA Position Statement on Weightlifting for Sports Performance"
    author: "National Strength and Conditioning Association"
    year: 2016
    credibility: expert_consensus
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
---

# Snatch Pull

The snatch pull is the snatch family's pulling derivative. The barbell is pulled from the floor with a wide (snatch) grip through a full triple extension and terminal shrug, but without the overhead catch of the power snatch or snatch. It is the primary overload tool in Olympic weightlifting, allowing loads of 100–140% of snatch 1RM to develop pulling strength without the overhead mobility or technical demands of the catch.

## Execution

1. **Setup:** Feet hip-width, bar over mid-foot, wide snatch grip (roughly 1.5× shoulder width). 120° hip flexion, neutral spine, elbows fully extended.
2. **First pull (floor to knee):** Drive hips and knees simultaneously; maintain back angle. Bar stays close to the shins.
3. **Transition:** As bar passes the knees, knees re-bend and hips push forward.
4. **Second pull (triple extension):** Explosive simultaneous hip, knee, and ankle extension; shrug at full extension without flexing the elbows. Bar is driven vertically — no pull-under follows.
5. **Termination:** Movement ends at peak shrug height. Lower the bar under control.

## What the EMG Data Shows

The snatch pull's most important finding is the contrast with the power snatch. At elite level and 90% 1RM, erector spinae activation is 212% MVIC versus 372% MVIC in the power snatch — a ~43% reduction. This difference is entirely attributable to the overhead catch: the eccentric deceleration of a high-velocity bar at arm's length demands extreme spinal stabilisation that the snatch pull never generates.

This makes the snatch pull a lower-lumbar-risk option when the training goal is developing pulling power rather than catch-position stability. Athletes with lumbar concerns can train triple-extension mechanics without the spinal overload of the overhead catch.

Lifting straps increase latissimus dorsi and vastus lateralis activation by removing grip fatigue as a limiting factor, allowing leg drive and back pull to operate at full capacity.

Upper trapezius (beginners, 50% 1RM: 79% MVIC) reflects the terminal shrug demand.

## Programming Notes

The snatch pull is uniquely positioned as an overload tool: 100–140% of snatch 1RM is a standard programming range because the pull can tolerate substantially more load than the catch phase can receive. It is the standard prescription for athletes who have reached their overhead catch limit but need to continue developing first- and second-pull strength.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Power snatch | Adds overhead catch | Complete snatch training; catch stability |
| Clean pull | Narrow clean grip | Clean-specific pulling pattern |
| Hang snatch pull | Starts mid-thigh | Higher peak RFD; simplified first pull |

> For system-specific training applications, see each system's lens entry.
