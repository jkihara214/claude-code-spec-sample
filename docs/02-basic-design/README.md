# 02-basic-design - 基本設計（外部設計）

システム全体のアーキテクチャ、UI、API、データベースの設計を行います。
ユーザーから見える部分（インターフェース）を決定するフェーズです。

## ディレクトリ構成

```
02-basic-design/
├── README.md                    # このファイル
├── architecture/                # アーキテクチャ設計
│   ├── technology-stack.md      # 技術スタック
│   ├── system-architecture.md   # システム構成図
│   ├── infrastructure.md        # インフラ構成
│   └── performance-design.md    # パフォーマンス設計
├── ui-design/                   # UI設計
│   ├── screen-overview.md       # 画面一覧・遷移図
│   └── screens/                 # 個別画面設計
├── api-design/                  # API設計（OpenAPI形式）
│   ├── openapi.yaml             # OpenAPI仕様書
│   └── api-guidelines.md        # API設計ガイドライン
├── database/                    # データベース設計
│   └── database-design.md       # ER図・テーブル定義
├── security/                    # セキュリティ設計
│   └── security-design.md       # 認証・認可・データ保護
├── report-design/               # [任意] 帳票設計
│   └── report-specifications.md # 帳票仕様書
├── batch-design/                # [任意] バッチ処理設計
│   └── batch-specifications.md  # バッチ仕様書
└── external-interface/          # [任意] 外部インターフェース設計
    └── external-api.md          # 外部API連携仕様
```

## 各サブディレクトリの説明

### architecture/ - アーキテクチャ設計

| ファイル | 内容 |
|---------|------|
| technology-stack.md | 使用技術・フレームワーク・ライブラリの選定理由 |
| system-architecture.md | システム全体構成図、コンポーネント構成 |
| infrastructure.md | クラウド構成、ネットワーク構成、環境定義 |
| performance-design.md | 性能目標、キャッシュ戦略、負荷分散設計 |

### ui-design/ - UI設計

| ファイル/ディレクトリ | 内容 |
|---------------------|------|
| screen-overview.md | 全画面の一覧表と画面遷移図（Mermaid形式） |
| screens/ | 各画面の詳細設計（レイアウト、UI要素、状態、関連API） |

screens/ 配下のファイル命名規則:
- `S001-login.md` - 画面ID + 画面名
- ワイヤーフレームは `screens/wireframes/` に配置

### api-design/ - API設計

| ファイル | 内容 |
|---------|------|
| openapi.yaml | OpenAPI仕様書（エンドポイント、リクエスト/レスポンス、スキーマ） |
| api-guidelines.md | API命名規則、認証方式、共通エラーコード、バージョニング方針 |

### database/ - データベース設計

| ファイル | 内容 |
|---------|------|
| database-design.md | ER図（Mermaid形式）、テーブル定義書 |

### security/ - セキュリティ設計

| ファイル | 内容 |
|---------|------|
| security-design.md | 認証方式、認可設計、データ保護、セキュリティ対策 |

### report-design/ - 帳票設計 [任意]

| ファイル | 内容 |
|---------|------|
| report-specifications.md | 帳票一覧、帳票レイアウト、出力形式 |

### batch-design/ - バッチ処理設計 [任意]

| ファイル | 内容 |
|---------|------|
| batch-specifications.md | バッチ一覧、実行タイミング、入出力、概要フロー |

### external-interface/ - 外部インターフェース設計 [任意]

| ファイル | 内容 |
|---------|------|
| external-api.md | 外部システム連携一覧、連携方式、データマッピング |
