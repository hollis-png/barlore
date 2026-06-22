---
id: tire_flip
name: Tire Flip
status: complete
category: exercise
pattern: [hinge]
equipment: [tire]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 4
  mobility_prerequisite: 2

muscles:
  - id: gluteus_maximus
    role: primary
  - id: erector_spinae
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: multifidus
    role: secondary
  - id: rectus_abdominis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: pectoralis_major
    role: secondary
  - id: triceps_long
    role: secondary
  - id: triceps_lateral
    role: secondary
  - id: triceps_medial
    role: tertiary
  - id: forearm_flexors
    role: secondary
  - id: trap_upper
    role: secondary
  - id: trap_middle
    role: tertiary
  - id: gastrocnemius_medial
    role: tertiary
  - id: gastrocnemius_lateral
    role: tertiary
  - id: soleus
    role: tertiary

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 100
  knee_flexion_deg: 90
  shoulder_flexion_deg: 60
  source: "biomechanical inference from deadlift-like initial pull and push-over phase"

strength_curve:
  type: ascending
  sticking_point: initial_break_from_ground
  notes: "Hardest at the floor where the moment arm on the hips is longest. Once past 45 degrees, the push-over phase is mechanically easier."

injury_risk:
  joint_stress:
    lumbar_spine: high
    biceps_tendon: high
    shoulder: moderate
  common_injuries:
    - structure: biceps_tendon_distal
      mechanism: supinated_grip_under_heavy_load_during_initial_lift
      risk_factors: [underhand_curl_grip, excessive_tire_weight, fatigue]
    - structure: lumbar_disc
      mechanism: flexion_under_load_with_rounded_spine
      risk_factors: [excessive_tire_weight, poor_hip_hinge, fatigue]
    - structure: pectoralis_major
      mechanism: explosive_push_phase_with_arms_extended
      risk_factors: [cold_muscles, excessive_speed, pre_existing_strain]
  contraindications:
    - active_biceps_tendinopathy
    - acute_lumbar_disc_herniation
    - pectoralis_major_strain

variations: []
progressions: []
alternatives: [barbell_deadlift, power_clean]

sources: []
---

# Tire Flip

A full-body strongman movement where the athlete lifts and overturns a large tractor tire. The initial phase resembles a deadlift with a more forward lean (pulling from the ground with hip and knee extension), transitioning into an explosive push-over once the tire passes roughly 45 degrees. The tire flip is unique in that it combines hip-dominant pulling with a chest/shoulder push in a single repetition.

## Execution

1. **Setup.** Face the tire, feet shoulder-width apart, toes close to the base of the tire. Drop the hips and grip the bottom of the tire on the tread with fingers underneath. Chest drives into the tire surface. Use a pronated (palms-down) grip — never supinate (curl grip), as this dramatically increases biceps tendon rupture risk.
2. **Initial Drive.** Extend through the hips, knees, and ankles simultaneously, driving your chest into the tire. Think "leg press the ground away" rather than pulling with the arms. The arms hold position; the legs and hips generate force.
3. **Transition.** As the tire reaches approximately 45 degrees, step forward aggressively. Drive a knee into the tire for support. Quickly switch hand position from an underside grip to the upper face of the tire.
4. **Push-Over.** With hands on the upper face, extend through the arms and drive the tire forward and over. Use a split stance for balance.
5. **Reset.** Let the tire settle flat before approaching for the next rep.

## Programming Note

The tire flip carries higher injury risk than most strongman events, particularly to the distal biceps tendon. The single most important coaching cue is to avoid a supinated (underhand curl) grip during the initial lift — always grip with palms facing down. Tire flips are typically programmed for low reps (3-6 per set) with full recovery between sets. They are not well-suited to high-rep conditioning circuits due to the technical breakdown that occurs under fatigue. Choose a tire weight where technique remains clean for every rep.
