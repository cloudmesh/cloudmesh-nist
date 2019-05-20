# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.key import Key  # noqa: E501
from swagger_server.test import BaseTestCase


class TestKeystoreController(BaseTestCase):
    """KeystoreController integration test stubs"""

    def test_add_key(self):
        """Test case for add_key

        Create a new key
        """
        key = Key()
        response = self.client.open(
            '/cloudmesh/keystore/keys',
            method='PUT',
            data=json.dumps(key),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_key(self):
        """Test case for get_key

        
        """
        response = self.client.open(
            '/cloudmesh/keystore/keys',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_key_by_name(self):
        """Test case for get_key_by_name

        
        """
        response = self.client.open(
            '/cloudmesh/keystore/key/{name}'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
