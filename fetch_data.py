# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///
import httpx

client = httpx.Client()
data = client.get("https://raw.githubusercontent.com/zkrising/Tachi/refs/heads/main/seeds/collections/songs-chunithm.json").json()

for datum in data:
    if datum["data"]["genre"] != "ORIGINAL":
        continue

    title = datum["title"]
    artist = datum["artist"]
    version = datum["data"]["displayVersion"]

    escaped_title = title.replace("\"", "\\\"")
    escaped_artist = artist.replace("\"", "\\\"")

    if version == "CHUNITHM":
        version = "ORIGIN"
    elif version == "CHUNITHM PLUS":
        version = "ORIGIN_PLUS"
    else:
        version = version.removeprefix("CHUNITHM ").replace(" ", "_")

    print(f"[\"{escaped_title}\", new Set([TITLE.{version}]), {{ title: \"{version}\" }}, \"\", \"{escaped_artist}\", ORIGINAL_TRACK, OTHER_THEME],")
