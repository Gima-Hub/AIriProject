# AIri / ai-projects Markdown Tree Guide (Human Guide)

## 0. このファイルの目的
このファイルは、Human（最終承認者）が **ai-projects** リポジトリ内の Markdown ファイルの配置、階層、および役割を迅速に把握するための**見取り図（補助ガイド）**です。

> [!IMPORTANT]
> **リポジトリ構造の正本（Source of Truth）は `2_PROJECT_MAP.md` です。**
> また、現在状態の正本は `3_CURRENT_STATUS.md` です。
> AI が構造や権威を確定するために参照するのはこれら正本であり、本ファイルはあくまで人間の理解を助けるための資料として位置づけられています。

---

## 1. まず見るべき正本一覧
情報の性質に応じて、参照すべき「正解（SoT）」を以下に整理します。

| 用途 | ファイル | 役割 | 備考 |
| :--- | :--- | :--- | :--- |
| **全体地図** | `2_PROJECT_MAP.md` | 構造地図・ドキュメント地図の正本 | どこに何があるかの正解 |
| **現在状態** | `3_CURRENT_STATUS.md` | 現在進行中の状態・フェーズの正本 | 今何をしているかの正解 |
| **実行タスク** | `recovery/ACTIVE_TASK.md` | 現在実行中のタスクへのアンカー | 実行中のタスク指示書へのリンク |
| **状態復旧** | `recovery/RUNTIME_STATE_PACKET.md` | ランタイム状態の復旧用パケット | セッション復旧時の状態 SoT |
| **報告形式** | `AIri_ROUTING_PROTOCOL.md` | 報告形式・Claim Boundary の正本 | AI 間の公式通信プロトコル |
| **現場道標** | `GEMINI.md` | Gemini CLI 用のサインポスト | 作業開始時にまず見るべきポインタ |
| **思考ルール** | `note-factory/tasks/ai-rules/GEMINI.md` | Gemini の思考・監査ルール | 補助的な行動規範 |
| **実装ルール** | `note-factory/tasks/ai-rules/GEMINI_WORKER.md` | 実装 Worker 用の具体的ルール | 実装作業時の制約 |

---

## 2. 階層別ツリー
リポジトリ内の主要な Markdown ファイルの階層構造です。

```text
<LOCAL_REPO_PATH>\
├─ 2_PROJECT_MAP.md             # [Structure Map] 全体構造地図の正本
├─ 3_CURRENT_STATUS.md          # [State SoT] 現在の進捗・フェーズの正本
├─ AIri_OPERATION_GUIDE.md      # [Guide] 運用の詳細ガイドライン
├─ AIri_ROUTING_PROTOCOL.md     # [Protocol SoT] 報告・通信形式の正本
├─ GEMINI.md                    # [Pointer] Gemini 用の現場サインポスト
├─ START_HERE.md                # [Entry] リポジトリ全体の総合入口
├─ Human\                       # Human 向け補助ナビゲーション（新設）
│  ├─ README.md                 # Human 向け総合入口
│  └─ AIri_MD_Tree_Guide.md     # 本ファイル
├─ governance\                  # AI の権律・自律動作の境界を定義
│  ├─ AUTHORITY_MATRIX.md       # 権限マトリクス
│  └─ GOVERNANCE_RULES.md       # ガバナンス基本ルール
├─ recovery\                    # セッション復旧・継続性のためのレイヤー
│  ├─ START.md                  # Recovery 専用のブートストラップ
│  ├─ ACTIVE_TASK.md            # [Task Anchor] 現在タスクへのアンカー
│  ├─ RUNTIME_STATE_PACKET.md   # [State Packet] ランタイム状態パケット
│  └─ CORE_BOOT_PACKET.md       # 起動用の最小構成パケット
└─ note-factory\                # AI 開発プロセス基盤（指示・タスク・報告・知見）
   ├─ tasks\                    # タスク管理
   │  ├─ active\                # 進行中タスクの指示書
   │  └─ ai-rules\              # AI 行動・思考ルールの正本
   ├─ outputs\                  # 作業完了報告（RESULT_*.md）
   ├─ ai-history\               # 対話・決定事項のログ
   ├─ ai-knowledge\             # 技術知見・再利用ルール・教訓
   ├─ briefs\                   # 指示書原本（やりたいこと）
   ├─ health\                   # 自律動作の観測・診断結果（未追跡）
   └─ external application project repository\         # アプリ開発プロジェクト（別枠）
```

---

## 3. repo直下 md の説明
リポジトリルートにある主要ファイルの説明です。

| Path | 種類 | 役割 | 正本 | 備考 |
| :--- | :--- | :--- | :--- | :--- |
| `START_HERE.md` | Entry | リポジトリの入口 | No | 新セッション開始時にまず読む |
| `2_PROJECT_MAP.md` | Structure Map | 全体構造・配置の定義 | **Yes** | 構造に関する唯一の正解 |
| `3_CURRENT_STATUS.md` | State SoT | 最新の進捗・フェーズ | **Yes** | 進行状況に関する唯一の正解 |
| `GEMINI.md` | Signpost | Gemini への現場指示 | No | 他の重要ファイルへのリンクを保持 |
| `AIri_ROUTING_PROTOCOL.md` | Protocol | 報告形式・通信規範 | **Yes** | AI 間の公式なやり取りのルール |
| `AIri_OPERATION_GUIDE.md` | Guide | 詳細な運用手順 | No | セッション復旧等の具体的な手順 |

---

## 4. recovery 配下 md の説明
セッション消失時でも作業の「継続性」を担保するためのファイル群です。

*   **`recovery/START.md`**: Recovery 専用の入口。GitHub Raw 参照を前提としたブートストラップ。
*   **`recovery/ACTIVE_TASK.md`**: **[Task Anchor]** 現在アクティブなタスクへのポインタ。`airi-cli` が自動更新する。
*   **`recovery/RUNTIME_STATE_PACKET.md`**: **[State Packet]** セッション消失時の動的な状態（State）を復元するための正本。
*   **`recovery/CORE_BOOT_PACKET.md`**: Core 再開時に必要な最小限の情報パケット。
*   **`recovery/CONTINUITY_RECOVERY_FLOW.md`**: 作業の継続性をいかにして取り戻すかのフロー説明。
*   **`recovery/CORE5_RECOVERY_TEST.md`**: 復旧プロセスが正常に機能するかの検証用ドキュメント。

---

## 5. governance 配下 md の説明
AI の自律動作における「安全境界」と「権限」を定義します。

*   **用途**: Governance Policy / Authority Boundary / Mutation Policy
*   **主要ファイル**:
    *   `governance/AUTHORITY_MATRIX.md`: 誰が（ChatGPT/Gemini/Human）何をできるかの定義。
    *   `governance/MUTATION_POLICY.md`: ファイルの変更・破壊的な操作の許可ルール。
    *   `governance/GOVERNANCE_RULES.md`: ガバナンス層の基本理念。

---

## 6. note-factory 配下 md の説明
AI 共同開発ライフサイクルを管理するフォルダ群です。

### 6.1 note-factory/tasks/ (タスク)
*   **`active/`**: 進行中タスクの指示書。
    *   `TASK_20260523_IMPLEMENT_RUNTIME_GOVERNANCE_LAYER.md`: 現在進行中（未追跡）のガバナンス層実装タスク。
*   **`ai-rules/`**: AI 行動規範。
    *   **`GEMINI.md`**: 内部思考・監査ルールの正本。
    *   **`GEMINI_WORKER.md`**: 実装作業に特化した具体的ルールの正本。
    *   **`MEMORY.md`**: プロジェクト固有の知識・教訓のインデックス。

### 6.2 note-factory/outputs/ (成果報告)
*   作業完了後の `RESULT_*.md` を格納。`AIri_ROUTING_PROTOCOL.md` に従った形式で作成される。

### 6.3 note-factory/ai-history/ & ai-knowledge/
*   **`ai-history/`**: 過去の会話の要約や決定事項のログ。
*   **`ai-knowledge/`**: 再利用可能なノウハウ、技術仕様、プロジェクト固有の用語集。

### 6.4 note-factory/health/ (観測)
*   **`latest_health_report.md`**: システムの自律診断結果。現在は未追跡（Untracked）。

---

## 7. Application Projects
AIri フレームワークを利用して開発されている、本線とは別枠のアプリケーション群です。

*   **`external application project repository/[APP_NAME_REDACTED]/`**
    *   **役割**: 仮想通貨取引履歴解析・損益計算 GUI ツール。
    *   **関係**: AIri の管理対象プロジェクト。
*   **`external application project repository/[APP_NAME_REDACTED]/`**
    *   **役割**: OCR を用いた報酬自動抽出ツール。
    *   **関係**: AIri の管理対象プロジェクト。

---

## 8. Legacy / Needs Review
整理・確認が必要、または古い可能性がある項目です。

| Path | 状態 | 理由 | 次に確認すべきこと |
| :--- | :--- | :--- | :--- |
| `STRUCTURE.md` | Legacy | `2_PROJECT_MAP.md` と重複。内容が古い | 更新後の地図で包含されているか確認 |
| `READ_ORDER.md` | Needs Review | `START_HERE.md` と役割が重複 | `START_HERE.md` への統合検討 |
| `note-factory/health/` | Untracked | 運用方針・Git 管理方針が未確定 | コミット対象にするか検討 |
| `note-factory/tasks/active/...` | Untracked | 進行中タスクの管理方法が過渡期 | 正式な Task SoT としての追跡検討 |

---

## 9. 見る順番の目安

### ■ AIriの現在地を知りたい時
1. `START_HERE.md` (入口の確認)
2. `3_CURRENT_STATUS.md` (現在のフェーズ・注力ポイント)
3. `recovery/ACTIVE_TASK.md` (現在実行中の具体的タスクへのリンク)

### ■ リポジトリの構造を知りたい時
1. `2_PROJECT_MAP.md` (ドキュメント配置と権威の把握)

### ■ Gemini (AI) に作業を依頼・継続させる時
1. `GEMINI.md` (現場サインポストの確認)
2. `note-factory/tasks/ai-rules/GEMINI.md` (思考ルールの同期)
3. `note-factory/tasks/ai-rules/GEMINI_WORKER.md` (作業制約の確認)
4. `AIri_ROUTING_PROTOCOL.md` (報告形式の再確認)

### ■ Runtime / Recovery 層の状況を見る時
1. `recovery/START.md` (復旧フローの入口)
2. `recovery/RUNTIME_STATE_PACKET.md` (保存されている状態の確認)
3. `recovery/ACTIVE_TASK.md` (中断されたタスクの特定)

---

## 10. 今後増える可能性があるmd候補
*   `RUNTIME_OBSERVATION_LOG.md`: 自律動作の継続的な観測ログ。
*   `RUNTIME_VALIDATION_REPORT.md`: ガバナンス層の正常動作検証報告。
*   `DAEMON_WATCHER_PLAN.md`: 常駐型監視（Watcher）の実装計画。
*   `RUNTIME_OPERATION_RUNBOOK.md`: 運用・トラブルシューティングの手順書。
*   `INCIDENT_LOG.md`: 異常検知・自動修復の履歴。
*   **`DOCUMENT_MAP.md`**: 将来的に地図が肥大化した場合の分離候補（現在は新設しない）。

---

## 11. 最後に
*   このファイルは **Human 向けの補助ガイド**であり、正本（Source of Truth）ではありません。
*   正式な構造地図は常に **`2_PROJECT_MAP.md`** です。
*   リポジトリに新しいドキュメント層が追加された場合、本ガイドも適宜更新してください。
