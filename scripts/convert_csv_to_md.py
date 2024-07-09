# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Copyright 2024, Alex Zhornyak, alexander.zhornyak@gmail.com

import csv
from dataclasses import dataclass
from collections import defaultdict
import numpy as np
import os


@dataclass
class Item:
    name: str = ''
    category: str = ''
    description: str = ''
    image_url: str = ''
    blendermarket_url: str = ''


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    s_out = os.path.join(base_dir, "../mkdocs/recommended_addons.md")

    s_in = os.path.join(base_dir, "recommended_addons.csv")

    with open(s_out, 'w') as out:
        out.write("# Recommended Add-ons")

        with open(s_in, 'r') as file:
            reader = csv.reader(file)

            t_addons = defaultdict(list)

            for row in reader:
                item = Item(
                    name=row[0].strip(),
                    category=row[1].strip(),
                    description=row[4].strip(),
                    image_url=row[3].strip(),
                    blendermarket_url=row[2].strip()
                )

                if item.category and "http" in item.blendermarket_url:
                    # NOTE: remove expired timestamp

                    idx_expire = item.image_url.find("?Expires=")
                    if idx_expire != -1:
                        item.image_url = item.image_url[:idx_expire]

                    t_addons[item.category].append(item)

            for cat, items in t_addons.items():
                remainder = len(items) % 3
                padding_needed = (3 - remainder) % 3
                padded_list = items + [Item()] * padding_needed

                reshaped_array = np.array(padded_list).reshape(-1, 3)

                out.write("\n")
                out.write(f"## {cat}\n")
                out.write("| | | |\n")
                out.write("|---|---|---|\n")
                for row in reshaped_array:
                    t_elements = [
                        (
                            f' [{item.name}]({item.blendermarket_url} "{item.description}") '
                            if item.name else "")
                        for item in row]
                    out.write(f"| {'|'.join(t_elements)} |\n")

                    t_icons = [
                        (
                            f' [![]({item.image_url})]({item.blendermarket_url} "{item.description}") '
                            if item.name else "")
                        for item in row]
                    out.write(f"| {'|'.join(t_icons)} |\n")
