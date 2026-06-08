---
id: sumo_deadlift
name: Sumo Deadlift
status: partial
source: free-exercise-db
category: exercise
pattern:
- hinge
equipment:
- barbell
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: erector_spinae
  role: primary
- id: biceps_femoris
  role: primary
- id: gluteus_maximus
  role: primary
- id: vastus_lateralis
  role: primary
- id: vastus_medialis
  role: secondary
- id: semitendinosus
  role: secondary
- id: adductor_magnus
  role: secondary
- id: adductor_longus
  role: secondary
- id: multifidus
  role: secondary
- id: rhomboids
  role: secondary
- id: trap_upper
  role: secondary
- id: forearm_flexors
  role: secondary
muscle_activation_studies:
- source_id: hanen_2025
  doi: "10.3389/fbioe.2025.1597209"
  n: 30
  population: null
  condition:
    load_pct_1rm: 85
    phase: concentric
    notes: "Phase 1 (liftoff to knee)"
  measurements:
  - muscle: biceps_femoris
    mean_pct_mvc: 71.3
    sd: null
  - muscle: gluteus_maximus
    mean_pct_mvc: 71.2
    sd: null
  - muscle: vastus_lateralis
    mean_pct_mvc: 63.3
    sd: null
  - muscle: erector_spinae
    mean_pct_mvc: 74.7
    sd: null
- source_id: hanen_2025
  doi: "10.3389/fbioe.2025.1597209"
  n: 30
  population: null
  condition:
    load_pct_1rm: 85
    phase: concentric
    notes: "Phase 2 (knee to lockout)"
  measurements:
  - muscle: biceps_femoris
    mean_pct_mvc: 69.9
    sd: null
  - muscle: gluteus_maximus
    mean_pct_mvc: 74.2
    sd: null
  - muscle: vastus_lateralis
    mean_pct_mvc: 40.0
    sd: null
  - muscle: erector_spinae
    mean_pct_mvc: 67.0
    sd: null
- source_id: escamilla_2002
  doi: "10.1097/00005768-200204000-00019"
  n: 13
  population: null
  condition:
    load_pct_1rm: null
    phase: full_rep
  measurements:
  - muscle: vastus_lateralis
    mean_pct_mvc: 48
    sd: null
  - muscle: vastus_medialis
    mean_pct_mvc: 44
    sd: null
joint_rom_required:
  hip_flexion_deg: 39.9
  knee_flexion_deg: 38.1
  ankle_dorsiflexion_deg: 15.0
  source: hanen_2025
strength_curve:
  type: descending
  peak_force_position: bottom
variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
- source_id: hanen_2025
  doi: "10.3389/fbioe.2025.1597209"
  title: "Biomechanics of the sumo deadlift"
  credibility: peer_reviewed
- source_id: escamilla_2002
  doi: "10.1097/00005768-200204000-00019"
  title: "Biomechanics of the deadlift"
  credibility: peer_reviewed
---

# Sumo Deadlift

## Execution

1. Begin with a bar loaded on the ground. Approach the bar so that the bar intersects the
   middle of the feet. The feet should be set very wide, near the collars. Bend at the
   hips to grip the bar. The arms should be directly below the shoulders, inside the
   legs, and you can use a pronated grip, a mixed grip, or hook grip. Relax the
   shoulders, which in effect lengthens your arms.
2. Take a breath, and then lower your hips, looking forward with your head with your chest
   up. Drive through the floor, spreading your feet apart, with your weight on the back
   half of your feet. Extend through the hips and knees.
3. As the bar passes through the knees, lean back and drive the hips into the bar, pulling
   your shoulder blades together.
4. Return the weight to the ground by bending at the hips and controlling the weight on the
   way down.

## Notes

> ⚠️ This is a stub entry imported from free-exercise-db.
> Fields marked `null` need human review.
> Add EMG data, ROM requirements, relations, and lens entries before
> changing `status` to `partial` or `complete`.
