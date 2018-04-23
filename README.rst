dwell_in_you_richly
###################
"Let the word of Christ dwell in you richly in all wisdom, teaching and admonishing one another with psalms and hymns and spiritual songs, singing with grace in your hearts to God." - Colossians 3:16

Installation
############

.. code-block:: shell

   pip install diyr

Usage
#####

To have diyr pull a random book and chapter from the internet simply type:

.. code-block:: shell

   diyr

To have diyr process an outline that's on disk, use:

.. code-block:: shell

   diyr -t outline -f <file_path_to_outline_text_file>

To change how many words diyr replaces, use the `-l` flag:

.. code-block:: shell

   diyr -l 9


Quick Start for fill-in-the-blank verse references
##################################################

.. code-block:: shell

   # Install the application
   $ pip install diyr
   # Create a file with a bunch of verse references. For example:
   $ cat ~/verse_references.txt
   There is now then no condemnation to those who are in Christ Jesus. - Romans 8:1
   For we know that all things work together for good to those who love God, to those who are called according to His purpose, - Romans 8:28
   As it is written, the first Adam became a living soul, the last Adam became a life giving Spirit - 1 Corinthians 15:45
   And you, though dead in your offenses and sins, - Ephesians 2:1   

   # Tell diyr the file contains verses with references (-t verse_references), then tell it
   # to quiz you on the verse references (-r)
   # The number of words to be hollowed out can be increased using the '-l' flag:

   $ diyr -f ~/verse_references.txt -l 8 -t referenced_verses -r

Example Output
##############

.. code-block::

   diyr -f ~/Documents/MysteryOfHumanLife/key_one.txt -t outline -l 8 -r
   _________ ___ _______ __ _____ _________
   UNLOCKING THE MYSTERY OF HUMAN EXISTENCE
   Amen!
   _____ ________
   GOD'S CREATION
   Amen!
   1.___ ___ _____ _____
   1.MAN HAS GOD'S IMAGE
   Amen!
   ___ God said, ___ Us make ___ in ___ ______ _________ __ ___ likeness.
   And God said, Let Us make man in our image, according to our likeness.
   Amen!
   Type the verse references verbatim:
   Genesis 1:26
   Amen!
   _____ ________ __ man is _________ ____ His ________ __ all _____ things.
   God's creaatin of man is different then His creation of all things. 
   Incorrect. Delta show below:
   - god's creaatin of man is different then his creation of all things.
   ?           -                        ^^^^
   + god's creation of man is different from his creation of all other things.
   ?             +                      ^^^^                     ++++++

Delta's will be printed when a line is inputted incorrectly.
Example with a file containing verses with their corresponding verse refrences:

Example output when using diyr when specifiying a book and chapter (must be connected to internet):

.. code-block::

   diyr --book Romans --chapter 8 -l 8
   The book Romans chapter 8 will be used
   1._____ __ now ____ __ ____________ to _____ who are __ ______ Jesus.
   1.There is now then no condemnation to those who are in Christ Jesus.
   Amen!
   2.For the ___ of the Spirit of ____ has _____ me __ Christ Jesus from ___ law of sin ___ __ ______
   2.For the law of the Spirit of life has freed me in Christ Jesus from the law of sin and of death.
   Amen!
   3.For that _____ ___ law could not do, in that __ was ____ through the flesh, God, sending His own Son in the ________ of ___ flesh of ___ ___ concerning sin, condemned sin in the flesh,
   3.For that which the law could not do, in that it was weak through the flesh, God, sending His own Son in the likeness of the flesh of sin, and concerning sin, conmnedd sin in the flesh,
   Incorrect. Delta show below:
   - 3.for that which the law could not do, in that it was weak through the flesh, god, sending his own son in the likeness of the flesh of sin, and concerning sin, conmnedd sin in the flesh,
   ?                                                                                                                                           -                           -
   + 3.for that which the law could not do, in that it was weak through the flesh, god, sending his own son in the likeness of the flesh of sin and concerning sin, condemned sin in the flesh,
   ?                                                                                                                                                                   ++
   
Enabling 'NAIL-IT' mode
#######################

NAIL-IT Modes helps the user really get the content into them by prompting them to re-enter any incorrectly typed line three times.

To enable 'NAIL-IT' mode, use the `-n` flag. 

Shuffling the data
##################
The data can be shuffled using the `-s` flag.
