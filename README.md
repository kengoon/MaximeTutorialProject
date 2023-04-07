# Kivy and KivyMD installation procedure

```shell
python -m pip install https://github.com/kivymd/KivyMD/archive/refs/heads/master.zip -U -I --no-deps
python -m pip install kivy --pre --no-deps --index-url  https://kivy.org/downloads/simple/
python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/
```