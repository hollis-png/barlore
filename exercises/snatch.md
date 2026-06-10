---
id: snatch
name: Snatch
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

# Geisler 2023 measured Hang Power Snatch (HPS) — a proxy for the full snatch's
# pull phase. The full snatch starts from the floor (adds first-pull demands) and
# catches in a full overhead squat (adds quad/hip squat recovery demands not
# captured here). Pull-phase activation is comparable; catch-phase ES values
# reflect the overhead eccentric load, which applies to the full snatch catch equally.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
      notes: "Hang Power Snatch proxy; full snatch adds overhead squat recovery demand"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 175.69, sd: 134.95}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
      notes: "Hang Power Snatch proxy"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 294.28, sd: 152.77}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull_and_catch
      notes: "Hang Power Snatch proxy; peak ES values"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 371.62, sd: 271.60}

joint_rom_required:
  hip_flexion_deg: 130
  knee_flexion_deg: 135
  ankle_dorsiflexion_deg: 38
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: >
    Setup: 120° hip flexion (same as power snatch). Full squat catch is more demanding
    than the power snatch: requires 130–135° knee flexion, 38° ankle dorsiflexion at
    full depth. Overhead lockout: 180° shoulder flexion required throughout squat recovery.
    Thoracic extension mobility is a secondary limiting factor — restricted thoracic extension
    forces forward trunk lean, shifting the bar forward out of the midfoot line.
  source: "nasm_2020 / setpt_2020; squat depth from Schoenfeld 2010"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Pull phase: bell-shaped GRF curve identical to power snatch — first pull ~1.5×BW,
    unweighting at double-knee bend ~1.0×BW, second pull peak 2.0–2.5×BW.
    The wider snatch grip (vs clean grip) shortens the effective pull height, requiring
    greater barbell velocity to achieve the catch. This is why snatch 1RM is consistently
    ~63–65% of clean-and-jerk 1RM across elite weightlifters.
    Catch/squat-recovery phase: ascending (same as front squat from deep position).
    ES at catch: elite, 90% 1RM: 372% MVIC — overhead eccentric stabilisation during
    the squat descent is the defining physiological demand of the full snatch vs the power snatch.
  source: "geisler_2023 / garhammer_1993"

injury_risk:
  joint_stress:
    shoulder: high
    wrist: high
    lower_back: high
    knee: moderate
  common_injuries:
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_catch_and_squat_recovery
      risk_factors: [insufficient_shoulder_flexion, restricted_thoracic_extension, fatigue]
    - structure: lumbar_disc
      mechanism: hyperextension_during_catch
      risk_factors: [excessive_lordosis, poor_bracing, bar_drifting_forward]
    - structure: knee
      mechanism: valgus_collapse_in_deep_squat_catch
      risk_factors: [insufficient_hip_external_rotation, weak_gluteus_medius, restricted_ankle_dorsiflexion]
  contraindications:
    - acute_shoulder_injury
    - lumbar_herniation
    - acute_knee_injury

variations: [power_snatch]
progressions: [snatch_pull, overhead_squat]
alternatives: [power_snatch]

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: garhammer_1993
    title: "A Review of Power Output Studies of Olympic and Powerlifting: Methodology, Performance Prediction, and Evaluation Tests"
    author: "Garhammer, J."
    year: 1993
    doi: "10.1519/1533-4287(1993)007<0076:AROPOS>2.3.CO;2"
    credibility: literature_review
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
  - source_id: everett_weightlifting
    title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    year: 2016
    doi: null
    credibility: practitioner
---

# Snatch

The snatch is one of the two Olympic competition lifts. The barbell is pulled from the floor with a wide grip and received overhead in a full squat — simultaneously the most technically demanding and mobility-intensive movement in competitive strength sports. The bar travels from the floor to arm's length overhead in a single uninterrupted motion; the lifter descends into a full overhead squat to receive it, then stands to complete the lift. World-class performances require coordinating more than 30 joints and over 200 muscles within approximately 1 second.

## Execution

1. **Setup:** Wide snatch grip (roughly 1.5× shoulder width, measured by a forearm-length from the hip). Feet hip-width, bar over mid-foot. Hips below shoulders, shoulders over or in front of the bar. 120° hip flexion, neutral spine throughout.
2. **First pull (floor to knee):** Push the floor away; maintain constant back angle. Bar stays against the shins and thighs.
3. **Transition (double-knee bend):** As bar passes the knees, knees re-bend and hips drive forward — the torso angle rises and the bar accelerates toward the hips.
4. **Second pull (triple extension):** Explosive simultaneous hip, knee, and ankle extension. Shrug at peak. At full extension the body is vertical and slightly posterior; arms still long.
5. **Third pull (pull-under):** Simultaneously pull the body under the bar by pulling the elbows high and wide; the bar continues upward while the body drops into the overhead squat position. The bar must be locked overhead with elbows fully extended before the catch is complete.
6. **Overhead squat catch:** Receive the bar in a full squat — hips below parallel, bar directly over the midfoot, arms locked, torso upright. Stabilise the position before standing.
7. **Recovery:** Drive through the floor to stand while maintaining the overhead position; lower the bar to the thighs and then the floor.

## The Pull Phase: EMG Data

The pull-phase erector spinae demand scales dramatically with expertise. At 50% 1RM: advanced athletes 176% MVIC, elite athletes 294% MVIC. This does not reflect greater brute force but rather superior motor unit synchronisation — elite lifters recruit more muscle simultaneously rather than sequentially, producing more force in less time.

At 90% 1RM, elite erector spinae activation reaches 372% MVIC. This value reflects the full pull-and-catch cycle; the overhead squat catch portion contributes the eccentric deceleration component that elevates ES above the equivalent snatch pull (≈212% MVIC at similar loads).

## The Full Snatch vs the Power Snatch

The critical difference is the catch depth:

| Parameter | Power Snatch | Full Snatch |
|-----------|-------------|------------|
| Catch depth | ≥90° knee flexion (partial squat) | Below parallel (full squat) |
| Maximum load | ~85–90% of snatch 1RM | 100% |
| Mobility demand | Shoulder dominant | Shoulder + full squat + ankle |
| ES at catch | High | Higher — longer eccentric overhead stabilisation during squat descent |

The full snatch can handle more total load because the lifter does not need to generate enough bar height for a power (partial) catch — the bar only needs to rise high enough for the lifter to drop under it into a deep position.

## The 63% Rule

Across elite weightlifters, snatch 1RM is consistently ~63–65% of clean-and-jerk 1RM. This ratio reflects the fundamental constraint of the snatch: the wide grip shortens the effective pull height, requiring greater barbell velocity to achieve a stable overhead catch. The clean grip's narrower width allows a higher bar trajectory at equivalent force input, enabling heavier absolute loads in the clean.

## Mobility Priorities

The snatch is the most mobility-dependent barbell exercise. Deficits in any of these create compensatory faults that cannot be trained around:

1. **Shoulder flexion** (≥180°): Bar must sit directly over midfoot in the overhead squat; any restriction pushes the bar forward
2. **Thoracic extension**: Supports upright torso in the catch; restriction causes forward lean
3. **Ankle dorsiflexion** (≥38° at full depth): Restricts squat depth; forces heel rise and forward bar displacement
4. **Hip external rotation**: Determines squat stance width; restriction causes valgus collapse at depth

Shoulder flexibility correlates significantly with trunk angle at depth (r = −0.67, p = 0.003): restricted lifters lean forward, which moves the bar off the midfoot line and destabilises the catch.

> For system-specific training applications, see each system's lens entry.
