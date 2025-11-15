# GitHub コミット規約

## 概要

このドキュメントは、チーム開発におけるGitHubのコミット規約を定義します。
一貫性のあるコミットメッセージにより、プロジェクトの変更履歴を理解しやすくし、自動化ツールとの連携を容易にします。

## コミットメッセージの形式

### 基本フォーマット

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 構成要素

#### 1. Type（必須）

変更の種類を表すプレフィックスです。以下のいずれかを使用してください：

| Type | 日本語 | 説明 | 使用例 |
|------|--------|------|--------|
| `feat` | 機能追加 | 新機能の追加 | ユーザー登録機能の実装 |
| `fix` | バグ修正 | バグの修正 | ログイン失敗時のエラー修正 |
| `docs` | ドキュメント | ドキュメントのみの変更 | READMEの更新 |
| `style` | スタイル | コードの意味に影響を与えない変更（空白、フォーマット、セミコロンなど） | インデントの修正 |
| `refactor` | リファクタリング | バグ修正や機能追加を伴わないコードの変更 | 関数の分割、変数名の変更 |
| `perf` | パフォーマンス | パフォーマンスを向上させるコード変更 | データベースクエリの最適化 |
| `test` | テスト | テストの追加や既存テストの修正 | ユニットテストの追加 |
| `build` | ビルド | ビルドシステムや外部依存関係に影響する変更 | webpackの設定変更 |
| `ci` | CI | CI設定ファイルとスクリプトの変更 | GitHub Actionsの設定 |
| `chore` | 雑務 | その他の変更（ソースやテストの変更を含まない） | .gitignoreの更新 |
| `revert` | 取り消し | 以前のコミットを取り消す | コミットのrevert |

#### 2. Scope（任意）

変更の影響範囲を括弧内に記載します。プロジェクトに応じて定義してください。

例：
- `feat(auth): ログイン機能を実装`
- `fix(api): ユーザー取得APIのエラー修正`
- `docs(readme): インストール手順を追加`

#### 3. Subject（必須）

変更の簡潔な説明です。以下のルールに従ってください：

- **50文字以内**で記載
- **現在形・命令形**で記載（「〜を追加」「〜を修正」）
- 文末に句点（。）を**付けない**
- **何を**変更したか、**なぜ**変更したかを明確に記載

#### 4. Body（任意）

より詳細な説明が必要な場合に記載します：

- Subject行から**1行空けて**記載
- **72文字**で改行
- **なぜ**この変更が必要だったかを説明
- 以前の動作と変更後の動作を比較

#### 5. Footer（任意）

以下の情報を記載します：

- **Breaking Changes**: 破壊的変更がある場合は`BREAKING CHANGE:`で始める
- **Issue参照**: 関連するIssueがある場合は`Closes #123`、`Fixes #456`の形式で記載
- **Co-authored-by**: 共同作業者がいる場合は記載

## コミットメッセージの例

### 基本的な例

```
feat: ユーザープロフィール編集機能を追加
```

### スコープ付きの例

```
fix(auth): ログイン失敗時のエラーメッセージを修正

ユーザー名が間違っている場合とパスワードが間違っている場合で
同じエラーメッセージが表示されていた問題を修正。
セキュリティの観点から、両方とも「認証に失敗しました」と表示するように統一。

Closes #234
```

### 破壊的変更を含む例

```
refactor(api)!: APIのレスポンス形式を変更

従来のフラットなJSON形式から、ネストした構造に変更。
これにより、関連データを効率的に取得できるようになります。

BREAKING CHANGE: APIレスポンスの形式が変更されました。
クライアント側のデータ取得処理を更新する必要があります。

移行ガイド：
- response.user_name → response.user.name
- response.user_email → response.user.email
```

### 複数の変更を含む例

```
feat(dashboard): ダッシュボードに統計グラフを追加

- 日別アクセス数のグラフを実装
- ユーザー登録数の推移を表示
- データのエクスポート機能を追加

Chart.jsライブラリを使用して実装。
パフォーマンスを考慮し、データは非同期で取得。

Fixes #123, #124
Co-authored-by: Tanaka Taro <tanaka@example.com>
```

## コミットのベストプラクティス

### 1. アトミックなコミット

- **1つのコミット = 1つの論理的な変更**
- 複数の独立した変更を1つのコミットにまとめない
- レビューしやすい適切な粒度を保つ

### 2. 頻繁なコミット

- 作業の区切りごとにコミット
- WIP（Work In Progress）コミットは後でsquashする
- 大きな変更は段階的にコミット

### 3. テストを通してからコミット

- コミット前に必ず関連テストを実行
- ビルドが通ることを確認
- Linterやフォーマッターを実行

### 4. コミット前のセルフレビュー

- `git diff --staged`で変更内容を確認
- 不要なデバッグコードが含まれていないか確認
- 機密情報が含まれていないか確認

## プルリクエストのルール

### タイトル

プルリクエストのタイトルは、マージコミットのメッセージになることを考慮して記載：

```
feat(auth): OAuth2.0認証機能を実装 (#PR番号)
```

### 説明

以下のテンプレートを使用：

```markdown
## 概要
この変更の目的と概要を記載

## 変更内容
- 変更点1
- 変更点2
- 変更点3

## テスト方法
1. テスト手順1
2. テスト手順2
3. 期待される結果

## スクリーンショット（UIの変更がある場合）
変更前：
変更後：

## チェックリスト
- [ ] テストを実行し、すべて成功することを確認
- [ ] ドキュメントを更新（必要な場合）
- [ ] 破壊的変更がない（ある場合はBREAKING CHANGEを記載）
- [ ] レビュー依頼前にセルフレビューを実施

## 関連Issue
Closes #xxx
```

## ブランチ戦略

### ブランチ命名規則

```
<type>/<issue番号>-<簡潔な説明>
```

例：
- `feat/123-user-profile`
- `fix/456-login-error`
- `docs/789-api-reference`

### 主要ブランチ

- **main/master**: プロダクション環境
- **develop**: 開発環境（開発中の最新版）
- **feature/**: 新機能開発用
- **fix/**: バグ修正用
- **hotfix/**: 緊急修正用
- **release/**: リリース準備用

## Git フックの活用

### commit-msg フック

コミットメッセージが規約に従っているか自動チェック：

```bash
#!/bin/sh
# .gitmessage に従ったフォーマットチェック
commit_regex='^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?: .{1,50}'

if ! grep -qE "$commit_regex" "$1"; then
    echo "コミットメッセージが規約に従っていません。"
    echo "形式: <type>(<scope>): <subject>"
    exit 1
fi
```

### pre-commit フック

コミット前の自動チェック：
- Linterの実行
- フォーマッターの実行
- テストの実行

## 便利なGitコマンド

### よく使うコマンド

```bash
# 直前のコミットメッセージを修正
git commit --amend

# インタラクティブなリベース（コミット整理）
git rebase -i HEAD~3

# 特定のコミットを取り消し（履歴は残る）
git revert <commit-hash>

# ステージングを取り消し
git reset HEAD <file>

# 作業中の変更を一時退避
git stash
git stash pop
```

### エイリアス設定例

```bash
# ~/.gitconfig に追加
[alias]
    st = status
    co = checkout
    br = branch
    cm = commit
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

## 参考資料

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)
- [Git Documentation](https://git-scm.com/doc)

## 改訂履歴

このドキュメントの変更履歴はGitのコミット履歴で管理されます。
`git log -- docs/00-rules/github-commit-rules.md`で確認してください。