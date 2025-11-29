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
- **README.md**: 機能概要・データモデル・使用するAPI一覧・実装ステータス
- **ui-specification.md**: UI設計（画面レイアウト・UI要素・バリデーションルール定義）

**注:**
- API仕様（エンドポイント・リクエスト/レスポンス）は `docs/04-api` ディレクトリで一元管理されています。画面仕様書からは、使用するAPIへのリンクで参照します。
- インタラクション仕様（UI×API紐づけ、処理フロー、バリデーション実行タイミング、エラーハンドリング）は `docs/05-interactions` ディレクトリで管理されています。

---

## ディレクトリ構成

```
03-ui-design/
├── README.md                          # このファイル（ディレクトリ構成と概要）
├── ui-common-specification.md         # UI共通仕様書
├── feature-guide.md                   # UI仕様書作成ガイド
├── ui-specification-template.md       # UI仕様書テンプレート
│
├── asset-management/                  # 資産管理機能
│   ├── asset-search/
│   │   ├── README.md                  # 資産検索画面の機能概要
│   │   └── ui-specification.md        # 資産検索画面のUI仕様
│   ├── asset-detail/
│   │   ├── README.md                  # 資産詳細画面の機能概要
│   │   └── ui-specification.md        # 資産詳細画面のUI仕様
│   ├── asset-registration/
│   │   ├── README.md                  # 資産登録画面の機能概要
│   │   └── ui-specification.md        # 資産登録画面のUI仕様
│   └── ...
│
├── lending-management/                # 貸出管理機能
│   ├── lending-application/
│   │   ├── README.md                  # 貸出申請画面の機能概要
│   │   └── ui-specification.md        # 貸出申請画面のUI仕様
│   ├── return-process/
│   │   ├── README.md                  # 返却処理画面の機能概要
│   │   └── ui-specification.md        # 返却処理画面のUI仕様
│   ├── lending-history/
│   │   ├── README.md                  # 貸出履歴画面の機能概要
│   │   └── ui-specification.md        # 貸出履歴画面のUI仕様
│   └── ...
│
├── inventory-management/              # 棚卸し管理機能
│   ├── inventory-execution/
│   │   ├── README.md                  # 棚卸し実施画面の機能概要
│   │   └── ui-specification.md        # 棚卸し実施画面のUI仕様
│   ├── inventory-discrepancy/
│   │   ├── README.md                  # 棚卸し差異対応画面の機能概要
│   │   └── ui-specification.md        # 棚卸し差異対応画面のUI仕様
│   └── ...
│
└── ...                                # その他の機能
```

**注:**
- 詳細な命名規則やディレクトリ作成手順は [UI仕様書作成ガイド](./feature-guide.md) を参照してください。
- インタラクション仕様書（処理フロー、API連携）は `docs/05-interactions/` ディレクトリで管理されています。

---

## ディレクトリとファイルの構成

### 管理用ファイル

| ファイル名 | 用途 |
|-----------|------|
| **README.md** | このファイル。ディレクトリの概要と各ファイルの説明 |
| **ui-common-specification.md** | UI共通仕様書（スタイルガイド、共通UIコンポーネント、アクセシビリティ等） |
| **feature-guide.md** | UI仕様書作成ガイド（命名規則、作成手順、注意事項） |
| **ui-specification-template.md** | UI仕様書のテンプレート（ui-specification.md作成時に使用） |

### 画面別ディレクトリ

各画面は **機能カテゴリ/画面名** の階層構造で管理されます。

**ディレクトリ構成:**
```
{機能カテゴリ}/{画面名}/
├── README.md                  # 機能概要（概要・データモデル・使用するAPI一覧・実装ステータス）
└── ui-specification.md        # UI仕様書（レイアウト・UI要素・バリデーションルール定義）
```

**注:** インタラクション仕様書（処理フロー、バリデーション実行タイミング、API連携、状態管理）は `docs/05-interactions/` ディレクトリで管理されています。

**例:**
- `asset-management/asset-search/` - 資産検索画面（README + UI仕様）
- `asset-management/asset-detail/` - 資産詳細画面（README + UI仕様）
- `lending-management/lending-application/` - 貸出申請画面（README + UI仕様）
- `lending-management/return-process/` - 返却処理画面（README + UI仕様）
- `inventory-management/inventory-execution/` - 棚卸し実施画面（README + UI仕様）

**命名規則:**
- **機能カテゴリ**: ハイフン区切りの英小文字（例: `asset-management`, `lending-management`, `inventory-management`）
- **画面名**: ハイフン区切りの英小文字（例: `asset-search`, `asset-detail`, `lending-application`）

詳細な作成手順は [UI仕様書作成ガイド](./feature-guide.md) を参照してください。

---

## 関連ドキュメント

### UI設計・仕様

- [UI共通仕様書](./ui-common-specification.md) - すべての画面に共通するUI仕様
- [UI仕様書作成ガイド](./feature-guide.md) - UI仕様書の作成方法
- [UI仕様書テンプレート](./ui-specification-template.md) - ui-specification.md のテンプレート

### インタラクション仕様（詳細設計）

- [インタラクション仕様書テンプレート](../05-interactions/interaction-specification-template.md) - interaction-specification.md のテンプレート

### 既存のUI仕様書

- [資産検索](./asset-management/asset-search/) - 資産検索画面のUI仕様
- [資産詳細](./asset-management/asset-detail/) - 資産詳細画面のUI仕様
- [資産登録](./asset-management/asset-registration/) - 資産登録画面のUI仕様（管理者向け）
- [貸出申請](./lending-management/lending-application/) - 貸出申請画面のUI仕様
- [返却処理](./lending-management/return-process/) - 返却処理画面のUI仕様
- [貸出履歴](./lending-management/lending-history/) - 貸出履歴画面のUI仕様
- [棚卸し実施](./inventory-management/inventory-execution/) - 棚卸し実施画面のUI仕様
- [棚卸し差異対応](./inventory-management/inventory-discrepancy/) - 棚卸し差異対応画面のUI仕様
- ...

### その他

- [機能要件定義書](../01-requirements/functional-requirements.md)
- [アーキテクチャ設計](../02-architecture/)
- [データベース設計書](../02-architecture/database-design.md)
- [API仕様書](../04-api/)
- [インタラクション仕様書](../05-interactions/)
- [テスト仕様書](../06-tests/)

---

**このディレクトリ内の機能仕様書は、実装前に必ずレビューを受けてください。**