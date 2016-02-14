import argparse
import textwrap

ALLOWED_MODULES = (
    'lda'
)

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
    choices=ALLOWED_MODULES,
	help='Module to load. One of the following: %s'
        % ','.join(ALLOWED_MODULES),
    dest='analysis')

parser.add_argument(
	'-p',
	'--path',
	type=str,
	help='relative path to required file')

if __name__ == '__main__':
    import modules
    pass
