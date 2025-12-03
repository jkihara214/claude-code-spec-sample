# API仕様ディレクトリ

## 目次

- [このディレクトリについて](#このディレクトリについて)
- [ディレクトリ構成](#ディレクトリ構成)
- [関連ドキュメント](#関連ドキュメント)

---

## このディレクトリについて

このディレクトリには、APIのインターフェース定義とドキュメントが格納されます。

**格納する内容:**
- RESTful API仕様
- GraphQL スキーマ
- リクエスト/レスポンス例
- 認証・認可仕様
- エラーコード定義
- API バージョニング方針

---

## ディレクトリ構成

```
04-api/
├── README.md                    # このファイル
├── api-specification-template.md # API仕様書テンプレート
│
├── users/                       # ユーザー関連API
│   ├── list/
│   │   └── specification.md     # GET /api/users
│   ├── create/
│   │   └── specification.md     # POST /api/users
│   ├── detail/
│   │   └── specification.md     # GET /api/users/:id
│   ├── update/
│   │   └── specification.md     # PUT /api/users/:id
│   └── delete/
│       └── specification.md     # DELETE /api/users/:id
│
├── assets/                      # 資産関連API
│   └── ...
│
└── ...                          # その他のAPI
```

**命名規則:**
- **リソース名**: 複数形の英小文字（例: `users`, `assets`, `groups`）
- **操作名**: `list`, `create`, `detail`, `update`, `delete` など

---

## 関連ドキュメント

- [アーキテクチャ設計](../02-architecture/)
- [UI仕様書](../03-ui-design/)
- [インタラクション仕様書](../05-interactions/)
- [テスト仕様書](../06-tests/)

---

**このディレクトリ内のAPI仕様書は、実装前に必ずレビューを受けてください。**
