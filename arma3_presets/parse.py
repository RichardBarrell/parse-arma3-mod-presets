from html.parser import HTMLParser


class ArmaModPresetParser(HTMLParser):
    on_mod_discovered = lambda mod_url, mod_name: None
    in_a = False
    in_name_td = False
    the_mod_name = None
    the_a_url = None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.in_a = True
        if tag == 'td' and dict(attrs).get('data-type', None) == 'DisplayName':
            self.in_name_td = True

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_a:
            self.in_a = False
        if tag == 'td':
            self.in_name_td = False
        if self.the_a_url and self.the_mod_name:
            self.on_mod_discovered(self.the_a_url, self.the_mod_name)
            self.the_a_url = None
            self.the_mod_name = None

    def handle_data(self, data):
        if self.in_a:
            self.the_a_url = data
        if self.in_name_td:
            self.the_mod_name = data


def parse_arma3_mod_preset(input_file):
    content_str = input_file.read().decode('utf-8')
    parser = ArmaModPresetParser()
    modlist = []
    def handle_mod_discovery(mod_url, mod_name):
        modlist.append((mod_name, mod_url))
    parser.on_mod_discovered = handle_mod_discovery
    parser.feed(content_str)
    parser.close()
    modlist.sort(key=lambda x: (x[0].casefold(), x[0], x[1]))
    return {mod_url: mod_name for mod_name, mod_url in modlist}
