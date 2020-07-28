import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

supported_browsers = {
        'chrome' : webdriver.Chrome,
        'firefox' : webdriver.Firefox
        }

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="You should enter --browser_name={name of the browser}")
    parser.addoption('--language', action='store', default='en', help="You should enter --language={test language}")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        print(f"\n Starting {browser_name} browser for test...")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print(f"\n Starting {browser_name} browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        
    else:
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: chrome, firefox")

    yield browser
    print("\n Quiting browser...")
    browser.quit()
