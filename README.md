# txtstats

Count lines, words and characters in text files or standard input.

## Usage

```
python txtstats.py [files...]
```

- `python txtstats.py notes.txt` — print per-file statistics.
- `cat data.txt | python txtstats.py` — read from standard input.
- With several files a total line is printed too.

Example:

```
$ python txtstats.py notes.txt
notes.txt: lines=12 words=45 chars=320
```
