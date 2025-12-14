# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///
import httpx

client = httpx.Client()
data = client.get("https://chunithm.beerpsi.cc/songs").json()

with open("tmp.js", "w", encoding="utf-8") as f:
    f.write("[\n")
    for datum in data:
        if datum["genre"] != "ORIGINAL":
            continue

        title = datum["title"]
        artist = datum["artist"]
        version = datum["version"]

        escaped_title = title.replace('"', '\\"')
        escaped_artist = artist.replace('"', '\\"')

        if version == "CHUNITHM":
            version = "ORIGIN"
        elif version == "CHUNITHM PLUS":
            version = "ORIGIN_PLUS"
        else:
            version = version.replace(" ", "_")

        f.write(
            f'    ["{escaped_title}", new Set([TITLE.{version}]), {{ title: "{version}" }}, "", "{escaped_artist}", ORIGINAL_TRACK, OTHER_THEME],\n'
        )
    f.write("]\n")
