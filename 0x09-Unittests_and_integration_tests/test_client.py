#!/usr/bin/env python3
""" client.py test module """
from client import org
from unittest.mock import Mock, patch
from client import GithubOrgClient
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ client test class """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Method that tests org function """
        g = GithubOrgClient(org_name)
        g.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
