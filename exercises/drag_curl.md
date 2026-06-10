---
id: drag_curl
name: Drag Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary

# No peer-reviewed EMG data found for the drag curl.
# The shoulder extension component and unique bar path are mechanically distinct from standard curls.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 120
  shoulder_extension_deg: 20
  source: "biomechanical inference"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Easiest at the top due to simultaneous shoulder extension reducing biceps effective length; resistance felt most at the start where shoulder is neutral and elbow begins extending"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
  common_injuries:
    - structure: biceps_tendon_long_head
      mechanism: repetitive_shoulder_extension
      risk_factors: [excessive_shoulder_extension_range, heavy_load, pre_existing_biceps_tendinopathy]
  contraindications:
    - acute_posterior_shoulder_impingement

variations: []
progressions: []
alternatives: [barbell_curl, dumbbell_bicep_curl]

sources: []
---

# Drag Curl

The drag curl is a barbell curl variation where the bar is kept in contact with the torso throughout the movement. Unlike a standard curl where the bar arcs forward away from the body, the drag curl pulls the bar directly upward while simultaneously pulling the elbows backward. This shoulder extension component fundamentally alters the movement pattern: as the elbows come back, the shoulder extends, which shortens the biceps from the proximal (shoulder) end while the elbow flexion shortens it from the distal end.

## Execution

1. Hold a barbell at the hips with a supinated grip
2. Keep the bar in contact with the torso throughout — do not allow it to swing forward
3. Initiate by pulling the elbows backward while curling the bar upward; the bar should drag up the torso
4. At the top, the elbows will be behind the torso and the bar near the upper abdomen/chest
5. Lower by reversing the path — elbows move forward while extending, bar returns to hips

## The Mechanical Rationale

In a standard curl, the shoulder stays fixed at 0° flexion while the elbow flexes. The biceps shortens only from the distal (elbow) end. In the drag curl:
- The elbows move backward (shoulder extends) while the elbow flexes
- The shoulder extension reduces the effective biceps moment arm at the proximal end
- This allows the elbow to flex to a higher degree without the "finishing" difficulty of a standard curl

The result is a strength curve that shifts load toward the shortened biceps position at the top — the opposite of the lengthened-position emphasis of preacher and incline curls.

## Data Note

No quantitative EMG data exists for the drag curl. The muscle priority assignments and strength curve characterization are based on mechanical analysis of the shoulder extension + elbow flexion coupling. The drag curl is most useful as a variation that provides peak-contraction emphasis for lifters who respond well to that stimulus type, rather than as a primary mass builder.

> For system-specific training applications, see each system's lens entry.
