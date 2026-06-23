---
id: seated_calf_raise
name: Seated Calf Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: soleus
    role: primary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# maeo_2023: Hypertrophy study comparing seated vs standing calf raise over a training period.
# Not an EMG %MVIC study — confirmed soleus selective hypertrophy vs standing raises.
# Seated position (knee ~90°) slackens gastrocnemius at proximal attachment,
# forcing soleus to carry nearly all plantarflexion load.
muscle_activation_studies: []

joint_rom_required:
  ankle_plantarflexion_deg: 40
  ankle_dorsiflexion_deg: 20
  knee_flexion_deg: 90
  source: "maeo_2023"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom
  notes: "Descending; torque production is maximized in deep dorsiflexion and declines linearly through the range; sticking point at full plantarflexion where soleus must bear load in a shortened state; bent knee eliminates gastrocnemius contribution throughout"
  source: "biomechanical inference; Maeo 2023"

injury_risk:
  joint_stress:
    ankle: low
    knee: low
  common_injuries:
    - structure: achilles_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_drop_below_platform, pre_existing_achilles_tendinopathy]
  contraindications:
    - acute_achilles_tendinopathy

variations: []
progressions: []
alternatives: [standing_calf_raises, donkey_calf_raises]

sources:
  - source_id: maeo_2023
    title: "Seated calf training selectively develops soleus hypertrophy vs standing calf training"
    author: "Maeo, Sumiaki et al."
    year: 2023
    doi: null
    credibility: rct
---

# Seated Calf Raise

The seated calf raise isolates the soleus by performing ankle plantarflexion with the knee bent at approximately 90°. The bent knee slackens the gastrocnemius at its proximal attachment (femoral condyles), removing it from meaningful load-bearing. The soleus — which only crosses the ankle, not the knee — maintains its full mechanical advantage and carries nearly all the plantarflexion load. Maeo 2023 confirmed that the seated raise selectively develops soleus hypertrophy compared to the standing raise.

## Execution

1. Sit on the machine with the lower thigh pad adjusted to rest just above the knees
2. Place the balls of the feet on the edge of the platform, heels off
3. Lift the thigh pad by pushing up on the heels to release the safety catch
4. Lower the heels below the platform for a full soleus stretch
5. Raise to full plantarflexion; hold briefly at the top, then lower under control

## Why the Soleus Matters

The soleus constitutes approximately 60% of calf muscle volume — larger than the gastrocnemius heads combined. It is primarily slow-twitch (Type I), making it resistant to fatigue but requiring high-volume, controlled loading for growth. Many programs under-develop the soleus by focusing exclusively on standing calf raises.

The seated raise is the only major exercise that fully isolates the soleus from gastrocnemius contribution.

## Maeo 2023 Key Finding

Direct comparison of seated vs standing calf raises over a training period:
- Standing calf raises → primarily gastrocnemius hypertrophy
- Seated calf raises → primarily **soleus** hypertrophy
- Neither variation produced significant hypertrophy in the other's primary target

The two variations are not interchangeable — they develop different muscles. A complete calf program requires both.

> For system-specific training applications, see each system's lens entry.
