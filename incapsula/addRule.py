#!/usr/bin/env python3

"""Posts a new rule to a specified site

https://docs.imperva.com/bundle/cloud-application-security/page/api/sites-api.htm#Add2

 site_id -- numerical site id to add rule to
 rule_name -- the string that will label the rule in the UI
 rule_filter -- the logic filter to identify traffic (max 400 chars)
 action -- the action applied to traffic matching the rule_filter (Defaults to alert mode)
    RULE_ACTION_ALERT, RULE_ACTION_BLOCK, RULE_ACTION_CAPTCHA, etc. (fully documented in link above)
 api_id -- API ID to use (Default: environment variable)
 api_key -- API KEY to use (Default: environment variable)
"""

import os
import requests
from .com_error import errorProcess

api_endpoint = 'https://my.incapsula.com/api/'


def addRule(
        site_id, rule_name, rule_filter, action="RULE_ACTION_ALERT", api_id=os.environ.get('API_ID'),
        api_key=os.environ.get('API_KEY')):

    url = api_endpoint+'prov/v1/sites/incapRules/add'
    try:
        payload = {
            'site_id': site_id,
            'name': rule_name,
            'filter': rule_filter,
            'action': action,
            'api_id': api_id,
            'api_key': api_key
        }
        r = requests.post(url, data=payload)
        return r.text
    except Exception as error:
        return errorProcess(error)


