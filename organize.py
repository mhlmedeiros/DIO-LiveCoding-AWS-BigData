# -*- coding: utf-8 -*-

import argparse


def parse_arguments():
    """
    Trata as entradas do usuário
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path for the input file")
    parser.add_argument("-hl", "--header_lines", default=0,
                        type=int, help="Number of header lines at the begining of the file.")
    args = parser.parse_args()
    input_file = args.input_file
    header_lines = args.header_lines
    return input_file, header_lines


def read_the_lines(file_name, headerlines):
    """
    Lê todas as linhas do arquivo entrada
    pulando as primeiras "headerlines"
    """
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return [list_lines.split('\t') for list_lines in lines[headerlines:]]


def ordena_palavras(word_list):
    """
    Reorganiza lista baseando-se na frequência
    em que a palavra aparece.
    """
    return sorted(word_list, key=lambda a : int(a[1]), reverse=True)


def show_strings(matrix, nlines=5):
    print(f"{nlines} lines of the string matrix:")
    for i in range(nlines):
        print(matrix[i])

def escreve_output(file_name, word_list):
    """
    Escreve resultados ordenados em um
    arquivo texto de nome "file_name".
    """
    with open(file_name, 'w') as file:
        for line in word_list:
            file.write(f"{line[0]}\t{line[1]}\n")


def main():
    fname, n_header_lines = parse_arguments()
    matrix_with_strings = read_the_lines(fname, n_header_lines)
    matrix_with_strings = ordena_palavras(matrix_with_strings)
    escreve_output('resultado_ordenado.txt', matrix_with_strings)

if __name__ == '__main__':
    main()
