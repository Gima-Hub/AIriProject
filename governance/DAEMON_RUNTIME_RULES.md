# AIri Runtime Daemon Rules

Version: 1.0.0
Date: 2026-05-23

## 1. Overview
This document defines the operational boundaries and safety constraints for all daemon and watcher processes within the AIri Runtime. It ensures background automation remains bounded, predictable, and compliant with the governance framework.

## 2. Operational Boundaries

### 2.1 Daemon and Watcher Scope
*   **Daemon Scope**: Limited strictly to monitoring, telemetry collection, and pre-authorized maintenance tasks.
*   **Watcher Boundary**: Watchers must be scoped to specific file paths or system subsystems. Global, unrestricted monitoring is prohibited.

### 2.2 Resource Constraints
*   **Polling Intervals**: Automated polling must respect a defined "minimum interval" to prevent excessive system load.
*   **Resource Limits**: Daemon processes must not exceed defined CPU/Memory thresholds. If exceeded, the daemon must throttle itself or transition to `Safe Mode`.

## 3. Execution Safety

### 3.1 Bounded Trigger Execution
All actions initiated by a daemon/watcher must be pre-validated against the `EVENT_TRIGGER_POLICY.md` and confined within the `MUTATION_POLICY.md` boundaries.

### 3.2 Recursive Prevention
Daemons must implement "Parent-Child" verification to ensure they do not spawn redundant or circular monitoring processes.

### 3.3 Safe Shutdown
Daemons must support graceful, immediate shutdown upon a `Safe Mode` signal. They must leave the runtime in a consistent state before exit.

## 4. Governance Validation

### 4.1 Pre-Action Validation
Before performing any action (e.g., triggering a repair, modifying a state file), the daemon must query the `governance layer` for authorization.

### 4.2 Health Fallback
If a daemon detects its own failure or inconsistency in telemetry, it must immediately stop its operations and report to the `health` component, triggering a potential fallback to a redundant process or human intervention.

### 4.3 Escalation
Continuous daemon failures or persistent resource violations must escalate to a Human Coordinator via the standard alert mechanism.
