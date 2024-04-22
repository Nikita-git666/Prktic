import argparse

def start_interface():
	print ("-----------------------")
	print ("|       GoB           |")
	print ("|                     |")
	print ("-----------------------")
def main():
	parser_start = subparsers.add_parser('start')
        parser_start.set_defaults(command='start')
