import argparse
import subprocess

def write(source, code):
    with open(source, 'a') as f:
        f.write(code)

def init_c_file(source):
    with open(source, 'w') as f:
        pass
    write(source, '#include <stdio.h>\n#include <stdlib.h>\n\nint main()\n{\n\tint *buffer = malloc(sizeof(int));\n\tbuffer[0] = 0;\n')

def finish_c_file(source):
    write(source, '\n\treturn 0;\n}\n')

def compile(source, dest, buffer=None, cursor=None, index=None, loop_pos=None, subprograms=None, code=None):
    if code is None:
        with open(source, 'r') as f:
            code = f.read()

    if buffer is None:
        buffer = [0]
    if cursor is None:
        cursor = 0
    if index is None:
        index = 0
    if loop_pos is None:
        loop_pos = [0]
    if subprograms is None:
        subprograms = {}
    in_comment = False

    while index < len(code):
        char = code[index]

        if not in_comment:
            if char == '4': # left
                if cursor <= 0:
                    raise Exception('Cursor out of bounds')
                cursor -= 1
            elif char == '6': # right
                if cursor >= len(buffer) - 1:
                    buffer.append(0)
                    write(dest, f"\tbuffer = realloc(buffer, {len(buffer)} * sizeof(int));\n\tif (buffer == NULL)\n" + "\t{\n\t\tprintf(\"Reallocation error\");\n\t\treturn 1;\n\t}\n" + f"\tbuffer[{cursor}] = 0;\n")
                cursor += 1
            elif char == '8': # up
                buffer[cursor] += 1
                write(dest, f"\tbuffer[{cursor}]++;\n")
            elif char == '2': # down
                if buffer[cursor] <= 0:
                    raise Exception('Buffer value out of bounds')
                buffer[cursor] -= 1
                write(dest, f"\tbuffer[{cursor}]--;\n")
            elif char == '7': # start
                if buffer[cursor] != 0:
                    loop_pos = index
            elif char == '1': # end
                if buffer[cursor] != 0:
                    index = loop_pos
                else:
                    loop_pos = 0
            elif char == '9': # print
                tmp_int = buffer[cursor]
                tmp_char = chr(tmp_int)
                # print(chr(buffer[cursor]), end='')
                if tmp_char == '\n':
                    write(dest, "\tprintf(\"\\n\");\n")
                else:
                    write(dest, f"\tprintf(\"%c\", buffer[{cursor}]);\n")
            elif char == '3': # read
                raise Exception('Read (3) is not suported yes')
                # try:
                #     buffer[cursor] = ord(input('')[0])
                # except ValueError:
                #     raise Exception('Invalid input')
            elif char == '5': # define subprogram
                index += 1
                subprogram = ''
                while code[index] != '5':
                    subprogram += code[index]
                    index += 1
                subprograms[buffer[cursor]] = subprogram
            elif char == '0': # call subprogram
                compile(source, dest, buffer, cursor, 0, loop_pos, subprograms, subprograms[buffer[cursor]])
            elif char == '(':
                in_comment = True
        elif char == ')':
            in_comment = False
        # Tout autre caractère est ignoré

        index += 1

def main():
    # Créer le parser d'arguments
    parser = argparse.ArgumentParser(description='Compile a Digited language file')
    
    # Ajouter les arguments
    parser.add_argument('source', type=str, help='source code to compile')
    parser.add_argument('dest', type=str, help='destination of compiled code')
    
    # Parser les arguments
    args = parser.parse_args()

    # Vérifier l'extension du fichier
    if not args.source.endswith('.dg'):
        raise Exception('Invalid file extension')

    # Convertir le code source en C
    init_c_file(args.dest + ".c")
    compile(args.source, args.dest + ".c")
    finish_c_file(args.dest + ".c")

    # Compiler le code source
    subprocess.run(['gcc', args.dest + ".c", '-o', args.dest])
    subprocess.run(['rm', args.dest + ".c"])

if __name__ == '__main__':
    main()