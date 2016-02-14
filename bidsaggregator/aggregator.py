import argparse
import textwrap
import modules

modules = {
    'lda': modules.lda.LDAModule
}

#######################
# COMMAND-LINE PARSER #
#######################

parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=textwrap.dedent('''\
============================================================
BIDS IEM Aggregator
This aggregator takes data inputs from various analyses
and converts all inputs into a uniform graph representation
in MySQL.
============================================================
'''))

parser.add_argument(
	type=str,
    choices=modules.keys(),
	help='Module to load. One of the following: %s'
        % ','.join(modules.keys()),
    dest='analysis')

parser.add_argument(
	'--csv',
	type=str,
	help='relative path to csv')

if __name__ == '__main__':
    args = parse.parse_args()
    Module = modules[analysis]
    Module().parse(args)
