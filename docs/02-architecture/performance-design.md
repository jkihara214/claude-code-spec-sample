# パフォーマンス設計

## 目次

- [概要](#概要)
- [パフォーマンス目標](#パフォーマンス目標)
  - [レスポンスタイム目標](#レスポンスタイム目標)
  - [スループット目標](#スループット目標)
  - [リソース使用率目標](#リソース使用率目標)
- [フロントエンド最適化](#フロントエンド最適化)
  - [Next.js SSR/SSG](#nextjs-ssrssg)
  - [コード分割](#コード分割)
  - [画像最適化](#画像最適化)
  - [バンドルサイズ最適化](#バンドルサイズ最適化)
- [バックエンド最適化](#バックエンド最適化)
  - [APIレスポンス最適化](#apiレスポンス最適化)
  - [N+1問題対策](#n1問題対策)
  - [非同期処理](#非同期処理)
- [キャッシュ戦略](#キャッシュ戦略)
  - [アプリケーションキャッシュ](#アプリケーションキャッシュ)
  - [データベースクエリキャッシュ](#データベースクエリキャッシュ)
  - [CDNキャッシュ](#cdnキャッシュ)
  - [ブラウザキャッシュ](#ブラウザキャッシュ)
  - [キャッシュ無効化戦略](#キャッシュ無効化戦略)
- [データベース最適化](#データベース最適化)
  - [インデックス戦略](#インデックス戦略)
  - [クエリ最適化](#クエリ最適化)
  - [コネクションプール](#コネクションプール)
  - [パーティショニング](#パーティショニング)
- [ネットワーク最適化](#ネットワーク最適化)
  - [CDN活用](#cdn活用)
  - [HTTP/2・HTTP/3](#http2http3)
  - [圧縮](#圧縮)
  - [接続の再利用](#接続の再利用)
- [スケーリング戦略](#スケーリング戦略)
  - [水平スケーリング](#水平スケーリング)
  - [垂直スケーリング](#垂直スケーリング)
  - [オートスケーリング](#オートスケーリング)
- [非同期処理とキュー](#非同期処理とキュー)
  - [ジョブキュー設計](#ジョブキュー設計)
  - [バッチ処理](#バッチ処理)
- [パフォーマンス監視](#パフォーマンス監視)
  - [メトリクス収集](#メトリクス収集)
  - [APM導入](#apm導入)
  - [ボトルネック分析](#ボトルネック分析)
- [負荷テスト](#負荷テスト)
  - [負荷テストシナリオ](#負荷テストシナリオ)
  - [性能基準](#性能基準)
- [最適化チェックリスト](#最適化チェックリスト)
- [関連ドキュメント](#関連ドキュメント)

## 概要

このドキュメントでは、社内資産・備品管理システムのパフォーマンス設計を定義します。
レスポンスタイム目標、キャッシュ戦略、データベース最適化、スケーリング戦略など、
システム全体のパフォーマンスを最適化するための設計方針を示します。

## パフォーマンス目標

### レスポンスタイム目標

| 操作 | 目標レスポンスタイム | 許容レスポンスタイム |
|-----|-----------------|-----------------|
| **ページ表示** |
| トップページ（初回） | 1秒以内 | 2秒以内 |
| トップページ（2回目以降） | 0.3秒以内 | 1秒以内 |
| 資産一覧表示（50件） | 0.5秒以内 | 1秒以内 |
| 資産詳細表示 | 0.3秒以内 | 1秒以内 |
| 資産検索結果表示 | 1秒以内 | 2秒以内 |
| **API呼び出し** |
| 資産検索API | 300ms以内 | 1秒以内 |
| 資産登録API | 500ms以内 | 1秒以内 |
| 資産更新API | 300ms以内 | 1秒以内 |
| 貸出申請API | 500ms以内 | 1秒以内 |
| 一覧取得API | 200ms以内 | 500ms以内 |
| **バッチ処理** |
| 棚卸レポート生成（4000件） | 30秒以内 | 60秒以内 |
| CSVエクスポート（4000件） | 10秒以内 | 30秒以内 |
| メール一斉送信（500件） | 5分以内 | 10分以内 |

**測定条件**:
- サーバーレスポンスタイム（ネットワーク遅延除く）
- 同時接続ユーザー数: 50人
- 測定環境: 本番環境相当

### スループット目標

| メトリクス | 目標値 |
|----------|-------|
| 同時ユーザー数 | 50人（通常時） |
| 最大同時ユーザー数 | 100人（ピーク時） |
| 1日あたりAPI呼び出し数 | 50,000リクエスト |
| 1秒あたりリクエスト数（平均） | 10 RPS |
| 1秒あたりリクエスト数（ピーク） | 50 RPS |

### リソース使用率目標

| リソース | 目標使用率 | 最大使用率 |
|---------|-----------|-----------|
| ECS CPU使用率 | 50%以下 | 80%以下 |
| ECS メモリ使用率 | 60%以下 | 80%以下 |
| RDS CPU使用率 | 50%以下 | 70%以下 |
| RDS 接続数 | 50以下 | 150以下 |
| ElastiCache CPU | 50%以下 | 75%以下 |
| ElastiCache メモリ | 70%以下 | 90%以下 |

## フロントエンド最適化

### Next.js SSR/SSG

**ページレンダリング戦略**:

| ページタイプ | レンダリング方法 | 理由 |
|-----------|--------------|------|
| トップページ | SSG (Static Generation) | 静的コンテンツ、高速表示 |
| 資産一覧ページ | SSR (Server-Side Rendering) | データ最新性、SEO |
| 資産詳細ページ | SSR + Client-side fetch | 初期表示SSR、詳細データClient fetch |
| ダッシュボード | CSR (Client-Side Rendering) | ユーザーごとに異なる、リアルタイム |
| 検索結果ページ | CSR | ユーザー入力に依存、リアルタイム |

**SSG実装例**:

```typescript
// pages/index.tsx (トップページ)
export async function getStaticProps() {
  const stats = await fetchSystemStats(); // ビルド時に取得

  return {
    props: { stats },
    revalidate: 3600, // 1時間ごとに再生成 (ISR)
  };
}
```

**SSR実装例**:

```typescript
// pages/assets/[id].tsx (資産詳細)
export async function getServerSideProps(context) {
  const { id } = context.params;
  const asset = await fetchAsset(id);

  return {
    props: { asset },
  };
}
```

**ISR (Incremental Static Regeneration)**:
- 静的ページを定期的に再生成
- トップページ: 1時間ごと
- カテゴリページ: 30分ごと

### コード分割

**ルートベース分割**:

```typescript
// Next.jsのファイルベースルーティングで自動分割
pages/
  index.tsx           → index.js (25KB)
  assets/
    index.tsx         → assets.js (30KB)
    [id].tsx          → assets-[id].js (20KB)
  lending/
    index.tsx         → lending.js (35KB)
```

**コンポーネント遅延ロード**:

```typescript
// 重いコンポーネントを遅延ロード
import dynamic from 'next/dynamic';

const ChartComponent = dynamic(() => import('@/components/Chart'), {
  loading: () => <p>Loading chart...</p>,
  ssr: false, // クライアントサイドのみ
});
```

**バンドル分析**:

```bash
npm run build
# → 各チャンクのサイズを確認
```

**目標バンドルサイズ**:
- 初期JSバンドル: 200KB以下（gzip後）
- 各ルートチャンク: 50KB以下（gzip後）

### 画像最適化

**Next.js Image コンポーネント**:

```typescript
import Image from 'next/image';

<Image
  src="/assets/asset-photo.jpg"
  alt="資産画像"
  width={300}
  height={200}
  placeholder="blur"
  loading="lazy"
  quality={85}
/>
```

**最適化内容**:
- 自動WebP/AVIF変換
- レスポンシブ画像（srcset自動生成）
- 遅延ロード（Intersection Observer）
- ぼかしプレースホルダー

**S3画像配信最適化**:
- CloudFront経由で配信
- キャッシュ有効期限: 1年
- サムネイル事前生成（Lambda@Edge）

**画像サイズガイドライン**:

| 用途 | サイズ | 品質 | フォーマット |
|-----|-------|------|------------|
| 資産画像（一覧） | 300x200 | 80% | WebP |
| 資産画像（詳細） | 800x600 | 85% | WebP |
| QRコード | 300x300 | 100% | PNG |
| アイコン | SVG | - | SVG |

### バンドルサイズ最適化

**Tree Shaking**:

```typescript
// ❌ 悪い例
import _ from 'lodash';

// ✅ 良い例
import debounce from 'lodash/debounce';
```

**モジュール最適化**:

```json
// package.json
{
  "sideEffects": false,
  "module": "dist/index.esm.js"
}
```

**不要なライブラリ削除**:
- moment.js → date-fns に置き換え（-67KB）
- lodash → 個別インポート（-50KB）

**CDN経由でのライブラリ読み込み**（検討）:

```html
<!-- React等の大きなライブラリをCDN化（検討中） -->
<script src="https://cdn.example.com/react@18.2.0.min.js"></script>
```

## バックエンド最適化

### APIレスポンス最適化

**JSON圧縮**:

```php
// app/Http/Middleware/CompressResponse.php
return response()->json($data)->withHeaders([
    'Content-Encoding' => 'gzip',
]);
```

**ペジネーション必須**:

```php
// app/Http/Controllers/AssetController.php
public function index(Request $request)
{
    $perPage = $request->input('per_page', 50); // デフォルト50件
    $assets = Asset::with(['category', 'location'])
        ->paginate($perPage);

    return response()->json($assets);
}
```

**レスポンスフィールド最適化**:

```php
// 必要なフィールドのみ返却
public function toArray($request)
{
    return [
        'id' => $this->id,
        'name' => $this->name,
        'asset_code' => $this->asset_code,
        'status' => $this->status,
        // 不要な large_description は除外
    ];
}
```

**HTTP/2 Server Push（検討中）**:
- 重要なAPIレスポンスをプッシュ

### N+1問題対策

**Eager Loading**:

```php
// ❌ N+1問題あり
$assets = Asset::all();
foreach ($assets as $asset) {
    echo $asset->category->name; // N回のクエリ
}

// ✅ Eager Loading
$assets = Asset::with(['category', 'location'])->get();
foreach ($assets as $asset) {
    echo $asset->category->name; // 1回のクエリ
}
```

**クエリ数監視**:

```php
// 開発環境でN+1検出
if (app()->environment('local')) {
    DB::listen(function ($query) {
        if ($query->time > 100) {
            Log::warning('Slow query detected', [
                'sql' => $query->sql,
                'time' => $query->time,
            ]);
        }
    });
}
```

### 非同期処理

**重い処理をキューに委譲**:

```php
// ❌ 同期処理（遅い）
public function store(Request $request)
{
    $asset = Asset::create($request->all());

    // QRコード生成（500ms）
    $this->generateQRCode($asset);

    // メール送信（1000ms）
    Mail::to($admin)->send(new AssetCreated($asset));

    return response()->json($asset); // 1500ms後にレスポンス
}

// ✅ 非同期処理（速い）
public function store(Request $request)
{
    $asset = Asset::create($request->all());

    // ジョブキューに追加
    GenerateQRCodeJob::dispatch($asset);
    SendAssetCreatedEmailJob::dispatch($asset);

    return response()->json($asset); // 100ms後にレスポンス
}
```

## キャッシュ戦略

### アプリケーションキャッシュ

**Redisキャッシュ階層**:

```
┌──────────────────────────────────────┐
│  Layer 1: ブラウザキャッシュ (1時間)  │
├──────────────────────────────────────┤
│  Layer 2: CDNキャッシュ (1日)        │
├──────────────────────────────────────┤
│  Layer 3: Redisキャッシュ (10分-1時間)│
├──────────────────────────────────────┤
│  Layer 4: データベース                │
└──────────────────────────────────────┘
```

**キャッシュ対象データ**:

| データ | キャッシュキー | TTL | 無効化タイミング |
|-------|-------------|-----|---------------|
| 資産カテゴリ一覧 | `categories:all` | 1時間 | カテゴリ変更時 |
| 拠点一覧 | `locations:all` | 1時間 | 拠点変更時 |
| ユーザー情報 | `user:{id}` | 30分 | ユーザー更新時 |
| 資産検索結果 | `search:{hash}` | 5分 | - |
| 資産詳細 | `asset:{id}` | 10分 | 資産更新時 |
| 貸出申請数 | `lending_count:{location}` | 1分 | 貸出申請時 |

**キャッシュ実装例**:

```php
// Laravelキャッシュ
use Illuminate\Support\Facades\Cache;

public function getCategories()
{
    return Cache::remember('categories:all', 3600, function () {
        return AssetCategory::all();
    });
}

// タグベースキャッシュ
Cache::tags(['assets', 'location:1'])->put('assets:location:1', $assets, 600);

// 無効化
Cache::tags(['assets'])->flush(); // 全資産キャッシュをクリア
```

### データベースクエリキャッシュ

**PostgreSQL クエリキャッシュ**:

PostgreSQL自体にクエリキャッシュ機能はないため、アプリケーション層でキャッシュ。

```php
// クエリ結果をRedisにキャッシュ
public function getAssetsByLocation(int $locationId)
{
    $cacheKey = "assets:location:{$locationId}";

    return Cache::remember($cacheKey, 600, function () use ($locationId) {
        return Asset::where('location_id', $locationId)
            ->with(['category'])
            ->get();
    });
}
```

### CDNキャッシュ

**CloudFront キャッシュ設定**:

| パス | TTL | キャッシュキー |
|-----|-----|------------|
| `/assets/*` (画像) | 1年 | URLのみ |
| `/_next/static/*` | 1年 | URLのみ |
| `/api/*` | キャッシュなし | - |
| `/*` (HTML) | 1時間 | URL + Cookie |

**Cache-Control ヘッダー**:

```typescript
// Next.js API Route
export default function handler(req, res) {
  res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400');
  res.json({ data });
}
```

### ブラウザキャッシュ

**静的リソース**:

```
Cache-Control: public, max-age=31536000, immutable
```

**HTMLページ**:

```
Cache-Control: public, max-age=3600, must-revalidate
```

**APIレスポンス**:

```
Cache-Control: no-cache, no-store, must-revalidate
```

### キャッシュ無効化戦略

**パターン1: Time-based Expiration（時間ベース）**

```php
Cache::put('key', $value, 600); // 10分で自動失効
```

**パターン2: Event-based Invalidation（イベントベース）**

```php
// 資産更新時にキャッシュクリア
public function update(Request $request, Asset $asset)
{
    $asset->update($request->all());

    Cache::forget("asset:{$asset->id}");
    Cache::tags(['assets'])->flush();
}
```

**パターン3: Cache Stampede対策**

```php
// 同時リクエストによるキャッシュスタンピード対策
Cache::lock("lock:asset:{$id}", 10)->get(function () use ($id) {
    return Cache::remember("asset:{$id}", 600, function () use ($id) {
        return Asset::find($id);
    });
});
```

## データベース最適化

### インデックス戦略

詳細は [database-design.md](database-design.md#インデックス設計) を参照。

**複合インデックス**:

```sql
-- 資産検索用
CREATE INDEX idx_assets_search ON assets(location_id, category_id, status);

-- 貸出履歴検索用
CREATE INDEX idx_lending_date_status ON lending_histories(borrowed_at, status);
```

**カバリングインデックス**:

```sql
-- よく使うカラムをインデックスに含める
CREATE INDEX idx_assets_list ON assets(location_id, status)
  INCLUDE (name, asset_code, category_id);
```

**パーシャルインデックス**:

```sql
-- 貸出中の資産のみインデックス
CREATE INDEX idx_assets_in_use ON assets(location_id)
  WHERE status = 'in_use';
```

### クエリ最適化

**EXPLAIN ANALYZE 使用**:

```sql
EXPLAIN ANALYZE
SELECT a.*, c.name as category_name
FROM assets a
INNER JOIN asset_categories c ON a.category_id = c.id
WHERE a.location_id = 1 AND a.status = 'available';
```

**インデックスヒント（必要時）**:

```php
// Eloquent: useIndex()は非推奨のため、生SQLで
DB::select('SELECT * FROM assets USE INDEX (idx_assets_search) WHERE ...');
```

**JOINの最適化**:

```php
// ❌ サブクエリ（遅い）
Asset::whereIn('id', function ($query) {
    $query->select('asset_id')->from('lending_histories')->where('status', 'borrowed');
})->get();

// ✅ JOIN（速い）
Asset::join('lending_histories', 'assets.id', '=', 'lending_histories.asset_id')
    ->where('lending_histories.status', 'borrowed')
    ->get();
```

### コネクションプール

**Laravel データベース接続設定**:

```php
// config/database.php
'connections' => [
    'pgsql' => [
        'driver' => 'pgsql',
        'host' => env('DB_HOST'),
        'port' => env('DB_PORT', '5432'),
        'database' => env('DB_DATABASE'),
        'username' => env('DB_USERNAME'),
        'password' => env('DB_PASSWORD'),
        'charset' => 'utf8',
        'prefix' => '',
        'prefix_indexes' => true,
        'schema' => 'public',
        'sslmode' => 'require',
        'pool' => [
            'min' => 2,
            'max' => 20, // 最大接続数
        ],
    ],
],
```

**pgBouncer使用（将来検討）**:
- コネクションプーリング専用ミドルウェア
- RDSの接続数を削減

### パーティショニング

**時系列データのパーティショニング（将来検討）**:

```sql
-- 貸出履歴を月ごとにパーティション
CREATE TABLE lending_histories (
    id BIGSERIAL,
    borrowed_at TIMESTAMP NOT NULL,
    ...
) PARTITION BY RANGE (borrowed_at);

CREATE TABLE lending_histories_2025_01 PARTITION OF lending_histories
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE lending_histories_2025_02 PARTITION OF lending_histories
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');
```

**パーティショニング基準**:
- 貸出履歴が10万件を超えたら導入を検討

## ネットワーク最適化

### CDN活用

**CloudFront 配信対象**:

| リソース | オリジン | キャッシュ戦略 |
|---------|---------|-------------|
| 静的JS/CSS | S3 | 1年キャッシュ |
| 画像 | S3 | 1年キャッシュ |
| API | ALB | キャッシュなし |
| HTML | ALB | 1時間キャッシュ |

**エッジロケーション最適化**:
- 日本のエッジロケーション優先
- 海外出張者のために全エッジロケーション有効

### HTTP/2・HTTP/3

**HTTP/2有効化**:
- ALBでHTTP/2自動有効
- 多重化による高速化
- ヘッダー圧縮

**HTTP/3（QUIC）検討**:
- CloudFrontでHTTP/3サポート
- 低遅延ネットワーク向け

### 圧縮

**Gzip圧縮**:

```nginx
# Next.js自動圧縮
# next.config.js
module.exports = {
  compress: true, // Gzip有効
};
```

**Brotli圧縮**:

```
Content-Encoding: br
```

- Gzipより高圧縮率
- Next.jsビルド時に事前圧縮

**圧縮率目標**:
- JavaScript: 70-80%削減
- CSS: 70-80%削減
- JSON: 60-70%削減

### 接続の再利用

**Keep-Alive設定**:

```
Connection: keep-alive
Keep-Alive: timeout=5, max=100
```

**HTTP/2多重化**:
- 同一接続で複数リクエスト
- 接続確立オーバーヘッド削減

## スケーリング戦略

### 水平スケーリング

**ECS Fargateタスク追加**:
- 負荷に応じてタスク数を増減
- ステートレス設計（セッションはRedis）
- タスク間でロードバランシング

**RDS リードレプリカ（将来）**:
- 読み取り負荷が高い場合
- レポート生成専用レプリカ

### 垂直スケーリング

**インスタンスサイズ変更**:

| リソース | 現在 | スケールアップ時 |
|---------|------|--------------|
| ECS CPU | 1 vCPU | 2 vCPU |
| ECS メモリ | 2 GB | 4 GB |
| RDS | db.t4g.medium | db.r6g.large |
| ElastiCache | cache.t4g.small | cache.r6g.medium |

**スケールアップ基準**:
- CPU使用率が継続的に70%超
- メモリ使用率が継続的に80%超

### オートスケーリング

**ECS Service Auto Scaling**:

| メトリクス | ターゲット | スケールアウト | スケールイン |
|----------|-----------|------------|-----------|
| CPU使用率 | 70% | タスク+1 | タスク-1 |
| メモリ使用率 | 80% | タスク+1 | タスク-1 |
| ALBリクエスト数/タスク | 1000 | タスク+1 | タスク-1 |

**スケーリングポリシー**:

```json
{
  "TargetTrackingScalingPolicyConfiguration": {
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ECSServiceAverageCPUUtilization"
    },
    "ScaleOutCooldown": 60,
    "ScaleInCooldown": 300
  }
}
```

## 非同期処理とキュー

### ジョブキュー設計

**Laravelキュー設定**:

```php
// config/queue.php
'connections' => [
    'redis' => [
        'driver' => 'redis',
        'connection' => 'default',
        'queue' => env('REDIS_QUEUE', 'default'),
        'retry_after' => 90,
        'block_for' => null,
    ],
],
```

**キュー種類**:

| キュー名 | 優先度 | 用途 | ワーカー数 |
|---------|-------|------|----------|
| `high` | 高 | メール送信、通知 | 3 |
| `default` | 中 | QRコード生成、レポート生成 | 2 |
| `low` | 低 | ログ集計、データクリーンアップ | 1 |

**ジョブ実装例**:

```php
// app/Jobs/GenerateQRCodeJob.php
class GenerateQRCodeJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public $tries = 3; // リトライ回数
    public $timeout = 120; // タイムアウト

    public function handle()
    {
        $qrCode = QrCode::format('png')
            ->size(300)
            ->generate($this->asset->asset_code);

        Storage::disk('s3')->put(
            "assets/qr-codes/{$this->asset->id}.png",
            $qrCode
        );

        $this->asset->update(['qr_code_url' => $url]);
    }

    public function failed(Exception $exception)
    {
        Log::error('QR code generation failed', [
            'asset_id' => $this->asset->id,
            'error' => $exception->getMessage(),
        ]);
    }
}
```

### バッチ処理

**Laravel Scheduler**:

```php
// app/Console/Kernel.php
protected function schedule(Schedule $schedule)
{
    // 毎日深夜3時に棚卸リマインダー送信
    $schedule->command('inventory:send-reminders')
        ->dailyAt('03:00')
        ->onOneServer();

    // 毎週月曜日にレポート生成
    $schedule->command('reports:weekly')
        ->weeklyOn(1, '04:00')
        ->onOneServer();

    // 1時間ごとにキャッシュクリーンアップ
    $schedule->command('cache:prune-stale-tags')
        ->hourly()
        ->onOneServer();
}
```

**バッチ処理のチャンク化**:

```php
// 大量データを分割処理
Asset::chunk(200, function ($assets) {
    foreach ($assets as $asset) {
        // 処理
    }
});
```

## パフォーマンス監視

### メトリクス収集

**CloudWatch メトリクス**:

| メトリクス | 説明 | アラート条件 |
|----------|------|------------|
| `ECSServiceAverageCPUUtilization` | ECS CPU使用率 | 80%超 |
| `ECSServiceAverageMemoryUtilization` | ECS メモリ使用率 | 80%超 |
| `TargetResponseTime` | ALBレスポンスタイム | 1秒超 |
| `HTTPCode_Target_5XX_Count` | 5xxエラー数 | 10件/5分超 |
| `DatabaseConnections` | RDS接続数 | 150超 |
| `CPUUtilization` (RDS) | RDS CPU使用率 | 70%超 |

**カスタムメトリクス**:

```php
// Laravel: CloudWatch Custom Metrics
use Aws\CloudWatch\CloudWatchClient;

$cloudwatch = new CloudWatchClient([...]);

$cloudwatch->putMetricData([
    'Namespace' => 'AssetManagement',
    'MetricData' => [
        [
            'MetricName' => 'AssetSearchLatency',
            'Value' => $latency,
            'Unit' => 'Milliseconds',
            'Timestamp' => time(),
        ],
    ],
]);
```

### APM導入

**Laravel Telescope（開発環境）**:

```bash
composer require laravel/telescope
php artisan telescope:install
```

- リクエストログ
- クエリログ
- ジョブログ
- キャッシュヒット率

**Sentry（エラートラッキング）**:

```php
// config/sentry.php
Sentry\captureException($exception);
```

**New Relic / Datadog（本番環境、検討中）**:
- APM（Application Performance Monitoring）
- 分散トレーシング
- リアルユーザーモニタリング

### ボトルネック分析

**分析ツール**:

| ツール | 用途 |
|-------|------|
| Laravel Telescope | 開発環境でのクエリ分析 |
| CloudWatch Logs Insights | ログ分析・クエリ |
| PostgreSQL `pg_stat_statements` | スロークエリ分析 |
| Chrome DevTools | フロントエンド分析 |
| Lighthouse | Webパフォーマンス測定 |

**スロークエリログ**:

```sql
-- PostgreSQL設定
log_min_duration_statement = 1000  -- 1秒以上のクエリをログ
```

**分析クエリ例**:

```sql
-- 最も遅いクエリTOP 10
SELECT
    query,
    mean_exec_time,
    calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

## 負荷テスト

### 負荷テストシナリオ

**JMeter / Locust 使用**:

**シナリオ1: 通常負荷**

| 操作 | 同時ユーザー数 | 継続時間 |
|-----|-------------|---------|
| ログイン | 10 | 30分 |
| 資産一覧表示 | 30 | 30分 |
| 資産検索 | 20 | 30分 |
| 資産詳細表示 | 40 | 30分 |
| 貸出申請 | 5 | 30分 |

**シナリオ2: ピーク負荷**

| 操作 | 同時ユーザー数 | 継続時間 |
|-----|-------------|---------|
| 全操作 | 100 | 10分 |

**シナリオ3: スパイクテスト**

```
ユーザー数
  100│     ┌─┐
     │     │ │
   50│┌────┘ └────┐
     ││           │
    0└┴───────────┴─> 時間
     0  5  10 15 20分
```

### 性能基準

**合格基準**:

| メトリクス | 目標 |
|----------|------|
| 平均レスポンスタイム | 500ms以下 |
| 95パーセンタイル | 1秒以下 |
| 99パーセンタイル | 2秒以下 |
| エラー率 | 0.1%以下 |
| スループット | 50 RPS以上 |

**負荷テスト実施タイミング**:
- リリース前（必須）
- インフラ変更時
- パフォーマンス改善後

## 最適化チェックリスト

**フロントエンド**:
- [ ] Next.js SSR/SSG適切に設定
- [ ] コード分割実施
- [ ] 画像最適化（WebP、遅延ロード）
- [ ] バンドルサイズ200KB以下
- [ ] Lighthouseスコア90以上

**バックエンド**:
- [ ] N+1問題なし（Eager Loading使用）
- [ ] ペジネーション実装
- [ ] 重い処理は非同期化
- [ ] APIレスポンス500ms以下

**キャッシュ**:
- [ ] Redis キャッシュ戦略実装
- [ ] CDNキャッシュ設定
- [ ] ブラウザキャッシュ設定
- [ ] キャッシュヒット率80%以上

**データベース**:
- [ ] インデックス適切に設定
- [ ] スロークエリなし（1秒以上）
- [ ] コネクションプール設定
- [ ] EXPLAIN ANALYZE で検証

**インフラ**:
- [ ] オートスケーリング設定
- [ ] ヘルスチェック正常動作
- [ ] ロードバランサー設定
- [ ] CDN有効化

**監視**:
- [ ] CloudWatch メトリクス設定
- [ ] アラート設定
- [ ] ログ収集設定
- [ ] ダッシュボード作成

## 関連ドキュメント

- [システムアーキテクチャ](system-architecture.md) - アプリケーション設計
- [インフラ構成](infrastructure.md) - AWS構成とスケーリング
- [データベース設計](database-design.md) - インデックス設計
- [技術スタック](technology-stack.md) - 使用技術
- [../01-requirements/non-functional-requirements.md](../01-requirements/non-functional-requirements.md) - パフォーマンス要件
