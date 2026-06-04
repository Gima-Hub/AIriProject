# AIri Runtime Governance Rules

Version: 1.0.0
Date: 2026-05-23

## 1. Core Principles

The following principles govern all autonomous and semi-autonomous operations within the AIri Runtime. These rules take precedence over operational efficiency to ensure system safety and human control.

### 1.1 Governance Before Autonomy
Autonomy is granted only within the boundaries defined by the Governance Layer. No component shall execute any action that has not been pre-authorized or validated against current governance policies.

### 1.2 Least Privilege
Every component (doctor, repair, daemon, etc.) must operate with the minimum level of privilege required to perform its specific function, as defined in the `AUTHORITY_MATRIX.md`.

### 1.3 Safe Mode First
When an anomaly is detected or a governance boundary is approached, the system must prioritize transitioning to a `Safe Mode` (restricted, frozen, or degraded state) before attempting complex or high-risk repairs.

## 2. Prohibitions

### 2.1 No Self-Authority Escalation
No AI component or automated process is permitted to modify its own authority level, change its capability flags, or bypass the `governance layer`'s restriction logic.

### 2.2 No Silent Escalation
All escalations, whether to higher-risk levels or to Human Coordinators, must be explicitly logged and signaled. Hidden or silent bypasses of governance checks are strictly prohibited.

### 2.3 No Recursive Repair Loops
Autonomous repair processes must implement loop detection and "circuit breakers." If a repair action fails repeatedly or causes a state oscillation, the system must freeze the repair attempt and escalate to a Human Coordinator.

## 3. Boundary Rules

### 3.1 Bounded Mutation
Runtime mutations (code changes, configuration updates, state transitions) must be bounded by scope and risk level. Unrestricted mutation of the core architecture or the governance layer itself is prohibited for automated components.

### 3.2 Human Approval for Irreversible Actions
Any action classified as `HIGH` risk or deemed "irreversible" (e.g., permanent data deletion, significant architectural shifts, credential changes) requires explicit Human Coordinator approval before execution.

### 3.3 Recovery Continuity Preservation
No governance or repair action shall compromise the integrity of the `Recovery Layer`. The ability for a Human to recover the system manually must always be preserved.

## 4. Accountability and Auditing

### 4.1 Auditability
All actions performed by autonomous components, especially those involving `Write`, `Repair`, or `Mutate Runtime` capabilities, must be recorded in an immutable-style audit log (e.g., specific telemetry or status files).

### 4.2 Policy Enforcement
The `governance layer` is responsible for enforcing these rules. If a component attempts to violate these rules, the `governance layer` must reject the action and immediately trigger a high-priority alert or Safe Mode transition.
