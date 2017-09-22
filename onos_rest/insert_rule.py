import pycurl
import json

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:8181/onos/v1/flows/of:5e3e486e73020629')
json_rule = {
	  "priority": 400000,
	  "timeout": 0,
	  "isPermanent": True,
	  "deviceId": "of:5e3e486e73020629",
	  "treatment": {
	    "instructions": [
	      {
	        "type": "OUTPUT",
	        "port": "CONTROLLER"
	      }
	    ]
	  },
	  "selector": {
	    "criteria": [
	      {
	        "type": "ETH_TYPE",
	        "ethType": "0x88cc"
	      },
	      {
	        "type": "ETH_DST",
	        "mac": "00:00:11:00:00:01"
	      },
	      {
	        "type": "ETH_SRC",
	        "mac": "00:00:11:00:00:01"
	      }
	    ]
	  }
	}
#post_data = {'field': 'value'}
#post_data = json.loads(json_rule)
post_data = json_rule
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)
c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
c.setopt(pycurl.USERPWD, "onos:rocks")

c.perform()
c.close()
