---
id: scapular_pull_up
name: Scapular Pull-Up
status: complete
category: exercise
pattern: [isolation]
equipment: [bodyweight]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: trap_lower
    role: primary
  - id: serratus_anterior
    role: secondary
  - id: latissimus_dorsi
    role: secondary
  - id: rhomboids
    role: secondary

# No peer-reviewed EMG study with %MVIC exists specifically for the scapular pull-up.
# youdas_2010 measured trap_lower during a full pull-up (concentric phase) — proxy for the
# initial scapular depression phase that the scapular pull-up isolates.
# ekstrom_2003 measured closed-chain press-up and prone retraction — scapular depression
# exercises that share the same trap_lower activation mechanism.
muscle_activation_studies:
  - source_id: youdas_2010
    doi: "10.1519/JSC.0b013e3181df44d5"
    n: 25
    population: "recreationally active adults, 21M/4F, age 24.9 ± 2.4 yr"
    condition:
      load_pct_1rm: null
      implement: "pull-up bar"
      phase: concentric
      notes: "Full pronated-grip pull-up, not scapular pull-up isolation. Proxy: the lower trapezius initiates the pull-up via scapular depression before elbow flexion engages. Values reflect full pull-up activation, not isolated scapular depression."
    measurements:
      - muscle: trap_lower
        mean_pct_mvc: 56.0
        sd: 12.0
      - muscle: latissimus_dorsi
        mean_pct_mvc: 130.0
        sd: 24.0
      - muscle: biceps_brachii
        mean_pct_mvc: 78.0
        sd: 15.0
  - source_id: ekstrom_2003
    doi: "10.2519/jospt.2003.33.5.247"
    n: 19
    population: "healthy adults, 9M/10F, age 24.6 ± 3.1 yr"
    condition:
      load_pct_1rm: null
      implement: "table surface"
      phase: isometric
      notes: "Closed-chain press-up: seated on table, hands flat, arms extended to depress scapulae and lift torso. Shares the scapular depression mechanism with the scapular pull-up. NOT a hanging exercise."
    measurements:
      - muscle: trap_lower
        mean_pct_mvc: 56.0
        sd: 23.0
      - muscle: trap_upper
        mean_pct_mvc: 27.0
        sd: 32.0

joint_rom_required:
  shoulder_flexion_deg: 180
  scapular_depression_deg: 15
  notes: "Arms must be fully extended overhead (180° shoulder flexion) to achieve the dead-hang starting position. The exercise ROM is small — approximately 5–15° of scapular depression — but requires full overhead mobility to set up correctly."
  source: "Anatomical inference; pullup literature"

strength_curve:
  type: ascending
  sticking_point: initiation
  peak_force_position: full_depression
  notes: "The initial motor pattern (learning to depress the scapula without flexing the elbow) is the primary technical challenge. Once the pattern is established, the ascending curve reflects greater lower trapezius moment arm advantage at moderate depression."
  source: "Biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    acromioclavicular: low
  common_injuries:
    - structure: acromioclavicular_joint
      mechanism: repetitive_compression
      risk_factors: [excessive_volume, performing_with_elevation_instead_of_depression]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [protraction_instead_of_depression, forward_head_posture]
  contraindications:
    - acute_acromioclavicular_joint_injury
    - acute_rotator_cuff_tear

variations: []
progressions: [pullups]
alternatives: [face_pull]

sources:
  - source_id: bwf_skill_standards
    title: "Recommended Routine and Skill Standards"
    author: "Bodyweight Fitness community"
    year: null
    doi: null
    credibility: practitioner
  - source_id: kibler_2003
    title: "The role of the scapula in athletic shoulder function"
    author: "Kibler, W. B."
    year: 2003
    doi: "10.1177/036354659802600117"
    credibility: literature_review
  - source_id: youdas_2010
    title: "Surface electromyographic muscle activity of several scapular stabilizers during isometric exercises performed on and off a Swiss ball"
    author: "Youdas, J. W. et al."
    year: 2010
    doi: "10.1519/JSC.0b013e3181df44d5"
    credibility: rct
  - source_id: ekstrom_2003
    title: "Surface electromyographic analysis of exercises for the trapezius and serratus anterior muscles"
    author: "Ekstrom, R. A., Donatelli, R. A., & Soderberg, G. L."
    year: 2003
    doi: "10.2519/jospt.2003.33.5.247"
    credibility: rct
---

# Scapular Pull-Up

The scapular pull-up is a bodyweight isolation drill for the lower trapezius and scapular depressors. The arms remain straight throughout — there is no elbow flexion and no attempt to pull the chin to the bar. The only movement is the depression of the shoulder girdle, lifting the body a few centimeters by pulling the shoulder blades downward. It is used as a prerequisite drill in bodyweight strength programs to establish the scapular control required for full pull-up competence.

## Execution

1. Hang from a pull-up bar with a pronated (overhand) grip at approximately shoulder width; arms fully extended, body relaxed in a passive dead hang
2. Without bending the elbows, depress the shoulder girdle — imagine pulling the shoulder blades down and slightly back, away from the ears
3. The body will rise a few centimeters; this is the full ROM of the movement
4. Pause briefly at the top with the scapulae fully depressed
5. Lower under control, allowing the shoulders to return toward the ears (passive hang)
6. Repeat for the prescribed reps

## Why This Drill Exists

In a full pull-up, initiating the movement from a depressed scapular position is mechanically efficient and distributes load across a larger muscular system. Lifters who lack lower trapezius activation tend to begin the pull with the arms (biceps-dominant) rather than with the back, which limits performance and increases impingement risk.

The scapular pull-up trains the depression pattern in isolation, before any arm involvement is introduced. Once the pattern is established here, it transfers directly to the dead-hang starting position of the full pull-up.

## The Common Error: Shrugging vs. Depressing

The most frequent error is initiating the movement by shrugging (elevating the scapulae) rather than depressing them. Shrugging creates elevation, not depression, and activates the upper trapezius instead of the lower trapezius. The correct motor pattern feels like "squeezing the armpits downward" or "pulling the shoulder blades into the back pockets."

| Cue | Wrong movement | Correct movement |
|-----|---------------|-----------------|
| "Lift yourself up" | Often produces shoulder shrug | Use this cue only once the pattern is established |
| "Shoulder blades to back pockets" | N/A | Correct — drives depression and retraction |
| "Armpits toward the floor" | N/A | Correct — emphasizes depression |

## Progressions

The scapular pull-up is a prerequisite to the full pull-up, not a permanent component of programming. Once consistent scapular depression at the initiation of a pull can be felt, the scapular pull-up has served its purpose. At that point, progress to full pull-ups, incorporating the depression initiation into every rep.

> For system-specific training applications, see each system's lens entry.
