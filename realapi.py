"""
curl 'https://twitter.com/i/api/graphql/Qs44y3K0SXxItjNi6mUFQA/UserByRestId?variables=%7B%22userId%22%3A%22330262748%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D' \
  -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' \
  -H 'cookie: g_state={"i_l":0}; kdt=VRPpBrW3WHP97FAIdyKav6HuvUqWy4APgc19QpyQ; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A166263934843765962; guest_id_marketing=v1%3A166263934843765962; _gid=GA1.2.119190774.1669718079; eu_cn=1; des_opt_in=Y; _gcl_au=1.1.1872515193.1669723260; mbox=session#6389d4dc8f7d40f6afc664d4acce0f38#1669725214|PC#6389d4dc8f7d40f6afc664d4acce0f38.37_0#1732968154; _ga=GA1.2.1764267700.1663923628; _ga_34PHSZMC42=GS1.1.1669723258.1.1.1669725145.0.0.0; dnt=1; _sl=1; personalization_id="v1_8/lZWxCd5kw+HHjzmovCAg=="; guest_id=v1%3A166973081530683067; ct0=5e7db807e543737b4e3139cb10115ced; gt=1597592951600955394' \
  -H 'sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"' \
  -H 'x-csrf-token: 5e7db807e543737b4e3139cb10115ced' \
  -H 'x-guest-token: 1597660603535032321' \

  """

import requests
from urllib.parse import unquote
import json
import pprint


variables= {
  "userId":"134234000",
  "withSafetyModeUserFields":True,
  "withSuperFollowsUserFields":True
}
features= {
  "responsive_web_twitter_blue_verified_badge_is_enabled":True,
  "verified_phone_label_enabled":False,
  "responsive_web_graphql_timeline_navigation_enabled":True
}

params = {'variables':variables, 'features': features}


headers = {
  'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
  'x-guest-token': '1597660603535032321'
}

url = 'https://twitter.com/i/api/graphql/Qs44y3K0SXxItjNi6mUFQA/UserByRestId'
url = unquote(url)

params = {x:json.dumps(y) for x,y in params.items()}
r = requests.get(url, params=params, headers=headers)
assert r.status_code == 200, f"got status {r.status_code}"

# print(r.status_code, r.text)
pprint.pprint(r.json())