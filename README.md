## Christian Höltje's Python Morse Tutoring Program

Hello all!

I wrote this software because a friend of mine, Paul Guido (N5UIT)
was doing a morse course for the San Antonio Radio Club.  The software
he used was not full free.  It had a shareware limited mode and cost
$40 to register.

This seemed to go against the HAM spirit of promoting the hobby and
also offended me in that I know writing morse software isn't hard.
Also as an advocate of Free (as in liberty, something all Texans
care about) Software I thought this was something that should be
free.  (See http://www.gnu.org/ for more info)

So I wrote my own.  It wasn't very hard.  At this time I have spent
significantly less than a week of time to produce a full featured,
correct sounding, perfect timed version that'll help anyone pass
the ARRL and FCC exams.

I hope you like it.

BTW: The webster2 is *not* GPL.  It's technically in the public
domain as it's 1934 copyright has expired.  It's the Webster's
Unabridged dictionary distilled into a word list.  I got this
from NetBSD and seems to have been formatted by a James Woods.

Ciao!

-– Christian Höltje

File bugs, view source, etc. at
[github](http://github.com/docwhat/morse-python)

Requirements:
 * Python version 2.2 (you can get this from http://python.org/) It may work on newer versions, dunno.

Suggested Extras:
 * PyGame -- a cross platform game development library for playing sound on a lot of platforms (Windows, Unix, Mac OS, etc...)
 * SDL -- Required for PyGame
 * PyESD -- for playing under ESound in Unix operating systems.