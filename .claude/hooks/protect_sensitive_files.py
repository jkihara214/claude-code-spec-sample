#!/usr/bin/env python3
import sys
import json
import os
from pathlib import Path
from fnmatch import fnmatch

def load_settings():
    """グローバルとプロジェクトローカルの両方からClaude設定を読み込み、denyパターンをマージする"""
    deny_patterns = []

    # グローバル設定の読み込み
    global_settings_path = Path.home() / '.claude' / 'settings.json'
    # print(f"[DEBUG] グローバル設定パス: {global_settings_path}", file=sys.stderr)  # [DEBUG]
    try:
        with open(global_settings_path) as f:
            settings = json.load(f)
            global_deny = settings.get('permissions', {}).get('deny', [])
            # print(f"[DEBUG] グローバル設定から読み込んだdenyパターン数: {len(global_deny)}", file=sys.stderr)  # [DEBUG]
            deny_patterns.extend(global_deny)
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        # print(f"[DEBUG] グローバル設定の読み込み失敗: {e}", file=sys.stderr)  # [DEBUG]
        pass

    # プロジェクトローカル設定の読み込み
    project_dir = os.getenv('CLAUDE_PROJECT_DIR')
    # print(f"[DEBUG] CLAUDE_PROJECT_DIR: {project_dir}", file=sys.stderr)  # [DEBUG]
    if project_dir:
        project_settings_path = Path(project_dir) / '.claude' / 'settings.json'
        # print(f"[DEBUG] プロジェクト設定パス: {project_settings_path}", file=sys.stderr)  # [DEBUG]
        try:
            with open(project_settings_path) as f:
                settings = json.load(f)
                project_deny = settings.get('permissions', {}).get('deny', [])
                # print(f"[DEBUG] プロジェクト設定から読み込んだdenyパターン数: {len(project_deny)}", file=sys.stderr)  # [DEBUG]
                deny_patterns.extend(project_deny)
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            # print(f"[DEBUG] プロジェクト設定の読み込み失敗: {e}", file=sys.stderr)  # [DEBUG]
            pass

    # print(f"[DEBUG] マージ後の全denyパターン数: {len(deny_patterns)}", file=sys.stderr)  # [DEBUG]
    # print(f"[DEBUG] 全denyパターン: {deny_patterns}", file=sys.stderr)  # [DEBUG]
    return deny_patterns

def extract_pattern(deny_rule):
    """'Read(./path/pattern)'や'Bash(cat .env)'のようなdenyルールからパターンを抽出する"""
    # Read, Write, Edit, MultiEdit, Bash に対応
    for tool in ['Read(', 'Write(', 'Edit(', 'MultiEdit(', 'Bash(']:
        if deny_rule.startswith(tool) and deny_rule.endswith(')'):
            pattern = deny_rule[len(tool):-1]  # ツール名と括弧を削除
            tool_name = tool[:-1]  # 括弧を削除してツール名を取得
            # print(f"[DEBUG] ツール '{tool_name}' のパターン抽出成功: {pattern}", file=sys.stderr)  # [DEBUG]
            return (tool_name, pattern)
    return (None, None)

def matches_file_pattern(file_path, pattern):
    """ファイルパスがdenyパターンに一致するかチェックする"""
    file_path = str(file_path)
    file_name = os.path.basename(file_path)

    # 相対パターンを絶対パスで動作するように変換
    if pattern.startswith('./'):
        # './local/**' のようなパターンの場合、パスの任意の部分が一致するかチェック
        pattern = pattern[2:]  # './' を削除
        # パスの任意のサフィックスがパターンに一致するかチェック
        path_parts = file_path.split('/')
        for i in range(len(path_parts)):
            partial_path = '/'.join(path_parts[i:])
            if fnmatch(partial_path, pattern):
                return True
    else:
        # 直接パターンマッチング（フルパス）
        if fnmatch(file_path, pattern):
            return True
        # ファイル名のみでもマッチング（.env*, *.key などのパターン用）
        if fnmatch(file_name, pattern):
            return True

    return False

def matches_bash_pattern(command, pattern):
    """
    Bashコマンドがdenyパターンに一致するかチェックする

    パターン形式:
    - 'sudo:*' → sudo で始まるコマンド
    - 'rm:*' → rm で始まるコマンド
    - 'chmod 777 :*' → chmod 777 を含むコマンド
    - 'find :* -delete::*' → find で始まり、かつ -delete を含むコマンド（複合条件）

    ワイルドカード:
    - ':*' → 任意の引数（スペース区切り）
    - '::*' → それ以降の任意の内容
    """
    import re

    command = command.strip()

    # パターンを正規表現に変換
    regex_pattern = pattern

    # ステップ1: ワイルドカードをユニークなプレースホルダーに置換
    DOUBLE_WILDCARD_PLACEHOLDER = '\x00DOUBLE\x00'
    SINGLE_WILDCARD_PLACEHOLDER = '\x00SINGLE\x00'

    regex_pattern = regex_pattern.replace('::*', DOUBLE_WILDCARD_PLACEHOLDER)
    regex_pattern = regex_pattern.replace(':*', SINGLE_WILDCARD_PLACEHOLDER)

    # ステップ2: 正規表現の特殊文字をエスケープ
    regex_pattern = re.escape(regex_pattern)

    # ステップ3: エスケープされたプレースホルダーを取得
    escaped_double = re.escape(DOUBLE_WILDCARD_PLACEHOLDER)
    escaped_single = re.escape(SINGLE_WILDCARD_PLACEHOLDER)

    # ステップ4: プレースホルダーを正規表現に戻す
    # ::* を置換
    regex_pattern = regex_pattern.replace(escaped_double, r'.*')

    # :* の置換（文脈に応じて変える）
    # 末尾にある場合はオプション、途中にある場合は必須
    parts = regex_pattern.split(escaped_single)
    result = parts[0]
    for i in range(1, len(parts)):
        next_part = parts[i]

        # 前のパートの末尾と次のパートの先頭のエスケープされたスペースを削除
        if result.endswith('\\ '):
            result = result[:-2]  # 末尾の \ と空白を削除
        if next_part.startswith('\\ '):
            next_part = next_part[2:]  # 先頭の \ と空白を削除

        # 末尾かどうかをチェック
        if i == len(parts) - 1 and next_part.strip() == '':
            # 末尾の場合：オプション（あってもなくてもいい）
            result += r'(\s.*)?'
        else:
            # 途中の場合：必須（スペース + 任意の文字列 + 次のパターンの前まで）
            result += r'\s+.*?'

        result += next_part
    regex_pattern = result

    # コマンドの先頭からマッチングする
    regex_pattern = '^' + regex_pattern

    # print(f"[DEBUG] 変換後の正規表現パターン: {regex_pattern}", file=sys.stderr)

    # 正規表現をコンパイルしてマッチング
    try:
        pattern_re = re.compile(regex_pattern)
        match = pattern_re.match(command)
        if match:
            return True
    except re.error as e:
        # 正規表現エラーの場合、フォールバックとして単純なマッチングを行う
        # print(f"[DEBUG] 正規表現エラー: {e}, パターン: {regex_pattern}", file=sys.stderr)
        # フォールバック: 単純な文字列マッチング
        if pattern.endswith(':*'):
            command_name = pattern[:-2].strip()
            if command.startswith(command_name):
                if len(command) == len(command_name) or command[len(command_name)].isspace():
                    return True

    return False

def main():
    """
    フック入力を処理し、機密ファイルへのアクセスをチェックするメイン関数
    """
    try:
        # Claude Codeからstdin経由で渡されたJSONデータを読み込む
        data = json.load(sys.stdin)
        # print(f"[DEBUG] 受信したデータ: {json.dumps(data, indent=2)}", file=sys.stderr)  # [DEBUG]
        tool_input = data.get('tool_input', {})
        tool_name = data.get('tool_name')
        # print(f"[DEBUG] tool_name: {tool_name}", file=sys.stderr)  # [DEBUG]
        # print(f"[DEBUG] tool_input: {tool_input}", file=sys.stderr)  # [DEBUG]

        file_path_str = tool_input.get('file_path')
        command_str = tool_input.get('command')

        # print(f"[DEBUG] チェック対象のファイルパス: {file_path_str}", file=sys.stderr)  # [DEBUG]
        # print(f"[DEBUG] チェック対象のコマンド: {command_str}", file=sys.stderr)  # [DEBUG]

        # ファイルパスもコマンドもない場合は終了
        if not file_path_str and not command_str:
            # print("[DEBUG] ファイルパスもコマンドもなし - フック終了", file=sys.stderr)  # [DEBUG]
            sys.exit(0)

        # 設定からdenyパターンを読み込む
        deny_rules = load_settings()

        # ファイルパスのチェック
        if file_path_str:
            file_path = Path(file_path_str)
            # print(f"[DEBUG] ファイルパスのパターンマッチング開始", file=sys.stderr)  # [DEBUG]
            for rule in deny_rules:
                deny_tool, pattern = extract_pattern(rule)
                if deny_tool and deny_tool != 'Bash' and pattern:
                    # print(f"[DEBUG] ルール '{rule}' から抽出したパターン: {pattern}", file=sys.stderr)  # [DEBUG]
                    if matches_file_pattern(file_path, pattern):
                        # print(f"[DEBUG] *** マッチ検出! *** パターン '{pattern}' がファイル '{file_path}' に一致", file=sys.stderr)  # [DEBUG]
                        # LLMに対して明確で教育的なエラーメッセージを構築
                        error_message = (
                            f"\nセキュリティポリシー違反: '{file_path}' へのアクセスは拒否ルール {rule} によってブロックされました\n"
                            f"理由: このファイルはClaude settings.jsonの拒否リストのパターンに一致しています\n"
                            "対処: 拒否されたパス内のファイルには機密情報が含まれているため、AIによるアクセスは許可されません\n"
                            "      必要な場合は、ユーザー自身が直接ファイルを確認・編集してください"
                        )

                        # エラーメッセージをstderrに出力
                        print(error_message, file=sys.stderr)

                        # 終了コード2でツールをブロックし、stderrをClaudeにフィードバック
                        sys.exit(2)
                    # else:
                        # print(f"[DEBUG] マッチなし - 次のルールへ", file=sys.stderr)  # [DEBUG]

        # Bashコマンドのチェック
        if command_str and tool_name == 'Bash':
            # print(f"[DEBUG] Bashコマンドのパターンマッチング開始", file=sys.stderr)  # [DEBUG]
            for rule in deny_rules:
                deny_tool, pattern = extract_pattern(rule)
                if deny_tool == 'Bash' and pattern:
                    # print(f"[DEBUG] ルール '{rule}' から抽出したパターン: {pattern}", file=sys.stderr)  # [DEBUG]
                    if matches_bash_pattern(command_str, pattern):
                        # print(f"[DEBUG] *** マッチ検出! *** パターン '{pattern}' がコマンド '{command_str}' に一致", file=sys.stderr)  # [DEBUG]
                        # LLMに対して明確で教育的なエラーメッセージを構築
                        error_message = (
                            f"\nセキュリティポリシー違反: コマンド '{command_str}' は拒否ルール {rule} によってブロックされました\n"
                            f"理由: このコマンドはClaude settings.jsonの拒否リストのパターンに一致しています\n"
                            "対処: 拒否されたコマンドには危険な操作や機密情報へのアクセスが含まれているため、AIによる実行は許可されません\n"
                            "      必要な場合は、ユーザー自身が直接ターミナルでコマンドを実行してください"
                        )

                        # エラーメッセージをstderrに出力
                        print(error_message, file=sys.stderr)

                        # 終了コード2でツールをブロックし、stderrをClaudeにフィードバック
                        sys.exit(2)
                    # else:
                        # print(f"[DEBUG] マッチなし - 次のルールへ", file=sys.stderr)  # [DEBUG]

    except (json.JSONDecodeError, KeyError) as e:
        # 入力データの潜在的なエラーを処理
        # print(f"[DEBUG] エラー発生: {e}", file=sys.stderr)  # [DEBUG]
        print(f"フック入力の処理中にエラーが発生しました: {e}", file=sys.stderr)
        # ブロックしない終了コード
        sys.exit(1)

    # 機密ファイルが検出されなかった場合、0で終了してアクションを許可
    # print(f"[DEBUG] すべてのパターンチェック完了 - アクセス許可", file=sys.stderr)  # [DEBUG]
    sys.exit(0)

if __name__ == "__main__":
    main()