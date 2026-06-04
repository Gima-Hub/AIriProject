# AIriProject

AIriProject is a safe, experimental AI-assisted development runtime designed to bridge the gap between human designers (Architects) and AI executors (Workers). It provides a governed environment for autonomous or semi-autonomous software engineering tasks.

## Overview

AIriProject (pronounced "Airi") is not just a collection of scripts; it is a **runtime framework** that prioritizes:

*   **Safety & Governance:** Multi-layered policies that define what an AI can and cannot do.
*   **Operational Continuity:** Robust session recovery mechanisms that allow AI workers to resume tasks seamlessly after session resets.
*   **Structural Integrity:** Automated health checks and environment diagnostics.
*   **Clear Communication:** A strictly defined routing protocol (Claim Boundary) that separates facts from inferences.

## Core Components

- **`src/airi/`**: The core Python logic, including the daemon, doctor (self-healing), and state management.
- **`governance/`**: Definitive policies for authority, mutation, and escalation.
- **`recovery/`**: Primitives for session restoration and operational persistence.
- **`Human/`**: Navigation guides and instructions for human coordinators.

## Quick Start (Experimental)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Gima-Hub/AIriProject.git
    cd AIriProject
    ```
2.  **Environment Setup:**
    (Instructions for setting up the Python environment will be added soon)
3.  **Bootstrap AI CLI:**
    Point your AI CLI (e.g., Gemini CLI) to the `GEMINI.md` file in the root directory to begin operations.

## Safety Model

AIri operates on a **Trust but Verify** model. 
- **Architect (e.g., ChatGPT):** Handles high-level design and decision-making.
- **Worker (e.g., Gemini CLI):** Executes file modifications and local operations.
- **Human Coordinator:** The final authority who reviews and approves critical actions.

## Status

This project is currently in its **Initial Public Release (Alpha)**. 
- Core framework logic is included.
- Private application projects and personal data are strictly excluded from this repository.
- Deep implementation of the real-time daemon/watcher is currently deferred as we focus on stabilizing the safe development workflow.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Copyright (c) 2026 Gima-Hub
