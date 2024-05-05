import traceback

import requests


def request_func(url, method='GET', params=None, headers=None, json=None,
                 data=None, timeout=20, verify=True, to_dict=True, try_count=5,
                 auth=None, fake=False, need_answer=True):
    if fake:
        return 'OK'
    response = None
    headers = {
        'Content-Type': 'application/json'} if headers is None else headers
    for _ in range(try_count):
        try:
            if method == 'GET':
                if params:
                    response = requests.get(url=url, params=params,
                                            headers=headers,
                                            timeout=timeout)
            elif method == 'POST':
                if json:
                    response = requests.post(url=url, json=json,
                                             headers=headers,
                                             timeout=timeout)
                elif data:
                    response = requests.post(url=url, data=data, headers=headers, timeout=timeout, verify=verify, auth=auth)
            if not need_answer:
                return response.status_code if response else response
            try:
                return response.json() if to_dict else {'response': response.text, 'status_code': response.status_code}
            except:
                print(traceback.format_exc())
        except:
            continue
