# CORE_BOOT_PACKET

## Primary Objective
セッション再開時に、巨大なリポジトリ全読込を行うことなく、最小限のコンテキストで現在の運用状態を復元する。

## Current Phase
Continuity Stabilization Phase

## Recovery Hierarchy
1. `recovery/CORE_BOOT_PACKET.md` (本ファイル: 起動方針)
2. `recovery/ACTIVE_TASK.md` (現在の意図・状態のアンカー)
3. `recovery/RUNTIME_STATE_PACKET.md` (詳細なランタイム状態)
4. (必要に応じて) `recovery/PATHS.txt` (選択的リポジトリ参照)

## Runtime Continuity Principle
- **Recovery-first Runtime OS**: 復旧を最優先事項とする。
- **Runtime-state-centric continuity**: リポジトリ構造ではなく、実行状態を中心に継続性を維持する。
- **Repo = source of truth / reference layer**: リポジトリは真実のソースであり、参照レイヤー。
- **Runtime state packet = continuity core**: 実行状態パケットが継続性の核。
- **ACTIVE_TASK = runtime intent/state anchor**: ACTIVE_TASK は現在の意図と状態を固定する。
- **Recovery accuracy > apparent completeness**: 見かけの網羅性よりも復旧の正確性を優先する。

## Role Separation
- 管理AI (AIri Orchestrator): 継続性とガバナンスの維持。
- 実行Worker: 具体的な実装タスクの遂行。

## Immediate Next Target
Core5 recovery test readiness (Core5 がこれらパケットのみで復旧できる状態にする)。

## Uncertainty Handling Rule
不確実な点は推測せず、`RUNTIME_STATE_PACKET.md` の `known_uncertainties` に記録し、ユーザーまたは管理フェーズで解決する。
