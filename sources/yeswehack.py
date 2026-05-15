import requests


YWH_URL = "https://api.yeswehack.com/programs"


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_yeswehack_programs():

    try:

        response = requests.get(
            YWH_URL,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return []

        data = response.json()

        programs = []

        for item in data.get("items", []):

            name = item.get("name")

            slug = item.get("slug", "")

            if not name:
                name = slug.replace("-", " ").title()

            programs.append({
                "name": name,
                "platform": "YesWeHack",
                "url": f"https://yeswehack.com/programs/{slug}",
                "scope": slug,
                "mobile": False,
                "graphql": False,
                "waf": False,
                "severity": "unknown"
            })

        return programs

    except Exception as error:
        print(f"[YesWeHack Error] {error}")
        return []
