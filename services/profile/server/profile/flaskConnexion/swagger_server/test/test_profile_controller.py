# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProfileController(BaseTestCase):
    """ProfileController integration test stubs"""

    def test_add_profile(self):
        """Test case for add_profile

        Create a new profile
        """
        profile = Profile()
        response = self.client.open(
            '/cloudmesh/profile/profiles',
            method='PUT',
            data=json.dumps(profile),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profile(self):
        """Test case for get_profile

        
        """
        response = self.client.open(
            '/cloudmesh/profile/profiles',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profile_by_uuid(self):
        """Test case for get_profile_by_uuid

        
        """
        response = self.client.open(
            '/cloudmesh/profile/profiles/{uuid}'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
