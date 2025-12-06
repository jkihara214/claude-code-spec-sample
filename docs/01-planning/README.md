# 01-planning - 企画・要件定義

プロジェクトのビジネス要件とシステム要件を明確に記述します。
「何を作るか」「なぜ作るか」を定義するフェーズです。

## 目次

- [ディレクトリ構成](#ディレクトリ構成)
- [各ファイルの説明](#各ファイルの説明)
- [ドキュメント作成の手順](#ドキュメント作成の手順)

## ディレクトリ構成

```
01-planning/
├── README.md                    # このファイル
├── _templates/                  # ドキュメント作成テンプレート（設計補助）
│   ├── _business-requirements.md
│   ├── _business-flow.md
│   ├── _functional-requirements.md
│   ├── _non-functional-requirements.md
│   ├── _constraints.md
│   └── _use-cases.md
├── _interview/                  # ヒアリング用質問・回答（設計補助）
│   └── _00-basic.md             # 基本ヒアリング
├── business-requirements.md     # ビジネス要件
├── business-flow.md             # 業務フロー図
├── functional-requirements.md   # 機能要件
├── non-functional-requirements.md # 非機能要件
├── constraints.md               # 制約事項
├── use-cases/                   # ユースケース
└── user-stories/                # [任意] ユーザーストーリー
```

## 各ファイルの説明

### _templates/ - ドキュメント作成テンプレート

各ドキュメントの記述ルール・項目定義・フォーマットを定義します。
Claude Codeがドキュメントを生成する際に参照し、出力の一貫性を保ちます。

配置するファイル:
- `_business-requirements.md` - ビジネス要件のテンプレート
- `_business-flow.md` - 業務フロー図のテンプレート
- `_functional-requirements.md` - 機能要件のテンプレート
- `_non-functional-requirements.md` - 非機能要件のテンプレート
- `_constraints.md` - 制約事項のテンプレート
- `_use-cases.md` - ユースケースのテンプレート

注意:
- `_` プレフィックスは設計補助ファイルを示す

### _interview/ - ヒアリング

要件定義に必要な情報を収集するための質問・回答ファイルを格納します。

配置するファイル:
- `_00-basic.md` - 基本ヒアリング（デフォルト提供）
- `_01-additional.md` - 追加質問（Claude Code生成）
- 必要に応じて追加

### business-requirements.md - ビジネス要件

プロジェクトの目的・背景・ゴールを定義します。

記載内容:
- プロジェクトの背景・目的
- ビジネス上の課題
- 期待する効果・KPI
- ステークホルダー一覧
- プロジェクトスコープ

### business-flow.md - 業務フロー図

業務プロセス全体の流れを可視化します。

記載内容:
- 現行業務フロー（As-Is）
- 新業務フロー（To-Be）
- 業務とシステムの関係

### functional-requirements.md - 機能要件

システムが提供すべき機能の一覧を定義します。

記載内容:
- 機能一覧表
- 各機能の概要説明
- 機能間の依存関係
- 優先度

### non-functional-requirements.md - 非機能要件

性能・セキュリティ・可用性等を定義します。

記載内容:
- 可用性（稼働率、障害復旧時間）
- 性能・拡張性（応答時間、同時接続数）
- 運用・保守性（バックアップ、監視）
- 移行性（データ移行、システム移行）
- セキュリティ（認証、暗号化、アクセス制御）
- システム環境（対応ブラウザ、OS）

### constraints.md - 制約事項

技術・予算・期間・法的制約等を定義します。

記載内容:
- 技術的制約（既存システム連携、使用言語指定）
- 予算制約
- スケジュール制約
- 法的・規制上の制約
- 組織・体制の制約

### use-cases/ - ユースケース

アクターとシステムの相互作用を記述します。

配置するファイル:
- 機能単位またはアクター単位でファイルを作成
- 例: `UC001-login.md`, `UC002-order.md`

### user-stories/ - ユーザーストーリー [任意]

ユーザー視点での機能記述を行います。

配置するファイル:
- 機能単位でファイルを作成
- 「〜として、〜したい。なぜなら〜」形式で記述

## ドキュメント作成の手順

このディレクトリ配下のドキュメントは、以下の手順で作成します。

### 手順

1. **基本ヒアリングに回答**
   - `_interview/_00-basic.md` の各質問に回答を記入
   - 現時点でわかる範囲で記入（不明な項目は「未定」「要検討」と記載）

2. **Claude Codeに追加質問を生成させる**
   - 回答済みのヒアリングファイルをClaude Codeに読み込ませる
   - 回答内容に基づき、追加で確認が必要な質問が連番ファイルとして生成される
   - ファイル命名規則: `_01-additional.md`, `_02-additional.md`, `_03-additional.md` ...
   - プロンプト例（初回）:
     ```
     docs/01-planning/_interview/_00-basic.md を読み込んで、
     回答内容を分析し、追加で確認が必要な質問を
     docs/01-planning/_interview/_01-additional.md として作成してください。
     質問は _00-basic.md と同じ形式で作成してください。
     ```
   - プロンプト例（2回目以降）:
     ```
     docs/01-planning/_interview/ 配下のファイルをすべて読み込んで、
     回答内容を分析し、追加で確認が必要な質問を
     docs/01-planning/_interview/_02-additional.md として作成してください。
     質問は _00-basic.md と同じ形式で作成してください。
     ```

3. **追加質問に回答（顧客・チームで検討）**
   - 顧客への確認が必要な質問: 顧客とのミーティングやヒアリングで確認（外部検討）
   - チーム内で検討可能な質問: チーム内で議論して決定（内部検討）
   - 回答を記入

4. **必要に応じて手順2〜3を繰り返す**
   - 情報が十分に揃うまで繰り返す
   - 繰り返すたびに連番を増やして新しいファイルを生成（`_03-additional.md`, `_04-additional.md` ...）

5. **ドキュメントを順次生成**
   - 十分な情報が揃ったら、以下の順序でドキュメントを生成
   - 各ドキュメントはレビュー・ブラッシュアップしてから次に進む

### ドキュメント作成順序

| 順序 | ファイル | 理由 |
|-----|---------|------|
| 1 | business-requirements.md | プロジェクトの方向性を確定（他の基礎になる） |
| 2 | constraints.md | 制約を明確にしてから他を作成 |
| 3 | functional-requirements.md | 機能一覧を定義 |
| 4 | non-functional-requirements.md | 非機能要件を定義 |
| 5 | business-flow.md | 業務フローを可視化 |
| 6 | use-cases/ | ユースケース詳細を作成 |

### プロンプト例

```
docs/01-planning/README.md と docs/01-planning/_templates/_business-requirements.md と
docs/01-planning/_interview/ 配下のファイルをすべて読み込んで、
docs/01-planning/business-requirements.md を作成してください。
```
