#!/usr/bin/env python3
# TODO
# 1. generate easier testing unit
# 2. 'ii' or 'iii' etc. in title

import re
import sys

import httplib2


def get_name():
    names = sys.argv[1:]
    if len(names) > 0:
        problem_name = str('-'.join([name.lower() for name in names]))
    else:
        problem_name = str(
            input("Input problem name: ")).lower().strip().replace(
            ' ',
            '-')
    return problem_name


def get_page(url):
    h = httplib2.Http('.cache')
    response, contents = h.request(url)
    if response['status'] == '200':
        return "Success", contents.decode('utf-8')
    else:
        # error getting page
        return "ERROR", contents.decode('utf-8')


def parse_page(page):
    lines = page.splitlines()
    question_lines = []
    code_lines = []
    is_question = False
    is_code = False
    is_pre = False
    for line in lines:

        # get_description(): contents between
        # <div class="question-content">
        # and
        # the first </div>
        if line.find("question-content") != -1:
            is_question = True

        if is_question:
            if line.find('<pre>') != -1:
                is_pre = True
            # remove labels <?>
            line_clean = re.sub(r'<.*?>', '', line)
            if is_pre is False:
                line_clean = re.sub(r'^\s*', '', line_clean)
            # only add non-empty line
            if line_clean.replace(' ', '') != '':
                question_lines.append(line_clean)
            if line.find('</pre>') != -1:
                is_pre = False
            if line.find('</div>') != -1:
                is_question = False

        # get_code(): contents between
        # <textarea class="form-control python" rows="20">
        # and
        # </textarea>
        if line.find("form-control python") != -1:
            is_code = True
        if is_code:
            if line.find('</textarea>') != -1:
                is_code = False
                # this is last in of code template
                # put a `pass` here
                code_lines.append(' ' * 8 + '# TODO')
                code_lines.append(' ' * 8 + 'pass')
            else:
                # remove any labels <?>
                line_clean = re.sub(r'<.*?>', '', line)
                if line_clean.find('Solution') != -1:
                    line_clean = re.sub(r'^\s*', '', line_clean)
                code_lines.append(line_clean)

    # the structure is changed for default code
    code_lines = re.findall(r"'text': 'Python', 'defaultCode': '(.*?)' },", page)[0]
    code_lines = code_lines.replace('\\u000D\\u000A', '\n').strip().splitlines()
    code_lines.append(' ' * 8 + 'return')
    return question_lines, code_lines


header = '''# coding: utf-8

# author: Fei Gao
#
'''

main_func = '''

def main():
    solver = Solution()
    tests = []
    for test in tests:
        print(test)
        print(' ->')
        result = solver.{method}(test)
        print(result)
        print('~'*10)
    pass


if __name__ == '__main__':
    main()
    pass
'''


def generate_source_file(problem_name, question_lines, code_lines, method_name):
    try:
        # exclusively open
        f = open(problem_name + '.py',
                 mode='x',
                 encoding='utf-8',
                 newline='\n')

        # header
        f.write(header)

        # problem description
        f.write('# ' + ' '.join([word.capitalize()
                                 for word in problem_name.split('-')]) + '\n#\n')
        for line in question_lines:
            f.write("# " + line + '\n')
        f.write('\n\n')

        # code template
        for line in code_lines:
            f.write(line + '\n')

        # main function
        f.write(main_func.format(method=method_name))

        f.close()
        response = "Success"

    except FileExistsError:
        response = "ERROR: File Exists"

    return response


def retrive_method(code_lines):
    """

    :param code_lines:
    :type code_lines: str
    :return:
    :rtype:
    """
    for line in code_lines:
        method = re.findall(r'def ([a-zA-Z0-9]+)\(self', line)
        if method:
            return method[0]


def main():
    problem_name = get_name()
    # problem_name = 'spiral-matrix'

    separator = '\n' + '-' * 20 + '\n'

    print(separator + ">" * 3 + " Fetch Problem:\n")

    print("Title: " + problem_name)

    oj_prefix = 'https://oj.leetcode.com/problems/'
    response, page = get_page(oj_prefix + problem_name)

    print("Get Web Page: " + response)
    if response == "ERROR":
        return

    question_lines, code_lines = parse_page(page)
    if len(question_lines) > 0 and len(code_lines) > 0:
        response = "Success"
    else:
        response = "Maybe Some Error"
    print("Parse Page: " + response)

    method_name = retrive_method(code_lines)
    response = generate_source_file(problem_name, question_lines, code_lines, method_name)
    print("Generate .py File: " + response)

    print('\n>>> Done' + separator)

    # print(separator + "Problem Description:\n")
    # print('\n'.join(question_lines))
    #
    # print(separator + "Python Code Template:\n")
    # print('\n'.join(code_lines))


if __name__ == '__main__':
    main()
