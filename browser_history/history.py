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
    
    def back(self, steps):
        """
        Moves the current page pointer backward by steps.
        Stops at the homepage if steps is too large.
        Returns the URL of the page you land on.
        """
        # Keep moving back as long as:
        # we have steps to move
        # current page has a 'prev' node (we're not at the head)
        while steps > 0 and self.current_page.prev is not None:
            self.current_page = self.current_page.prev
            steps -= 1
            
        return self.current_page.url

    def forward(self, steps):
        """
        Moves the current page pointer forward by steps.
        Stops at the last page if steps is too large.
        Returns the URL of the page you land on.
        """
        # Keep moving forward as long as:
        #  we have steps to move
        #  current page has a next node
        while steps > 0 and self.current_page.next is not None:
            self.current_page = self.current_page.next
            steps -= 1
            
        return self.current_page.url