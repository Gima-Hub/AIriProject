# ARCHITECTURE

本repositoryは、
AIriとして設計されている。

目的：

* AI暴走防止
* session復旧性向上
* Human負担軽減
* review容易化
* rollback性向上
* docs中心運用

を実現すること。

---

# Core Philosophy

## docs = 状態源

AI短期記憶には依存しない。

repository docs を状態源とする。

---

## Role Separation

### Human

* 最終判断
* priority決定
* review
* merge判断

### ChatGPT

* architecture
* review
* workflow整理
* docs整理
* safety管理

### Gemini CLI

* 実装
* file operation
* Git operation
* local作業

---

# Structure Philosophy

repositoryでは：

* current
* history
* task
* workflow
* knowledge

を分離する。

目的：

* AI誤読防止
* session復旧性向上
* review容易化
* structure安定化

---

# Current Management

## Current状態

* 3_CURRENT_STATUS.md

## Short-term priority

* 05_CURRENT_PRIORITY.md

## History

* ai-history/

## Tasks

* tasks/

---

# Safety Philosophy

AIは：

* 最小変更原則
* rollback可能変更
* review可能変更
* structure保護

を優先する。

AIによる大規模自動最適化は禁止。

---

# Future Direction

将来的には：

* semi autonomous workflow
* AI routing
* review gate
* task queue
* automation pipeline

を導入予定。
