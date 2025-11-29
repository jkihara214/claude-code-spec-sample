# UI設計ディレクトリ

## 目次

- [このディレクトリについて](#このディレクトリについて)
- [ディレクトリ構成](#ディレクトリ構成)
- [ディレクトリとファイルの構成](#ディレクトリとファイルの構成)
- [関連ドキュメント](#関連ドキュメント)

---

## このディレクトリについて

このディレクトリには、各画面のUI設計ドキュメントが格納されます。

各画面は、**機能カテゴリ > 画面単位でディレクトリ化**され、以下のドキュメントで構成されます：
- **README.md**: 機能概要・データモデル・実装ステータス
- **ui-specification.md**: UI設計（画面レイアウト・UI要素・バリデーションルール定義）

**注:**
- API仕様（エンドポイント・リクエスト/レスポンス）は `docs/04-api` ディレクトリで一元管理されています。
- インタラクション仕様（UI×API紐づけ、処理フロー、バリデーション実行タイミング、エラーハンドリング）は `docs/05-interactions` ディレクトリで管理されています。

---

## ディレクトリ構成

ディレクトリ名は [画面設計書](../02-architecture/screen-design.md) の英語表記に従います。

```
03-ui-design/
├── README.md                          # このファイル（ディレクトリ構成と概要）
├── ui-common-specification.md         # UI共通仕様書
├── ui-design-guide.md                 # UI仕様書作成ガイド
├── ui-specification-template.md       # UI仕様書テンプレート
│
├── user-management/                   # ユーザー管理機能
│   ├── login-screen/
│   │   ├── README.md                  # ログイン画面の機能概要
│   │   └── ui-specification.md        # ログイン画面のUI仕様
│   └── profile-screen/
│       ├── README.md                  # プロフィール画面の機能概要
│       └── ui-specification.md        # プロフィール画面のUI仕様
│
├── asset-management/                  # 資産管理機能
│   ├── asset-search-screen/
│   │   ├── README.md                  # 資産検索画面の機能概要
│   │   └── ui-specification.md        # 資産検索画面のUI仕様
│   ├── asset-detail-screen/
│   │   ├── README.md                  # 資産詳細画面の機能概要
│   │   └── ui-specification.md        # 資産詳細画面のUI仕様
│   └── category-list-screen/
│       ├── README.md                  # カテゴリー一覧画面の機能概要
│       └── ui-specification.md        # カテゴリー一覧画面のUI仕様
│
├── lending-management/                # 貸出・返却機能
│   ├── lending-application-screen/
│   │   ├── README.md                  # 貸出申請画面の機能概要
│   │   └── ui-specification.md        # 貸出申請画面のUI仕様
│   ├── return-process-screen/
│   │   ├── README.md                  # 返却処理画面の機能概要
│   │   └── ui-specification.md        # 返却処理画面のUI仕様
│   ├── lending-history-screen/
│   │   ├── README.md                  # 貸出履歴画面の機能概要
│   │   └── ui-specification.md        # 貸出履歴画面のUI仕様
│   └── ...
│
├── inventory/                         # 棚卸し機能
│   ├── inventory-check-screen/
│   │   ├── README.md                  # 棚卸し実施画面の機能概要
│   │   └── ui-specification.md        # 棚卸し実施画面のUI仕様
│   ├── inventory-discrepancy-screen/
│   │   ├── README.md                  # 棚卸し差異一覧画面の機能概要
│   │   └── ui-specification.md        # 棚卸し差異一覧画面のUI仕様
│   └── ...
│
├── reports/                           # レポート・分析機能
│   ├── dashboard-screen/
│   │   ├── README.md                  # ダッシュボード画面の機能概要
│   │   └── ui-specification.md        # ダッシュボード画面のUI仕様
│   └── ...
│
├── admin/                             # 管理機能
│   ├── asset-register-screen/
│   │   ├── README.md                  # 資産登録画面の機能概要
│   │   └── ui-specification.md        # 資産登録画面のUI仕様
│   └── ...
│
├── notifications/                     # 通知機能
│   └── notification-list-screen/
│       ├── README.md                  # 通知一覧画面の機能概要
│       └── ui-specification.md        # 通知一覧画面のUI仕様
│
└── common/                            # 共通画面
    ├── error-screen/
    │   └── ui-specification.md        # エラー画面のUI仕様
    └── not-found-screen/
        └── ui-specification.md        # 404エラー画面のUI仕様
```

**注:**
- 機能名（英語）・画面名（英語）は [画面設計書](../02-architecture/screen-design.md) を参照してください。
- 詳細な命名規則やディレクトリ作成手順は [UI仕様書作成ガイド](./ui-design-guide.md) を参照してください。
- インタラクション仕様書（処理フロー、API連携）は `docs/05-interactions/` ディレクトリで管理されています。

---

## ディレクトリとファイルの構成

### 管理用ファイル

| ファイル名 | 用途 |
|-----------|------|
| **README.md** | このファイル。ディレクトリの概要と各ファイルの説明 |
| **ui-common-specification.md** | UI共通仕様書（スタイルガイド、共通UIコンポーネント、アクセシビリティ等） |
| **ui-design-guide.md** | UI仕様書作成ガイド（命名規則、作成手順、注意事項） |
| **ui-specification-template.md** | UI仕様書のテンプレート（ui-specification.md作成時に使用） |

### 画面別ディレクトリ

各画面は **機能カテゴリ/画面名** の階層構造で管理されます。

**ディレクトリ構成:**
```
{機能カテゴリ}/{画面名}/
├── README.md                  # 機能概要（概要・データモデル・実装ステータス）
└── ui-specification.md        # UI仕様書（レイアウト・UI要素・バリデーションルール定義）
```

**注:** インタラクション仕様書（処理フロー、バリデーション実行タイミング、API連携、状態管理）は `docs/05-interactions/` ディレクトリで管理されています。

**例:**
- `asset-management/asset-search-screen/` - 資産検索画面（README + UI仕様）
- `asset-management/asset-detail-screen/` - 資産詳細画面（README + UI仕様）
- `lending-management/lending-application-screen/` - 貸出申請画面（README + UI仕様）
- `lending-management/return-process-screen/` - 返却処理画面（README + UI仕様）
- `inventory/inventory-check-screen/` - 棚卸し実施画面（README + UI仕様）

**命名規則:**
- **機能カテゴリ**: [画面設計書](../02-architecture/screen-design.md) の「機能名（英語）」を使用
  - 例: `user-management`, `asset-management`, `lending-management`, `inventory`, `reports`, `admin`, `notifications`, `common`
- **画面名**: [画面設計書](../02-architecture/screen-design.md) の「画面名（英語）」を使用
  - 例: `login-screen`, `asset-search-screen`, `lending-application-screen`

詳細な作成手順は [UI仕様書作成ガイド](./ui-design-guide.md) を参照してください。

---

## 関連ドキュメント

### UI設計・仕様

- [UI共通仕様書](./ui-common-specification.md) - すべての画面に共通するUI仕様
- [UI仕様書作成ガイド](./ui-design-guide.md) - UI仕様書の作成方法
- [UI仕様書テンプレート](./ui-specification-template.md) - ui-specification.md のテンプレート

### インタラクション仕様（詳細設計）

- [インタラクション仕様書テンプレート](../05-interactions/interaction-specification-template.md) - interaction-specification.md のテンプレート

### 既存のUI仕様書

- [資産検索](./asset-management/asset-search-screen/) - 資産検索画面のUI仕様
- [資産詳細](./asset-management/asset-detail-screen/) - 資産詳細画面のUI仕様
- [資産登録](./admin/asset-register-screen/) - 資産登録画面のUI仕様（管理者向け）
- [貸出申請](./lending-management/lending-application-screen/) - 貸出申請画面のUI仕様
- [返却処理](./lending-management/return-process-screen/) - 返却処理画面のUI仕様
- [貸出履歴](./lending-management/lending-history-screen/) - 貸出履歴画面のUI仕様
- [棚卸し実施](./inventory/inventory-check-screen/) - 棚卸し実施画面のUI仕様
- [棚卸し差異対応](./inventory/inventory-discrepancy-screen/) - 棚卸し差異対応画面のUI仕様
- ...

### その他

- [画面設計書](../02-architecture/screen-design.md) - 機能名（英語）・画面名（英語）の参照元
- [機能要件定義書](../01-requirements/functional-requirements.md)
- [アーキテクチャ設計](../02-architecture/)
- [データベース設計書](../02-architecture/database-design.md)
- [API仕様書](../04-api/)
- [インタラクション仕様書](../05-interactions/)
- [テスト仕様書](../06-tests/)

---

**このディレクトリ内の機能仕様書は、実装前に必ずレビューを受けてください。**