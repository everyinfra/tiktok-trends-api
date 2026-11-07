# TikTok Trends API

Read TikTok trends from Python: the trending sounds chart (Top 50 or Viral 50) with use counts, and the videos under any hashtag with views, likes, comments and shares. Each call is one POST request to the EveryInfra API. A new account can try it with $1 of trial credit, no card needed.

Also covers: TikTok trends API free, TikTok data API free.

## Quick start

```bash
git clone https://github.com/everyinfra/tiktok-trends-api.git
cd tiktok-trends-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=your_key   # get one at everyinfra.com
python main.py sounds --chart viral50 --out sounds.csv
python main.py hashtag booktok --out booktok.csv
```

Get an API key: [everyinfra.com/en/docs](https://everyinfra.com/en/docs?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api#quickstart). Without `--out`, the script prints the first three rows as JSON.

## Price

| Call | Price per 1,000 calls | Rows per call |
|---|---|---|
| [`tiktok/music_chart`](https://everyinfra.com/en/tiktok-api/music_chart?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api) | $0.81 | 50 in our test |
| [`tiktok/hashtag`](https://everyinfra.com/en/tiktok-api/hashtag?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api) | $0.56 | 10 in our test |

- You pay per call, not per month. Failed calls and empty results are not charged.
- New accounts can claim $1 of trial credit: create an account, star [everyinfra-agent-plugins](https://github.com/everyinfra/everyinfra-agent-plugins) and [seo-skills](https://github.com/everyinfra/seo-skills), then claim it in the console. It is valid for 24 hours and needs no card. See [pricing](https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api).

## What you get

### `music_chart`

| Field | Meaning |
|---|---|
| `rank` | Position on the chart. |
| `id` | The record's unique ID on the platform. Unique only within one platform; IDs can repeat across platforms. |
| `url` | Link to the record on the platform. |
| `title` | Title. null when the platform has no titles (for example text-only posts). |
| `author_name` | Author's display name. |
| `album` | Album name. |
| `language` | Content language code (for example zh, en) as judged by the platform; it can be wrong. |
| `duration_seconds` | Duration in seconds. null for content that is not video or audio. |
| `duration_sec` | Duration in seconds. |
| `released_at` | Release date of the track. |
| `cover_image_url` | Cover image link. |
| `audio_url` | Audio file link. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |

Also returned, named as on the platform: `use_count`, `is_commercial`.

Full parameter list: [TikTok music chart API](https://everyinfra.com/en/tiktok-api/music_chart?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api).

### `hashtag`

| Field | Meaning |
|---|---|
| `id` | The record's unique ID on the platform. Unique only within one platform; IDs can repeat across platforms. |
| `url` | Link to the record on the platform. |
| `text` | Body text with HTML removed, returned in full and never cut short (on a few platforms the list results themselves carry only an excerpt; the platform's field notes say so). |
| `author_name` | Author's display name. |
| `author_username` | Author's username (@handle), usually usable in URLs. |
| `like_count` | Likes. null means the platform or this capability does not disclose it; it is not 0. |
| `comment_count` | Comments. null means not disclosed, not 0. |
| `share_count` | Shares. null means not disclosed, not 0. |
| `view_count` | Views or plays. null means not disclosed, not 0. |
| `posted_at` | Publish time in ISO 8601, UTC (for example 2026-08-07T12:34:56+00:00). Non-standard strings from the platform are passed through as is, so parse defensively. null means the platform does not disclose it. |
| `collect_count` | Saves or favorites. null means not disclosed, not 0. |
| `repost_count` | Reposts (as distinct from quote posts). null means not disclosed. |
| `duration_sec` | Duration in seconds. |
| `duration_seconds` | Duration in seconds. null for content that is not video or audio. |
| `cover_image_url` | Cover image link. |
| `language` | Content language code (for example zh, en) as judged by the platform; it can be wrong. |
| `country` | Country or region: a full name or an ISO code depending on the platform, not normalized. |
| `hashtags` | Hashtags in the text, in order of appearance; absent when there are none. |
| `author_id` | Author's unique ID on the platform. |
| `author_url` | Link to the author's profile on the platform. |
| `author_avatar_url` | Author's profile picture link. |
| `author_follower_count` | Author's follower count. null means not disclosed. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |

Also returned, named as on the platform: `music`, `is_ad`, `is_pinned`, `is_sponsored`, `is_slideshow`, `has_shop_product`, `author_bio`, `author_is_verified`, `author_is_private`, `author_is_seller`, `author_following_count`, `author_like_count`, `author_video_count`.

Full parameter list: [TikTok hashtag API](https://everyinfra.com/en/tiktok-api/hashtag?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api).

## Tested

We ran both commands against the live API before publishing this repository (times in Singapore time, UTC+8).

| Command | Run at (SGT) | Rows | Charged |
|---|---|---|---|
| `sounds --chart viral50` | 2026-11-08 03:37 | 50 | $0.000806 |
| `hashtag booktok` | 2026-11-08 03:37 | 10 | $0.000556 |

First row of the `music_chart` result (long text cut, author fields left out of this sample):

```json
{
  "rank": 1,
  "id": "6919100601457215489",
  "url": "https://www.tiktok.com/music/Ramalama-Bang-Bang-6919100601457215489",
  "title": "Ramalama (Bang Bang)",
  "album": "Ruby Blue",
  "language": "English",
  "duration_seconds": 60,
  "use_count": 851917,
  "is_commercial": false,
  "released_at": "2005-06-13T00:00:00+00:00",
  "audio_url": "https://sf19.tiktokcdn-us.com/obj/tos-alisg-ve-2774/osB5IlusAw6WW1OrKrtytJAUi0avPyYkKiXMW",
  "platform": "tiktok",
  "duration_sec": 60
}
```

## How it works

Every call is one request. `everyinfra.py` wraps it in about 60 lines of `requests`:

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"platform": "tiktok", "action": "music_chart", "params": {"chart": "viral50"}}'
```

- Slow actions (Instagram `user_posts`, for example) answer with a `job_id`. The script polls `GET /api/v1/jobs/{job_id}` every 5 seconds; polling is free.
- Errors come back as JSON with a code, a message and whether you were charged. A missing parameter returns 422 before any charge.
- The same key also works over MCP for Claude, Cursor and other AI agents: [docs](https://everyinfra.com/en/docs?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api).

## More

- [TikTok API on EveryInfra](https://everyinfra.com/en/tiktok-api?utm_source=github&utm_medium=example_repo&utm_campaign=tiktok-trends-api): every TikTok action, with prices and live health
- Other examples: [google-maps-scraper](https://github.com/everyinfra/google-maps-scraper) · [instagram-scraper-python](https://github.com/everyinfra/instagram-scraper-python) · [tiktok-scraper-python](https://github.com/everyinfra/tiktok-scraper-python) · [douyin-api-python](https://github.com/everyinfra/douyin-api-python)

## License

MIT
