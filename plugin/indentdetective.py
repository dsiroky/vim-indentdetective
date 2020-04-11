import re

USE_UNKNOWN = 0
USE_TABS = 1
USE_SPACES = 2

def statistics(buf):
    tab_indents = 0
    space_indents = 0
    for line in buf:
        if line.startswith(" "):
            space_indents += 1
        elif line.startswith("\t"):
            tab_indents += 1
    return (tab_indents, space_indents)

def decide(stats):
    UNKNOWN_THRESHOLD = 0.2
    UNKNOWN_THRESHOLD_SUM = 10

    tab_indents, space_indents = stats

    if tab_indents + space_indents < UNKNOWN_THRESHOLD_SUM:
        return USE_UNKNOWN

    minval = min(tab_indents, space_indents)
    maxval = max(tab_indents, space_indents)
    if minval / float(maxval) > UNKNOWN_THRESHOLD:
        return USE_UNKNOWN

    return USE_TABS if tab_indents > space_indents else USE_SPACES
