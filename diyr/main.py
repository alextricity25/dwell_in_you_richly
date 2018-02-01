#!/user/bin/env python
# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from diyr import args
from diyr.command_line import CommandLineRunner
# MAPS COMMAND LINE TYPES TO FORMATTERS
FORMAT_MAPPER = {
    "listed_verses": "ListedVerses",
    "referenced_verses": "ReferencedVerses",
    "outline": "Outline"
}

ENGINE_MAPPER = {
    'fitb': 'FillInTheBlank'
}


def main():
    parsed_args = args.get_parser().parse_args()
    with open(parsed_args.file, 'r') as f:
        # Import respective formattype module
        format_module = __import__('diyr.formattypes.{}'.format(
                                  parsed_args.type),
                                  fromlist = ['blah'])
        # Get class of formatter
        format_class = getattr(format_module,
                               FORMAT_MAPPER[parsed_args.type])
        # Instantiate object
        formatter = format_class(f)
        # Now we pass the formatter to whatever
        # Engine we want to use
        # testing
        #for line in formatter.get_result():
            #print line
        # Import the respective engine
        engine_module = __import__('diyr.engines.{}'.format(
                                 parsed_args.mode),
                                 fromlist = ['blah'])
        engine_class = getattr(engine_module,
                               ENGINE_MAPPER[parsed_args.mode])
        engine = engine_class(formatter)
        #engine.run_engine()
        runner = CommandLineRunner(engine)
        runner.run()
        #for line in engine.run_engine():
            #print line
 
    


if __name__ == "__main__":
    main()
