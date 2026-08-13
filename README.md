# Unhuman-Ru
Перевод игры на Русский.

## Переведено:
0/49

## Установка
- Заменить файл в `UNHUMAN/package.nw/lang`
- Включить Китайский Язык в настройках игры.

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

Скрипты полностью написаны локальной `Qwen 3.6 35B-A3B UD_Q4_K_XL`.
