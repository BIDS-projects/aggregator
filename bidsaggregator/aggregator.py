import argparse
import textwrap
import modules.lda
import modules.pagerank
import modules.researchers
from utils.db import MySQL
from utils.config import MySQLConfig

modules = {
    'lda': modules.lda.LDAModule,
    'pagerank': modules.pagerank.PageRankModule,
    'researchers': modules.researchers.ResearchersModule
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
    mysql = MySQL(config=MySQLConfig)
    args = parser.parse_args()
    Module = modules[args.analysis]
    Module().run(args)
