---
id: power_snatch
name: Power Snatch
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
- id: multifidus
  role: primary
- id: vastus_lateralis
  role: primary
- id: gluteus_maximus
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
  role: secondary
muscle_activation_studies:
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 11
  population: "beginners"
  condition:
    load_pct_1rm: 50
    phase: pull_and_catch
  measurements:
  - muscle: trap_upper
    mean_pct_mvc: 71.69
    sd: 23.21
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 10
  population: "advanced"
  condition:
    load_pct_1rm: 50
    phase: pull_and_catch
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 175.69
    sd: 134.95
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 6
  population: "elite"
  condition:
    load_pct_1rm: 50
    phase: pull_and_catch
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 294.28
    sd: 152.77
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 11
  population: "beginners"
  condition:
    load_pct_1rm: 90
    phase: pull_and_catch
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 215.68
    sd: 321.69
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 6
  population: "elite"
  condition:
    load_pct_1rm: 90
    phase: pull_and_catch
  measurements:
  - muscle: erector_spinae
    mean_pct_mvc: 371.62
    sd: 271.60
joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 90
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: "Setup: 120 hip flexion; catch requires 90 knee flexion and 180 shoulder flexion"
  source: geisler_2023
strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: "Wider grip vs clean shortens pull height; ES catch demand 371% MVIC at 90% 1RM (elite)"
variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  title: "Effects of Expertise on Muscle Activity during Hang Power Clean and Hang Power Snatch vs Clean/Snatch Pulls"
  credibility: peer_reviewed
---

# Power Snatch

## Execution

1. Begin with a loaded barbell on the floor. The bar should be close to or touching the
   shins, and a wide grip should be taken on the bar. The feet should be directly below
   the hips, with the feet turned out as needed. Lower the hips, with the chest up and
   the head looking forward. The shoulders should be just in front of the bar. This will
   be the starting position.
2. Begin the first pull by driving through the front of the heels, raising the bar from the
   ground. The back angle should stay the same until the bar passes the knees.
3. Transition into the second pull by extending through the hips knees and ankles, driving
   the bar up as quickly as possible. The bar should be close to the body. At peak
   extension, shrug the shoulders and allow the elbows to flex to the side.
4. As you move your feet into the receiving position, a slightly wider position, pull
   yourself below the bar as you elevate the bar overhead. The bar should be received in
   a partial squat. Continue raising the bar to the overhead position, receiving the bar
   locked out overhead.
5. Return to a standing position with the weight over head.

## Notes

> ⚠️ This is a stub entry imported from free-exercise-db.
> Fields marked `null` need human review.
> Add EMG data, ROM requirements, relations, and lens entries before
> changing `status` to `partial` or `complete`.
