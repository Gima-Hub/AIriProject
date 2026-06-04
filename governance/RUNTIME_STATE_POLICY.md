# AIri Runtime State Policy

Version: 1.0.0
Date: 2026-05-23

## 1. Overview
This policy governs the persistence, synchronization, and restoration of the AIri Runtime state. It ensures system continuity, prevents state corruption, and guarantees that recovery processes are always based on a valid and consistent operational state.

## 2. Persistence and Synchronization Rules

### 2.1 State Persistence Rules
*   **Snapshot Frequency**: Critical runtime states must be snapshotted at significant task milestones.
*   **Atomic Writes**: State updates to persistence files must be atomic to prevent partial writes and corruption.
*   **Persistence Timing**: State persistence must occur post-validation of a completed operation, not mid-transition.

### 2.2 Recovery Synchronization
*   **ACTIVE_TASK Continuity**: The `recovery/ACTIVE_TASK.md` must be the "Source of Truth" for system progress. Any state persistence must be synchronized with the task tracker.
*   **Consistency Validation**: Before any recovery restoration, the system must validate the consistency of the state files against current operational environment expectations.

## 3. Integrity and Anti-Corruption

### 3.1 Stale State Prevention
*   **Timestamping**: All state snapshots must be timestamped.
*   **Validation**: Upon restoration, the system must verify the age of the state. If a state exceeds a defined "freshness threshold," it must be rejected, and a manual Human Coordinator check is required.

### 3.2 State Corruption Handling
*   **Detection**: Automated components must perform checksum verification of state files upon read/write.
*   **Isolation**: If corruption is detected, the affected state file must be quarantined (moved to a backup folder), and the system must revert to the last known good state or enter `Safe Mode`.

## 4. Restoration Policy

### 4.1 Safe Recovery Restoration
Restoration must be incremental and validated. The system must verify the state's validity after loading each subsystem before proceeding to full runtime activation.

### 4.2 Governance-First Restoration
If the system detects a mismatch between persisted state and the current `AUTHORITY_MATRIX.md` or `GOVERNANCE_RULES.md`, the state restoration must be halted, and the `governance layer` must reconcile the deviation before continuing.
