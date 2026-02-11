'''
Docstring for python_advanced.aulas.aula005
'''
from pathlib import Path
from aula004 import matching_lines_from_file


def parse_log_records(lines):
    for line in lines:
        level, massage = line.split(':', 1)
        yield {'level': level, 'massage': massage}

CAMINHO_LOG = Path(__file__).parent.parent /'exercicios'/'log.txt'

log_lines = matching_lines_from_file(CAMINHO_LOG, 'WARNING')

for record in parse_log_records(log_lines):
    print(record)