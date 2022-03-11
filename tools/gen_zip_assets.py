#!/usr/bin/env python3

import datetime
import hashlib
import requests
import sys
import xml.etree.ElementTree as ET

ASSETS_URL = 'https://downloadirpf.receita.fazenda.gov.br/irpf/{year:d}/irpf/update/{path:s}'

def usage():
    print(f'Usage: {sys.argv[0]} <year>')
    sys.exit(1)

if len(sys.argv) < 2:
    year = datetime.datetime.now().year
else:
    year = sys.argv[1]
    if year.isnumeric():
        year = int(year)
    else:
        print('Error: Year argument must be numeric.')
        usage()

final_url = ASSETS_URL.format(year = year, path = 'latest.xml')

print('Requesting URL:', final_url)

try:
    r = requests.get(final_url)
except Exception as err:
    print('Error:', err)
    sys.exit(1)

if r.status_code != 200:
    print('Error: Unexpected HTTP response code:', r.status_code)
    sys.exit(1)

try:
    root = ET.fromstring(r.text)
except:
    print('Error: Unable to parse the following data as XML:\n')
    print(r.text)
    sys.exit(1)

zip_assets = root.findall('.//extra/files/file')
total = len(zip_assets)

if total == 0:
    print('Found no zip assets.')
    sys.exit(1)

print('Found a total of', len(zip_assets), 'zip assets.')
count = 1
assets = []

for file in zip_assets:
    id = path = file.find('fileId').text
    path = file.find('filePackageName').text

    if not path.endswith('.zip'):
        print(f'WARNING: Ignoring asset \'{path}\' because it doesn\'t seem to be a zip asset.')
        count += 1
        continue

    zip_url = ASSETS_URL.format(year = year, path = path)

    try:
        print(f'Requesting zip asset #{count} of #{total} at:', zip_url)
        r = requests.get(zip_url)
    except Exception as err:
        print('Error:', err)
        sys.exit(1)

    sha256 = hashlib.sha256(r.content).hexdigest()

    assets.append({
        'id': id,
        'url': zip_url,
        'sha256': sha256
    })
    count += 1

assets = sorted(assets, key = lambda i: i['id'])

print('\nDone! YAML-formatted response:')

print('\nsources:')
for asset in assets:
    print('  - type: archive')
    print('    url:', asset['url'])
    print('    sha256:', asset['sha256'])
    print('    strip-components: 2')