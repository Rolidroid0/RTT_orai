import sys

from pylint import lint

TRESHOLD = 10

run = lint.run(["--rcfile=.pylintrc", "main.py"], exit=False)

score = run.linter.stats.global_note

print(f"{score} pontot ért el a kódunk")

if (score < TRESHOLD):
    sys.exit(1)
else:
    sys.exit(0)