def measure_name_col_width(modlists):
    longest_mod_name_length = 0
    for modlist in modlists:
        for mod_name in modlist.values():
            longest_mod_name_length = max(longest_mod_name_length, len(mod_name))
    return longest_mod_name_length + 1


def format_mod_line(mod_url, mod_name, name_col_width):
    name_col = f'{mod_name},'
    return f'    {name_col:{name_col_width}}    url: {mod_url}'