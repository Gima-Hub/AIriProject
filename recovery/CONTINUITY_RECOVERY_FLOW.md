# CONTINUITY_RECOVERY_FLOW (v1)

## Purpose
Core5以降のセッションが、巨大なリポジトリの全走査を行うことなく、安全かつ迅速に運用の継続性（Operational Continuity）を復元するための標準手順を定義する。

## Standard Recovery Flow
セッション開始直後、AIは以下の順序でコンテキストを読み込む。

1. **`recovery/CORE_BOOT_PACKET.md`**
   - 起動方針、リカバリ階層、および現在のフェーズの基本原則を確認する。
2. **`recovery/ACTIVE_TASK.md`**
   - 現在の意図（Intent）と具体的なタスクアンカーを確認し、活動地点を特定する。
3. **`recovery/RUNTIME_STATE_PACKET.md`**
   - 詳細なランタイム状態、実行の確信度、および既知の不確実性を把握する。
4. **`recovery/PATHS.txt` (Selective Lookup)**
   - 次のステップに必要なリポジトリ内の特定ファイルへのパスを取得する。
5. **Optional Repo Lookup**
   - 上記ステップで特定された「どうしても必要な参照」のみ、リポジトリから追加取得する。

## Rule of Engagement
- **Minimal Traversal**: 上記 1-4 の確認で十分な場合、リポジトリの全読込や無差別な走査を禁止する。
- **Recovery-first**: 既存のリポジトリ構造の理解よりも、現在の「実行状態」の復元を優先する。
- **Uncertainty Propagation**: 情報が不足している場合は、推測せず `RUNTIME_STATE_PACKET.md` に不確実性を記録し、復旧フェーズ内で解決を試みる。
