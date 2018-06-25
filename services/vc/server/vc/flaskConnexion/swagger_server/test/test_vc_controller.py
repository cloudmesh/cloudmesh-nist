# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.node import Node  # noqa: E501
from swagger_server.models.vc import VC  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVcController(BaseTestCase):
    """VcController integration test stubs"""

    def test_add_vc(self):
        """Test case for add_vc

        Create a new vc
        """
        vc = VC()
        response = self.client.open(
            '/cloudmesh/vc/vcs',
            method='PUT',
            data=json.dumps(vc),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vc(self):
        """Test case for get_vc

        
        """
        response = self.client.open(
            '/cloudmesh/vc/vcs',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vc_by_name(self):
        """Test case for get_vc_by_name

        
        """
        response = self.client.open(
            '/cloudmesh/vc/vcs/{vcname}'.format(vcname='vcname_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vc_fe_by_name(self):
        """Test case for get_vc_fe_by_name

        
        """
        response = self.client.open(
            '/cloudmesh/vc/vcs/{vcname}/fe'.format(vcname='vcname_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vc_node_by_name(self):
        """Test case for get_vc_node_by_name

        
        """
        response = self.client.open(
            '/cloudmesh/vc/vcs/{vcname}/{nodename}'.format(vcname='vcname_example', nodename='nodename_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
