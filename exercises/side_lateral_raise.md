---
id: side_lateral_raise
name: Side Lateral Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_lateral
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: supraspinatus
    role: secondary
  - id: trap_upper
    role: stabilizer

# Multiple studies across different humeral rotation conditions.
# Sweeney 2014 used bent-arm (elbow ~90°) variation at 70% 1RM → deltoid_lateral 77% ± 16.1%.
# Coratella 2020 shows humeral rotation dramatically shifts anterior vs posterior delt dominance:
#   External rotation → anterior delt 80%; Internal rotation → posterior delt 85%.
# Standard neutral position: lateral delt is primary (30–77% MVIC across studies).
muscle_activation_studies:
  - source_id: campos_2020
    doi: "10.1515/hukin-2020-0023"
    n: 13
    population: "resistance-trained males, 60% 1RM, standard neutral"
    condition:
      load_pct_1rm: 60
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 21.2, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 30.3, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 24.0, sd: null}
  - source_id: coratella_2020
    doi: "10.3390/ijerph17176015"
    n: 10
    population: "competitive bodybuilders, neutral humeral rotation"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      phase: concentric
      notes: "Standard neutral grip"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 36.0, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 55.0, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 52.0, sd: null}
  - source_id: coratella_2020
    doi: "10.3390/ijerph17176015"
    n: 10
    population: "competitive bodybuilders, external humeral rotation"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      phase: concentric
      notes: "Humerus externally rotated — shifts emphasis to anterior deltoid"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 80.0, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 48.0, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 36.0, sd: null}
  - source_id: coratella_2020
    doi: "10.3390/ijerph17176015"
    n: 10
    population: "competitive bodybuilders, internal humeral rotation"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      phase: concentric
      notes: "Humerus internally rotated — shifts emphasis to posterior deltoid"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 34.0, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 52.0, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 85.0, sd: null}
  - source_id: sweeney_2014
    doi: null
    n: 16
    population: "healthy males, 70% 1RM, bent-arm variation"
    condition:
      load_pct_1rm: 70
      implement: dumbbell
      phase: full_rep
      notes: "Bent-arm (elbow ~90°) reduces moment arm and allows heavier load"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 32.0, sd: 18.5}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 77.0, sd: 16.1}
      - {muscle: deltoid_posterior, mean_pct_mvc: 33.0, sd: 14.4}

joint_rom_required:
  shoulder_abduction_deg: 90
  source: "Sweeney 2014"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Gravity moment arm increases from 0 at side to maximum at 90° abduction — resistance is lowest at the start and peaks at full parallel position"
  source: "Kassiano 2023"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries:
    - structure: supraspinatus_tendon
      mechanism: subacromial_impingement
      risk_factors: [internal_rotation_past_90_deg, pronated_grip_at_top, pre_existing_impingement]
    - structure: upper_trapezius
      mechanism: compensatory_shrug_under_load
      risk_factors: [load_too_heavy, fatigue, poor_scapular_depression_cue]
  contraindications:
    - acute_shoulder_impingement
    - supraspinatus_tear

variations: []
progressions: []
alternatives: [cable_seated_lateral_raise]

sources:
  - source_id: campos_2020
    title: "Different Shoulder Exercises Affect the Activation of Deltoid Portions in Resistance-Trained Individuals"
    author: "Campos, Yuri de Almeida Costa et al."
    year: 2020
    doi: "10.1515/hukin-2020-0023"
    credibility: rct
  - source_id: coratella_2020
    title: "An Electromyographic Analysis of Lateral Raise Variations and Frontal Raise in Competitive Bodybuilders"
    author: "Coratella, Giuseppe et al."
    year: 2020
    doi: "10.3390/ijerph17176015"
    credibility: rct
  - source_id: sweeney_2014
    title: "Dynamite Delts: ACE Research Identifies Top Shoulder Exercises"
    author: "Sweeney, Samantha; Porcari, John P. et al."
    year: 2014
    doi: null
    credibility: rct
---

# Side Lateral Raise

The side lateral raise is the primary open-chain isolation exercise for the lateral deltoid. Performed by abducting the arms from the sides to shoulder height against a dumbbell or cable load, it produces the characteristic shoulder width associated with bodybuilding aesthetics. Despite its apparent simplicity, the lateral raise is highly sensitive to humeral rotation — a single technical variable that shifts the primary load among all three deltoid heads.

## Execution

1. Stand with dumbbells at the sides, arms nearly straight (slight elbow bend to reduce joint stress)
2. Depress the scapulae before initiating — do not allow the traps to shrug as the primary movement
3. Raise the arms to approximately shoulder height (90° abduction), leading with the elbows rather than the hands
4. Keep the thumbs slightly lower than the pinkies throughout (slight internal rotation) to avoid subacromial impingement
5. Lower under control; avoid letting the weight crash back to the starting position

## What the EMG Data Shows

Three independent studies establish the lateral deltoid as the primary mover in the standard neutral raise:

| Study | Condition | Deltoid Lateral | Deltoid Anterior | Deltoid Posterior |
|-------|-----------|-----------------|------------------|-------------------|
| Campos 2020 | 60% 1RM, neutral | 30.3% | 21.2% | 24.0% |
| Coratella 2020 | Neutral, bodybuilders | 55.0% | 36.0% | 52.0% |
| Sweeney 2014 | 70% 1RM, bent-arm | 77.0% ± 16.1% | 32.0% ± 18.5% | 33.0% ± 14.4% |

The wide range in lateral deltoid values (30–77%) reflects both load and technique differences. Sweeney 2014 used a bent-arm (elbow 90°) variation at 70% 1RM — shorter moment arm, heavier absolute load, highest values. The Campos 2020 values at 60% 1RM with full extension represent the stricter, lighter version.

## The Humeral Rotation Effect

Coratella 2020 is the critical study for programming decisions. The three rotation conditions produced dramatically different activation profiles:

| Rotation | Lateral Delt | Anterior Delt | Posterior Delt |
|----------|--------------|---------------|----------------|
| Neutral | 55% | 36% | 52% |
| External | 48% | **80%** | 36% |
| Internal | 52% | 34% | **85%** |

External rotation primarily recruits the anterior deltoid — a muscle already well-stimulated by pressing. Internal rotation at end-range (above 90°) increases subacromial impingement risk. Keep the thumb-down position only through the middle range; do not force full internal rotation at peak.

## Cable vs Dumbbell

Free-weight dumbbells have zero resistance when the arms hang at the sides and peak resistance at 90° abduction. This mismatches the deltoid's strength curve and creates a dead zone at the start. Cable variations from a low pulley provide resistance at longer deltoid lengths. See `cable_seated_lateral_raise` for cable-specific guidance.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Seated lateral raise | Eliminates leg drive and momentum | Strict isolation |
| Cable lateral raise | Constant tension at bottom of range | Lengthened-position loading |
| Bent-arm lateral raise | Shorter moment arm; heavier load | Load progression |

> For system-specific training applications, see each system's lens entry.
