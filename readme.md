## フィクスチャ

データベースからデータを出力したい場合、以下のコマンドでフィクスチャを自動生成できるが、
```
python manage.py dumpdata --format yaml --output book.yaml main.book
```
とすると、```ModuleNotFoundError: No module named 'yaml'```とエラーが出る為、
```pip install pyyaml```コマンドで、PyYAMLをインストールする必要がある。

また、拡張子を```.yml```とすると、```CommandError: Problem installing fixture 'initial_data': yml is not a known serialization format.```
とエラーが出てしまうので、拡張子は.yamlを使用する必要がある。

https://djangobrothers.com/blogs/fixture/

