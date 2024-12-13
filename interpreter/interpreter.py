import argparse

def interpret(source, buffer=None, cursor=None, index=None, loop_pos=None, subprograms=None, code=None):
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
                cursor += 1
            elif char == '8': # up
                buffer[cursor] += 1
            elif char == '2': # down
                if buffer[cursor] <= 0:
                    raise Exception('Buffer value out of bounds')
                buffer[cursor] -= 1
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
                print(chr(buffer[cursor]), end='')
            elif char == '3': # read
                try:
                    buffer[cursor] = ord(input('')[0])
                except ValueError:
                    raise Exception('Invalid input')
            elif char == '5': # define subprogram
                index += 1
                subprogram = ''
                while code[index] != '5':
                    subprogram += code[index]
                    index += 1
                subprograms[buffer[cursor]] = subprogram
            elif char == '0': # call subprogram
                interpret(source, buffer, cursor, 0, loop_pos, subprograms, subprograms[buffer[cursor]])
            elif char == '(':
                in_comment = True
        elif char == ')':
            in_comment = False
        # Tout autre caractère est ignoré

        index += 1

def main():
    # Créer le parser d'arguments
    parser = argparse.ArgumentParser(description='Interpret a Digited language file')
    
    # Ajouter les arguments
    parser.add_argument('source', type=str, help='source code to interpret')
    
    # Parser les arguments
    args = parser.parse_args()

    # Vérifier l'extension du fichier
    if not args.source.endswith('.dg'):
        raise Exception('Invalid file extension')

    # Interpréter le code source
    interpret(args.source)

if __name__ == '__main__':
    main()