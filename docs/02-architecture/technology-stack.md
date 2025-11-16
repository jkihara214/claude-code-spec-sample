# 技術スタック

## 目次

- [概要](#概要)
- [技術スタック一覧](#技術スタック一覧)
- [バックエンド](#バックエンド)
  - [PHP](#php)
  - [Laravel](#laravel)
  - [主要パッケージ](#主要パッケージ)
- [フロントエンド](#フロントエンド)
  - [React](#react)
  - [TypeScript](#typescript)
  - [Next.js](#nextjs)
  - [主要ライブラリ](#主要ライブラリ)
- [データベース](#データベース)
  - [PostgreSQL](#postgresql)
  - [Redis](#redis)
- [インフラストラクチャ](#インフラストラクチャ)
  - [AWS](#aws)
  - [Docker](#docker)
- [開発ツール](#開発ツール)
  - [バージョン管理](#バージョン管理)
  - [CI/CD](#cicd)
  - [コード品質](#コード品質)
- [セキュリティ](#セキュリティ)
- [監視・ログ](#監視ログ)
- [技術選定の理由](#技術選定の理由)
- [関連ドキュメント](#関連ドキュメント)

## 概要

このドキュメントでは、社内資産・備品管理システムで採用する技術スタックを定義します。
各技術の選定理由、バージョン、代替案との比較を記載します。

## 技術スタック一覧

### バックエンド技術

| 技術 | バージョン | 用途 |
|------|-----------|------|
| PHP | 8.2+ | サーバーサイドプログラミング言語 |
| Laravel | 10.x (LTS) | Webアプリケーションフレームワーク |
| Composer | 2.x | PHPパッケージ管理 |

### フロントエンド技術

| 技術 | バージョン | 用途 |
|------|-----------|------|
| TypeScript | 5.x | 型安全な開発言語 |
| React | 18.x | UIコンポーネントライブラリ |
| Next.js | 14.x | フルスタックReactフレームワーク |
| Tailwind CSS | 3.x | ユーティリティファーストCSSフレームワーク |
| npm/pnpm | 10.x/8.x | Node.jsパッケージ管理 |

### データベース・ストレージ

| 技術 | バージョン | 用途 |
|------|-----------|------|
| PostgreSQL | 14+ | リレーショナルデータベース（メインデータストア） |
| Redis | 7+ | インメモリデータベース（セッション・キャッシュ） |
| Amazon S3 | - | オブジェクトストレージ（画像・ファイル保存） |

### インフラストラクチャ

| 技術 | バージョン | 用途 |
|------|-----------|------|
| AWS | - | クラウドプラットフォーム |
| Docker | 24.x | コンテナ化技術 |
| ECS Fargate | - | サーバーレスコンテナ実行環境 |
| Application Load Balancer | - | 負荷分散 |
| CloudFront | - | CDN（オプション） |

### 開発・運用ツール

| 技術 | バージョン | 用途 |
|------|-----------|------|
| Git | 2.x | バージョン管理システム |
| GitHub | - | ソースコードホスティング |
| GitHub Actions | - | CI/CDパイプライン |
| CloudWatch | - | 監視・ログ管理 |
| AWS Secrets Manager | - | シークレット管理 |

## バックエンド

### PHP

**バージョン**: 8.2+

**選定理由**:
- チームの既存スキルセット
- Laravel 10の推奨バージョン
- PHP 8.2の新機能（型システム強化、パフォーマンス向上）
- 長期サポート（2025年12月まで）

**主要機能**:
- JIT コンパイラによる高速化
- 強化された型システム
- Enum型のサポート
- Readonly クラス

**代替案検討**:
- **Node.js**: チームのスキルセット不足
- **Go**: 学習コストが高い
- **Python**: Laravelに相当する成熟フレームワークが少ない

### Laravel

**バージョン**: 10.x (LTS)

**選定理由**:
- PHPフレームワークのデファクトスタンダード
- 豊富なエコシステムとパッケージ
- Eloquent ORMによる生産性向上
- 認証・認可機能が充実（Sanctum, Socialite）
- キューシステムの標準装備
- 優れたドキュメント

**主要機能**:
- Eloquent ORM（データベースアクセス）
- Blade テンプレートエンジン
- Artisan CLI（コマンドラインツール）
- Laravel Sanctum（API認証）
- Laravel Socialite（SNS/SSO認証）
- Queue システム（非同期処理）
- Task Scheduling（定期実行）

**代替案検討**:
- **Symfony**: 高機能だが学習コスト高い
- **CodeIgniter**: 機能が限定的
- **Slim**: マイクロフレームワークで機能不足

### 主要パッケージ

| パッケージ | 用途 |
|-----------|------|
| `laravel/sanctum` | API認証（JWT） |
| `laravel/socialite` | SSO連携（Google, Microsoft） |
| `spatie/laravel-permission` | 権限管理（RBAC） |
| `barryvdh/laravel-debugbar` | 開発時デバッグ |
| `laravel/telescope` | 開発時デバッグ・モニタリング |
| `phpunit/phpunit` | テストフレームワーク |
| `phpstan/phpstan` | 静的解析 |
| `symfony/http-client` | HTTP通信 |
| `intervention/image` | 画像処理 |
| `simple-qrcode/simple-qrcode` | QRコード生成 |

## フロントエンド

### React

**バージョン**: 18.x

**選定理由**:
- コンポーネントベースの再利用性
- 豊富なエコシステム
- Next.jsの基盤
- Server Components（React 18+）
- 優れたTypeScriptサポート

**主要機能**:
- Virtual DOM
- Hooks API
- Server Components
- Suspense
- Concurrent Rendering

### TypeScript

**バージョン**: 5.x

**選定理由**:
- 型安全性による品質向上
- IDEサポートによる開発効率向上
- リファクタリングの安全性
- JavaScriptとの互換性
- Next.jsの推奨

**主要機能**:
- 静的型チェック
- インターフェース定義
- ジェネリクス
- Union/Intersection型
- 型推論

### Next.js

**バージョン**: 14.x (App Router)

**選定理由**:
- Reactのフルスタックフレームワーク
- SSR/SSGによるパフォーマンス最適化
- ファイルベースルーティング
- API Routes（プロキシとして利用）
- Image最適化
- 優れた開発体験

**主要機能**:
- App Router（推奨の新ルーター）
- Server Components
- Server Actions
- Streaming SSR
- 自動コード分割
- Image最適化
- TypeScript完全サポート

**代替案検討**:
- **Vite + React**: ビルドは高速だがSSR機能が弱い
- **Create React App**: メンテナンス終了
- **Remix**: Next.jsより採用事例少ない

### 主要ライブラリ

| ライブラリ | 用途 |
|-----------|------|
| `tailwindcss` | CSSフレームワーク |
| `shadcn/ui` | UIコンポーネント |
| `react-hook-form` | フォーム管理 |
| `zod` | バリデーション・型定義 |
| `axios` | HTTP通信 |
| `swr` / `tanstack/react-query` | データフェッチ・キャッシュ |
| `zustand` | 状態管理（軽量） |
| `date-fns` | 日付操作 |
| `react-hot-toast` | 通知表示 |
| `recharts` | グラフ表示 |

## データベース

### PostgreSQL

**バージョン**: 14+

**選定理由**:
- ACID準拠の信頼性
- JSON型サポート
- 強力なインデックス機能
- パフォーマンスと拡張性
- オープンソース
- AWS RDSの完全サポート

**主要機能**:
- JSONB型（柔軟なデータ保存）
- 全文検索
- パーティショニング
- トランザクション分離レベル
- ストアドプロシージャ
- トリガー

**代替案検討**:
- **MySQL**: JSON機能がPostgreSQLより劣る
- **MongoDB**: RDBMSが要件に適合
- **Oracle**: ライセンスコスト高

### Redis

**バージョン**: 7+

**選定理由**:
- 高速なインメモリキャッシュ
- セッション管理に最適
- Laravelキューのバックエンド
- データ型の豊富さ
- AWS ElastiCacheサポート

**用途**:
- セッション保存
- APIレスポンスキャッシュ
- ジョブキュー
- レート制限
- リアルタイムデータ

## インフラストラクチャ

### AWS

**選定理由**:
- 社内標準クラウドプラットフォーム
- 豊富なマネージドサービス
- 高い可用性とスケーラビリティ
- セキュリティ機能の充実
- 既存の社内ネットワーク接続

**使用サービス**:

| サービス | 用途 |
|---------|------|
| ECS Fargate | コンテナ実行環境 |
| RDS (PostgreSQL) | データベース |
| ElastiCache (Redis) | キャッシュ |
| S3 | 静的ファイル・画像保存 |
| CloudFront | CDN（オプション） |
| ALB | ロードバランサー |
| Route 53 | DNS |
| VPC | ネットワーク |
| PrivateLink/VPN | 社内ネットワーク接続 |
| SES | メール送信 |
| CloudWatch | 監視・ログ |
| IAM | アクセス管理 |

### Docker

**バージョン**: 24.x

**選定理由**:
- 開発環境の統一
- 本番環境との整合性
- ECS Fargateとの親和性
- ポータビリティ

**用途**:
- ローカル開発環境
- CI/CDパイプライン
- 本番環境デプロイ

## 開発ツール

### バージョン管理

**Git + GitHub**

- ソースコード管理
- プルリクエストレビュー
- Issue管理
- GitHub Actions（CI/CD）

### CI/CD

**GitHub Actions**

パイプライン:
1. コードプッシュ
2. 自動テスト実行
3. 静的解析
4. ビルド
5. デプロイ（staging/production）

### コード品質

| ツール | 用途 |
|-------|------|
| **PHPStan** | PHP静的解析 |
| **PHP CS Fixer** | PHPコードフォーマット |
| **ESLint** | TypeScript/JavaScript Lint |
| **Prettier** | コードフォーマット |
| **Husky** | Git hooks |
| **lint-staged** | コミット前チェック |

## セキュリティ

| ツール/サービス | 用途 |
|---------------|------|
| **Dependabot** | 脆弱性検知・自動PR |
| **OWASP ZAP** | 脆弱性スキャン |
| **AWS WAF** | Webアプリケーションファイアウォール |
| **AWS Secrets Manager** | シークレット管理 |
| **Let's Encrypt** | SSL証明書 |

## 監視・ログ

| サービス | 用途 |
|---------|------|
| **CloudWatch** | インフラ監視・ログ集約 |
| **CloudWatch Alarms** | アラート通知 |
| **X-Ray** | 分散トレーシング |
| **Laravel Telescope** | アプリケーション監視（開発） |
| **Sentry** | エラートラッキング（オプション） |

## 技術選定の理由

### なぜLaravel + Next.jsか

**Laravel (バックエンド)**:
- チームの既存PHP経験を活かせる
- 豊富な機能で開発速度向上
- SSO連携が容易（Socialite）
- ジョブキュー標準装備

**Next.js (フロントエンド)**:
- Reactエコシステムの活用
- SSRによるパフォーマンス最適化
- TypeScriptによる型安全性
- モダンな開発体験

**分離アーキテクチャの利点**:
- フロントエンド・バックエンドの独立した開発
- 将来的なモバイルアプリ対応が容易
- フロントエンドのスケーリングが独立
- チーム分担がしやすい

### パフォーマンス考慮

- **Redis**: 高速キャッシュでDB負荷軽減
- **PostgreSQL**: インデックス最適化
- **Next.js SSR**: 初期表示高速化
- **CDN**: 静的ファイル配信（S3 + CloudFront）
- **ECS Fargate**: オートスケーリング

### セキュリティ考慮

- **SSO統合**: パスワード管理不要
- **JWT認証**: ステートレスで安全
- **HTTPS強制**: 全通信暗号化
- **CSRF対策**: Laravel標準機能
- **SQL Injection対策**: Eloquent ORM
- **XSS対策**: React自動エスケープ

## 関連ドキュメント

- [システムアーキテクチャ](system-architecture.md) - アーキテクチャ全体像
- [データベース設計](database-design.md) - DB設計詳細
- [インフラ構成](infrastructure.md) - AWS構成詳細
- [セキュリティアーキテクチャ](security-architecture.md) - セキュリティ設計
- [../01-requirements/constraints.md](../01-requirements/constraints.md) - 技術的制約
