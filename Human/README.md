# Human/ README (AIri Human Index)

## 0. はじめに
このフォルダは、Human（最終承認者）が数ヶ月ぶりに戻ってきた際や、リポジトリの全貌を素早く把握したい時のための**補助ガイド置き場**です。

> [!CAUTION]
> **本フォルダは「正本（Source of Truth）」ではありません。**
> リポジトリの正確な構造は `2_PROJECT_MAP.md` を、最新の進捗状態は `3_CURRENT_STATUS.md` を常に優先してください。

---

## 1. 用途別・まず見る場所

### ■ 今どこまで進んでいるか知りたい
*   **`3_CURRENT_STATUS.md`**: 現在のフェーズ、進捗、注力ポイントの正本。
*   **`recovery/RUNTIME_STATE_PACKET.md`**: 直前のセッション終了時の動的状態。
*   **`recovery/ACTIVE_TASK.md`**: 現在実行中の具体的タスクへのアンカー。

### ■ リポジトリの構造や各 md の役割を知りたい
*   **`2_PROJECT_MAP.md`**: 構造地図・ドキュメント配置の正解。
*   **`Human/AIri_MD_Tree_Guide.md`**: 全階層の md ファイルの見取り図（補助ガイド）。

### ■ Gemini (AI) に作業を依頼したい
*   **`GEMINI.md`**: リポジトリ直下の Gemini 用サインポスト。
*   **`note-factory/tasks/ai-rules/GEMINI.md`**: 内部思考・監査ルール。
*   **`note-factory/tasks/ai-rules/GEMINI_WORKER.md`**: 実装 Worker 用具体的ルール。
*   **`AIri_ROUTING_PROTOCOL.md`**: 成果物報告形式と Claim Boundary の正本。

### ■ 操作・運用方法を思い出したい
*   **`AIri_OPERATION_GUIDE.md`**: セッションライフサイクルや復旧の詳細手順。
*   **`QUICK_START.md`**: 最短で作業を再開するための手順。
*   **`READ_ORDER.md`**: 文脈構築のための推奨読込順。

### ■ 思想・用語・長期目標を確認したい
*   **`note-factory/AIri_SYSTEM_OVERVIEW.md`**: AIri の思想と 5 分でわかる全体像。
*   **`REPOSITORY_GLOSSARY.md`**: AIri 固有の用語定義。
*   **`ROADMAP.md`**: フェーズごとの中長期開発目標。

---

## 2. 人間が守るべき原則
1. **Human/ を SoT にしない**: 状態の確定は必ず `3_CURRENT_STATUS.md` で行ってください。
2. **矛盾時は正本優先**: 本ガイドの内容とルート直下の正本（SoT）が矛盾する場合、常に正本を優先してください。
3. **未追跡ファイルの保護**: `note-factory/health/` 等、未追跡のファイルは Core5 の判断なしに勝手に `git add` しないでください。

---
※本ドキュメントは Human の利便性のために作成されています。
