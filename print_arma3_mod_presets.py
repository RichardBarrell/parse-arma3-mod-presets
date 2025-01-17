import sys
import json
from arma3_presets.parse import parse_arma3_mod_preset
from arma3_presets.print import measure_name_col_width, format_mod_line


usage = """
python3 print_arma3_mod_presets.py file1.html [file2.html...]

prints output like:

mods in "file1.html":
    Large rats,    url: https://steamcommunity.com/sharedfiles/filedetails/?id=123
---
"""


def main(filenames):
    for filename in filenames:
        with open(filename, 'rb') as f:
            modlist = parse_arma3_mod_preset(f)
        name_col_width = measure_name_col_width((modlist,))
        print(f'mods in {json.dumps(filename)}:')
        for mod_url, mod_name in modlist.items():
            print(format_mod_line(mod_url, mod_name, name_col_width))
        print('---\n')


if len(sys.argv) > 1:
    main(sys.argv[1:])
else:
    print(usage.strip())
