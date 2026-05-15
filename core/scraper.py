from sources.hackerone import fetch_hackerone_programs
from sources.bugcrowd import fetch_bugcrowd_programs
from sources.yeswehack import fetch_yeswehack_programs


def deduplicate(programs):

    seen = set()
    unique = []

    for program in programs:

        key = (
            program.get("name", "").lower(),
            program.get("platform", "").lower()
        )

        if key not in seen:
            seen.add(key)
            unique.append(program)

    return unique


def fetch_programs():

    programs = []

    # HackerOne temporarily disabled
    # programs.extend(fetch_hackerone_programs())

    programs.extend(fetch_bugcrowd_programs())
    programs.extend(fetch_yeswehack_programs())

    return deduplicate(programs)
