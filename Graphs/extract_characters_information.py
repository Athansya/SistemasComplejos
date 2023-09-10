'''
File: extract_characters_information.py
Project: Graphs
File Created: Tuesday, 5th September 2023 1:47:43 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Tuesday, 5th September 2023 1:47:53 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
'''

import json
# import networkx as nx
import re
from collections import defaultdict

CHARACTERS = [
    "Aaron",
    "Abenthy",
    "Aethe",
    "Alder",
    "Aleph",
    "Alleg",
    "Ambrose",
    "Amlia",
    "Andan",
    "Anisat",
    "Anker",
    "Anne",
    "Arliden",
    "Arthur",
    "Arwyl",
    "Auri",
    "Greyfallow",
    "Jakis",
    "Basil",
    "Bast",
    "Ben",
    "Benjamin",
    "Bil",
    "Brandeur",
    "Brann",
    "Brean",
    "Bredon",
    "Brenden",
    "Caleb",
    "Cammar",
    "Carter",
    "Caudicus",
    "Caverin",
    "Celean",
    "Cinder",
    "Martin",
    "Cyphus",
    "Daeln",
    "Dagon",
    "Deah",
    "Dedan",
    "Denna",
    "Dennais",
    "Deouch",
    "Derrik",
    "Devan",
    "Devi",
    "Drenn",
    "Ellie",
    "Elodin",
    "Elxa",
    "Emberlee",
    "Encanis",
    "Enlas",
    "Erlus",
    "Fela",
    "Felurian",
    "Fenton",
    "Finol",
    "Fren",
    "Gaskin",
    "Geisa",
    "Gel",
    "Gerrerk",
    "Graham",
    "Gran",
    "Greggor",
    "Haliax",
    "Hap",
    "Hespe",
    "Hetera",
    "Iax",
    "Illien",
    "Imet",
    "Inyssa",
    "Jacob",
    "Jake",
    "Jamison",
    "Jane",
    "Jarret",
    "Hemme",
    "Waterson",
    "Jaxim",
    "Jenna",
    "Jessom",
    "Josh",
    "Josn",
    "Kaerva",
    "Kale",
    "Katie",
    "Kete",
    "Kilvin",
    "Kirel",
    "Kostrel",
    "Krin",
    "Kvothe",
    "Laclith",
    "Lanre",
    "Larel",
    "Laren",
    "Lasrel",
    "Laurel",
    "Laurian",
    "Lecelte",
    "Lerand",
    "Lily",
    "Lin",
    "Loni",
    "Lorren",
    "Losine",
    "Lyra",
    "Magwyn",
    "Mandrag",
    "Manet",
    "Marea",
    "Marie",
    "Marten",
    "Mary",
    "Ash",
    "Mauthens",
    "Anwater",
    "Lant",
    "Meluan",
    "Meradin",
    "Mola",
    "Walker",  # Mr and Ms
    "Naden",
    "Nalto",
    "Nathan",
    "Netalia",
    "Cob",
    "Ordal",
    "Oren",
    "Otto",
    "Penny",
    "Penthe",
    "Perial",
    "Pete",
    "Pike",
    "Icing",
    "Puppet",
    "Remmen",
    "Reta",
    "Rethe",
    "Rian",
    "Riem",
    "Rike",
    "Roderic",
    "Roent",
    "Selitos",
    "Sephran",
    "Seth",
    "Shandi",
    "Shehyn",
    "Shep",
    "Simmon",
    "Savien",
    "Skarpi",
    "Skoivan",
    "Sleat",
    "Sovoy",
    "Stanchion",
    "Stapes",
    "Syl",
    "Taborlin",
    "Tam",
    "Tanne",
    "Teccam",
    "Tehlu",
    "Tempi",
    "Teren",
    "Cthaeh",
    "High King",
    "Listener",
    "Tim",  # Too many! 
    "Trapis"
]

FRIEND_RADIUS = 30
test_char = ["Elodin", "Lorren"]

def main():
    # Initialize dict of names count
    name_counts = {name: 0 for name in CHARACTERS}

    # Initialize a defaultdict to store the related names and their counts
    related_names = defaultdict(lambda: defaultdict(int))

    # Define a regular expression pattern to match complete names
    name_pattern = r'\b(?:' + '|'.join(re.escape(name) + r's?' for name in CHARACTERS) + r')\b'

    # Initialize a buffer to store words from the previous line
    line_buffer = []

    # translation table to remove special characters

    # Read txt book file
    with open("./Graphs/example_text.txt", 'r') as book_file:
        for idx, line in enumerate(book_file):
            # print(f"Line: {idx}")
            # Guarda los matches
            # print(line)
            # line = line.translate(translation_table)
            matches = re.findall(name_pattern, line)
            line = line.split() # Eliminamos espacios
            # line = [word.replace("’s", "") for word in line] # Eliminamos las 's
            # line = [word.replace("’", "") for word in line] # Eliminamos las 's

            # Update counter
            for name in matches:
                print(f"{name=}")
                # print(line)
                # Increment the count for the current name occurrence
                name_counts[name.capitalize()] += 1
                # Look for the index of the name in the sentence
                for i, word in enumerate(line):
                    if name in word:
                        name_index = i
                        break
                # print(name)
                print(f"{name_index=}")
                # Creo que no tiene caso crear relaciones entre personajes que esten en oraciones distintas,
                # pues que puede ser que este ocurriendo algo diferente. No siempre será el caso, pero de
                # momento así lo dejaré
                end_line_search = min(name_index + FRIEND_RADIUS, len(line))  # Checa que no se nos acabe la linea
                # print(f"{end_line_search=}")
                # Looks for new related names
                for word in line[name_index+1:end_line_search]:
                    # print(f"{word=}")
                    if word in CHARACTERS and word != name:
                        related_names[name][word] += 1

                # print(f"{line[name_index]=}")
                # print(f"name index: {line.index(name)}")
                # print(f"Match: {name}")
            

                # Find the words within the next 15 words
            #     try:
            #         index = [w.capitalize() for w in line_buffer].index(name)
            #     except ValueError:
            #         continue
            #     end_index = min(index + 100, len(line_buffer))
            #     next_words = line_buffer[index+1:end_index]
            
            #     for word in next_words:
            #         # print(f"Checking for related names to {name}...")
            #         # Check if the word is another name from the list
            #         word = word.capitalize()
            #         if word in CHARACTERS and word != name:
            #             # print(f"Found related name: {word}")
            #             # Increment the count for the related name
            #             related_names[name][word] += 1

            #     # Remove processed words from the buffer
            # line_buffer = line_buffer[end_index:]
        
    with open('name_counts_example.json', 'w') as name_counts_file:
        json.dump(name_counts, name_counts_file)

    with open('related_names_example.json', 'w') as related_names_file:
        json.dump(related_names, related_names_file)

    # with open("name_counts.json", "w") as name_counts_file:
    #     json.dump(name_counts, name_counts_file)

if __name__ == "__main__":
    main()