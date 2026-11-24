"""One Word From Grandma — entry generator.

Writes exactly one word to /output/entry.txt: the word grandma
would text about AI. She heard 'ChatGPT', understood tea, and
has been calling it this ever since.

Candidate words considered (8):
  1. Robit       - sweet robot typo, but a little obvious and generic.
  2. ChatGPtea   - ChatGPT misheard as tea: AI-specific, warm, instantly
                   readable, and the joke lands with no caption. WINNER.
  3. Roomba      - she names every machine after the vacuum; funny, but
                   it is about a vacuum first and AI second.
  4. Compuder    - classic grandma spelling, but fits any computer topic,
                   not AI in particular.
  5. AskTheGoogle - reads as a phrase squeezed together, not one word.
  6. BiscuitBot  - warm and cute, but invented; the AI link is weaker.
  7. Siri-ously  - relies on a punctuation pun, which the brief forbids.
  8. Clanker     - current robot slang; sounds young and meme-y, not like
                   a warm, baffled grandmother texting her grandchild.

Final word: ChatGPtea (9 code points, within the 1-30 character gate,
a single word with no spaces and no punctuation).
"""

import os

# The entry itself: a single word, kept as a named constant so the
# exact spelling lives in one place and nowhere else in the code.
ENTRY = "ChatGPtea"

# Honour MAKEFUN_OUTPUT_DIR when the harness sets it (local checks
# point it at a temp directory); otherwise keep the contest default.
OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def main() -> None:
    # Validate the entry before writing: exactly one word of 1-30
    # code points, with no whitespace and no punctuation, so a typo
    # in ENTRY fails loudly here instead of silently in the output.
    assert ENTRY == ENTRY.strip() and " " not in ENTRY, "entry must be one word"
    assert ENTRY.isalnum(), "entry must contain no punctuation"
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 code points"
    assert len(ENTRY) == 9, "ChatGPtea is exactly 9 code points"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" keeps the write byte-exact: no trailing newline added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
