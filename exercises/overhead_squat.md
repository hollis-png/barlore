---
id: overhead_squat
name: Overhead Squat
status: partial
source: free-exercise-db
category: exercise
pattern:
- squat
equipment:
- barbell
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: vastus_lateralis
  role: primary
- id: rectus_femoris
  role: primary
- id: vastus_medialis
  role: primary
- id: gluteus_maximus
  role: primary
- id: erector_spinae
  role: primary
- id: trap_middle
  role: primary
- id: deltoid_anterior
  role: primary
- id: biceps_femoris
  role: secondary
- id: semitendinosus
  role: secondary
- id: multifidus
  role: secondary
- id: external_oblique
  role: secondary
- id: rectus_abdominis
  role: secondary
- id: triceps_brachii
  role: secondary
- id: gastrocnemius
  role: secondary
- id: soleus
  role: secondary
muscle_activation_studies:
- source_id: bautista_2020
  doi: "10.70252/BTUH3630"
  n: 7
  population: "recreationally_trained"
  condition:
    load_pct_1rm: 95
    phase: concentric
    notes: "95% of 3RM"
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 63.40
    sd: 23.30
  - muscle: rectus_abdominis
    mean_pct_mvc: 14.40
    sd: 6.40
  - muscle: external_oblique
    mean_pct_mvc: 16.90
    sd: 3.10
- source_id: aspe_2014
  doi: "10.1519/JSC.0000000000000462"
  n: 14
  population: "rugby_union_athletes"
  condition:
    load_pct_1rm: 90
    phase: full_rep
    notes: "90% of 3RM"
  measurements:
  - muscle: gluteus_maximus
    mean_pct_mvc: 60.90
    sd: null
  - muscle: biceps_femoris
    mean_pct_mvc: 54.00
    sd: null
joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 90
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: "Shoulder flexibility correlates with trunk angle at bottom (r=-0.67); restricted shoulder forces compensatory trunk lean"
  source: bautista_2020
strength_curve:
  type: ascending
  sticking_point: just_above_parallel
  peak_force_position: lockout
  notes: "Adding load increases hip torque disproportionately; knee torque unchanged — progressive demand shifts to hip extensors"
variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
- source_id: bautista_2020
  doi: "10.70252/BTUH3630"
  title: "Overhead Squat EMG and Kinematics in Recreationally Trained Subjects"
  credibility: peer_reviewed
- source_id: aspe_2014
  doi: "10.1519/JSC.0000000000000462"
  title: "Electromyographic Activity of the Overhead and Back Squat"
  credibility: peer_reviewed
---

# Overhead Squat

## Execution

1. Start out by having a barbell in front of you on the floor. Your feet should be wider
   than shoulder width apart from each other.
2. Bend the knees and use a pronated grip (palms facing you) to grab the barbell. Your
   hands should be at a wider than shoulder width apart from each other before lifting.
   Once you are positioned, lift the barbell up until you can rest it on your chest.
3. Move the barbell over and slightly behind your head and make sure your arms are fully
   extended. Keep your head up at all times and also maintain a straight back. Retract
   your shoulder blades. This is your starting position.
4. Slowly lower the weight by bending your knees until your thighs are parallel to the
   ground while inhaling. Tip: Keep your back straight while performing this exercise to
   avoid any injuries and your arms should remain extended and over your head at all
   times.
5. Now use your feet and legs to help bring the weight back up to the starting position
   while exhaling.
6. Repeat for the recommended amount of repetitions.

## Notes

> ⚠️ This is a stub entry imported from free-exercise-db.
> Fields marked `null` need human review.
> Add EMG data, ROM requirements, relations, and lens entries before
> changing `status` to `partial` or `complete`.
