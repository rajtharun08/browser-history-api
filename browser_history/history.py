class Node:
    """
    it holds the URL and pointers to the previous and next nodes
    """
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    """
    class to simulate browser history functionality using a doubly linked list
    """
    
    def __init__(self, homepage):
        """
        initializes the browser history with a homepage
        """
        #  first node is the homepage
        self.current_page = Node(homepage)
        print(f"History initialized with homepage: {homepage}")

    def visit(self, url):
        """
        visits a new URL. This adds a new node after the current page
        and clears any "forward" history.
        """
        # new node for the visited URL
        new_node = Node(url)
        
        # new node's 'prev' to the current page
        new_node.prev = self.current_page
        
        #    This automatically clears any old "forward" history
        self.current_page.next = new_node
        
        # Move the 'current_page' pointer to the new node
        self.current_page = new_node
        
        print(f"Visited new page: {url}")