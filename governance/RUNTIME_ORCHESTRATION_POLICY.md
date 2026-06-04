# AIri Runtime Orchestration Policy

Version: 1.0.0
Date: 2026-05-23

## 1. Overview
This policy defines the coordination and orchestration protocols for all components within the AIri Runtime (e.g., doctor, repair, health, daemon). It ensures that semi-autonomous interactions remain bounded, predictable, and fully governed by policy.

## 2. Component Orchestration Protocols

### 2.1 Coordination Chains
*   **Doctor to Repair**: The `doctor` provides diagnosis, which the `governance layer` validates before authorizing the `repair` component to act.
*   **Health to Safe Mode**: If `health` reports a critical integrity loss, it must bypass standard repair channels and trigger an immediate `Safe Mode` escalation.
*   **Daemon to Watcher**: Daemons manage watcher lifecycle, ensuring watchers are only scoped to authorized subsystems.

### 2.2 Component Isolation
Components must operate as isolated services. No component is permitted to access the internal memory or state of another component without a defined API or governance-approved channel.

## 3. Orchestration Safety and Anti-Collision

### 3.1 Orchestration Priority
If multiple components trigger orchestration requests simultaneously, the `governance layer` applies the following priority:
1.  Safe Mode / Health Critical Escalations.
2.  Human-Authorized Repairs.
3.  Autonomous Maintenance (Daemons).
4.  Standard Telemetry/Observation.

### 3.2 Collision Handling
If orchestration requests conflict (e.g., conflicting repair targets), the `governance layer` must freeze all conflicting actions, log the collision, and escalate to a Human Coordinator.

### 3.3 Orchestration Timeout and Rollback
All orchestrated actions must have a strict timeout. If an action fails to complete or reach a stable state within the window, the system must trigger a rollback or move to `Safe Mode`.

## 4. Governance Enforcement

### 4.1 Bounded Execution
Orchestration is strictly bounded. Components cannot extend their interaction chains beyond pre-defined authorization flows.

### 4.2 Governance-First Validation
No component shall initiate an interaction or coordination request with another component without explicit authorization from the `governance layer` (pre-check of `AUTHORITY_MATRIX.md` and `GOVERNANCE_RULES.md`).
