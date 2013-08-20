# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
from gaiatest import GaiaTestCase
from gaiatest.apps.testapp.app import TestContainer


class TestModal(GaiaTestCase):

    def test_modal_switching(self):
        self.container = TestContainer(self.marionette)
        self.container.launch()
        # create an element and attach a modal trigger to it
        self.marionette.execute_script("""
        var modalButton= document.createElement("button");
        modalButton.id = "modalButton";
        modalButton.onclick = function() { 
            console.log('firing');
            confirm("test");
        };
        var newContent = document.createTextNode("Tap here to trigger a modal");
        modalButton.appendChild(newContent);
        let container = document.getElementById('test-container');
        document.body.insertBefore(modalButton, container);
        """)
        modalButton = self.marionette.find_element("id", "modalButton")
        origin_url = self.marionette.get_url()
        modalButton.tap()
        modal_url = self.marionette.get_url()
        # assert that we're no longer in the original frame
        self.assertNotEqual(origin_url, modal_url)
        # assert that we're in the system app
        self.assertTrue("system" in modal_url)
        confirm = self.marionette.find_element("id", "modal-dialog-confirm-ok")
        confirm.tap()
        after_tap_url = self.marionette.get_url()
        # assert that we've returned to the original frame after dismissing the modal
        self.assertEqual(origin_url, after_tap_url)

