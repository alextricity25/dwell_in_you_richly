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

Example Output
##############

.. code-block::

   I. ___ _______ __ ___ ________
   I. The purose of the training.
   Incorrect.
   A. __ _____ up the trainees in Christ in ___ growth __ ___ life ____ ________
   A. To build up the trainees in Christ in the growth of His life unto maturity
   Amen!
   B. To equip the trainees in the ___________ __ the ______ ______ according to the Scriptures __ ___ revelation of ___ Holy Spirit
   B. To equip the trainees in the realization of the divine truths according to the Scriptures by the revelation of the Holy Spirit
   Amen!
   C. To raise up the trainees in the cultivation __ _____ spiritual capacity in the _________ of the gospel, the nourishing of the young believers, the perfecting of the saints, and the ___________ __ the word of God for ________ up of the local churches, consummating in the building up of ___ Body of Christ

Example with a file containing verses with their corresponding verse refrences:

.. code-block::

   diyr -t referenced_verses -f example_format_types/verse_references.txt -l 8
   _____ __ now then __ condemnation __ those who ___ __ ______ ______ Romans 8:1
   There is now then no condemnation to those who are in Christ Jesus. Romans 8:1
   Amen!
   For __ know that all ______ work together ___ ____ to those ___ love God, __ those who are called according __ ___ purpose, Romans 8:28
   For we know that all things work together for good to those who love God, to those who are called according to His purpose, Romans 8:28
   Amen!
   As it is ________ ___ first ____ ______ _ living soul, the ____ Adam became a ____ giving ______ 1 Corinthians 15:45

Example output when using diyr when specifiying a book and chapter:

.. code-block::

   diyr --book "Romans" --chapter 8 -l 9
   The book Romans chapter 8 will be used
   1. _____ __ ___ then __ ____________ to those ___ ___ __ ______ Jesus.
   1. There is now then no condemnation to those who are in Christ Jesus.
   Amen!
   2. ___ ___ law __ ___ Spirit __ ____ has freed me in Christ _____ from the law of ___ and __ death.
   2. For the law of the Spirit of life has freed me in Christ Jesus from the law of sin and of death.
   Amen!
   3. For that which the law could not ___ __ that __ was weak _______ the ______ ____ sending His ___ Son in the likeness of the flesh of sin ___ concerning sin, _________ sin in the flesh,
   3. For that which the law could not do, in that it was weak through the flesh, God, sending His own Son in the likeness of the flesh of sin but concerning sin, condemned sin in the flesh,
   Incorrect.
   4. That ___ _________ requirement of ___ ___ might __ _________ in us, who do ___ walk _________ __ the flesh but according to the spirit.
