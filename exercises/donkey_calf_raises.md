---
id: donkey_calf_raises
name: Donkey Calf Raises
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 2

muscles:
  - id: gastrocnemius_medial
    role: primary
  - id: gastrocnemius_lateral
    role: primary
  - id: soleus
    role: secondary

# No peer-reviewed EMG data found for the donkey calf raise.
# Mechanically: hip ~90° flexion + knee extended → gastrocnemius stretched at BOTH ends.
# Proximal stretch (hip flexion elongates gastrocnemius from above the knee)
# + distal stretch (ankle dorsiflexion) = maximum gastrocnemius length of any calf exercise.
muscle_activation_studies: []

joint_rom_required:
  ankle_plantarflexion_deg: 40
  ankle_dorsiflexion_deg: 20
  hip_flexion_deg: 90
  source: "biomechanical inference"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped similar to standing raise; gastrocnemius starts from a greater elongated length due to hip flexion, providing greater stretch-mediated stimulus than standing raises"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    ankle: low
    knee: low
  common_injuries:
    - structure: achilles_tendon
      mechanism: eccentric_overload
      risk_factors: [excessive_dorsiflexion, rapid_eccentric, pre_existing_achilles_tendinopathy]
    - structure: gastrocnemius_muscle
      mechanism: stretch_overload_at_maximum_length
      risk_factors: [heavy_load_at_maximum_hip_and_ankle_flexion, pre_existing_gastrocnemius_strain]
  contraindications:
    - acute_achilles_tendinopathy
    - gastrocnemius_strain

variations: []
progressions: []
alternatives: [standing_calf_raises, seated_calf_raise]

sources: []
---

# Donkey Calf Raises

The donkey calf raise is performed with the torso bent forward at 90°, placing the hip in approximately 90° flexion while the knees remain extended. This position elongates the gastrocnemius from both ends simultaneously: hip flexion stretches it proximally (above the knee) and ankle dorsiflexion stretches it distally. No other calf exercise achieves this dual-end gastrocnemius stretch, making it the most mechanically favorable exercise for loading the gastrocnemius at its greatest possible length.

## Execution

1. Use a donkey calf raise machine — position the lower back/tailbone under the padded lever; or bend forward 90° at the hips with hands on a fixed support
2. Place the balls of the feet on the platform edge with heels off; keep the knees straight
3. Lower the heels below the platform to the maximum comfortable dorsiflexion
4. Raise the heels to full plantarflexion; hold briefly
5. Lower under full control

## The Dual-Stretch Advantage

The gastrocnemius crosses two joints: the knee and the ankle. In a standard standing raise, only the ankle is loaded in dorsiflexion. In the donkey position:

| Stretch point | Standing raise | Donkey raise |
|--------------|---------------|-------------|
| Proximal (via hip) | None | Hip flexion pulls origin further from calcaneus |
| Distal (via ankle) | Full dorsiflexion | Full dorsiflexion |
| Overall gastrocnemius length | Moderate | Maximum |

Loading muscles at longer lengths provides a greater stimulus for hypertrophy — the theoretical basis for why the donkey raise has historically been preferred by bodybuilders for gastrocnemius development.

## No EMG Data

No quantitative EMG data exists for the donkey calf raise. Expected activation: similar to or greater than standing calf raises for the gastrocnemius medial and lateral heads. The soleus remains secondary due to the extended knee.

## Practical Access

Traditional donkey calf raises require a dedicated machine or a training partner to load the hips. When unavailable, the standing calf raise is the primary gastrocnemius alternative.

> For system-specific training applications, see each system's lens entry.
