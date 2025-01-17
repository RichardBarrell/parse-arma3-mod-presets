# parse-arma3-mod-presets

A set of utilities for parsing the mod preset HTML files that Arma 3 emits.

## How to get an Arma 3 mod preset HTML file

To create one of the HTML input files:

- open the Arma 3 launcher
- click "Mods" on the left
- at the top of the screen near the middle, click "...More"
- click "Export list of mods to a file..."
- save the HTML file somewhere

## Prerequisites

You will need Python 3. Any version >=3.10 will almost definitely work.
Older versions will probably work too but I haven't checked.
This code should work on any OS, including without limitation Windows, Linux and MacOS.

## How to use these programs:

To print the contents of a mod file to the terminal:

```
python3 print_arma3_mod_presets.py file1.html
```

Or to print the contents of several mod files to the terminal:

```
python3 print_arma3_mod_presets.py file1.html file2.html file3.html ...
```

To compare two mod preset files to see which files are in one but not the other:

```
python3 compare_arma3_mod_presets.py file1.html file2.html
```

To compare one mod preset file to a bunch of others, in order to check if there are any mods in it that don't appear in any of the other files, run:

```
python3 find_unused_mods.py all_mods_preset.html mod_preset_1.html [mod_preset_2.html...]
```
