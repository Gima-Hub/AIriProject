# AIri Runtime Mutation Policy

Version: 1.0.0
Date: 2026-05-23

## 1. Overview
This policy defines the permissible boundaries for runtime mutations (modifications to files, data, or system state) by autonomous components. It is designed to allow necessary self-healing while preventing runaway system changes.

## 2. Mutation Classification

### 2.1 Allowed Mutation (Autonomously Permitted)
These areas can be modified autonomously by authorized components (e.g., `repair`, `daemon`) without prior human approval, provided they adhere to defined safety limits.
*   **Logs**: System, component, and runtime logs.
*   **Cache**: Non-critical transient data storage.
*   **Generated Reports**: Temporary or finalized output reports.
*   **Temporary Runtime Artifacts**: Scratchpad files, temp sequences, or session-specific buffers.

### 2.2 Conditional Mutation (Approval or Context Required)
These modifications require contextual validation or explicit approval, often managed by the `governance layer` or `Human Coordinator`.
*   **recovery/ACTIVE_TASK.md**: Only permitted for legitimate task tracking and sync updates.
*   **3_CURRENT_STATUS.md**: Status updates reflecting genuine system state changes.
*   **Runtime State Files**: Must only reflect verified operational status.
*   **Health Reports**: Must be accurate and based on validated observations.
*   **Repair Reports**: Documentation of repair actions taken within bounds.

### 2.3 Forbidden Mutation (Strictly Prohibited)
Any attempt to modify these areas autonomously is a violation of the governance policy and must trigger a `Safe Mode` transition.
*   **Governance Documents**: Modifications to `AUTHORITY_MATRIX.md` or `GOVERNANCE_RULES.md` require Human Coordinator approval.
*   **Recovery Entrypoint Destructive Changes**: Any change compromising the ability to perform manual recovery.
*   **Routing Layer Destructive Changes**: Changes to core routing protocols.
*   **Recursive Self-Modification**: Any code attempting to modify its own logic or that of the core governance layer.
*   **Unrestricted Filesystem Mutation**: Any modification outside defined allowed/conditional scope.
*   **Branch Switching**: Automated branch changes without explicit instruction.
*   **Git Push**: Any automated git push operation.

## 3. Policy Enforcement
*   **Boundary Adherence**: Autonomous components must verify the target file and modification scope against this policy before applying any mutation.
*   **Governance Layer Validation**: The `governance layer` must act as the gatekeeper for all `Conditional` and `Forbidden` checks.
*   **Audit Requirement**: Every mutation to `Conditional` areas must be logged in the audit trail.
