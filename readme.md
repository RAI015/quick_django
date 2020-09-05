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

JSONファイルを使用して秘密データを隠す
https://riptutorial.com/ja/django/example/8734/json%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E7%A7%98%E5%AF%86%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E9%9A%A0%E3%81%99
