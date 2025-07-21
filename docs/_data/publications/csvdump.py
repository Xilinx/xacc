# Copyright (C) 2025 Advanced Micro Devices, Inc
#
# SPDX-License-Identifier: MIT

import glob
import os
import yaml


def sort(path: str = '', stats: bool = False):
    """Sort YAML files alphabetically by title"""
    search_path = path + '*.yaml'
    yaml_files = sorted(glob.glob(search_path))
    count = 0
    output_file = 'papers.csv'
    with open(output_file, 'w', encoding='utf-8') as fcsv:
        fcsv.write(f"Year|Title|Author|Institution|\n")
        for file in yaml_files:
            with open(file, 'r', encoding='utf-8') as yaml_file:
                data = yaml.safe_load(yaml_file)
                pubs = {item['title'].lower(): item for item in data}
                sorted_dict = {k: pubs[k] for k in sorted(pubs)}
            
            base_name = os.path.basename(file)
            file_name, _ = os.path.splitext(base_name)

            for k, v in sorted_dict.items():
                fcsv.write(f"{file_name}|{v['title']}|{v['author']}|{v['institution']}|\n")


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    sort(path, False)
