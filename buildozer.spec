[app]

# (str) Nazwa twojej aplikacji
title = AlfaApp

# (str) Pakiet, w którym znajduje się twoja aplikacja
package.name = alfa_app

# (str) Nazwa pakietu w formie 'com.twoje.imie.nazwisko'
package.domain = com.twoje.imie.nazwisko

# (str) Wersja twojej aplikacji
package.version = 0.1

# (list) Wymagane zależności
requirements = python3==3.9.10,kivy,beautifulsoup4,requests

# (list) Pliki / katalogi do uwzględnienia (i do kopiowania do APK)
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png

# (list) Pliki / katalogi do uwzględnienia w archiwum
source.exclude_exts = pyc,pyo,pyd,db,json,png,jpg,jar,kv,atlas
source.exclude_patterns = images/*.xcf, .git/*

# (str) Plik główny kodu źródłowego
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png
source.exclude_exts = pyc,pyo,pyd,db,json,png,jpg,jar,kv,atlas
source.exclude_patterns = images/*.xcf, .git/*
source.main.filename = main.py

# (str) Katalog, w którym znajdują się pliki źródłowe
source.dir = .

# (str) Wersja Kivy
osx.python_version = 3.8.10
osx.kivy_version = 2.1.0
ios.kivy_version = 2.1.0
android.kivy_version = 2.1.0

# (list) Dodatkowe moduły do załączenia w archiwum
# Wymagane, jeśli używasz modułów spoza standardowej biblioteki Pythona
android.permissions = INTERNET

# (list) Wyłącz niektóre niepotrzebne opcje, które mogą spowodować błędy
# android.permissions = INTERNET

# (list) Architektury, na które kompilujemy (wspierane wartości: armeabi-v7a, arm64-v8a, x86, x86_64)
# Możesz usunąć niepotrzebne architektury, aby zmniejszyć rozmiar pliku APK
