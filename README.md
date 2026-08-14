# Unhuman-Ru
Перевод игры на Русский Язык нейросетью.

## Переведено:
20/49

## Установка
1. Скачать `zh.js` из последнего [релиза](https://github.com/Sipovec/Unhuman-Ru/releases).
2. Заменить им файл в `UNHUMAN/package.nw/lang`.
3. Включить Китайский Язык в настройках игры `Options → Display → Language`.

## Файлы
- `zh.js` — Оригинальный файл с Китайским переводом из `UNHUMAN/package.nw/lang`
- `split_i18n.py` — разбивает файл на части в папку `parts`.
```cmd
python split_i18n.py zh.js
```

- `merge_i18n.py` собирает части обратно:
```cmd
python merge_i18n.py -i parts -o restored_dict.js
```

Скрипты написаны `Qwen 3.6 35B-A3B UD_Q4_K_XL`.
Перевод выполнен `Gemma 4 26B-A4B-it UD_Q4_K_XL`.
