---
id: reverse_hyperextension
name: Reverse Hyperextension
status: partial
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- machine
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: erector_spinae
  role: primary
- id: multifidus
  role: primary
- id: biceps_femoris
  role: primary
- id: gluteus_maximus
  role: secondary
- id: semitendinosus
  role: secondary
- id: gastrocnemius
  role: secondary
- id: soleus
  role: secondary
muscle_activation_studies:
- source_id: dicus_2023
  doi: "10.70252/ZAOJ6139"
  n: null
  population: "apparently healthy young males"
  condition:
    load_pct_1rm: 50
    phase: concentric
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 81.6
    sd: 5.9
  - muscle: multifidus
    mean_pct_mvc: 89.8
    sd: 7.2
  - muscle: gluteus_maximus
    mean_pct_mvc: 64.3
    sd: 9.5
  - muscle: biceps_femoris
    mean_pct_mvc: 70.8
    sd: 7.0
  - muscle: semitendinosus
    mean_pct_mvc: 57.1
    sd: 8.9
- source_id: dicus_2023
  doi: "10.70252/ZAOJ6139"
  n: null
  population: "apparently healthy young males"
  condition:
    load_pct_1rm: 50
    phase: eccentric
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 54.6
    sd: 6.0
  - muscle: multifidus
    mean_pct_mvc: 59.0
    sd: 5.1
  - muscle: gluteus_maximus
    mean_pct_mvc: 36.3
    sd: 4.1
  - muscle: biceps_femoris
    mean_pct_mvc: 55.6
    sd: 8.1
  - muscle: semitendinosus
    mean_pct_mvc: 43.8
    sd: 9.5
- source_id: dicus_2023
  doi: "10.70252/ZAOJ6139"
  n: null
  population: "apparently healthy young males"
  condition:
    load_pct_1rm: 50
    phase: full_rep
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 66.6
    sd: 4.4
  - muscle: multifidus
    mean_pct_mvc: 72.8
    sd: 4.6
  - muscle: gluteus_maximus
    mean_pct_mvc: 49.1
    sd: 5.8
  - muscle: biceps_femoris
    mean_pct_mvc: 62.4
    sd: 6.5
  - muscle: semitendinosus
    mean_pct_mvc: 49.4
    sd: 7.8
- source_id: cuthbert_2021
  doi: "10.1519/JSC.0000000000004049"
  n: 10
  population: null
  condition:
    load_pct_1rm: null
    phase: concentric
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 71.0
    sd: 20.5
  - muscle: gluteus_maximus
    mean_pct_mvc: 23.4
    sd: 15.8
  - muscle: biceps_femoris
    mean_pct_mvc: 39.7
    sd: 13.4
- source_id: cuthbert_2021
  doi: "10.1519/JSC.0000000000004049"
  n: 10
  population: null
  condition:
    load_pct_1rm: null
    phase: eccentric
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 51.8
    sd: 16.1
  - muscle: gluteus_maximus
    mean_pct_mvc: 18.6
    sd: 9.2
  - muscle: biceps_femoris
    mean_pct_mvc: 28.3
    sd: 2.3
- source_id: lawrence_2019
  doi: "10.1519/JSC.0000000000003146"
  n: 20
  population: null
  condition:
    load_pct_1rm: null
    phase: full_rep
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 36.9
    sd: 25.4
  - muscle: gluteus_maximus
    mean_pct_mvc: 50.1
    sd: 23.7
  - muscle: biceps_femoris
    mean_pct_mvc: 44.7
    sd: 31.3
joint_rom_required:
  hip_flexion_deg: 76.6
  source: dicus_2023
strength_curve:
  type: ascending
  peak_force_position: lockout
variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
- source_id: dicus_2023
  doi: "10.70252/ZAOJ6139"
  title: "Posterior Chain EMG During Hip Hinge Exercises"
  credibility: peer_reviewed
- source_id: cuthbert_2021
  doi: "10.1519/JSC.0000000000004049"
  title: "EMG of reverse hyperextension"
  credibility: peer_reviewed
- source_id: lawrence_2019
  doi: "10.1519/JSC.0000000000003146"
  title: "Reverse hyperextension muscle activation"
  credibility: peer_reviewed
---

# Reverse Hyperextension

## Execution

1. Place your feet between the pads after loading an appropriate weight. Lay on the top
   pad, allowing your hips to hang off the back, while grasping the handles to hold your
   position.
2. To begin the movement, flex the hips, pulling the legs forward.
3. Reverse the motion by extending the hips, kicking the leg back. It is very important not
   to over-extend the hip on this movement, stopping short of your full range of motion.
4. Return by again flexing the hip, pulling the carriage forward as far as you can.
5. Repeat for the desired number of repetitions.

## Notes

> ⚠️ This is a stub entry imported from free-exercise-db.
> Fields marked `null` need human review.
> Add EMG data, ROM requirements, relations, and lens entries before
> changing `status` to `partial` or `complete`.
