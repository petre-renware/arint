# -*- coding: utf-8 -*-
# zato: ide-deploy=True

from zato.server.service import Service

class GetSomeData(Service):
    """ Returns details of a user by the person's ID.
    """
    name = 'ari.get-some-data'

    def handle(self):

        # For now, return static data only
        self.response.payload = {
            'user_name': 'petrica iordanescu',
            'user_type': 'SRT', 
            'virsta': '53' 
        }