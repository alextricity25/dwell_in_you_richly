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

import logging
import os
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

SINK_MAPPER = {
    'seek': 'SeekSinkClass',
    'shuffle': 'Shuffle',
    'nothing': 'NothingSink'
}


def main():
    parsed_args = args.get_parser().parse_args()

    # Setting up logging
    log_file = os.path.expanduser("~/diyr.log")
    numeric_level = getattr(logging, parsed_args.loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log Level: {}'.format(parsed_args.loglevel))
    logging.basicConfig(filename = log_file, level = numeric_level)

    # If file argument is used, then use the FileSourceClass source plugin
    if parsed_args.file:
        from diyr.sources.file import FileSourceClass
        source_class = FileSourceClass(parsed_args.file)
    # If a file argument is not used, then online.recoveryversion.bible
    # is used as a source.
    # For now, a random book and chapter will be used and ran through
    # the formatter and engine.
    else:
        from diyr.sources.online import OnlineSourceClass
        source_class = OnlineSourceClass(
            "http://online.recoveryversion.bible/txo",
            book = parsed_args.book,
            chapter = parsed_args.chapter
        )

    stream_object = source_class.get_stream()

    # Import respective formattype module
    format_module = __import__('diyr.formattypes.{}'.format(
                              parsed_args.type),
                              fromlist = ['blah'])
    # Get class of formatter
    format_class = getattr(format_module,
                           FORMAT_MAPPER[parsed_args.type])
    # Instantiate object
    formatter = format_class(stream_object)
    # Now we pass the formatter to whatever
    # Engine we want to use
    # Import the respective engine
    engine_module = __import__('diyr.engines.{}'.format(
                                parsed_args.mode),
                                fromlist = ['blah'])
    engine_class = getattr(engine_module,
                           ENGINE_MAPPER[parsed_args.mode])
    engine = engine_class(formatter, level = parsed_args.level)

    # Time for the sinks to do their thing!
    # At this time only the shuffle sink is available.
    if parsed_args.shuffle:
        sink_name = "shuffle"
    elif parsed_args.pattern:
        sink_name = "seek"
    else:
        sink_name = "nothing"
    sink_module = __import__('diyr.sinks.{}'.format(
                              sink_name),
                              fromlist = ['blah'])
    sink_class = getattr(sink_module,
                         SINK_MAPPER[sink_name])
    sink = sink_class(
        engine,
        pattern = parsed_args.pattern if parsed_args.pattern else ''
    )
    data = sink.process()

    runner = CommandLineRunner(data, parsed_args)
    runner.run()
 

if __name__ == "__main__":
    main()
