from browser_history.history import BrowserHistory

def test_browser_initialization():
    """
    Tests that the browser initializes correctly with the homepage.
    """
    browser = BrowserHistory("homepage.com")

    #  'assert' statements check if the code is correct
    assert browser.current_page.url == "homepage.com"
    assert browser.current_page.prev is None
    assert browser.current_page.next is None

# another test function (starts with "test_")
def test_visit_works():
    """
    Tests that the visit method correctly adds a new page.
    """
    browser = BrowserHistory("homepage.com")
    browser.visit("google.com")

    # Check the new page
    assert browser.current_page.url == "google.com"

    # Check that it's linked to the previous page
    assert browser.current_page.prev.url == "homepage.com"