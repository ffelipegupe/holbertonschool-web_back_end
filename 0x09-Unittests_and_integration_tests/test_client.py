#!/usr/bin/env python3
""" client.py test module """

from client import org
from unittest.mock import Mock, patch
from client import GithubOrgClient
from parameterized import parameterized
from unittest import mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ client test class """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ Method that tests org function """
        gitcli = GithubOrgClient(org_name)
        gitcli.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
