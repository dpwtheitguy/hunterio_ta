import sys
import requests
import sys

from splunklib.searchcommands import dispatch, StreamingCommand, Configuration

### vars
lstEmail = []
api_key="YOURKEYHERE"

### Exec
@Configuration()
class hunterio(StreamingCommand):
  def stream(self, records):
    for record in records:
      domain = record['hunter_domain']
      url = "https://api.hunter.io/v2/domain-search?domain="+ domain +"&api_key="+api_key
      hunterJsonData = requests.get(url)
      for email in hunterJsonData.json()['data']['emails']:
        lstEmail.append(email['value'])

      record['hunter_addresses'] = lstEmail
      yield record

if __name__ == "__main__":
  dispatch(hunterio, sys.argv, sys.stdin, sys.stdout, __name__)
