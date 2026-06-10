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
# The lower trapezius and serratus anterior roles are inferred from:
# (1) the movement being pure scapular depression with no elbow flexion, and
# (2) EMG studies of scapular depression in other contexts (wall slide, serratus push-up).
muscle_activation_studies: []

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
