# 🧰 InstructLab Knowledge Utilities

Here's a tiny and hopefully growing collection of utilities to make it easier to create knowledge nodes for 🐶 InstructLab using **Wikipedia**.

Here's what we got so far...

## 1. ✍️ **`wikipedia-attribution-gen.py`**
*🐍 Python script*

This is a small python utility to generate attribution.txt files for wikipedia-based knowledge nodes for InstructLab. It uses the [`wikipedia` pypi package](https://pypi.org/project/wikipedia/) - but note this might not be great for heavy-duty API calls to wikipedia. The PyPi page recommends using [`pywikipediabot`](http://www.mediawiki.org/wiki/Manual:Pywikipediabot) for that. But I didn't, because I'd already written this when I noticed! 🤦‍♀️ *(PRs welcome!!)*

How do you use this?

```
python3 wikipedia-attribution-gen.py <wikipedia article name>
```
Where <wikipedia article name> is the name of a wikipedia article. If the article name has spaces in it, put it in quotes like so:

```
python3 wikipedia-attribution-gen.py "Grace O'Malley"
```
It will spit out an `attribution.txt` in the directory you ran the script from, in [the InstructLab knowledge node attribution format](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#for-your-attributiontxt-file).

Here's an example run:

```
$ python3 wikipedia-attribution-gen.py "Grace O'Malley"
Title of work: Grace O'Malley
Link to work: https://en.wikipedia.org/wiki/Grace_O%27Malley
Revision: https://en.wikipedia.org/w/index.php?title=Grace_O%27Malley&oldid=1236872074
License of the work: CC-BY-SA-4.0
Creator names: Wikipedia Authors
$ 
```
It creates an `attribution.txt` in the directory I ran it from that matches the output it spit out to the terminal.

## 2. 🗂️ **`make-knowledge-node-dirs.sh`**
*⚒️ Bash script*


This script assumes you have a flat directory (or messy directory structure, some strewn across various subdirs, some in the same dir) of markdown files in or under the directory you run the script from. It looks for all `*.md` files in the file tree starting at the current directory (excluding any `README.md` files), creates a subdirectory using the name of each `*.md` file, and moves each `*.md` file into its corresponding directory. Then, it will run through all of those directories and generate an attribution.txt file for each `*.md` file you have!

**✨ it's like magic! ✨**

That was a lot of words. Let me show you an example of how to use it, and then the before and after.

Here's how you use it (make sure you `chmod +x make-knowledge-node-dirs.sh` beforehand):

```
./make-knowledge-node-dirs.sh
```

Whoah yeh that's it! So here's a bit of a before and after. Here's how my files looked before:

#### Before
```
knowledge
- artifacts/
  - boheh_stone.md
  - cloonmorris_ogham_stone.md
- people/
  - grace_o'malley.md
  - james_connolly.md
  - máirtín_ó_direáin.md
- places/
  - clew_bay.md
  - croagh_patrick.md
  - magheracloone.md
  - Westport,_County_Mayo.md
- galway.md
```
Ok, so if you had this layout of files and directories, and you did a `cd` into that top `knowledge` directory and ran `./make-knowledge-node-dirs.sh` in that `knowledge` directory, here is what the after would look like:

#### After
```
knowledge
- artifacts/
  - boheh_stone/
    - attribution.txt
    - boheh_stone.md
  - cloonmorris_ogham_stone/
    - attribution.txt
    - cloonmorris_ogham_stone.md
- people/
  - grace_o'malley/
    - attribution.txt
    - grace_o'malley.md
  - james_connolly/
    - attribution.txt
    - james_connolly.md
  - máirtín_ó_direáin
    - attribution.txt
    - máirtín_ó_direáin.md
- places/
  - clew_bay
    - attribution.txt
    - clew_bay.md
  - croagh_patrick
    - attribution.txt
    - croagh_patrick.md
  - magheracloone
    - attribution.txt
    - magheracloone.md
  - Westport,_County_Mayo
    - attribution.txt
    - Westport,_County_Mayo.md
- galway
  - attribution.txt
  - galway.md
```
