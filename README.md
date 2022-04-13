# auto-deriv
自動微分を二重数でしてみるライブラリ。

<!-- ### ブランチ戦略

Githubフローです。MR先はmasterブランチです。 -->

### 環境について
numpy があれば動く。推奨されていない `numpy.matrix` を使っているのでバージョンによっては今後動かなくなるかも。

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
他にもexpとかsinとかの微分も求まります([参照](https://github.com/somisawa/auto-deriv/blob/main/tests/test_deriv.py))。

### 原理
二重数を無理やり演算から実装してもいいですが，次の事実を用いました(証明してみよう)。

(命題)$\mathbb{R} / [x^2]$ という $\mathbb{R}$ -加群は $[[a + b, b],[-b, a - b]]$ ($a, b\in \mathbb{R}$)という行列全体のなす $\mathbb{R}$ -加群と同型

### テスト

[pytest](https://docs.pytest.org/en/latest/)を使います。テストは以下のように実行できます。

```shell
pipenv run pytest --doctest-modules
```
