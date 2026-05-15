import requests


INTIGRITI_URL = "https://api.intigriti.com/core/public/programs"


def fetch_intigriti_programs():
    try:
        response = requests.get(INTIGRITI_URL, timeout=10)

        if response.status_code != 200:
            return []

        data = response.json()

        programs = []

        for item in data:
            handle = item.get("handle", "")

            programs.append({
                "name": item.get("name", "Unknown"),
                "platform": "Intigriti",
                "url": f"https://app.intigriti.com/programs/{handle}",
                "scope": handle,
                "mobile": False,
                "graphql": False,
                "waf": False,
                "severity": "unknown"
            })

        return programs

    except Exception as error:
        print(f"[Intigriti Error] {error}")
        return []
