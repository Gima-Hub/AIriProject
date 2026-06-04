# プロジェクト構造（external application project repository）

## ルート
ai-projects/
├── README.md
├── STRUCTURE.md
└── note-factory/

---

## note-factory 内

note-factory/
├── briefs/        # やりたいこと（指示）
├── tasks/         # 実行手順（AI用）
├── outputs/       # 成果物
└── external application project repository/

---

## external application project repository 内（メイン開発）

external application project repository/
├── [APP_NAME_REDACTED]/   # 仮想通貨計算アプリ
└── [APP_NAME_REDACTED]/      # STEPN税務自動化

---

## フロー（作業の流れ）

1. briefs にやりたいことを書く
2. tasks に分解（ChatGPTで作る）
3. AI（Gemini / Codex）で実装
4. outputs またはアプリに反映
5. Gitで保存

---

## Git運用ルール

■ 作業前（バックアップ）
git add .
git commit -m "backup"
git checkout -b ai-edit

■ 成功した場合
git add .
git commit -m "update"
git checkout main
git merge ai-edit
git push

■ 失敗した場合
git checkout main
git branch -D ai-edit

---

## ルール

・本番は main ブランチ
・AI作業は ai-edit ブランチ
・必ずバックアップしてから作業
・差分で修正させる