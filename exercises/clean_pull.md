---
id: clean_pull
name: Clean Pull
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
- id: rectus_femoris
  role: secondary
- id: vastus_medialis
  role: secondary
- id: biceps_femoris
  role: secondary
- id: semitendinosus
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
    phase: pull
  measurements:
  - muscle: vastus_lateralis
    mean_pct_mvc: 152.72
    sd: 70.36
  - muscle: gluteus_maximus
    mean_pct_mvc: 81.67
    sd: 27.32
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 10
  population: "advanced"
  condition:
    load_pct_1rm: 50
    phase: pull
  measurements:
  - muscle: vastus_lateralis
    mean_pct_mvc: 195.47
    sd: 165.81
  - muscle: gluteus_maximus
    mean_pct_mvc: 90.53
    sd: 52.44
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 6
  population: "elite"
  condition:
    load_pct_1rm: 50
    phase: pull
  measurements:
  - muscle: vastus_lateralis
    mean_pct_mvc: 239.40
    sd: 86.53
  - muscle: gluteus_maximus
    mean_pct_mvc: 258.65
    sd: 258.35
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 11
  population: "beginners"
  condition:
    load_pct_1rm: 90
    phase: pull
  measurements:
  - muscle: vastus_lateralis
    mean_pct_mvc: 225.98
    sd: 201.09
- source_id: geisler_2023
  doi: "10.52082/jssm.2023.778"
  n: 6
  population: "elite"
  condition:
    load_pct_1rm: 90
    phase: pull
  measurements:
  - muscle: vastus_lateralis
    mean_pct_mvc: 311.81
    sd: 271.74
joint_rom_required:
  hip_flexion_deg: 120
  notes: "Setup: 120 hip flexion; terminates at full extension (no catch phase)"
  source: geisler_2023
strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: "Midthigh pull: peak force 2880 N, RFD 15321 N/s — superior overload vs floor start"
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

# Clean Pull

## Execution

1. With a barbell on the floor close to the shins, take an overhand or hook grip just
   outside the legs. Lower your hips with the weight focused on the heels, back
   straight, head facing forward, chest up, with your shoulders just in front of the
   bar. This will be your starting position.
2. Begin the first pull by driving through the heels, extending your knees. Your back angle
   should stay the same, and your arms should remain straight and elbows out. Move the
   weight with control as you continue to above the knees.
3. Next comes the second pull, the main source of acceleration for the clean. As the bar
   approaches the mid-thigh position, begin extending through the hips. In a jumping
   motion, accelerate by extending the hips, knees, and ankles, using speed to move the
   bar upward. There should be no need to actively pull through the arms to accelerate
   the weight; at the end of the second pull, the body should be fully extended, leaning
   slightly back, with the arms still extended. Full extension should be violent and
   abrupt, and ensure that you do not prolong the extension for longer than necessary.

## Notes

> ⚠️ This is a stub entry imported from free-exercise-db.
> Fields marked `null` need human review.
> Add EMG data, ROM requirements, relations, and lens entries before
> changing `status` to `partial` or `complete`.
