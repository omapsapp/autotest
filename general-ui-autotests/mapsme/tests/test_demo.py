from time import sleep

import pytest
from mapsmefr.pageobjects.base import BottomPanel
from mapsmefr.steps.locators import Locator, LocalizedButtons


@pytest.mark.base
class TestMainMapsme:

    @pytest.fixture
    def main(self, testitem, emulate_location_moscow, press_back_to_main):
        pass

    @pytest.mark.name("Роутинг")
    def test_routing_base(self, main, download_moscow_map, steps):
        panel = BottomPanel()
        steps.search("Проспект Мира 78")
        steps.choose_first_search_result()

        panel.to().click()
        el = steps.try_get_by_text(LocalizedButtons.ACCEPT.get())
        if el:
            el.click()

        assert steps.try_get_by_text(LocalizedButtons.START.get()) or steps.try_get(Locator.START.get())


