import argparse

def start_interface():
	print("hello")
def main():
	parser_start = subparsers.add_parser('start')
	
        args = parser.parse_args()
	if hasattr(args, 'command'):
        if args.command == 'start':
            start_interface()
    else
        parser.print_help()

if __name__ == "__main__":
    main()
