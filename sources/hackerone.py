import requests


H1_URL = "https://hackerone.com/directory/programs"


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_hackerone_programs():

    try:

        response = requests.get(
            H1_URL,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return []

        programs = []

        lines = response.text.splitlines()

        for line in lines:

            if "handle" in line:

                programs.append({
                    "name": "HackerOne Program",
                    "platform": "HackerOne",
                    "url": H1_URL,
                    "scope": "*",
                    "mobile": False,
                    "graphql": False,
                    "waf": False,
                    "severity": "unknown"
                })

                break

        return programs

    except Exception as error:
        print(f"[HackerOne Error] {error}")
        return []
