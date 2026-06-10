---
id: concentration_curls
name: Concentration Curls
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 97.9% MVIC — highest of all curl variations tested.
# The braced elbow position eliminates momentum and anterior deltoid contribution.
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Elbow braced against inner thigh"
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 97.9, sd: null}

joint_rom_required:
  elbow_flexion_deg: 145
  shoulder_flexion_deg: 30
  source: "Porcari 2014 protocol"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; bracing the elbow against the thigh eliminates momentum but does not fundamentally alter the moment arm profile"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, grip_too_heavy]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [dumbbell_bicep_curl, preacher_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
---

# Concentration Curls

The concentration curl produces the highest biceps brachii activation of all curl variations in the ACE-commissioned Porcari 2014 study (97.9% MVIC), outperforming the barbell curl (76.5%), EZ-bar curl (75.4%), and incline dumbbell curl (77.5%). The seated position with the elbow braced against the inner thigh forces the biceps to produce the entire curl force without contributions from the anterior deltoid, upper body swing, or gravity-assisted momentum.

## Execution

1. Sit at the end of a bench with the legs spread; hold a dumbbell in one hand
2. Lean forward and brace the back of the working upper arm against the inner thigh, near the knee
3. Curl the dumbbell upward while supinating the wrist; the elbow stays fixed against the thigh
4. At the top, fully supinate and contract; lower under control through the full eccentric
5. Complete all reps for one arm, then switch

## Why Concentration Curls Produce Highest Activation

The braced elbow eliminates three compensation patterns that reduce effective biceps work in free-standing curls:
1. **Anterior deltoid swing** — the shoulder cannot flex to assist the curl when the upper arm is pinned
2. **Momentum** — no swing available; all force must come from elbow flexion
3. **Bilateral assistance** — the unilateral load prevents the stronger arm from compensating

The combination produces a purer biceps stimulus. The trade-off is that load is limited by the single-arm position and the inability to use controlled momentum at the sticking point.

## ROM Note

ROM approximates the barbell curl (144.6°) because elbow flexion range is not constrained by the thigh position. The shoulder is flexed approximately 30° by the lean-forward posture, which places the biceps long head in a slightly shorter length than an incline curl but longer than a preacher curl.

> For system-specific training applications, see each system's lens entry.
