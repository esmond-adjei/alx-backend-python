#!/usr/bin/env python3
"""Unit tests for client.py
"""
from typing import Dict
import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class."""
    @parameterized.expand([
        ("google", {'post': "google"}),
        ("abc", {'post': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, t_org: str, resp: Dict, mocked_: MagicMock) -> None:
        """Tests the org method."""
        mocked_.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(t_org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(t_org)
        )
