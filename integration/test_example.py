def test_example(browser):
    browser.get('http://python.org')
    assert 'Python' in browser.title

def test_google(browser):
    browser.get('https://www.google.com/')
    assert 'Google' in browser.title
