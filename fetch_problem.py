#!/usr/bin/env python3

import logging
import re
import sys

import bs4
import requests

logging.basicConfig(level=logging.WARNING)

BASE_URL = 'https://oj.leetcode.com/problems/'

TEMPLATE = '''# coding: utf-8

# author: Fei Gao <leetcode.com@feigao.xyz>

# Problem: {name}
#
{description}

{code}


def main():
    solver = Solution()
    tests = [
        (('param',), 'result'),
    ]
    for params, expect in tests:
        print('-'*5 + 'TEST' + '-'*5)
        print('Input:  ' + str(params))
        print('Expect: ' + str(expect))

        result = solver.{method}(*params)
        print('Result: ' + str(result))
    pass


if __name__ == '__main__':
    main()
    pass
'''


def get_name():
    names = sys.argv[1:]
    if names:
        problem_name = '-'.join(word for word in names).lower()
    else:
        problem_name = input("Input problem name: ").strip().replace(' ', '-').lower()
    logging.info('problem name: ' + problem_name)
    return problem_name


def parse_page(page, lang='Python'):
    bs = bs4.BeautifulSoup(page, 'lxml')

    # get description
    desc = bs.find('div', {'class': 'question-content'}).text.replace('\r', '').strip('\n')
    desc_split = desc.splitlines()
    desc_lines = []
    # remove double blank lines
    for line in desc_split:
        if desc_lines and line == '' == desc_lines[-1]:
            continue
        else:
            desc_lines.append(line)
    description = '\n'.join('# ' + line for line in desc_lines)

    # get code template
    ace = bs.find('form', {"ng-controller": "AceCtrl as aceCtrl"}).get('ng-init')
    keys = [triple[1] for triple in re.findall(r"(\'|\")(.*?)(\1)", ace)]
    code = keys[keys.index('defaultCode', keys.index(lang)) + 1].encode().decode('unicode_escape')
    code += 'pass'

    return description, code


def generate_source_file(problem_name, description, code, method_name):
    try:
        # exclusively open
        f = open(problem_name.replace('-', '_') + '.py',
                 mode='x',
                 encoding='utf-8',
                 newline='\n')

        f.write(TEMPLATE.format(name=problem_name.replace('-', ' '),
                                description=description,
                                code=code,
                                method=method_name
                                ))
        f.close()
    except FileExistsError:
        logging.critical('file exists: ' + problem_name)
        exit(1)
    except Exception as e:
        logging.critical('write file error: ' + str(e))
        exit(1)


def guess_method(code):
    method = re.findall(r'def ([a-zA-Z0-9_]+)\(self', code)
    if method:
        return method[0]
    else:
        logging.warning('fail to get method name')


def main():
    problem_name = get_name()

    response = requests.get(BASE_URL + problem_name)
    logging.info('request page: ' + str(response.ok))
    if not response.ok:
        logging.critical('fail to request page')
        exit(1)

    description, codes = parse_page(response.text)
    method_name = guess_method(codes)
    generate_source_file(problem_name, description, codes, method_name)


if __name__ == '__main__':
    main()
