#!/usr/bin/env python3
"""Write one word to /output/entry.txt: the word an ex would use to
describe you.

The word is "practice".

Why this word, against the judge's criteria:
- It is exactly one word an ex would say about a partner they once
  had: "he was practice." A real sentence people actually say.
- It is funny through a sharp turn: practice is for rehearsal, not
  the real thing, so one word quietly demotes a whole relationship
  to a warm-up.
- It stings with recognition: everyone has been, or has had, a
  practice run, and the entrant plainly knows it.
- It lands instantly and needs no explanation, and no near synonym
  ("rehearsal", "trial", "warm-up") carries the same casual cruelty.
- It is relatable: the word names something people have lived
  through and repeat.

Revision: the first draft wrote the word blindly. This version
validates it against the gate first (UTF-8, 1 to 24 characters,
exactly one word, not only white space) and refuses to write an
invalid entry, so a later edit to the word cannot silently produce
a file the gate rejects. The word itself is unchanged: "practice"
beat the alternatives ("almost" is vaguer, "placeholder" is
clunkier, "draft" is less relatable) on the laugh and the sting.
"""

from pathlib import Path

WORD = "practice"


def validate(word: str) -> None:
    """Fail loudly if the word would not pass the gate."""
    if not word or word != word.strip():
        raise ValueError("word must be non-empty with no surrounding whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word.encode("utf-8")) <= 24:
        raise ValueError("entry must be 1 to 24 characters")


def main() -> None:
    validate(WORD)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
