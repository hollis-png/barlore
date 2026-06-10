---
id: seated_bent_over_rear_delt_raise
name: Seated Bent-Over Rear Delt Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_posterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: trap_middle
    role: secondary
  - id: rhomboids
    role: secondary
  - id: infraspinatus
    role: stabilizer

# Sweeney 2014 (n=16): 70% 1RM, torso bent forward parallel to ground.
# Posterior delt 73% ± 9.9% MVIC; lateral delt 70% ± 14.6%.
# Anterior delt near-zero (5% ± 4.1%) confirms effective posterior isolation.
# Bending torso 90° forward aligns the transverse plane of horizontal abduction with gravity.
muscle_activation_studies:
  - source_id: sweeney_2014
    doi: null
    n: 16
    population: "healthy males, 70% 1RM, torso parallel to floor"
    condition:
      load_pct_1rm: 70
      implement: dumbbell
      phase: full_rep
      notes: "Seated, torso bent forward until parallel to ground"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 5.0,  sd: 4.1}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 70.0, sd: 14.6}
      - {muscle: deltoid_posterior, mean_pct_mvc: 73.0, sd: 9.9}

joint_rom_required:
  shoulder_abduction_deg: 90
  hip_flexion_deg: 90
  source: "Sweeney 2014"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Maximum gravity-dependent resistance torque at 90° horizontal abduction when humerus is parallel to the ground"
  source: "Sweeney 2014"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: prolonged_hip_flexion_under_load
      risk_factors: [heavy_loads, sustained_bent_over_position, pre_existing_lumbar_pathology]
  contraindications:
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: [face_pull, bent_over_dumbbell_rear_delt_raise_with_head_on_bench]

sources:
  - source_id: sweeney_2014
    title: "Dynamite Delts: ACE Research Identifies Top Shoulder Exercises"
    author: "Sweeney, Samantha; Porcari, John P. et al."
    year: 2014
    doi: null
    credibility: rct
---

# Seated Bent-Over Rear Delt Raise

The seated bent-over rear delt raise is the most evidence-supported open-chain isolation exercise for the posterior deltoid. Performed seated with the torso hinged forward until parallel to the floor, the movement targets the posterior deltoid and lateral deltoid simultaneously through horizontal abduction against gravity. The near-zero anterior deltoid activation (5% MVIC) confirms that the bent-forward torso position effectively eliminates anterior deltoid contribution present in upright movements.

## Execution

1. Sit at the end of a bench with dumbbells hanging between the legs
2. Hinge the torso forward until nearly parallel to the floor; keep the spine neutral (do not round)
3. With elbows slightly bent and fixed, raise the dumbbells laterally in an arc until arms are parallel to the floor
4. Focus on "opening" the shoulder blades apart rather than shrugging
5. Lower under control; do not let the dumbbells pull the shoulders forward at the bottom

## What the EMG Data Shows

Sweeney 2014 (n=16, 70% 1RM):

| Muscle | Activation |
|--------|-----------|
| Posterior deltoid | 73.0 ± 9.9% MVIC |
| Lateral deltoid | 70.0 ± 14.6% MVIC |
| Anterior deltoid | 5.0 ± 4.1% MVIC |

The posterior and lateral deltoid values are nearly identical, confirming that bending the torso 90° forward aligns both heads with the gravity vector. Compared to the standard lateral raise (posterior delt only 33% MVIC in Sweeney 2014), the torso-forward position more than doubles posterior delt activation without changing the load.

## Torso Angle Is the Key Variable

By bending 90° forward, the horizontal plane of shoulder abduction becomes the line of action against gravity. The posterior deltoid, which performs horizontal abduction, now drives directly against gravitational resistance rather than acting as a stabilizer. Sitting removes lower-body compensation and prevents upper-body momentum.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Face pull | Cable; adds external rotation | Shoulder health; rotator cuff involvement |
| Chest-supported rear delt raise | Forehead on bench; eliminates spinal erector demand | Lumbar sensitivity |
| Cable rear delt fly | Constant tension | Lengthened-position load |

> For system-specific training applications, see each system's lens entry.
