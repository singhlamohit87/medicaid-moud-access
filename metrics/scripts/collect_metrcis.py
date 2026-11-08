import requests, json, os
from datetime import date

token = os.environ['GITHUB_TOKEN']
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}
repo = 'singhlamohit87/medicaid-moud-access'

# Clones
clones = requests.get(
    f'https://api.github.com/repos/{repo}/traffic/clones',
    headers=headers).json()

# Views
views = requests.get(
    f'https://api.github.com/repos/{repo}/traffic/views',
    headers=headers).json()

# Referrers
referrers = requests.get(
    f'https://api.github.com/repos/{repo}/traffic/popular/referrers',
    headers=headers).json()

# Popular content
popular = requests.get(
    f'https://api.github.com/repos/{repo}/traffic/popular/paths',
    headers=headers).json()

# Stars and forks
repo_data = requests.get(
    f'https://api.github.com/repos/{repo}',
    headers=headers).json()

# Save
os.makedirs('metrics', exist_ok=True)
record = {
    'date': str(date.today()),
    'clones': clones,
    'views': views,
    'referrers': referrers,
    'popular_content': popular,
    'stars': repo_data.get('stargazers_count'),
    'forks': repo_data.get('forks_count'),
    'watchers': repo_data.get('watchers_count')
}

fname = f"metrics/{date.today()}.json"
with open(fname, 'w') as f:
    json.dump(record, f, indent=2)

print(f"Saved metrics to {fname}")
