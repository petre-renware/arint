# -*- coding: utf-8 -*-
# zato: ide-deploy=True

# Zato
from zato.server.service import Service

# ##############################################################################

class GetUserDetails(Service):
    """ Returns details of a user by the person's ID.
    """
    name = 'api.user.get-details'

    def handle(self):

        # For later use
        user_name = self.request.payload['user_name']

        # Get data from CRM ..
        crm_data = self.invoke_crm(user_name)

        # .. extract the CRM information we are interested in ..
        user_type = crm_data['UserType']
        account_no = crm_data['AccountNumber']

        # .. get data from Payments ..
        payments_data = self.invoke_payments(user_name, account_no)

        # .. extract the CRM data we are interested in ..
        account_balance = payments_data['ACC_BALANCE']

        # .. optionally, notify the fraud detection system ..
        if self.should_notify_fraud_detection(user_type):
            self.notify_fraud_detection(user_name, account_no)

        # .. now, produce the response for our caller.
        self.response.payload = {
          'user_name': user_name,
          'user_type': user_type,
          'account_no': account_no,
          'account_balance': account_balance,
      }

# ##############################################################################

    def invoke_crm(self, user_name):

        # Log what we are about to do
        self.logger.info('Invoking CRM; u=%s', user_name)

        # Obtain a connection to CRM ..
        conn = self.out.rest['CRM'].conn

        # .. produce a request for CRM ..
        request = {
            'UserName': user_name,
        }

        # .. invoke the CRM ..
        crm_response = conn.get(self.cid, request)

        # .. return data received from CRM.
        return crm_response.data

# ##############################################################################

    def invoke_payments(self, user_name, account_no):

        # Log what we are about to do
        self.logger.info('Invoking Payments; u=%s, a=%s', user_name, account_no)

        # Obtain a connection to Payments ..
        conn = self.out.rest['Payments'].conn

        # .. prepare a request for Payments ..
        request = {
            'ACC_NUM': account_no,
        }

        # .. prepare query string parameters ..
        params={'USER':user_name}

        # .. invoke Payments ..
        response = conn.post(self.cid, params=params)

        # .. return data received from Payments.
        return response.data

# ##############################################################################

    def notify_fraud_detection(self, user_name, account_no):

        # Log what we are about to do
        self.logger.info('Notifying Fraud detection; u=%s', user_name)

        # Data to send to the Fraud detection system
        data = 'User `{}` accessed `{}`'.format(user_name, account_no)

        # AMQP configuration
        outconn = 'Fraud Detection Connection'
        exchange = '/tutorial'
        routing_key = 'api'

        # Send the message to Fraud Detection
        self.out.amqp.send(data, outconn, exchange, routing_key)

# ##############################################################################

    def should_notify_fraud_detection(self, user_type):
        return self.kvdb.conn.get('notify.fraud.{}'.format(user_type))

# ##############################################################################