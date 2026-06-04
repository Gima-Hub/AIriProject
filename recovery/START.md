# AIri Recovery Start

## 1. Context
- BRANCH: `ai-edit`
- LAST_UPDATE: `2026-05-23`
- RECOVERY_V: `2.0`

## 2. Core Retrieval Pointers (Raw URLs)
- STATUS: https://raw.githubusercontent.com/Gima-Hub/AIriProject/refs/heads/main/3_CURRENT_STATUS.md
- ACTIVE_TASK_INDEX: https://raw.githubusercontent.com/Gima-Hub/AIriProject/refs/heads/main/recovery/ACTIVE_TASK.md
- ROUTING: https://raw.githubusercontent.com/Gima-Hub/AIriProject/refs/heads/main/AI_ROUTING.md
- OPS_GUIDE: https://raw.githubusercontent.com/Gima-Hub/AIriProject/refs/heads/main/AIri_OPERATION_GUIDE.md

## 3. Recovery Flow (Multi-Stage)
1. **Stage 1: Bootstrap**
   - Fetch `recovery/START.md` (This file).
   - Sync `3_CURRENT_STATUS.md` and `AI_ROUTING.md`.
2. **Stage 2: Task Resolution**
   - Fetch `recovery/ACTIVE_TASK.md` to get the current task URL.
   - Access the Task URL to load specific objectives.
3. **Stage 3: Execution**
   - Continue execution based on the loaded Task and Status.

## 4. Next Action
1. 上記 URL を順番に Fetch し、SoT を同期せよ。
2. `recovery/ACTIVE_TASK.md` から現在のタスク URL を取得し、詳細を確認せよ。
3. 同期完了後、タスクを継続せよ。
