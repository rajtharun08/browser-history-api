from browser_history.history import BrowserHistory

if __name__ == "__main__":
    """
    manual test of the BrowserHistory class.
    """

    browser = BrowserHistory("homepage.com")
    
    browser.visit("google.com")
    browser.visit("github.com")
    browser.visit("pytest.org")

    print("\n--- Testing Current State ---")
    
    # Test 1: Where are we now?
    print(f"Current Page: {browser.current_page.url}") 
    # EXPECTED: pytest.org
    
    # Test 2: Can we go back one step?
    print(f"Previous Page: {browser.current_page.prev.url}") 
    # EXPECTED: github.com
    
    # Test 3: Can we go back two steps?
    print(f"Page before that: {browser.current_page.prev.prev.url}") 
    # EXPECTED: google.com
    
    # Test 4: Can we go back three steps?
    print(f"Homepage: {browser.current_page.prev.prev.prev.url}") 
    # EXPECTED: homepage.com

    # Test 5: Is the 'homepage' the start?
    print(f"Start of list: {browser.current_page.prev.prev.prev.prev}") 
    # EXPECTED: None
    
    # Test 6: Is the current page the end? (No forward history)
    print(f"Forward from list: {browser.current_page.next}") 
    # EXPECTED: None