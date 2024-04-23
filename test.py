import time
import argparse

def start_interface():
    print("Запуск интерфейса..")
    time.sleep(0.5)
    print("10101011000101100101101001001001011100100101001101
01101110010010100101001101001101110100110101101110
10011010010101101001010010101001101011010011010101
10110010101001010110100100101011001010100101011010
01001010110101010110101001010010101010101010101010")
    time.sleep(3)
    print("мне лень давай сам(:")
def main():
    parser = argparse.ArgumentParser(description='Завтра может будет (:')
    subparsers = parser.add_subparsers(help='Доступные подкоманды')

    # Подкоманда для интерфейса
    parser_start = subparsers.add_parser('start', help='Запуск интерфейса')
    parser_start.set_defaults(command='start')

    args = parser.parse_args()

    if hasattr(args, 'command'):
        if args.command == 'start':
            start_interface()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
