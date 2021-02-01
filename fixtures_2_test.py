import allure
import pytest
import time


class TestFixtures:

    @allure.title('Fixture 1')
    @pytest.fixture(autouse=True)
    def fixture_1(self, common_fixture):
        time.sleep(1)
        print('Fixture 1')
        print(f'Return value from common_fixture: {common_fixture}')

    @pytest.fixture(autouse=False)
    @allure.title('Common fixture')
    def common_fixture(self):
        time.sleep(1)
        print('Common fixture')
        return 42

    @allure.title('Test 1')
    def test_1(self, common_fixture):
        with allure.step('Allure step in test'):
            print('Test 1')
            print(f'Return value from common_fixture: {common_fixture}')
