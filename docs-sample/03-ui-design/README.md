# UI設計ディレクトリ

## 目次

- [このディレクトリについて](#このディレクトリについて)
- [ディレクトリ構成](#ディレクトリ構成)
- [ディレクトリとファイルの構成](#ディレクトリとファイルの構成)
- [関連ドキュメント](#関連ドキュメント)

---

## このディレクトリについて

このディレクトリには、各画面のUI設計ドキュメントが格納されます。

各画面は、**機能カテゴリディレクトリ配下に画面単位のファイル**として配置されます：
- **{画面名}-ui-specification.md**: UI設計（画面レイアウト・UI要素・バリデーションルール定義）

**注:**
- API仕様（エンドポイント・リクエスト/レスポンス）は `docs/04-api` ディレクトリで一元管理されています。

---

## ディレクトリ構成

ディレクトリ名・ファイル名は [画面設計書](../02-architecture/screen-design.md) の英語表記に従います。

```
03-ui-design/
├── README.md                                      # このファイル（ディレクトリ構成と概要）
├── ui-common-specification.md                     # UI共通仕様書
├── ui-design-guide.md                             # UI仕様書作成ガイド
├── ui-specification-template.md                   # UI仕様書テンプレート
├── screens/                                       # ワイヤーフレーム画像
│
├── user-management/                               # ユーザー管理機能
│   ├── login-screen-ui-specification.md           # ログイン画面のUI仕様
│   └── profile-screen-ui-specification.md         # プロフィール画面のUI仕様
│
├── asset-management/                              # 資産管理機能
│   ├── asset-search-screen-ui-specification.md    # 資産検索画面のUI仕様
│   ├── asset-detail-screen-ui-specification.md    # 資産詳細画面のUI仕様
│   └── category-list-screen-ui-specification.md   # カテゴリー一覧画面のUI仕様
│
├── lending-management/                            # 貸出・返却機能
│   ├── lending-application-screen-ui-specification.md  # 貸出申請画面のUI仕様
│   ├── return-process-screen-ui-specification.md       # 返却処理画面のUI仕様
│   ├── lending-history-screen-ui-specification.md      # 貸出履歴画面のUI仕様
│   └── ...
│
├── inventory/                                     # 棚卸し機能
│   ├── inventory-check-screen-ui-specification.md      # 棚卸し実施画面のUI仕様
│   ├── inventory-discrepancy-screen-ui-specification.md # 棚卸し差異一覧画面のUI仕様
│   └── ...
│
├── reports/                                       # レポート・分析機能
│   ├── dashboard-screen-ui-specification.md       # ダッシュボード画面のUI仕様
│   └── ...
│
├── admin/                                         # 管理機能
│   ├── asset-register-screen-ui-specification.md  # 資産登録画面のUI仕様
│   └── ...
│
├── notifications/                                 # 通知機能
│   └── notification-list-screen-ui-specification.md # 通知一覧画面のUI仕様
│
└── common/                                        # 共通画面
    ├── error-screen-ui-specification.md           # エラー画面のUI仕様
    └── not-found-screen-ui-specification.md       # 404エラー画面のUI仕様
```

**注:**
- 機能名（英語）・画面名（英語）は [画面設計書](../02-architecture/screen-design.md) を参照してください。
- 詳細な命名規則やファイル作成手順は [UI仕様書作成ガイド](./ui-design-guide.md) を参照してください。

---

## ディレクトリとファイルの構成

### 管理用ファイル

| ファイル名 | 用途 |
|-----------|------|
| **README.md** | このファイル。ディレクトリの概要と各ファイルの説明 |
| **ui-common-specification.md** | UI共通仕様書（スタイルガイド、共通UIコンポーネント、アクセシビリティ等） |
| **ui-design-guide.md** | UI仕様書作成ガイド（命名規則、作成手順、注意事項） |
| **ui-specification-template.md** | UI仕様書のテンプレート（作成時に使用） |

### 画面別ファイル

各画面は **機能カテゴリディレクトリ配下にファイル**として配置されます。

**ファイル構成:**
```
{機能カテゴリ}/
└── {画面名}-ui-specification.md   # UI仕様書（レイアウト・UI要素・バリデーションルール定義）
```

**例:**
- `asset-management/asset-search-screen-ui-specification.md` - 資産検索画面のUI仕様
- `asset-management/asset-detail-screen-ui-specification.md` - 資産詳細画面のUI仕様
- `lending-management/lending-application-screen-ui-specification.md` - 貸出申請画面のUI仕様
- `lending-management/return-process-screen-ui-specification.md` - 返却処理画面のUI仕様
- `inventory/inventory-check-screen-ui-specification.md` - 棚卸し実施画面のUI仕様

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
- [UI仕様書テンプレート](./ui-specification-template.md) - テンプレート

### その他

- [画面設計書](../02-architecture/screen-design.md) - 機能名（英語）・画面名（英語）の参照元
- [機能要件定義書](../01-requirements/functional-requirements.md)
- [アーキテクチャ設計](../02-architecture/)
- [データベース設計書](../02-architecture/database-design.md)
- [API仕様書](../04-api/)
- [テスト仕様書](../06-tests/)

---

**このディレクトリ内の機能仕様書は、実装前に必ずレビューを受けてください。**