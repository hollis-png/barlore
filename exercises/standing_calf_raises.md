---
id: standing_calf_raises
name: Standing Calf Raises
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: gastrocnemius_medial
    role: primary
  - id: gastrocnemius_lateral
    role: primary
  - id: soleus
    role: secondary

# riemann_2011: gastrocnemius_medial 46%, gastrocnemius_lateral 35%, soleus 35% MVIC.
# Standing (knee extended) → gastrocnemius at optimal length (crosses knee joint).
# Soleus activates at lower relative level vs gastrocnemius because knee extension
# puts gastrocnemius at a favorable length while soleus (knee-independent) contributes proportionally less.
muscle_activation_studies:
  - source_id: riemann_2011
    doi: null
    n: null
    population: "healthy adults, standing calf raise machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Standing with knee extended; gastrocnemius at optimal length"
    measurements:
      - {muscle: gastrocnemius_medial,  mean_pct_mvc: 46.0, sd: null}
      - {muscle: gastrocnemius_lateral, mean_pct_mvc: 35.0, sd: null}
      - {muscle: soleus,               mean_pct_mvc: 35.0, sd: null}

joint_rom_required:
  ankle_plantarflexion_deg: 40
  ankle_dorsiflexion_deg: 20
  source: "riemann_2011"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; peak plantarflexion force at mid-range (heel level with platform); decreasing at extreme dorsiflexion and extreme plantarflexion"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    ankle: low
    knee: low
  common_injuries:
    - structure: achilles_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_drop_below_platform, pre_existing_achilles_tendinopathy]
    - structure: plantar_fascia
      mechanism: stretch_overload_at_bottom
      risk_factors: [excessive_dorsiflexion_range, pre_existing_plantar_fasciitis]
  contraindications:
    - acute_achilles_tendinopathy
    - acute_plantar_fasciitis

variations: []
progressions: []
alternatives: [seated_calf_raise, donkey_calf_raises]

sources:
  - source_id: riemann_2011
    title: "Electromyographic analysis of the calf complex during various heel-raise conditions"
    author: "Riemann, Bryan L. et al."
    year: 2011
    doi: null
    credibility: rct
---

# Standing Calf Raises

The standing calf raise is the primary gastrocnemius-biased calf exercise. Performed with the knee extended, the gastrocnemius — which crosses both the knee and ankle joints — is at its optimal mechanical length for force production. Riemann 2011 confirms gastrocnemius medial dominance (46% MVIC) with the soleus as secondary contributor at the same level as the lateral head (35% each).

## Execution

1. Position the shoulders under the machine pads; stand with the balls of the feet on the edge of the platform, heels hanging off
2. Keep the knees straight but not hyperextended throughout
3. Lower the heels below platform level to achieve full ankle dorsiflexion (calf stretch)
4. Raise the heels as high as possible into full plantarflexion; hold at the top for a count
5. Lower under full control — do not let the heels bounce at the bottom

## What the EMG Data Shows

Riemann 2011 (standing, knee extended):

| Muscle | Activation |
|--------|-----------|
| Gastrocnemius medial | 46% MVIC |
| Gastrocnemius lateral | 35% MVIC |
| Soleus | 35% MVIC |

The medial gastrocnemius dominates, consistent with its larger cross-sectional area.

## Why the Knee Must Be Extended

The gastrocnemius originates above the knee (femoral condyles). When the knee is bent, the gastrocnemius is slackened at its proximal end, reducing its mechanical advantage. Standing calf raises with the knee straight maximize gastrocnemius length and contribution. The seated calf raise (knee ~90°) dramatically reduces gastrocnemius contribution and isolates the soleus instead.

## Foot Position

| Foot position | Effect |
|--------------|--------|
| Toes forward | Balanced medial/lateral |
| Toes out (external rotation) | Slightly greater medial head emphasis |
| Toes in (internal rotation) | Slightly greater lateral head emphasis |

> For system-specific training applications, see each system's lens entry.
