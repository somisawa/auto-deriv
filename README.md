# auto-deriv
## 開発手順

<!-- ### ブランチ戦略

Githubフローです。MR先はmasterブランチです。 -->

### 開発環境構築

[pipenv](https://github.com/pypa/pipenv) で環境を作成します。pipenv の使い方は[公式ドキュメント](https://pipenv-ja.readthedocs.io/ja/translate-ja/)を参照してください。

```shell
pip install pipenv
export PIPENV_VENV_IN_PROJECT=true # .bashrc に書いておくと良い
pipenv install --dev
```

### 利用方法
有理関数を定義します。
```python
def f(x): return x ** 2 + x
```
このx = 2における微分は次のように計算できます。
```python
deriv(f, 2) # 5
```

### テスト

[pytest](https://docs.pytest.org/en/latest/)を使います。テストは以下のように実行できます。

```shell
pipenv run pytest --doctest-modules
```

### mypy による型チェック

```bash
mypy server --config-file mypy.ini
```

### mypy Daemon を利用する場合

繰り返す場合はより高速．

```bash
dmypy run -- server --config-file mypy.ini --follow-imports=skip
```

<!-- ### スタイルチェック

[mypy](http://www.mypy-lang.org/), [black](https://github.com/psf/black) などでテストします。`bin/lint`でまとめて実行できます。

```shell
bin/lint
``` -->
<!-- 
### リリース

マージ後、担当者は以下の手順でリリースします。

**1. setup.cfg のバージョンを更新**

`setup.cfg` 関数の引数のバージョンを更新します。

```diff
  [metadata]
  name = hoge
- version = 1.4.0
+ version = 1.5.0
```

変更をコミットし push してください。

```shell
$ git commit -m "バージョン 1.5.0" setup.cfg
$ git push
```

**2. バージョンタグの追加**

`setup` と同じバージョン番号のタグを作ってください。

```shell
$ git tag 1.5.0
$ git push --tag
```

**3. 社内PyPIへのデプロイ**

ローカルマシンで `setup.py` を実行して公開物をビルドします。

```shell
$ pipenv run python setup.py sdist
```

[twine](https://twine.readthedocs.io/en/latest/)を使って社内PyPIにデプロイします。環境変数を定義し忘れると公式PyPIに公開されるかもしれないので注意。

```shell
$ export TWINE_REPOSITORY_URL=https://packages.example.com/repository/pypi-internal/
$ export TWINE_USERNAME=ore-boku # LDAPユーザー名
$ pipenv run twine upload dist/hoge-1.5.0.tar.gz # 公開物を指定して実行
```

**4. リリース連絡**

社内Slackで連絡してください。

```
各位

hoge のバージョン 1.0.0 をリリースしました。以下の機能を追加しています：

- 機能の説明
- 機能の説明
- 機能の説明

なお、後方互換性を崩す変更は加えていません。

アップデートは、各チームごとに影響を判断した上で、以下のコマンドで行なってください。

pip install --upgrade hoge==1.0.0
``` -->
