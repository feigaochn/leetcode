#! /usr/local/bin/python3

import httplib2
import re
import sys
import time


def get_name():
    names = sys.argv[1:]
    if len(names) > 0:
        problem_name = str('-'.join([name.lower() for name in names]))
    else:
        problem_name = str(input("Input problem name: ")).lower().replace(' ', '-')
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

    return question_lines, code_lines


def generate_source_file(problem_name, question_lines, code_lines):
    try:
        # exclusively open
        f = open(problem_name + '.py', mode='x', encoding='utf-8', newline='\n')

        # header
        f.write("# author: Fei Gao\n")
        f.write('# date: ' + time.asctime() + '\n#\n')

        # problem description
        f.write('# ' + problem_name.replace('-', ' ').capitalize() + '\n#\n')
        for line in question_lines:
            f.write("# " + line + '\n')
        f.write('\n\n')

        # code template
        for line in code_lines:
            f.write(line + '\n')

        # main function
        f.write('\n\n')
        main_func = \
            "def main():\n" + \
            "    pass\n\n\n" + \
            "if __name__ == '__main__':\n" + \
            "    pass\n"

        f.write(main_func)
        f.close()
        response = "Success"

    except FileExistsError:
        response = "ERROR: File Exists"

    return response


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

    response = generate_source_file(problem_name, question_lines, code_lines)
    print("Generate .py File: " + response)

    print('\n>>> Done' + separator)

    # print(separator + "Problem Description:\n")
    # print('\n'.join(question_lines))
    #
    # print(separator + "Python Code Template:\n")
    # print('\n'.join(code_lines))


if __name__ == '__main__':
    main()
