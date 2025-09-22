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
def test_back_functionality():
    """Tests that the back method works correctly."""
    browser = BrowserHistory("homepage.com")
    browser.visit("google.com")
    browser.visit("github.com")
    
    # Go back 1 step
    url = browser.back(1)
    assert url == "google.com"
    assert browser.current_page.url == "google.com"
    
    # Go back another step
    url = browser.back(1)
    assert url == "homepage.com"
    assert browser.current_page.url == "homepage.com"

def test_back_edge_case():
    """Tests going back further than history allows."""
    browser = BrowserHistory("homepage.com")
    browser.visit("google.com")
    
    # Go back 100 steps (should stop at homepage)
    url = browser.back(100)
    assert url == "homepage.com"
    assert browser.current_page.url == "homepage.com"

def test_forward_functionality():
    """Tests that the forward method works after going back."""
    browser = BrowserHistory("homepage.com")
    browser.visit("google.com")
    browser.visit("github.com")
    
    # Go back
    browser.back(1)
    assert browser.current_page.url == "google.com"
    
    # Go forward
    url = browser.forward(1)
    assert url == "github.com"
    assert browser.current_page.url == "github.com"

def test_forward_edge_case():
    """Tests going forward further than history allows."""
    browser = BrowserHistory("homepage.com")
    browser.visit("google.com")
    
    # Go back
    browser.back(1)
    
    # go forward 100 steps (should stop at the last page)
    url = browser.forward(100)
    assert url == "google.com"
    assert browser.current_page.url == "google.com"

def test_forward_history_cleared_on_visit():
    """
    Tests that visiting a new page clears the forward history
    """
    browser = BrowserHistory("A.com")
    browser.visit("B.com")
    browser.visit("C.com")
    
    # Go back to B.com
    browser.back(1)
    assert browser.current_page.url == "B.com"
    
    # C.com is now in the forward history.
    # visit a new page, D.com
    browser.visit("D.com")
    assert browser.current_page.url == "D.com"
    
    #  It should fail (stay on D.com),
    # because visiting D.com should have cleared C.com from history.
    url = browser.forward(1)
    assert url == "D.com"
    assert browser.current_page.next is None