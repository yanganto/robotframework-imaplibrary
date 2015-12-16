#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright 2015 Richard Huang <rickypc@users.noreply.github.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
IMAP Library - a IMAP email testing library.
"""

from sys import path
path.append('src')
from ImapLibrary import ImapLibrary
import mock
import unittest


class ImapLibraryTests(unittest.TestCase):
    """Imap library test class."""

    def setUp(self):
        """Instantiate the Imap library class."""
        self.library = ImapLibrary()
        self.password = 'password'
        self.secure_port = 993
        self.server = 'my.imap'
        self.username = 'username'

    def test_should_have_default_values(self):
        """Imap library instance should have default values set."""
        self.assertIsInstance(self.library, ImapLibrary)
        self.assertIsNone(self.library._email_index)
        self.assertIsNone(self.library._imap)
        self.assertIsInstance(self.library._mails, list)
        self.assertIsNone(self.library._mp_iter)
        self.assertIsNone(self.library._mp_msg)
        self.assertIsNone(self.library._part)
        self.assertEqual(self.library._port, self.secure_port)

    @mock.patch('ImapLibrary.imaplib.IMAP4_SSL')
    def test_should_open_mailbox(self, mock_imap):
        """Open mailbox should open connection to Imap server with requested credentials."""
        self.library.open_mailbox(self.server, self.username, self.password)
        mock_imap.assert_called_with(self.server, self.secure_port)
        self.library._imap.login.assert_called_with(self.username, self.password)
        self.library._imap.select.assert_called_with()
