from pywikibot import Site, Page, User
import mwparserfromhell as mwp

def main():
    site = Site('en', 'wikipedia')
    for rfa in rfas(site):
        user = User(site, rfa)
        for entry in site.logevents(page=user, logtype="block"):
            if entry['action'] != 'unblock':
                print(f"# {user.title()} [https://en.wikipedia.org/w/index.php?title=Special:Log&logid={entry['logid']} {entry.timestamp()}] ({entry.duration() or 'indef'}) <nowiki>{entry['comment']}</nowiki>")


def rfas(site):
    for year in range(2003, 2024):
        index_page = Page(site, f'Wikipedia:Successful requests for adminship/{year}')
        wikicode = mwp.parse(index_page.text)
        for row in wikicode.filter_templates(matches=lambda t: t.name.matches("rfarow")):
            user = row.params[0]
            yield user



if __name__ == "__main__":
    main()
