#!/usr/bin/env python3
""" client.py test module """
from unittest.mock import Mock, patch, PropertyMock
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
    def test_org(self, name, mock):
        """ Method that tests org function """
        gitcli = GithubOrgClient(name)
        gitcli.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{name}')

    def test_public_repos_url(self):
        """ Method that tests _public_repos_url function """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @mock.patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ Method that tests public_repos function """
        mock_get_json.return_value = [{"name": "google"},
                                      {"name": "abc"}]
        with mock.patch.object(GithubOrgClient, "_public_repos_url",
                               new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "http://testurl.com"
            g_client = GithubOrgClient("facebook")
            res = g_client.public_repos()
            self.assertEqual(res, ["google", "abc"])
            mock_get_json.assert_called_once()
            mock_public.assert_called_once()
