---
id: clean_pull
name: Clean Pull
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 3

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
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023: Hang Clean Pull (HCP) across three expertise levels and three loads.
# %MVIC values, pull phase. No catch phase — all motor drive directed into shrug terminal.
# Elite TZ activation significantly greater in clean pull than power clean at 50–70% 1RM
# (p < 0.05, Hedges' g = 0.61–1.08); specific %MVIC values not tabulated in Geisler 2023.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 152.72, sd: 70.36}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 81.67,  sd: 27.32}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 213.18, sd: 111.04}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 118.62, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 225.98, sd: 201.09}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 195.47, sd: 165.81}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 90.53,  sd: 52.44}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 215.58, sd: 189.90}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 109.90, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 273.86, sd: 271.11}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 239.40, sd: 86.53}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 258.65, sd: 258.35}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 279.38, sd: 138.83}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 228.31, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 311.81, sd: 271.74}

joint_rom_required:
  hip_flexion_deg: 120
  notes: "Setup: 120° hip flexion. No catch — terminates at full triple extension with shrug."
  source: "nasm_2020 / geisler_2023"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Midthigh (hang) start: peak GRF 2880±482 N, instantaneous RFD 15321±3533 N/s —
    significantly greater than floor-start power clean (2306±388 N; 8840±2940 N/s).
    Removing the catch phase directs terminal motor drive entirely into shoulder elevation,
    producing superior upper trapezius stimulus vs the power clean at submaximal loads
    (elite, p < 0.05, Hedges' g = 0.61–1.08).
    Can be loaded at 100–110%+ of power clean 1RM as an overload tool.
  source: "kawamori_2005 / geisler_2023"

injury_risk:
  joint_stress:
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_away_from_body, poor_bracing]
  contraindications:
    - acute_lumbar_injury

variations: [power_clean]
progressions: []
alternatives: [snatch_pull]

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

# Clean Pull

The clean pull is an Olympic weightlifting derivative in which the barbell is pulled from the floor through a full triple extension (hip, knee, ankle) with a terminal shrug, but without the catch phase of the power clean or clean. It trains the pulling mechanics of the clean with reduced technical demand and the ability to exceed the athlete's catching 1RM.

## Execution

1. **Setup:** Identical to the clean — feet hip-width, bar over mid-foot, 120° hip flexion, neutral spine, elbows fully extended, hook grip just outside knees.
2. **First pull (floor to knee):** Drive hips and knees simultaneously; maintain constant back angle. Bar stays close to the shins.
3. **Transition:** As bar passes the knees, knees re-bend and hips push forward.
4. **Second pull (triple extension):** Explosive simultaneous hip, knee, and ankle extension drives the bar vertically. Shrug the shoulders at full extension without flexing the elbows.
5. **Termination:** Movement ends at peak shrug height — no arm pull, no catch. Lower the bar to the floor under control.

## What the EMG Data Shows

Vastus lateralis (VL) and gluteus maximus (GM) are the primary pull-phase movers, with activation profiles nearly identical to the power clean at equivalent relative loads. At elite level and 70% 1RM: VL 279% MVIC, GM 228% MVIC.

The key differentiation from the power clean is the upper trapezius. Removing the catch phase allows the athlete to direct peak motor drive entirely into the terminal shrug: at submaximal loads (50–70% 1RM), elite weightlifters show significantly greater upper trapezius activity during the clean pull versus the power clean (p < 0.05, Hedges' g = 0.61–1.08, Geisler 2023).

The midthigh hang variation produces substantially higher peak GRF (2880 vs 2306 N) and RFD (15321 vs 8840 N/s) than the floor-start power clean, confirming its utility as a pure power development overload tool.

## Programming Notes

The clean pull can be loaded at 100–110% of the power clean 1RM. This makes it the primary overload tool in the Olympic lifting system for athletes who cannot increase their catch capacity but need to continue developing triple-extension power. For athletes with restricted front-rack mobility, the clean pull delivers an equivalent lower-body stimulus without the wrist, elbow, and shoulder demands of the catch.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Hang clean pull | Starts from mid-thigh | Higher peak RFD; simplified first pull |
| Power clean | Adds front-rack catch | Complete lift; catch-position conditioning |
| Snatch pull | Wide snatch grip | Snatch-specific pulling pattern |

> For system-specific training applications, see each system's lens entry.
