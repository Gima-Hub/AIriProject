# AIri Runtime Authority Matrix

Version: 1.0.0
Date: 2026-05-23

## 1. Overview
This matrix defines the authority boundaries for AIri Runtime components and roles. It establishes the Trust Boundary to balance autonomy and safety.

## 2. Authority Matrix

| Role / Component | Read | Write | Diagnose | Repair | Mutate Runtime | Modify Governance | Git Commit | Git Push | Approve Escalation |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Human Coordinator** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **ChatGPT Architect** | ✅ | ⚠️¹ | ✅ | ⚠️² | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Gemini CLI Worker** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **doctor** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **repair** | ✅ | ⚠️⁴ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **health** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **daemon** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **safe mode** | ✅ | ❌ | ❌ | ❌ | ✅³ | ❌ | ❌ | ❌ | ❌ |
| **governance layer** | ✅ | ⚠️⁵ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |

### Notes:
1. **⚠️¹ ChatGPT Architect Write**: Indirectly through instructions to Gemini CLI Worker.
2. **⚠️² ChatGPT Architect Repair**: Strategic repair planning only; execution handled by repairer or Gemini.
3. **✅³ safe mode Mutate Runtime**: Limited to restriction, freezing, or degradation of system state/services.
4. **⚠️⁴ repair Write**: Scoped / bounded repair writes only; unrestricted write is prohibited.
5. **⚠️⁵ governance layer Write**: Policy-controlled governance writes only; unrestricted governance mutation is prohibited.

## 3. Component Design Principles

*   **doctor**: Diagnosis only. Identifies symptoms and potential root causes without making changes.
*   **health**: Observation and reporting only. Monitors system telemetry and status.
*   **repair**: Bounded repair only. Executes pre-approved repair actions within defined safety limits.
*   **daemon**: Monitor and trigger only. Observes states and initiates cycles or alerts.
*   **safe mode**: Restrict / Freeze / Degrade only. Transitions system to a known safe state when anomalies are detected.
*   **governance layer**: Authorize / Reject / Enforce only. Evaluates actions against policies and manages escalation.
*   **Gemini CLI**: Implementation worker only. Executes file modifications and local operations based on directives.
*   **ChatGPT**: Architect / Reviewer only. Provides high-level design, review, and strategic guidance.
*   **Human**: Final approval authority. Holds ultimate power for high-risk actions and configuration changes.

## 4. Constraint Rules

1.  **No Direct Git Push**: No automated component is permitted to perform `git push`.
2.  **Repair Boundary**: The `repair` component must not modify the `governance layer` or `safe mode` logic.
3.  **Diagnosis Isolation**: `doctor` must be read-only regarding the runtime core and application files.
4.  **Governance Independence**: Only the `governance layer` (and Human) can modify governance policies.
