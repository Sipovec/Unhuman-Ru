#!/usr/bin/env python3
# merge_i18n.py
import os
import glob
import argparse
import sys

def merge_i18n(parts_dir, output_path):
    # relative -> absolute path resolution
    parts_dir = os.path.join(os.path.dirname(os.path.abspath(parts_dir)), parts_dir)
    if not os.path.isdir(parts_dir):
        print(f"❌ Ошибка: Папка '{parts_dir}' не найдена.")
        sys.exit(1)

    # Собираем только part_*.js и сортируем лексикографически
    pattern = os.path.join(parts_dir, "part_*.js")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"❌ Ошибка: В папке '{parts_dir}' не найдено файлов part_*.js")
        sys.exit(1)

    with open(output_path, 'w', encoding='utf-8', newline='\n') as out_f:
        for fpath in files:
            with open(fpath, 'r', encoding='utf-8') as in_f:
                content = in_f.read()
                # Если последний символ не \n, добавляем его
                if content and not content.endswith('\n'):
                    content += '\n'
                out_f.write(content)

    print(f"✅ Готово. Собрано {len(files)} файлов в '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Сборка i18n частей обратно в один файл")
    parser.add_argument("-i", "--input-dir", default="parts", help="Папка с частями (по умолчанию: parts)")
    parser.add_argument("-o", "--output", default="merged_i18n.js", help="Путь выходного файла")
    args = parser.parse_args()
    merge_i18n(args.input_dir, args.output)
