##### 修复flask-script在flask2.0以上版本的导入
```shell
sed -i "s/from flask._compat import text_type/from flask_script._compat import text_type/" $(pip show flask-script | awk 'NR==8{print}' | awk '{print $2}')/flask_script/__init__.py
```

##### cannot import name 'MigrateCommand' from 'flask_migrate'
```shell
pip install Flask-Migrate<=3.0.0
```