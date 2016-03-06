# markov-text-generator
A simple Markov text generator. Supports Python2 and Python3.

Have it write lyrics, required coursework, arcane texts; anything your heart
desires.

Included are two sample texts: William Blake's ["And did those feet..."][0]
and Van Der Graaf Generator's ["A Plague of Lighthouse Keepers"][1]
([lyrics][2]). Go nuts.

### Command line arguments and flags.
```
usage: text-generator.py [-h] [--length [length]] [--lower [lower]]
                         [--punct [punct]]
                         file [file ...]

Generates text using a Markov text generator

positional arguments:
  file               the file to read in as source

optional arguments:
  -h, --help         show this help message and exit
  --length [length]  the length of text to output
  --lower [lower]    y/yes/true: force all words to lowercase
  --punct [punct]    y/yes/true: strip punctuation from input file
```

### Example usage

```
>>> python text-generator.py lighthouse.txt

But sea will I count the points of the hands stretch in the iron-jaw mask,
lost my eyes on window-slits, the best I stay in. I know that there's no
harbour left to feel like seaweed...I'm so that there's no paraffin for my
eyes have blunt scissors, I am so far out of mine? Would you around me, I join
or do I crawl the stranger I am drowning - hands of the table lies blank paper
and if I am drowning - hands stretch in the light,. I let me deep: one more
haggard drowned man. Do I am.
```

```
>>> python text-generator.py and_did_those_feet.txt

Jerusalem builded here, Among these dark Satanic Mills? Bring me my Sword
sleep in ancient time, Walk upon Englands pleasant pastures seen! And did
the Countenance Divine, Shine forth upon our clouded hills? And was the
Countenance Divine, Shine forth upon Englands mountains green: And did those
feet in my Arrows of desire: Bring me my Bow of God, On Englands mountains
green: And did those feet in ancient time, Walk upon our clouded hills? And
did the Countenance Divine, Shine forth upon our clouded hills? And was
Jerusalem builded here, Among these dark Satanic Mills? Bring me my Arrows.
```

```
>>> python text-generator.py and_did_those_feet.txt --punct False --lower True --length 50

Shall my chariot of burning gold bring me my bow of god on englands green
pleasant pastures seen and did those feet in englands pleasant pastures seen
and was the holy lamb of burning gold bring me my sword sleep in my hand till
we have built jerusalem in.
```

[0]: https://en.wikipedia.org/wiki/And_did_those_feet_in_ancient_time
[1]: https://en.wikipedia.org/wiki/A_Plague_of_Lighthouse_Keepers
[2]: http://sofasound.com/vdgcds/phtlyrics.htm#3
