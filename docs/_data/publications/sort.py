# Copyright (C) 2024 Advanced Micro Devices, Inc
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
    for file in yaml_files:
        with open(file, 'r', encoding='utf-8') as yaml_file:
            data = yaml.safe_load(yaml_file)
            pubs = {item['title'].lower(): item for item in data}
            sorted_dict = {k: pubs[k] for k in sorted(pubs)}
            sorted_list = [sorted_dict[item] for item in sorted_dict]
            if stats:
                print(f'In {file=} the alphabetical order should be:')
                for index, value in enumerate(sorted_list):
                    print(f'{index:02d}: {value.get["title"]}')
                print('\n')
        basename = os.path.basename(file).split('.yaml')[0]
        output_file = os.path.dirname(file) + '/' + basename + '_sorted.yml'
        if stats:
            print(f'{output_file=}')
        print(f'Year {basename} has {len(sorted_list)} papers')
        count += len(sorted_list)
        with open(output_file, 'w', encoding='utf-8') as sorted_file:
            for v in sorted_list:
                sorted_file.write(f'- title: "{v["title"]}"\n')
                sorted_file.write(f'  author: "{v["author"]}"\n')
                if v.get('bestpaper'):
                    sorted_file.write(f'  bestpaper: "{v["bestpaper"]}"\n')
                sorted_file.write(f'  institution: "{v["institution"]}"\n')
                sorted_file.write(f'  link: "{v["link"]}"\n')
                if v.get('github'):
                    sorted_file.write(f'  github: "{v["github"]}"\n')
                sorted_file.write(f'  abstract: |\n    "'
                                  f'{v["abstract"][:-2]}"\n\n')

    print(f'Total number of papers is: {count}')


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    sort(path, False)
