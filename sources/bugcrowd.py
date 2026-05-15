import requests
import re
import html
import json


BUGCROWD_URL = "https://bugcrowd.com/programs"


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_bugcrowd_programs():

    try:

        response = requests.get(
            BUGCROWD_URL,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return []

        content = response.text

        match = re.search(
            r'data-react-props="(.*?)"',
            content
        )

        if not match:
            print("[Bugcrowd] No react props found")
            return []

        raw_json = html.unescape(match.group(1))

        data = json.loads(raw_json)

        programs = []

        request_params = data.get("requestParams", "")

        if "bug_bounty" not in request_params:
            return []

        programs.append({
            "name": "Bugcrowd Public Programs",
            "platform": "Bugcrowd",
            "url": BUGCROWD_URL,
            "scope": "*",
            "mobile": False,
            "graphql": False,
            "waf": False,
            "severity": "unknown"
        })

        return programs

    except Exception as error:
        print(f"[Bugcrowd Error] {error}")
        return []
