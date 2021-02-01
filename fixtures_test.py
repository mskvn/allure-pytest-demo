import allure
import pytest
import time


class TestFixtures:

    @allure.title('Class fixture title')
    @pytest.fixture(scope='class', autouse=True)
    def class_fixture_with_title(self, ):
        with allure.step('Allure step in class fixture'):
            time.sleep(1)
            print('Class fixture')

    @pytest.fixture(autouse=True)
    @allure.step('Function fixture 1')
    def function_fixture_with_test_1(self):
        with allure.step('Allure step in function fixture'):
            time.sleep(1)
            print('Function fixture 1')

    @pytest.fixture(autouse=False)
    @allure.step('Function fixture 2')
    def function_fixture_2(self):
        with allure.step('Allure step in function fixture'):
            time.sleep(1)
            print('Function fixture 2')

    @allure.title('Test 1')
    def test_1(self, function_fixture_2):
        with allure.step('Allure step in test'):
            print('Test 1')
