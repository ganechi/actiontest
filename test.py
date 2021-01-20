import requests
import json

def send_slack_webhook(text,url):
	return requests.post(url,{'text': text})

if __name__ == '__main__':
	text = "from GitHub Actions"
	url = "https://hooks.slack.com/services/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"
	result = send_slack_webhook(text,url)
	print(result)
