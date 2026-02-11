'''
Docstring for python_advanced.aulas.aula004
'''
from pathlib import Path


def matching_lines_from_file(path, pattern):
    with open(path) as hendle:
        for line in hendle:
            if pattern in line:
                yield line.rstrip('\n')


CAMINHO_LOG = Path(__file__).parent.parent /'exercicios'/'log.txt'

for line in matching_lines_from_file(CAMINHO_LOG, 'WARNING'):
    print(line)