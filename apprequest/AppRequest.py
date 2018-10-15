"""
author: arun.rs
21st September 2018
"""
import uuid

class AppRequest(object):
    """

    """
    __request_id = None

    def __init__(self):
        pass

    def get_request_id(self, renew=False):
        """
        :Brief: This method is used in every place to get the already generated request ID or
        generate new request ID and sent off
        """
        if not AppRequest.__request_id or renew:
            self.set_request_id(uuid.uuid1())
        return AppRequest.__request_id

    def set_request_id(self, value):
        """
        :Brief: This method is used by entry points where the incoming HTTP request has the
        request ID in its headers
        """
        AppRequest.__request_id = value