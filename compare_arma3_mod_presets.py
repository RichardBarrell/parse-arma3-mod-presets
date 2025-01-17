import sys
import json
from arma3_presets.parse import parse_arma3_mod_preset
from arma3_presets.print import measure_name_col_width, format_mod_line

usage = """
python3 compare_arma3_mod_presets.py file1.html file2.html

prints output like:

mods in "file1.html" but not "file2.html":
    Large rats,    url: https://steamcommunity.com/sharedfiles/filedetails/?id=123
---

mods in "file2.html" but not "file1.html":
    Small rats,    url: https://steamcommunity.com/sharedfiles/filedetails/?id=456
---
"""


def main(filenames):
    name_to_modlist = {}
    for filename in filenames:
        with open(filename, 'rb') as f:
            modlist = parse_arma3_mod_preset(f)
        name_to_modlist[filename] = modlist

    name_col_width = measure_name_col_width(name_to_modlist.values())
    first_name = filenames[0]
    first_modlist = name_to_modlist[first_name]

    for second_name in filenames[1:]:
        second_modlist = name_to_modlist[second_name]
        mods_only_in_first_modlist = []
        mods_only_in_second_modlist = []
        for mod_url, mod_name in first_modlist.items():
            if mod_url not in second_modlist:
                mods_only_in_first_modlist.append((mod_url, mod_name))
        for mod_url, mod_name in second_modlist.items():
            if mod_url not in first_modlist:
                mods_only_in_second_modlist.append((mod_url, mod_name))

        if mods_only_in_first_modlist:
            print(f'mods in {json.dumps(first_name)} but not {json.dumps(second_name)}:')
            for mod_url, mod_name in mods_only_in_first_modlist:
                print(format_mod_line(mod_url, mod_name, name_col_width))
            print('---\n')

        if mods_only_in_second_modlist:
            print(f'mods in {json.dumps(second_name)} but not {json.dumps(first_name)}:')
            for mod_url, mod_name in mods_only_in_second_modlist:
                print(format_mod_line(mod_url, mod_name, name_col_width))
            print('---\n')

if len(sys.argv) > 1:
    main(sys.argv[1:])
else:
    print(usage.strip())
