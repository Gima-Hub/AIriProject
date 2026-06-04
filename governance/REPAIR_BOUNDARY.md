# AIri Runtime Repair Boundary

Version: 1.0.0
Date: 2026-05-23

## 1. Overview
This document defines the safety boundaries and operational constraints for all autonomous repair actions within the AIri Runtime. It prevents runaway repair behavior and ensures system stability through bounded and supervised self-healing.

## 2. Core Constraints

### 2.1 Repair is Bounded
All automated repair actions must be strictly bounded in scope, risk, and target. Unrestricted system mutation during repair is strictly prohibited.

### 2.2 Not Unrestricted Mutation
A repair action is not a general-purpose mutation. It must map directly to a known, verified corrective procedure for a specific, diagnosed symptom.

### 2.3 No Recursive Repair Loops
Repair components must detect and terminate recursive loops. If a repair action (or sequence) fails more than three times, it must be aborted, and the system must escalate to a Human Coordinator.

## 3. Safety and Escalation

### 3.1 Repair Uncertainty Handling
When repair uncertainty is high (e.g., ambiguous diagnosis, multiple potential causes), the repair component must abort and request Human Coordinator intervention or transition to `Safe Mode`.

### 3.2 Safe Mode Fallback
If any repair action triggers an anomaly or fails, the system must immediately trigger a `Safe Mode` fallback (system restriction or degradation) to preserve stability.

### 3.3 Repair Escalation Rules
* **Low Risk**: Automated repair permitted with logging.
* **Medium Risk**: Automated repair permitted if system is healthy; requires human notice if system is degraded.
* **High Risk**: Human Coordinator approval mandatory before repair.

## 4. Operational Principles

### 4.1 Human Approval Boundary
Actions that modify core components, permanent state, or governance files are strictly classified as `HIGH` risk and always require Human Coordinator approval.

### 4.2 Repair Scope Limitation
Repairs must be limited to the `Allowed` and `Conditional` mutation zones as defined in `MUTATION_POLICY.md`.

### 4.3 Recovery Continuity Preservation
No repair action shall ever delete, lock, or corrupt the `Recovery Layer` or any mechanism required for human-led system recovery.
