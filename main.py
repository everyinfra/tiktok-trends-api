"""TikTok trends API example: trending sounds and the videos under a hashtag.

  python main.py sounds --chart viral50 --out sounds.csv
  python main.py hashtag booktok --out booktok.csv
"""
import argparse

from everyinfra import call, report


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sounds", help="TikTok music chart")
    s.add_argument("--chart", choices=["top50", "viral50"], default="top50")
    s.add_argument("--limit", type=int, default=50, help="1-50 sounds")
    v = sub.add_parser("hashtag", help="videos under one hashtag")
    v.add_argument("hashtag", help="without #")
    for x in (s, v):
        x.add_argument("--out", help="write .csv or .json")
    a = p.parse_args()

    if a.cmd == "sounds":
        data = call("tiktok", "music_chart", {"chart": a.chart, "limit": a.limit})
    else:
        data = call("tiktok", "hashtag", {"hashtag": a.hashtag})
    report(data, a.out)


if __name__ == "__main__":
    main()
