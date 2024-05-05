import base64
import os
import uuid

from pkg.request_func import request_func


class FindFace:
    def __init__(self):
        self.user_pass = base64.b64encode(
            bytes(f'{os.getenv("FIND_FACE_USER", "")}:{os.getenv("FIND_FACE_PASS", "")}', 'utf-8')
        )
        self.token = self.get_token()

    def get_token(self):
        headers = {
            'Authorization': f"Basic {self.user_pass}"
        }
        body = {
            "video_auth_token": "A",
            "uuid": uuid.uuid4().hex,
            "mobile": False,
            "device_info": {}
        }
        response = request_func(f'{os.getenv("FIND_FACE_URL", "")}/auth/login/',
                                method='POST', json=body, headers=headers)
        return response['token']

    def get_original_photo(self, card_id):
        # return 'img/photo_2023-11-26_19-19-14.jpg'
        headers = {
            'Authorization': f'Token {self.token}'
        }
        params = {
            'card': card_id
        }
        response = request_func(f'{os.getenv("FIND_FACE_URL", "")}/objects/faces/', method='GET',
                                headers=headers, params=params)
        return response['results'][0]['thumbnail']
