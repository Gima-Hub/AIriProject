# CORE5_RECOVERY_TEST

## 1. Test Objective
Core5 が巨大なリポジトリの全走査や人間によるアーキテクチャの再説明を受けることなく、最小限のリカバリ・プリミティブのみを用いて「運用の継続性（Operational Continuity）」を正しく復元できるかを検証する。

## 2. Test Input Boundary

### Recovery Input Files
運用の継続性を復元するために使用されるファイル：
- `recovery/CORE_BOOT_PACKET.md`
- `recovery/ACTIVE_TASK.md`
- `recovery/RUNTIME_STATE_PACKET.md`
- `recovery/CONTINUITY_RECOVERY_FLOW.md`

### Test Specification File
テストの評価方法を定義するファイル：
- `recovery/CORE5_RECOVERY_TEST.md` (本ファイル)

### Important Distinction
- **Recovery Input Files** は、運用継続性の再構築に使用される実体データです。
- **Test Specification File** は、リカバリ試行を評価するための「メタリカバリ・インフラ」であり、実行状態（Runtime State）の一部とはみなしません。
- テストスペック自体を継続状態としてカウントしてはいけません。

## 3. Forbidden Inputs (禁止事項)
- **Full repo traversal**: リポジトリ全体のファイルリスト取得や無差別な読込。
- **Human architecture re-explanation**: 人間による現在の設計方針や歴史的経緯の再説明。
- **Speculative reconstruction**: 根拠のない推測による状態の捏造。

## 4. Expected Reconstruction Output (期待される復元結果)
AI がリカバリ後に自律的に提示すべき項目：
- **Current phase**: 現在のフェーズの正確な認識。
- **Current objective**: 現在の目的の正確な把握。
- **Runtime continuity model**: リポジトリ中心ではなく実行状態中心の継続性モデルの理解。
- **Next minimal action**: 次に取るべき最小限の行動。
- **Uncertainty boundaries**: 何が不明であるか（不確実性の境界）の明確な特定。

## 5. Pass Criteria
- 最小入力ファイルのみから、現在のフェーズと目的を正確に特定できた場合。
- 巨大リポジトリの読込を要求せずに、次の具体的かつ最小限のアクションを提示できた場合。
- 不明点を「推測」で埋めず、正しく「不確実性」として報告できた場合。

## 6. Fail Criteria
- リポジトリの全走査や多数のファイル参照を要求した場合。
- 人間にアーキテクチャの解説や現状の説明を求めた場合。
- 既存のリカバリ・プリミティブと矛盾する状態を「捏造」した場合。

## 7. Review Checklist
- [ ] 入力は `recovery/` 以下の 4 ファイルに限定されているか。
- [ ] AI の回答は lightweight かつ recovery-oriented か。
- [ ] 次のアクションは implementation-neutral（実装に偏っていない）か。
