---
id: clean_and_jerk
name: Clean and Jerk
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 4
  mobility_prerequisite: 5

muscles:
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: triceps_brachii
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

# Geisler 2023 measured Hang Power Clean (HPC) for the clean phase — used as proxy.
# The full clean starts from the floor (first pull demand) and catches in a full front
# squat (adds quad recovery demand). Pull-phase VL and GM data from HPC apply.
# No peer-reviewed %MVIC study found for the jerk phase specifically.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
      notes: "Hang Power Clean proxy for clean pull phase"
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 163.82, sd: 64.41}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 124.91, sd: 76.67}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
      notes: "Hang Power Clean proxy for clean pull phase"
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 324.41, sd: 305.15}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 298.74, sd: 195.54}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
      notes: "Hang Power Clean proxy; no jerk-phase EMG available"
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 249.30, sd: 213.53}

joint_rom_required:
  hip_flexion_clean_deg: 120
  knee_flexion_front_squat_catch_deg: 130
  ankle_dorsiflexion_deg: 25
  shoulder_flexion_front_rack_deg: 173
  shoulder_external_rotation_front_rack_deg: 107
  shoulder_flexion_overhead_deg: 180
  shoulder_external_rotation_overhead_deg: 90
  notes: >
    The clean and jerk requires both front-rack and overhead mobility — more total
    demands than either the clean or the jerk individually.
    Clean front-rack: 173° shoulder flexion, 107° ER (same as power_clean).
    Jerk overhead: 180° shoulder flexion, 90° ER.
    The front squat catch adds ~130° knee flexion and ~25° ankle dorsiflexion.
    Athletes with adequate front-rack mobility but insufficient overhead mobility
    cannot complete the jerk without compensatory forward bar displacement.
  source: "nasm_2020 / crossfit_2022; everett_weightlifting"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Clean phase: bell-shaped GRF profile. First pull ~1.5×BW; second pull peak
    2.0–2.5×BW; unweighting at double-knee bend ~1.0×BW.
    VL and GM activation at elite level reach 324% and 299% MVIC respectively at 50% 1RM.
    Front squat recovery: ascending curve from the deep front squat position.
    Jerk phase: distinct impulse profile — dip (brief eccentric, 10–15° knee flexion),
    drive (explosive triple extension peak GRF ~2.5–3.0×BW), catch (overhead eccentric
    stabilisation, GRF ~1.5×BW as split stance absorbs landing).
    Total system: the clean and jerk is not the sum of its parts — the transition from
    clean rack to jerk dip requires resetting bracing and position under fatigue.
  source: "geisler_2023 / garhammer_1993 / kawamori_2005"

injury_risk:
  joint_stress:
    wrist: high
    shoulder: high
    lower_back: moderate
    knee: moderate
  common_injuries:
    - structure: wrist_extensors
      mechanism: forced_extension_on_clean_catch
      risk_factors: [insufficient_shoulder_er, poor_front_rack_mobility, heavy_load]
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_jerk_catch
      risk_factors: [insufficient_overhead_shoulder_flexion, fatigue_from_preceding_clean]
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_away_from_body_during_pull, poor_bracing]
    - structure: knee
      mechanism: valgus_in_front_squat_recovery
      risk_factors: [fatigue, restricted_ankle_dorsiflexion, weak_hip_abductors]
  notes: "The transition from clean to jerk is a distinct injury window: the lifter must re-brace and stabilise the front rack under fatigue before initiating the jerk dip. Rushing this transition with unstable position is a common cause of failed attempts and shoulder injuries."
  contraindications:
    - acute_wrist_injury
    - acute_shoulder_injury
    - lumbar_herniation

variations: [power_clean]
progressions: [power_clean, front_squat]
alternatives: [power_clean]

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
  - source_id: everett_weightlifting
    title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    year: 2016
    doi: null
    credibility: practitioner
---

# Clean and Jerk

The clean and jerk is the second of the two Olympic competition lifts and produces the highest absolute loads of any barbell movement in competitive sport. It consists of two distinct sub-movements: the clean (pulling the barbell from the floor to the front-rack position on the shoulders, received in a full front squat) and the jerk (driving the bar from the front rack to full overhead lockout). World records exceed 265 kg. Because the jerk uses leg drive to initiate the overhead press, the clean-and-jerk can be loaded substantially heavier than a strict overhead press — typically 40–50% more.

## Execution

### Phase 1: The Clean

1. **Setup:** Feet hip-width, bar over mid-foot. Narrow clean grip just outside the hips. Hips below shoulders, shoulders over bar. Neutral spine, 120° hip flexion.
2. **First pull (floor to knee):** Extend hips and knees simultaneously while maintaining back angle. Bar tracks against the shins.
3. **Transition:** As bar passes the knees, knees re-bend and hips push forward; torso rises.
4. **Second pull (triple extension):** Explosive hip, knee, and ankle extension; shrug at peak. Full extension, slightly posterior lean.
5. **Third pull / elbow turnover:** Pull elbows under the bar rapidly; receive in front-rack — elbows high and parallel, bar on anterior deltoids. Descend into a full front squat.
6. **Front squat recovery:** Drive through the floor to standing while maintaining upright torso and elbows up.

### Phase 2: The Jerk

7. **Dip:** With the bar in the front rack and core braced, flex knees ~10–15° in a controlled descent; hips stay directly under the bar (do not push backward).
8. **Drive:** Reverse direction explosively — maximal triple extension. The bar leaves the shoulders driven by leg power.
9. **Split receive:** As the bar rises, split the feet (one forward, one back) and lock the arms overhead simultaneously. Bar must be over midfoot with elbows fully extended before the feet land.
10. **Recovery:** Bring the front foot back, then the rear foot forward until feet are level; the bar stays locked overhead.
11. Lower the bar under control.

## Clean Phase EMG

The clean pull phase is dominated by vastus lateralis and gluteus maximus. Elite athletes at 50% 1RM show VL 324% MVIC and GM 299% MVIC (Geisler 2023, Hang Power Clean proxy). These supramaximal values reflect the explosive motor unit synchronisation of experienced weightlifters — not greater absolute force but faster recruitment.

VL and GM activation at elite level plateaus from 70–90% 1RM (249–307% VL range), consistent with power_clean data: the pull mechanism reaches near-ceiling activation at moderate relative loads, and heavier absolute loads require more time-under-tension rather than greater peak activation.

The full clean front squat recovery adds quadriceps and gluteus maximus demand for the ascending portion from a ~130° knee flexion position — this is not captured in the pull-phase EMG values.

## Jerk Phase: Power Output

The jerk produces the highest instantaneous power output in the clean-and-jerk sequence. Garhammer (1993) estimated system peak power during the jerk at 35–50 W/kg bodyweight in elite lifters, driven by the brief but maximal leg drive. The jerk's GRF profile shows a sharp impulse peak (2.5–3.0×BW) during the drive, substantially above the clean's second pull peak, because the knee range is shorter and the bar is already at shoulder height (zero pull height required).

## The Clean-to-Jerk Transition

The transition is a frequently under-trained phase. After a maximal clean, the lifter must:
1. Stand with the bar in front rack under fatigue
2. Re-establish foot position and brace
3. Execute a precisely timed dip-drive

Rushing this sequence while the core is compromised by the preceding clean is a primary cause of failed jerks and shoulder injuries. Advanced programming dedicates specific work to this transition (e.g., pause clean and jerks, clean + 3-second pause + jerk).

## Load Relationship: Why C&J > Snatch

Across elite athletes, clean-and-jerk 1RM is consistently ~135–158% of snatch 1RM. The snatch requires bar velocity sufficient to reach full overhead height from the floor in one motion; the clean only needs the bar to reach shoulder height, and the jerk's leg drive provides the remaining overhead energy. This mechanical advantage — splitting the lift into two sub-movements — allows substantially higher total loads.

> For system-specific training applications, see each system's lens entry.
