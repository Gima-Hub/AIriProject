# Contributing to AIriProject

Thank you for your interest in AIriProject! We are in the early stages of building a safe, governed runtime for human-AI collaboration.

## Experimental State
AIriProject is currently an **experimental, alpha-stage project**. Our focus is on stabilizing core safety and recovery primitives before expanding features.

## Where to Contribute
We prioritize contributions in the following areas:
1.  **Documentation:** Improving guides for human coordinators and AI workers.
2.  **Safety & Governance:** Refining policies and boundary checks in `governance/`.
3.  **Recovery Workflows:** Enhancing session restoration logic and robustness.
4.  **Security Audits:** Reviewing code for potential leaks or unsafe automation.

## Contribution Process
1.  **Discuss first:** For large implementations (e.g., real-time daemons, new mutation engines), please open an issue for discussion before starting work.
2.  **Claim Boundary Protocol:** All contributions (especially those made via AI CLI) must follow the `AIri_ROUTING_PROTOCOL.md`.
3.  **Pull Request Requirements:**
    - Clearly state the **Scope**, **Verification results**, and **Potential Risks**.
    - Do not include personal data, local absolute paths, or real app data.
    - Automated tests are highly encouraged.

## AI-Generated Content
If your contribution was generated or assisted by an AI (e.g., Gemini, ChatGPT, Claude), please **state this clearly** in your PR description. Human review and behavioral validation are mandatory for all AI-assisted changes.

## Data Safety
We enforce a strict policy against including:
- Real-world transaction data (CSV/Excel).
- Screenshots or media containing private information.
- Operational logs from private environments.
