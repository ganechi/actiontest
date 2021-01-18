import requests
import json

def send_slack_webhook(text,url):
	result = requests.post(url, data = json.dumps({
			'text': text
	}))
	return result

if __name__ == '__main__':
	text = "from GitHub Actions"
	url = "https://hooks.slack.com/services/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"
	result = send_slack_webhook(text,url)
	print(result)
