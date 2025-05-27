import re
import sys
import csv
import time
from pathlib import Path
from urllib.request import urlopen
from tqdm import tqdm
from markdownify import markdownify

BANNER_OFFSETS = {"Acquisitions-Incorporated": 0.4,
                  "Baldurs-Gate-Descent-Into-Avernus": 0.8,
                  "Candlekeep-Mysteries": 0.5,
                  "Critical-Role": 0.0,
                  "Critical-Role-Call-Of-The-Netherdeep": 0.5,
                  "Curse-Of-Strahd": 1.0,
                  "Dragonlance-Shadow-Of-The-Dragon-Queen": 0.6,
                  "Dungeon-Masters-Guide": 0.4,
                  "Eberron-Rising-From-The-Last-War": 0.3,
                  "Wayfinders-Guide-To-Eberron": 0.0,
                  "Divine-Contention": 0.4,
                  "Sleeping-Dragons-Wake": 0.4,
                  "Explorers-Guide-To-Wildemount": 0.45,
                  "Fizbans-Treasury-Of-Dragons": 0.56,
                  "Ghosts-Of-Saltmarsh": 0.0,
                  "Guildmasters-Guide-To-Ravnica": 0.0,
                  "Icewind-Dale-Rime-Of-The-Frostmaiden": 0.0,
                  "Infernal-Machine-Rebuild": 0.5,
                  "Journeys-Through-The-Radiant-Citadel": 0.3,
                  "Keys-From-The-Golden-Vault": 0.1,
                  "Legends-Of-Runeterra-Dark-Tides-Of-Bilgewater": 0.7,
                  "Lost-Laboratory-Of-Kwalish": 0.0,
                  "Lost-Mine-Of-Phandelver": 0.7,
                  "Mythic-Odysseys-Of-Theros": 0.0,
                  "Out-Of-The-Abyss": 0.0,
                  "Princes-Of-The-Apocalypse": 0.2,
                  "Spelljammer-Adventures-In-Space-Boos-Astral-Menagerie": 0.4,
                  "Spelljammer-Adventures-In-Space-Astral-Adventurers-Guide": 0.4,
                  "Storm-Kings-Thunder": 0.2,
                  "Strixhaven-A-Curriculum-Of-Chaos": 0.4,
                  "Sword-Coast-Adventurers-Guide": 0.0,
                  "Taldorei-Campaign-Setting-Reborn": 0.0,
                  "Taldorei-Campaign-Guide-Reborn": 0.0,
                  "Tales-From-The-Yawning-Portal": 0.5,
                  "Tashas-Cauldron-Of-Everything": 0.3,
                  "The-Rise-Of-Tiamat": 0.2,
                  "The-Wild-Beyond-The-Witchlight": 0.3,
                  "Tomb-Of-Annihilation": 0.3,
                  "Tyranny-Of-Dragons": 0.3,
                  "Van-Richtens-Guide-To-Ravenloft": 0.3,
                  "Volos-Guide-To-Monsters": 0.3,
                  "Waterdeep-Dragon-Heist": 0.3,
                  "Waterdeep-Dungeon-Of-The-Mad-Mage": 0.2,
                  "Xanathars-Guide-To-Everything": 0.5,
                  "Players-Handbook": 0.3,
                  "Unearthed-Arcana": 0.0,
                  "Elemental-Evil-Players-Companion": 0.0,
                  "Acquisitions-Inc": 0.0
                  }

SOURCE_ACRONYMS ={
    "AI":"Acquisitions Incorporated",
    "BGDIA": "Baldur's Gate - Descent into Avernus",
    "BGG": "Bigby Presents - Glory of the Giants",
    "BAM": "Spelljammer - Adventures In Space",
    "CM": "Candlekeep Mysteries",
    "CRCotN": "Critical Role - Call of the Netherdeep",
    "CoS": "Curse of Strahd",
    "DC": "Divine Contention",
    "DIP": "Dragon of Icespire Peak",
    "DMG": "Dungeon Master's Guide",
    "DSotDQ": "Dragonlance - Shadow of the Dragon Queen",
    "DoSI": "Dragons of Stormwreck Isle",
    "EGW": "Explorer's Guide to Wildemount",
    "ERLW": "Eberron - Rising from the Last War",
    "ESK": "Essentials Kit",
    "FTD": "Fizban's Treasury of Dragons",
    "GGR": "Guildmaster's Guide to Ravnica",
    "GoS": "Ghosts of Saltmarsh",
    "HftT": "Hunt for the Thessalhydra",
    "HoL": "The House of Lament",
    "HotDQ": "Hoard of the Dragon Queen",
    "IDRotF": "Icewind Dale - Rime of the Frostmaiden",
    "JttRC": "Journeys through the Radiant Citadel",
    "KKW": "Krenko's Way",
    "KftGV": "Keys from the Golden Vault",
    "LMoP": "Lost Mine of Phandelver",
    "LoX": "Light of Xaryxis",
    "MM": "Monster Manual",
    "MOT": "Mythic Odysseys of Theros",
    "MPMM": "Mordenkainen Presents - Monsters of the Multiverse",
    "MPP": "Morte's Planar Parade",
    "MTF": "Mordenkainen's Tome of Foes",
    "OoW": "The Orrery of the Wanderer",
    "OotA": "Out of the Abyss",
    "PHB": "Player's Handbook",
    "PaBTSO": "Phandelver and Below - The Shattered Obelisk",
    "PotA": "Princes of the Apocalypse",
    "RMBRE": "The Lost Dungeon of Rickedness - Big Rick Energy",
    "RoT": "The Rise of Tiamat",
    "SCC": "Strixhaven - A Curriculum of Chaos",
    "SDW": "Sleeping Dragon's Wake",
    "SKT": "Storm King's Thunder",
    "SLW": "Storm Lord's Wrath",
    "TCE": "Tasha's Cauldron of Everything",
    "TDCSR": "Tal'Dorei Campaign Setting Reborn",
    "TftYP": "Tales from the Yawning Portal",
    "ToA": "Tomb of Annihilation",
    "ToFW": "Turn of Fortune's Wheel",
    "VGM": "Volo's Guide to Monsters",
    "VRGR": "Van Richten's Guide to Ravenloft",
    "WBtW": "The Wild Beyond the Witchlight",
    "WDH": "Waterdeep - Dragon Heist",
    "WDMM": "Waterdeep - Dungeon of the Mad Mage",
    "XGE": "Xanathar's Guide to Everything"
}

NAME = 0
SOURCE = 1
SIZE = 2
TYPE = 3
ALIGNMENT = 4
AC = 5
HP = 6
SPEED = 7
STR = 8
CHA = 13
SAVING_THROWS = 14
SKILLS = 15
DAMAGE_VULN = 16
DAMAGE_RES = 17
DAMAGE_IMM = 18
CONDITION_IMM = 19
SENSES = 20
LANGUAGES = 21
CR = 22
TRAITS = 23
ACTIONS = 24
BONUS_ACTIONS = 25
REACTIONS = 26
LEGENDARY_ACTIONS = 27
MYTHIC_ACTIONS = 28
LAIR_ACTIONS = 29
REGIONAL_EFFECTS = 30
ENVIRONMENT = 31

class Monster:
    name = ""
    source = ""
    size = ""
    type = ""
    alignment = ""
    ac = ""
    hp = ""
    speed = []
    stats = []
    saving_throws = []
    skills = []
    damage_vuln = []
    damage_res = []
    damage_imm = []
    condition_imm = []
    senses = []
    languages = []
    cr = ""
    traits = []
    actions = []
    bonus_actions = []
    reactions = []
    legendary_actions = []
    mythic_actions = []
    liar_actions = []
    regional_effects = []
    environment = []

    def __init__(self, name):
        self.name = name

class Spell:
    # Properties to output to .md file in text
    PROPS_TO_OUTPUT = ["casting_time", "range", "components", "duration"]

    def __init__(self, name):
        self.name = clean_name(name)
        self.tags = ["Spell"]
        self.properties = {"ritual": False, "concentration": False, "scales": False, "sources": [],
                           "schools": [], "components": [], "classes": [], "banner": "", "banner_y": 0.0,
                           "banner_lock": True, "type": "Spell", "icon": "LiWand2" }
        self.description = []
        self.higher_levels = ""

    def __str__(self):
        return f"{self.name}"

    def get_level_descriptor(self):
        if self.properties["level"] == "0":
            return "*`=this.schools` Cantrip*"
        elif self.properties["level"] == "1":
            return "*`=this.level`st-Level `=this.schools`*"
        elif self.properties["level"] == "2":
            return "*`=this.level`nd-Level `=this.schools`*"
        elif self.properties["level"] == "3":
            return "*`=this.level`rd-Level `=this.schools`*"
        else:
            return "*`=this.level`th-Level `=this.schools`*"

class Item:

    RARITIES = [ "uncommon", "common", "very rare", "rare", "legendary", "artifact", "unique", "???", "rarity varies", "rarity"]
    ITEM_TYPES = ["weapon", "armor", "wondrous item", "potion", "scroll", "staff", "wand", "rod", "ring", "shield"]
    BASE_ITEM_ICONS = {
        "weapon": "LiSwords",
        "armor": "RaKnightHelmet",
        "wondrous item": "LiComponent",
        "potion": "LiFlaskRound",
        "scroll": "LiScrollText",
        "staff": "RaCrystalWand",
        "wand": "LiWand",
        "rod": "LiWand2",
        "ring": "LiComponent",
        "shield": "LiShield"
    }
    EXTENDED_ITEM_ICONS = {
        "shield": "LiShield",
        "hammer": "RaLargeHammer",
        "amulet": "RaGemPendant",
        "periapt": "RaGemPendant",
        "greataxe": "RaAxe",
        "axe": "RaBatteredAxe",
        "spear": "RaSpearHead",
        "book": "LiBookMarked",
        "vial": "RaVial",
        "boots": "RaBootStomp",
        "bottle": "LiFlaskRound",
        "deck of": "RaHeartsCard",
        "eyes of": "LiGlasses",
        "goggles": "LiGlasses",
        "glove": "RaHand",
        "helm": "RaHelmet",
        "lantern": "RaLanternFlame",
        "manual of": "LiBookMarked",
        "medal of": "LiMedal",
        "mirror of": "RaMirror",
        " gem": "RaGem",
        "gem ": "RaGem",
        "scissors": "LiScissors",
        "sending stone": "RaRuneStone",
        "tome of": "LiBookMarked",
        " shard": "RaCrystals",
        "shard ": "RaCrystals",
        "cloak of": "RaHood",
        "dagger": "PaPlainDagger",
        "key": "RaKey",
        "dust of": "TiMoneybag"
        }

    def __init__(self, name):
        self.name = name
        self.tags = ["Item"]
        self.properties = {"sources": [], "attunement": False, "type": "", "classes": [], "banner": "", "banner_y": 0.0, "banner_lock": True, "icon": "LiComponent" }
        self.description = []

    def __str__(self):
        return f"{self.name}"

    def get_description(self):
        if self.properties["type_details"] == "":
            type_string = self.properties["type"]
        else:
            type_string = f"{self.properties["type"]} ({self.properties["type_details"]})"

        rarity_string = self.properties["rarity"]
        
        if self.properties["attunement"]:
            if self.properties["attunement_details"] == "":
                attunement_string = " (Requires Attunement)"
            else:
                attunement_string = f" (Requires Attunement {self.properties["attunement_details"]})"
        else:
            attunement_string = ""

        return f"*{type_string}, {rarity_string}{attunement_string}*"
    
    def setIcon(self):
        self.properties["icon"] = self.BASE_ITEM_ICONS[self.properties["type"].lower()]
        for item in self.EXTENDED_ITEM_ICONS:
            if (item in self.name.lower()) or (item in self.properties["type_details"].lower()):
                self.properties["icon"] = self.EXTENDED_ITEM_ICONS[item]
                break


def clean_source(string):
    if "Spelljammer" in string:
        return "Spelljammer - Adventures in Space"
    else:
        return string

def clean_name(string):
    return (string.title().replace("'S", "'s").replace("(Ua)", "(UA)").replace("/", "-").replace("(Hb)", "(HB)")
            .replace(":", "").strip())

def get_attunement_details(string):
    return re.match(r"[\s\S]*requires attunement([\s\S]*)\)[\s\S]*", string).group(1).strip()

def translate_source(source):
    if "Unearthed-Arcana" in source:
        return "Unearthed-Arcana"
    elif "Acquisitions-Inc" in source:
        return "Acquisitions-Incorporated"
    return source


TAG_REMOVE = [":", "\\", "/", "'", "."]
def tagify(string):
    string = string.strip().lower()

    string = re.sub(r"[_-]", " ", string).strip()

    for to_delete in TAG_REMOVE:
        string = string.replace(to_delete, "")

    string = re.sub(r"[\s\-\.]+", "-", string)

    return titleify(string)

TITLE_REMOVE = ["\\", "/"]
TITLE_REPLACE = {":": " - "}

def titleify(string):
    string = string.strip().lower()

    for to_delete in TITLE_REMOVE:
        string = string.replace(to_delete, " ")

    for to_replace in TITLE_REPLACE:
        string = string.replace(to_replace, TITLE_REPLACE[to_replace])

    string = re.sub(r"[\s]+", " ", string)

    regex = re.compile("[a-z]+('[a-z]+)?", re.I)
    return regex.sub(lambda grp: grp.group(0)[0].upper() + grp.group(0)[1:].lower(),
                     string)

def is_empty(string):
    return string.isspace() or string == ""

def clean_line(line):
    if re.search(r"<p>[^<>]+</p>", line):
        return re.match(r'<p>([^<>]+)</p>', line).group(1).strip()
    else:
        return line

def clean_links(line):
    edited_line = line
    regex = r"[\s\S]*?(<a href=[\s\S]+?\">([^<>]+?)</a>)[\s\S]*?"
    m = re.match(regex, edited_line)

    # Clean line of links
    while m is not None:
        to_replace = m.group(1)
        new_link = "[[{}]]".format(titleify(m.group(2)))
        edited_line = edited_line.replace(to_replace, new_link)
        m = re.match(regex, edited_line)
    
    return edited_line

def clean_source_links(line):
    return re.sub(r"\(<a href=\"[\s\S]+\">Twitter</a>\)", "", line)

def is_item_properties_line(line):
    if not line.startswith("<p><em>"):
        return False

    if not line.endswith("</em></p>"):
        return False 

    if "," not in line:
        return False
    
    if not any([rarity_ for rarity_ in Item.RARITIES if rarity_ in line.lower()]):
        return False

    if not any([item_ for item_ in Item.ITEM_TYPES if item_ in line.lower()]):
        return False

    return True

def get_parenthesis(string):
    if "(" not in string and ")" not in string:
        return ""
    return re.match(r"[\s\S]*\(([\s\S]+)\)[\s\S]*", string).group(1).strip()

def details_split(string):
    splits = []
    last_split = 0
    in_parenthesis = False
    for i in range(len(string)):
        if string[i] == '(':
            in_parenthesis = True
        elif string[i] == ')':
            in_parenthesis = False
        elif string[i] == ',' and not in_parenthesis:
            splits.append(string[last_split:i].strip())
            last_split = i + 1
        
        if i == len(string) - 1:
            splits.append(string[last_split:].strip())
    
    return splits

def convert_rarities(rarity):
    rarities = {"???": "unknown rarity",
                "rarity": "rarity varies",
                "rarity varies": "rarity varies"}
    if rarity in rarities:
        return rarities[rarity]
    else:
        return rarity

class DndContentLoader:
    CLASS_LIST = ["artificer", "barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue",
                  "sorcerer", "warlock", "wizard"]
    RACE_LIST = ["human"]

    def __init__(self, loading_bar_disabled):
        self.loading_bar_disabled = loading_bar_disabled
        self.spells = []
        self.items = []
        self.monsters = []
        self.class_list = {}

    def output_spells_md(self, directory):
        if not Path(directory).exists():
            Path(directory).mkdir()

        loading_bar = tqdm(range(len(self.spells)), desc="Outputting {} spell files".format(len(self.spells)),
                           ascii=True, ncols=100, file=sys.stdout, disable=self.loading_bar_disabled)
        if self.loading_bar_disabled:
            print(f"Outputting {len(self.spells)} spell files...", flush=True)

        for i in loading_bar:
            spell = self.spells[i]

            # Sort properties
            spell.properties = dict(sorted(spell.properties.items()))

            # Get output path
            output_path = Path(directory).joinpath("{}.md".format(spell.name))
            with open(output_path, "w+", encoding="utf-8") as output_file:
                # Add metadata
                output_file.write("---\n")
                output_file.write("tags:\n")
                for tag in spell.tags:
                    output_file.write("  - {}\n".format(tag))
                for prop in spell.properties:
                    if type(spell.properties[prop]) is str:
                        output_file.write(f"{prop}: {spell.properties[prop]}\n")
                    elif type(spell.properties[prop]) is float:
                        output_file.write(f"{prop}: {str(spell.properties[prop])}\n")
                    elif type(spell.properties[prop]) is bool:
                        output_file.write(f"{prop}: {str(spell.properties[prop])}\n")
                    elif type(spell.properties[prop]) is list:
                        output_file.write(f"{prop}:\n")
                        for value in spell.properties[prop]:
                            output_file.write("  - {}\n".format(value.replace("'S", "'s")))
                output_file.write("---\n")

                # Print data
                output_file.write(f">[!spell-callout] `=this.file.name`\n")
                output_file.write(f">{spell.get_level_descriptor()}\n")
                output_file.write(f">\n")
                for prop in Spell.PROPS_TO_OUTPUT:
                    output_file.write(f">**{prop.title().replace('_',' ')}:** `=this.{prop}`\n")

                output_file.write(f">\n")

                # Print description
                for section in spell.description:
                    for line in section.split("\n"):
                        output_file.write(f">{line}\n")

                # Print higher level info
                if spell.higher_levels != "":
                    output_file.write("***At Higher Levels.*** {}".format(spell.higher_levels.strip()))
        print("Done", flush=True)

    def output_wondrous_items_md(self, directory):
        if not Path(directory).exists():
            Path(directory).mkdir()

        loading_bar = tqdm(range(len(self.items)), desc="Outputting {} item files".format(len(self.items)),
                           ascii=True, ncols=100, file=sys.stdout, disable=self.loading_bar_disabled)
        if self.loading_bar_disabled:
            print(f"Outputting {len(self.items)} item files...", flush=True)

        for i in loading_bar:
            item = self.items[i]

            # Sort properties
            item.properties = dict(sorted(item.properties.items()))

            # Get output path
            output_path = Path(directory).joinpath("{}.md".format(item.name))
            with open(output_path, "w+", encoding="utf-8") as output_file:
                # Add metadata
                output_file.write("---\n")
                output_file.write("tags:\n")
                for tag in item.tags:
                    output_file.write("  - {}\n".format(tag))
                for prop in item.properties:
                    if type(item.properties[prop]) is str:
                        output_file.write(f"{prop}: {item.properties[prop]}\n")
                    elif type(item.properties[prop]) is bool:
                        output_file.write(f"{prop}: {str(item.properties[prop])}\n")
                    elif type(item.properties[prop]) is list:
                        output_file.write(f"{prop}:\n")
                        for value in item.properties[prop]:
                            output_file.write(f"  - {value}\n")
                output_file.write("---\n")

                # Print data
                callout_name = f"{tagify(item.properties["rarity"])}-{tagify(item.properties["type"])}-callout".lower()
                output_file.write(f">[!{callout_name}] `=this.file.name`\n")
                output_file.write(f">{item.get_description()}\n")
                output_file.write(f">\n")

                # Print description
                for section in item.description:
                    for line in section.split("\n"):
                        output_file.write(f">{line}\n")
        print("Done", flush=True)

    def load_spells_from_wiki(self):
        print("Loading spells from site...", flush=True)
        spell_url = "http://dnd5e.wikidot.com/spells"
        page = urlopen(spell_url)

        # Get list of spells from sites
        print("Getting spell list...", flush=True)
        html_bytes = page.readlines()
        urls = []
        for line in [l.decode("utf-8") for l in html_bytes]:
            if "/spell:" in line:
                url_snip = re.match(r"[\s\S]*(/spell:[\s\S]*)\">[\s\S]*", line).group(1)
                spell_name = re.match(r"[\s\S]*\">([\s\S]*)</a[\s\S]*", line).group(1).strip().title()
                # print("Found spell <{}> and URL: {}".format(spell_name, url_snip))
                urls.append([url_snip, spell_name])

        # Load spell one by one
        loading_bar = tqdm(range(len(urls)), desc="Loading {} spell urls".format(len(urls)), ascii=True,
                           ncols=100, file=sys.stdout, disable=self.loading_bar_disabled)
        if self.loading_bar_disabled:
            print(f"Loading {len(urls)} spell urls...", flush=True)
        for i in loading_bar:
            url = urls[i]
            full_url = "http://dnd5e.wikidot.com" + url[0]
            page = urlopen(full_url)

            # Create spell object
            s = Spell(titleify(url[1]))

            # loading_bar.write("Found Spell: <{}>".format(s.name))

            # Get the spell section
            html = page.read().decode("utf-8")
            start_string = "<div id=\"page-content\">"
            spell_start = html.find(start_string) + len(start_string)
            spell_end = html.find("<!-- wikidot_bottom_300x250 -->")
            spell_raw = html[spell_start:spell_end]

            raw_html = ""

            # Split it into lines
            lines = [l.strip() for l in spell_raw.split("\n")]
            for line in lines:
                if line.isspace():
                    continue
                elif "<p>Source:" in line:
                    # Source data
                    raw_sources = re.match(r"<p>Source:([\s\S]+)</p>[\s\S]*", line).group(1).strip()
                    raw_sources = clean_source_links(raw_sources)
                    sources = re.split(r"[\\\/]", raw_sources)
                    for source in sources:
                        cleaned_source = titleify(clean_source(source))
                        s.properties["sources"].append(f"\"[[{cleaned_source}]]\"")
                        # s.tags.append(tagify(source))

                        banner_source = translate_source(tagify(source))
                        s.properties["banner"] = f"\"[[{banner_source}-Banner.jpg]]\""
                        s.properties["banner_y"] = BANNER_OFFSETS[banner_source]
                elif "</em></p>" in line and ("-level" in line or "cantrip" in line or "-Level" in line):
                    # Spell School and Level Data
                    line = line.lower()
                    if "evel" in line:
                        if "(ritual)" in line:
                            line = line.replace("(ritual)", "")
                            # s.tags.append("Ritual")
                            s.properties["ritual"] = True
                        m = re.match(r"[\s\S]*(\d)[\s\S]+evel([\s\S]+)</em[\s\S]*", line)
                        level = m.group(1)
                        schools = m.group(2).strip().split()
                        s.tags.append("lvl" + level)
                        for school in schools:
                            # s.tags.append(tagify(school))
                            s.properties["schools"].append(titleify(school))
                        s.properties["level"] = level
                    else:
                        m = re.match(r"[\s\S]+em>([\s\S]*)cantrip[\s\S]*", line)
                        schools = m.group(1).strip().split()
                        # s.tags.append("Cantrip")
                        for school in schools:
                            # s.tags.append(tagify(school))
                            s.properties["schools"].append(titleify(school))
                        s.properties["level"] = "0"
                elif "<strong>Casting Time:" in line:
                    # Casting time
                    casting_time = (re.match(r"[\s\S]*Casting Time:</strong>([\s\S]*)<br />[\s\S]*", line)
                                    .group(1).strip())
                    s.properties["casting_time"] = titleify(casting_time)
                elif "<strong>Range:" in line:
                    # Range
                    range_ = (re.match(r"[\s\S]*Range:</strong>([\s\S]*)<br />[\s\S]*", line)
                              .group(1).strip())
                    s.properties["range"] = titleify(range_)
                elif "<strong>Components:" in line:
                    # Components
                    components = titleify(re.match(r"[\s\S]*Components:</strong>([\s\S]*)<br />[\s\S]*", line)
                                  .group(1).strip()).split(",", 2)
                    s.properties["components"] = [c.strip() for c in components]
                elif "<strong>Duration:" in line:
                    # Duration
                    duration = (re.match(r"[\s\S]*Duration:</strong>([\s\S]*)</p>[\s\S]*", line)
                                .group(1).strip())
                    s.properties["duration"] = titleify(duration)
                    if "Concentration" in line:
                        # s.tags.append("Concentration")
                        s.properties["concentration"] = True
                elif "At Higher Levels" in line:
                    # At higher levels
                    higher_levels = re.match(r"[\s\S]+</strong>([\s\S]+)</p>[\s\S]*", line).group(1).strip()
                    s.higher_levels = higher_levels
                    s.properties["scales"] = True
                elif "spell lists" in line.lower():
                    # Class list
                    for c in self.CLASS_LIST:
                        if c in line.lower():
                            # s.tags.append(tagify(c))
                            s.properties["classes"].append(titleify(c))
                else:
                    # Add the new description line
                    raw_html += clean_links(line)
                    continue

            markdown = markdownify(raw_html, bullet="-")
            # loading_bar.write(markdown)
            s.description.append(markdown)

            # Add spell to output list
            self.spells.append(s)
        print("Done", flush=True)

    def load_wondrous_items_from_wiki(self):
        print("Loading items from site...")
        wondrous_item_url = "http://dnd5e.wikidot.com/wondrous-items"
        page = urlopen(wondrous_item_url)

        # Get list of spells from sites
        print("Getting wondrous items list...", flush=True)
        html_bytes = page.readlines()
        urls = []
        for line in [l.decode("utf-8") for l in html_bytes]:
            if "/wondrous-items:" in line:
                url_snip = re.match(r"[\s\S]*(/wondrous-items:[\s\S]*)\">[\s\S]*", line).group(1)
                item_name = titleify(re.match(r"[\s\S]*\">([\s\S]*)</a[\s\S]*", line).group(1).strip())
                #print("Found item <{}> and URL: {}".format(spell_name, url_snip))
                urls.append([url_snip, item_name])
            if "Items by Type" in line:
                break

        homebrew_item_url = "http://dnd5e.wikidot.com/wondrous-items:homebrew"
        page = urlopen(homebrew_item_url)

        # Get list of items from sites
        print("Getting homebrew items list...", flush=True)
        html_bytes = page.readlines()
        for line in [l.decode("utf-8") for l in html_bytes]:
            if "/wondrous-items:" in line:
                url_snip = re.match(r"[\s\S]*(/wondrous-items:[\s\S]*)\">[\s\S]*", line).group(1)
                item_name = titleify(re.match(r"[\s\S]*\">([\s\S]*)</a[\s\S]*", line).group(1).strip())
                #print("Found item <{}> and URL: {}".format(spell_name, url_snip))
                urls.append([url_snip, item_name])
            if "Items by Type" in line:
                break
        
         # Initialize loading bar
        loading_bar = tqdm(range(len(urls)), desc="Loading {} item urls".format(len(urls)), ascii=True,
                           ncols=100, file=sys.stdout, disable=self.loading_bar_disabled)
        if self.loading_bar_disabled:
            print(f"Loading {len(urls)} item urls...", flush=True)

        # Load items one by one
        for i in loading_bar:
            url = urls[i]
            full_url = "http://dnd5e.wikidot.com" + url[0]
            page = urlopen(full_url)
            
            item = Item(url[1])

            loading_bar.write(f"Found Item: {item.name}")
            
            # Get the spell section
            html = page.read().decode("utf-8")
            start_string = "<div id=\"page-content\">"
            item_start = html.find(start_string) + len(start_string)
            item_end = html.find("<!-- wikidot_bottom_300x250 -->")
            item_raw = html[item_start:item_end]

            raw_html = ""
            lines = [l.strip() for l in item_raw.split("\n")]
            for line in lines:
                if line.isspace():
                    continue
                elif "<p>Source:" in line:
                    # Source data
                    raw_sources = re.match(r"<p>Source:([\s\S]+)</p>[\s\S]*", line).group(1).strip()
                    sources = re.split(r"[\\\/,]", raw_sources)
                    for source in sources:
                        cleaned_source = clean_source(source)
                        item.properties["sources"].append(f"\"[[{cleaned_source}]]\"")
                        # item.tags.append(tagify(source))
                        banner_source = translate_source(tagify(source))
                        item.properties["banner"] = f"\"[[{banner_source}-Banner.jpg]]\""
                        item.properties["banner_y"] = BANNER_OFFSETS[banner_source]
                elif is_item_properties_line(line):
                    raw_info = re.match(r"<p><em>([\s\S]+)</em></p>", line).group(1).strip().lower()
                    
                    # Split the details line into sections by commas
                    details_list = details_split(raw_info)

                    # Handle the item type
                    raw_type = details_list[0]
                    base_type = raw_type.split("(")[0].strip()
                    type_details = get_parenthesis(raw_type)
                    # item.tags.append(tagify(base_type))
                    item.properties["type"] = titleify(base_type)
                    item.properties["type_details"] = titleify(type_details)

                    # Handle the item rarity
                    if len(details_list) > 2:
                        # If there are more than 2 splits, there are mutiple rarities
                        # item.tags.append("Rarity-Varies")
                        item.properties["rarity"] = "Rarity Varies"
                    else:
                        # Find the rarity
                        raw_rarity = details_list[1]
                        for rarity in Item.RARITIES:
                            if rarity in raw_rarity:
                                # item.tags.append(tagify(convert_rarities(rarity)))
                                item.properties["rarity"] = titleify(convert_rarities(rarity))
                                break

                    # Handle the attunement
                    if "requires attunement" in raw_info:
                        # item.tags.append("Attunement")
                        item.properties["attunement"] = True
                        item.properties["attunement_details"] = titleify(get_attunement_details(raw_info))
                    
                    # Handle the classes
                    for class_string in self.CLASS_LIST:
                        if class_string in raw_info:
                            # item.tags.append(tagify(class_string))
                            item.properties["classes"].append(titleify(class_string))
                else:
                    # Add the new description line
                    raw_html += clean_links(line)
                    continue
            
            markdown = markdownify(raw_html, bullet="-")
            item.description.append(markdown)
            item.setIcon()
            self.items.append(item)
        print("Done", flush=True)
    
    def load_beastiary_from_csv(self, file):
        print("Loading monsters from file...")

        with open(file, newline='\n') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

            lines = [line for line in reader]

            for i in range(len(lines[0])):
                print(f"[{lines[0][i]}-[{i}]")

            loading_bar = tqdm(range(1,len(lines)), desc="Loading {} monster lines".format(len(lines)),
                                    ascii=True, ncols=100, file=sys.stdout, disable=self.loading_bar_disabled)
            if self.loading_bar_disabled:
                print(f"Outputting {len(lines)} item files...\n", flush=True)

            for i in loading_bar:
                row = lines[i]

                loading_bar.write(f"Found Monster: {row[NAME]}")
                
                # Name
                m = Monster(row[NAME].strip())

                # Source
                m.souce = f"\"[[{SOURCE_ACRONYMS[row[SOURCE]]}]]\""

                # Size
                m.size = row[SIZE].strip()

                # Type
                m.type = row[TYPE].strip()

                # Alignment
                m.alignment = row[ALIGNMENT].strip()

                # AC
                m.ac = row[AC].strip()

                # HP
                m.hp = row[HP].strip()

                # Speed
                m.speed = [speed.strip() for speed in row[SPEED].split(",")]

                # Stats
                m.stats = [stat.strip() for stat in row[STR:CHA+1]]

                # Saving throws
                m.saving_throws = [throw.strip() for throw in row[SAVING_THROWS].split(",")]
                
                # Skills
                m.skills = [skill.strip() for skill in row[SKILLS].split(",")]

                # Damage Vulnerabilities
                m.damage_vuln = [vuln.strip() for vuln in row[DAMAGE_VULN].split(",")]
                
                # Damage Resistances
                m.damage_res = [res.strip() for res in row[DAMAGE_RES].split(",")]

                # Damage Immunities 
                m.damage_imm = [imm.strip() for imm in row[DAMAGE_IMM].split(",")]

                # Condition Immunities
                m.condition_imm = [imm.strip() for imm in row[CONDITION_IMM].split(",")]
                
                # Senses
                m.senses = [sense.strip() for sense in row[SENSES].split(",")]
                
                # Languages
                m.languages = [lang.strip() for lang in row[LANGUAGES].split(",")]
                
                # CR
                m.cr = row[CR].strip()

                # Traits
                m.traits = row[TRAITS].strip()
                # m.traits = [trait.strip() for trait in row[TRAITS].split(",")]
                
                print(row[ACTIONS])
                continue

        # Get list of spells from sites