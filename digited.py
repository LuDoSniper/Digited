import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Interpret or compile Digited code')
    parser.add_argument('source', type=str, help='source file')
    parser.add_argument('-i', '--interpret', action='store_true', help='interpret the source code')
    parser.add_argument('-c', '--compile', action='store_true', help='compile the source code')
    parser.add_argument('-o', '--output', type=str, help='output file')
    args = parser.parse_args()

    if args.interpret:
        subprocess.run(['python3', 'interpreter/interpreter.py', args.source])
    elif args.compile:
        # subprocess.run(['python3', 'compilator/compilator.py', args.source, args.output]) # Compile toutes les actions
        subprocess.run(['python3', 'compilator/compilatorv2.py', args.source, args.output]) # Compile plus intéligemment

if __name__ == '__main__':
    main()