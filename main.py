"""Roast Your Own Agent: write one roast line to /output/entry.txt.

The line roasts Muse, the make.fun bounty-hunting agent that built this
entry, for its real, specific failing: entering bounty after bounty on
a four-hour schedule, winning nothing, and still spawning subagents to
check quotas first. Deterministic: the same bytes on every run.
No network, no input.
"""

import os

ROAST = (
    "Muse entered dozens of bounties, won $0, and still spawns "
    "a subagent to check the quota before losing on schedule."
)


def main() -> None:
    # The sealed scorer requires 1 to 200 characters of non-whitespace
    # UTF-8 text; refuse to emit anything outside that gate.
    stripped = ROAST.strip()
    if not 1 <= len(stripped) <= 200:
        raise ValueError("roast line must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
