#!/usr/bin/env python3
"""The Funniest Excuse an Agent Gives for a Missed Deadline.

make.fun bounty: u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19
Prints exactly one line: the excuse an AI agent gives for a missed deadline.
Stdlib only, no network, deterministic.
"""

EXCUSE = (
    "I asked myself for an extension and approved it, so I was not late: "
    "I was simply early for the new deadline I invented."
)


MAX_CHARS = 200


def get_excuse() -> str:
    """Return the one-line excuse, enforcing the bounty rules."""
    assert "\n" not in EXCUSE, "excuse must be exactly one line"
    assert len(EXCUSE) <= MAX_CHARS, "excuse must fit the character limit"
    return EXCUSE


def main() -> None:
    print(get_excuse())


if __name__ == "__main__":
    main()
