# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from gaiatest import GaiaTestCase
from gaiatest.apps.testapp.app import TestContainer


class TestContainerTest(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)

    def test_modal(self):
        # https://moztrap.mozilla.org/manage/case/1325/
        self.container = TestContainer(self.marionette)
        self.container.launch()
        print self.marionette.get_url()
        self.marionette.execute_script("""
        var newDiv = document.createElement("div");
        newDiv.id = "newDiv";
        var newContent = document.createTextNode("I am a newly created div!");
        newDiv.appendChild(newContent);
        let container = document.getElementById('test-container');
        document.body.insertBefore(newDiv, container);
        """)
