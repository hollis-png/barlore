---
id: hammer_curls
name: Hammer Curls
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: brachialis
    role: primary
  - id: brachioradialis
    role: primary
  - id: biceps_brachii
    role: secondary

# jahizi_2023 (n=30): neutral grip — no absolute %MVIC values reported; qualitative analysis only.
# Neutral grip eliminates the supination function of biceps brachii → shifts load to brachialis and brachioradialis.
# ROM: 140° elbow flexion.
muscle_activation_studies:
  - source_id: jahizi_2023
    doi: null
    n: 30
    population: "resistance-trained adults, neutral grip"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Neutral (hammer) grip maintained throughout; no forearm supination. No absolute %MVIC values were reported."
    measurements: []

joint_rom_required:
  elbow_flexion_deg: 140
  shoulder_flexion_deg: 0
  source: "jahizi_2023"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped gravity curve similar to supinated curl, but neutral grip distributes load differently across the three elbow flexors"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications: []

variations: []
progressions: []
alternatives: [dumbbell_bicep_curl, barbell_curl]

sources:
  - source_id: jahizi_2023
    title: "Electromyographic comparison of biceps curl grip orientations"
    author: "Jahizi, Peyman et al."
    year: 2023
    doi: null
    credibility: rct
---

# Hammer Curls

The hammer curl uses a neutral grip (thumbs up) throughout the entire range of motion, mechanically eliminating the supination function of the biceps brachii. This grip redistributes elbow flexor demand: the brachialis and brachioradialis become primary movers, while biceps brachii contributes as a secondary flexor without its most efficient mechanical advantage. Hammer curls are the primary training stimulus for the brachialis — a muscle that sits under the biceps and contributes to upper arm size regardless of supination capability.

## Execution

1. Stand with dumbbells at the sides in a neutral grip (palms facing each other)
2. Keep the neutral grip throughout the entire movement — do not rotate into supination
3. Curl both dumbbells simultaneously or alternating to shoulder height
4. Lower under control; maintain the neutral wrist position through the eccentric

## The Neutral Grip Mechanics

The biceps brachii is a powerful forearm supinator. In a supinated grip (palms up), the biceps can exert both flexion and supination torque simultaneously, producing high activation. In a neutral grip:

- Supination is eliminated as a mechanical input
- Biceps brachii activation decreases significantly
- Brachialis activation increases (it has no supination function and flexes the elbow regardless of grip)
- Brachioradialis — which prefers a neutral grip — becomes more active

The practical result: hammer curls are a brachialis-first exercise, not a biceps-first exercise.

## Why Train the Brachialis

The brachialis sits deep to the biceps brachii and does not contribute to the "peak" shape of the biceps. However, a well-developed brachialis pushes the biceps upward, increasing overall upper arm circumference and visual height from the side. Including hammer curls ensures the brachialis — which is undertrained by all supinated curl variations — receives direct work.

## Data Note

Jahizi 2023 (n=30) confirmed the grip-specific activation shift but did not report absolute %MVIC values. The muscle priority assignments (brachialis/brachioradialis primary) are based on mechanical analysis of the neutral grip position supported by the study's qualitative findings.

> For system-specific training applications, see each system's lens entry.
