---
id: power_jerk
name: Power Jerk
status: complete
category: exercise
pattern: [vertical press]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 4

muscles:
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_medialis
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: trap_upper
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: gluteus_medius
    role: stabilizer

# No peer-reviewed EMG %MVIC study found for the power jerk.
# Muscle activation pattern is inferred from structural similarity to push_press
# (dip-drive-overhead sequence) with the difference that the power jerk includes
# a receiving catch in a partial squat, adding eccentric quadriceps demand.
muscle_activation_studies: []

joint_rom_required:
  knee_flexion_dip_deg: 15
  knee_flexion_catch_deg: 90
  hip_flexion_catch_deg: 45
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  notes: >
    Dip: only 10–15° knee flexion; hips remain directly under bar.
    Catch (power receive): ~90° knee flexion, ~45° hip flexion in a shallow squat.
    Overhead lockout: 180° shoulder flexion required; elbow full extension.
    Overhead mobility is the limiting factor — insufficient shoulder flexion forces
    the bar to land behind the midfoot, creating an unstable receive position.
  source: "everett_weightlifting / crossfit_2022"

strength_curve:
  type: bell_shaped
  sticking_point: dip_reversal
  peak_force_position: drive_phase_peak
  notes: >
    The jerk GRF profile is a sharp impulse: brief eccentric dip (~10–15° knee flexion),
    maximal concentric drive (peak GRF 2.5–3.0×BW), then an eccentric landing phase
    as the feet shift and the arms receive the bar.
    The sticking point is the dip-to-drive reversal — any forward hip displacement
    during the dip shifts the bar forward off the shoulders, making the drive
    mechanically inefficient. The drive must be perfectly vertical.
    Unlike the push press (which continues pressing through the top), the power jerk
    drive terminates at full extension and the lifter drops under the bar, requiring
    precise timing of the re-squat.
  source: "garhammer_1993 / everett_weightlifting"

injury_risk:
  joint_stress:
    shoulder: high
    knee: moderate
    lower_back: low
  common_injuries:
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_overhead_catch
      risk_factors: [insufficient_shoulder_flexion, fatigue, bar_forward_of_midfoot_at_receive]
    - structure: glenohumeral_joint
      mechanism: anterior_impingement
      risk_factors: [internal_rotation_at_lockout, insufficient_thoracic_extension]
    - structure: knee
      mechanism: valgus_in_squat_catch
      risk_factors: [fatigue, heavy_load_with_weak_hip_abductors, restricted_ankle_dorsiflexion]
  notes: "The power jerk is safer than the split jerk for athletes with limited hip mobility; the symmetric squat receive is easier to stabilise than the split. However, the partial squat catch places substantial quadriceps eccentric demand at ~90° knee flexion — a high-torque position."
  contraindications:
    - acute_shoulder_injury
    - acute_knee_injury

variations: [push_press]
progressions: []
alternatives: [push_press, overhead_press]

sources:
  - source_id: garhammer_1993
    title: "A Review of Power Output Studies of Olympic and Powerlifting: Methodology, Performance Prediction, and Evaluation Tests"
    author: "Garhammer, J."
    year: 1993
    doi: "10.1519/1533-4287(1993)007<0076:AROPOS>2.3.CO;2"
    credibility: literature_review
  - source_id: everett_weightlifting
    title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    year: 2016
    doi: null
    credibility: practitioner
  - source_id: crossfit_2022
    title: "Olympic Weightlifting Movement Standards"
    author: "CrossFit Training"
    year: 2022
    doi: null
    credibility: practitioner
---

# Power Jerk

The power jerk is a jerk variation in which the bar is driven from the front rack to overhead using an explosive leg drive (dip-drive), and received with both feet moving to a slightly wider stance in a partial squat (≥90° knee angle at receive). It differs from the split jerk — the standard competition style — in that the receive position is symmetric rather than split. It is primarily used as a teaching progression to establish overhead barbell stability and dip-drive mechanics before introducing the asymmetric split position.

## Execution

1. **Front rack:** Barbell rests on the anterior deltoids with elbows high and parallel to the floor; same position as the front squat rack. Feet hip-width, core braced.
2. **Dip:** Flex the knees approximately 10–15° with a controlled, vertical descent. The hips stay directly under the bar — do not allow the torso to incline forward or the hips to push backward. This is the most commonly broken technical point.
3. **Drive:** Immediately reverse the dip with maximum force. Extend hips, knees, and ankles explosively. The bar leaves the shoulders driven entirely by the legs and momentum — do not initiate a press from the shoulders.
4. **Drop:** As the bar reaches peak height, push the body downward by pressing the arms into full lockout overhead. Move the feet slightly wider (approximately hip-width) as the body drops into the partial squat catch.
5. **Receive:** Lock the elbows completely before the feet re-contact the floor. Bar must be over the midfoot with the torso upright; hips and knees in the partial squat (~90° knee flexion).
6. **Recover:** Stand by extending hips and knees while keeping the bar locked overhead; return feet to hip-width.

## Power Jerk vs Push Press vs Split Jerk

| Feature | Push Press | Power Jerk | Split Jerk |
|---------|-----------|------------|------------|
| Leg drive | Yes (drives bar) | Yes (drives bar) | Yes (drives bar) |
| Receive position | Standing (no drop) | Symmetric partial squat | Split stance |
| Overhead stability | Stationary catch | Symmetric squat | Asymmetric split |
| Maximum load | Moderate | High | Highest |
| Technical demand | Lower | Moderate | High |

The push press does not involve dropping under the bar — the lifter stands and presses through. The power jerk drops under the bar into a receive position, allowing heavier loads because the bar needs to travel a shorter vertical distance before being caught. The split jerk allows the heaviest loads of the three by providing the deepest possible drop under the bar.

## The Dip: The Critical Phase

The dip is the most commonly faulted phase. Two errors eliminate the effectiveness of the jerk drive:

1. **Forward torso inclination during the dip** — shifts the bar forward off the anterior deltoids onto the wrists, making the drive non-vertical. The bar follows the torso angle; a forward-inclined dip produces a forward bar trajectory that cannot be received over the midfoot.

2. **Hip travel backward during the dip** — same effect: the hips moving back shift the center of mass and produce a non-vertical bar path. The cue "dip straight down, not back" corrects this.

A correctly executed dip is indistinguishable from a vertical piston movement: the bar and the hips travel down the same vertical line and reverse direction together.

## The Drive-to-Drop Transition

The window between the end of the leg drive and the overhead catch is where timing determines success. At full extension:
- The bar has peak upward velocity
- The legs are no longer in contact with the floor (brief weightless phase in maximal efforts)
- The feet must relocate to the slightly wider receive stance before the bar reaches peak height

Practicing the footwork pattern without load — "dip, drive, stomp" — builds the motor pattern before load is introduced.

> For system-specific training applications, see each system's lens entry.
