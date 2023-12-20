import requests

res = requests.get("https://automatethebingstuff/files/rs.txt")
print(res.raise_for_status())