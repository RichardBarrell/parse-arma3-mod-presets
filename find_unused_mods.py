import sys
import json
from arma3_presets.parse import parse_arma3_mod_preset
from arma3_presets.print import measure_name_col_width, format_mod_line


usage = """
python3 find_unused_mods.py all_mods_preset.html mod_preset_1.html [mod_preset_2.html...]

prints output like:

mods in "all_mods_preset.html" but not any of the other presets:
    Large rats,    url: https://steamcommunity.com/sharedfiles/filedetails/?id=123
    Small rats,    url: https://steamcommunity.com/sharedfiles/filedetails/?id=456
---
"""


def main(filenames):
    with open(filenames[0], 'rb') as f:
        all_modlist = parse_arma3_mod_preset(f)

    for filename in filenames[1:]:
        with open(filename, 'rb') as f:
            modlist = parse_arma3_mod_preset(f)
        for mod_url in modlist.keys():
            if mod_url in all_modlist:
                del all_modlist[mod_url]

    if not all_modlist:
        print(f'There are no unused mods in {json.dumps(filenames[0])}')
        return

    print(f'mods in {json.dumps(filenames[0])} but not any of the other presets:')
    name_col_width = measure_name_col_width((all_modlist,))
    for mod_url, mod_name in all_modlist.items():
        print(format_mod_line(mod_url, mod_name, name_col_width))
    print('---\n')


if len(sys.argv) > 2:
    main(sys.argv[1:])
else:
    print(usage.strip())
