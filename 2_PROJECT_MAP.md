# 2_PROJECT_MAP.md (AIri Repository Structure Map)

## 1. Purpose
本ドキュメントは、ai-projects / AIri リポジトリ全体の構造、ドキュメントの配置、および情報の権威（Authority）を定義する**構造地図の正本**である。

*   **Structure Map / Document Map Authority**: 本ファイルはリポジトリの構造定義における正解（SoT）である。
*   **状態・タスクの非保持**: 本ファイルは「現在状態（State）」や「具体的なタスク」の詳細は保持しない。それらは `3_CURRENT_STATUS.md` や `recovery/ACTIVE_TASK.md` を参照すること。
*   **ドキュメント地図の集約**: 現時点では `DOCUMENT_MAP.md` は新設せず、本ファイルがその役割を兼ねる。将来的に肥大化した場合のみ分離を検討する。

## 2. Core Navigation
リポジトリへのアクセスおよび復旧は、以下のポインタを起点とする。

*   **`START_HERE.md`**: AIri リポジトリの総合入口。
*   **`recovery/START.md`**: Recovery 層専用の入口（新セッション復旧用）。
*   **`2_PROJECT_MAP.md`**: 【本ファイル】リポジトリの全体地図・構造定義。
*   **`GEMINI.md`**: リポジトリ直下の Gemini CLI 用サインポスト（現場ポインタ）。

## 3. Authority Separation
情報の性質に応じて、以下の正本（SoT）を適切に参照・更新すること。

*   **リポジトリ構造 / ドキュメント地図**: `2_PROJECT_MAP.md` (Structure Map)
*   **現在状態 / 進捗状況**: `3_CURRENT_STATUS.md` (State SoT)
*   **現在実行中のタスクアンカー**: `recovery/ACTIVE_TASK.md` (Task Anchor)
*   **ランタイム状態の復旧**: `recovery/RUNTIME_STATE_PACKET.md` (Runtime State Packet)
*   **報告形式 / Claim Boundary**: `AIri_ROUTING_PROTOCOL.md` (Protocol SoT)
*   **Gemini 思考・監査ルール**: `note-factory/tasks/ai-rules/GEMINI.md` (Rule)
*   **Gemini 実装 Worker ルール**: `note-factory/tasks/ai-rules/GEMINI_WORKER.md` (Rule)

## 4. Document Classification Table

| Path | Layer | Role | Authority Type | Current Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `START_HERE.md` | Entry | Portal | Entry Point | Active | AIri 総合入口 |
| `2_PROJECT_MAP.md` | Core | Map | Structure Map | Active | 構造地図の正本 |
| `3_CURRENT_STATUS.md` | Core | Progress SoT | State SoT | Active | 現在状態の正本 |
| `GEMINI.md` | Core | Pointer | Signpost / Pointer | Active | Gemini 用現場ポインタ |
| `AIri_ROUTING_PROTOCOL.md` | Rules | Protocol | Protocol SoT | Active | 報告形式の正本 |
| `AIri_OPERATION_GUIDE.md` | Core | Guide | Guide / Overview | Active | 運用ルールの詳細 |
| `READ_ORDER.md` | Entry | Helper | Guide / Overview | **Needs Review** | 読込順補助。START_HEREと重複の可能性 |
| `ROADMAP.md` | Core | Vision | Guide / Overview | Active | 長期目標 |
| `STRUCTURE.md` | Core | Map | Legacy / Needs Review | **Legacy** | 更新後役割再確認 |
| `recovery/START.md` | Recovery | Boot | Entry Point | Active | Recovery専用入口 |
| `recovery/ACTIVE_TASK.md` | Recovery | Task Anchor | Task Anchor | Active | 現在タスクへのアンカー |
| `recovery/RUNTIME_STATE_PACKET.md` | Recovery | State Packet | Runtime State Packet | Active | runtime状態復旧用正本 |
| `recovery/CORE_BOOT_PACKET.md` | Recovery | Boot Packet | Runtime State Packet | Active | Core起動用最小パケット |
| `recovery/CONTINUITY_RECOVERY_FLOW.md` | Recovery | Flow | Guide / Overview | Active | 継続性復旧手順 |
| `recovery/CORE5_RECOVERY_TEST.md` | Recovery | Test | Guide / Overview | Active | Core5 復旧テスト系 |
| `governance/` | Governance | Policy | Policy | Active | 権限・修復境界の定義 |
| `note-factory/tasks/ai-rules/GEMINI.md` | Rules | Thinking Rule | Rule | Active | 補助的な思考・監査ルール |
| `note-factory/tasks/ai-rules/GEMINI_WORKER.md` | Rules | Worker Rule | Rule | Active | 実装Worker用ルール |
| `note-factory/tasks/ai-rules/MEMORY.md` | Rules | Knowledge | Rule | Active | 固有知識・教訓インデックス |
| `note-factory/tasks/active/` | Tasks | Task Path | Task | Active | 進行中タスクの配置場所 |
| `note-factory/tasks/active/TASK_20260523_IMPLEMENT_RUNTIME_GOVERNANCE_LAYER.md` | Tasks | Task | Task / Needs Review | **Untracked** | 追跡/統合判断待ち |
| `note-factory/health/` | Health | Observation | Health / Log | **Needs Review** | 未追跡。運用・Git管理方針検討中 |
| `note-factory/outputs/` | Outputs | Result | Health / Log | Active | 実行結果・作業報告書 |
| `note-factory/ai-history/` | History | Log | Health / Log | Active | 対話・決定の経緯 |
| `note-factory/ai-knowledge/` | Knowledge | Know-how | Knowledge / Reference | Active | 技術知見・再利用ノウハウ |
| `note-factory/briefs/` | Inputs | Instruction | Task | Active | 指示書原本 |
| `note-factory/tasks/` | Tasks | Management | Task | Active | タスク管理全般 |
| `external application project repository/` | Application | Project Root | Application Project | Active | 外部/アプリプロジェクト群 |
| `Human/` | Human | Human Support | Guide / Overview | Active | Human 向け補助資料置き場。正本ではない |
| `Human/README.md` | Human | Portal | Entry Point | Active | Human 向け総合入口・ナビゲーション |
| `Human/AIri_MD_Tree_Guide.md` | Human | Tree Guide | Guide / Overview | Active | ドキュメント階層・役割の見取り図 |

## 5. Layer Details

### 5.1 Recovery Layer (`recovery/`)
セッション消失時でも作業の「継続性」を担保するためのレイヤー。
`airi-cli` や `recovery/START.md` を通じて、最新の状態（State）とアクティブなタスクへ最短で到達することを目的とする。

### 5.2 Runtime / Governance Layer (`governance/`)
AI の自律動作における「安全境界」と「権限」を定義する。
自動修復（Self-healing）やファイル変更（Mutation）の許可範囲を、リスクレベル（Risk Level）に応じて制御するポリシーを格納。

### 5.3 AI Rules / Protocols
AI (Gemini) が作業時に遵守すべき行動規範と、AI 間の通信形式。
*   **`AIri_ROUTING_PROTOCOL.md`**: 成果物報告の「Claim Boundary」を定義し、事実と推論を厳格に区別する。
*   **`note-factory/tasks/ai-rules/`**: Gemini の内部思考および実装作業の具体的な制約。

### 5.4 note-factory (`note-factory/`)
AI 共同開発プロセスの全ライフサイクルを管理する基盤。
指示（Briefs）→ 分解（Tasks）→ 実行（Worker）→ 報告（Outputs）→ 蓄積（Knowledge/History）のフローを支える。

### 5.5 Application Projects (`external application project repository/`)
AIri フレームワークを利用して開発される、具体的なアプリケーション群。
現在の AIri Runtime / Governance 本線の開発からは論理的に分離されており、独立した SoT を持つ。
*   **`external application project repository/[APP_NAME_REDACTED]/`**: 仮想通貨取引履歴解析 GUI ツール。
*   **`external application project repository/[APP_NAME_REDACTED]/`**: 動画・画像からの報酬自動抽出ツール。

### 5.6 Human Layer (`Human/`)
Human（最終承認者）向けの補助資料置き場。
リポジトリの構造や運用ルールを人間が素早く思い出すためのガイドを格納する。
*   **注意**: 本フォルダ内のファイルは「SoT（正本）」ではなく、人間向けの補助ガイドである。

## 6. Legacy / Needs Review
以下のファイル・フォルダは、整理・アーカイブ・または運用方針の確定が必要な項目である。

*   **`STRUCTURE.md`**: 【Legacy / Needs Review】古い構造地図の可能性がある。本ファイルの更新定着後に役割を再確認する。
*   **`READ_ORDER.md`**: 【Guide / Overview】読込順の補助だが、`START_HERE.md` 等と内容が重複する可能性がある。
*   **`note-factory/health/`**: 【Health / Log / Needs Review】診断出力エリア。コミット対象とするか `.gitignore` で除外するかを検討中。
*   **`note-factory/tasks/active/TASK_20260523_IMPLEMENT_RUNTIME_GOVERNANCE_LAYER.md`**: 【Task / Needs Review】未追跡の進行中タスク。

## 7. Planned / Candidate Documents
将来的に追加・分離が検討されているドキュメント候補。

*   **`RUNTIME_OBSERVATION_LOG.md`**: 自律動作の観測記録。
*   **`RUNTIME_VALIDATION_REPORT.md`**: ガバナンス層の検証結果。
*   **`DAEMON_WATCHER_PLAN.md`**: ランタイム監視（Watcher）の設計。
*   **`RUNTIME_OPERATION_RUNBOOK.md`**: 運用手順書。
*   **`INCIDENT_LOG.md`**: 異常・修復・判断停止の履歴。
*   **`DOCUMENT_MAP.md`**: 本ファイルが肥大化した場合の分離候補（現時点では新設しない）。

## 8. AI Roles & Responsibilities
セッション復旧時でも役割を即座に復元できるよう、以下の責務を遵守する。

*   **Human (最終承認者)**: 最終的な意思決定および承認。
*   **Core5 / ChatGPT (Architect / Reviewer)**: 設計、タスク分解、実装コードのレビュー、状態(SoT)の確定。
*   **Gemini CLI (Worker / Executor)**: タスクに基づく実装、環境操作、事実ベースの報告。

## 9. Maintenance Rule
*   主要な md ファイルの新規作成・移動・廃止を行った場合、必ず本ファイルの更新要否を確認すること。
*   本ファイルは「構造地図」であり、動的な現在状態（`3_CURRENT_STATUS.md`）やタスク詳細は書き込みすぎないこと。

---
以上が、AIri リポジトリにおける正本構造地図である。構造や参照先に迷った場合は本内容を確認し、作業内容に応じた適切な情報源（Authority）を参照すること。
