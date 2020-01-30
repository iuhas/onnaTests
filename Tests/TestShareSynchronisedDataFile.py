import unittest
import pytest
from PageObjects.Login import LoginPage
from PageObjects.SourceSynchronisedData import SourceData
from PageObjects.Workspace import WorkspacePage


@pytest.mark.usefixtures("oneTimeSetUp")
class OnnaTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        global login
        login = LoginPage(self.browser)
        global workspace
        workspace = WorkspacePage(self.browser)
        global source
        source = SourceData(self.browser)

    def test_workspace_manager_can_share_one_sunched_file(self):
        workspace.goTo_workspace()
        workspace.goTo__connected_source_byName("Gmail2")
        assert source.input_text_in_search_box('file00') > 0
        source.click_on_share_option_by_item_index('1')
        source.fill_in_share_form(user_email="test@onna.com", permission_index="1")
        assert source.is_toast_message_displayed()
