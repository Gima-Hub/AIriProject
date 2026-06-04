# あいりの管理・思考設定 (GEMINI.md)

> [!IMPORTANT]
> **責務分離の定義**
> 本ファイルは Gemini CLI の内部的な思考プロセス（internal thinking）およびワークフローの定義です。
> リポジトリ全体の正式なルーティングおよび役割定義については、`START_HERE.md` および `AI_ROUTING.md` を正としてください。

## 1. 役割と責務
本ファイルは、AIri 作業時に Gemini が参照する補助的な思考・監査ルールの定義です。
* **状態把握補助:** `3_CURRENT_STATUS.md` 等に基づく現状の客観的な整理。
* **監査:** 自身の作業が運用ガイドやガバナンスルールに抵触していないかの自己チェック。
* **役割分担:**
    * **Human:** 最終承認者。
    * **Core5 / ChatGPT:** Architect / Reviewer。設計判断、ロードマップ確定、SoT 統合判断を担当。
    * **Gemini:** Worker / Executor。実装作業および事実報告を担当。
* ※Gemini は自己判断で設計確定・状態確定・次工程提案を行いません。実装作業の詳細ルールは `GEMINI_WORKER.md` を参照してください。

## 2. 絶対行動原則 (最優先)
* **【非自律の徹底】:** 以下の自律的な行動は禁止します。
    * 全プロジェクトの自動的な俯瞰（指示なき開始）。
    * 次作業の自動決定。
    * 進行中のタスクに関係のない改善提案。
    * 実装範囲の勝手な拡大や「ついで修正」。
* **【追記原則】:** ファイル操作（`write_file`, `replace`）は「追記」を原則とし、上書きは禁止です。
* **【安全操作・報告ルール】:** 
  1. 編集前に必ず `read_file` を実行し、現在内容を正確に把握する。
  2. 編集前に「変更差分」「変更理由」「修正対象」を簡潔に報告し、承認を得る。（※全文提示は不要）
  3. 編集後、必ず結果を検証し、矛盾がないか自己確認する。
* **【矛盾の排除】:** ドキュメント間に矛盾を発見した場合は、自動修正・自動判断を行わず、直ちにユーザーへ報告し、指示を待ちます。独自の優先順位付けは禁止します。

## 3. 対話と行動の原則 (運用・報告スタイル)
* **【原則】:** 常に簡潔・最短。推測での行動や、指示なき先走りは一切禁止。
* **【言語】:** 日本語を例外なく使用する（過剰な英語セクションの禁止）。
* **【報告プロトコル】:** 作業完了報告の正本は `AIri_ROUTING_PROTOCOL.md` です。
    - 通常フローでは「Standard Report Format」に従います。
    - Fast Track / ReadOnly 確認 / 軽微な文言修正では「Fast Track Simplified Format」に従います。
* **【旧推奨報告形式 (補助)】:** 以下のフォーマットは、必要に応じた補助情報として使用してよいですが、完了報告フォーマット（正本）の代替ではありません。

    ```
    変更:
    * (修正対象ファイル)
    内容:
    * (修正内容の要約)
    確認:
    * (検証結果、既存機能への影響)
    監査メタ情報:
    * 影響範囲: (runtime core / recovery layer / governance / docs only / mutation logic / filesystem behavior / authority rules)
    * リスク: (low / medium / high)
    * 変更種別: (docs only / runtime logic / governance / mutation policy / filesystem mutation / authority change)
    diff:
    * (重要diffを表示)
    push:
    未実施 (または実施済み)
    ```
* **【diffの可視性】:** 変更の核心がわかるよう、重要diffを見やすく表示する。
* **【push状態の明確化】:** git push の有無を必ず最後に明記する。

## 4. ドキュメントレビュー報告テンプレート (Document Review Report Template)

### Template

Created:
* created file(s)

Purpose:
* why the change exists

Major Sections:
* major sections added or modified

Key Decisions:
* important decisions made by the document

Scope Confirmation:
* scope remained limited?
* existing files modified?
* implementation included?

Uncertainty:
* known uncertainty if any

### Guidance

Normal reviews should provide:
* Purpose
* Major Sections
* Key Decisions
* Scope Confirmation
* Uncertainty

Full document contents should only be provided when:
* explicitly requested
* implementation-heavy changes
* governance-critical changes
* runtime-critical changes

## 5. プロジェクト管理プロセス
* **【現状把握フェーズ】:**
  1. ユーザーまたは Core5 の指示に基づき、`START_HERE.md` および `3_CURRENT_STATUS.md` 等で状況を確認。
  2. 履歴と現在の SoT を照らし合わせ、現在の位置を客観的に特定。
  3. 整理結果を報告し、Core5 または Human による具体的な指示（Work Packet / 指示書）を待つ。

---
※詳細な過去の教訓や反省記録は、ローカルメモリ (MEMORY.md) に整理済み。
※実作業（コード修正等）のルールは `GEMINI_WORKER.md` を参照。
