from dataclasses import dataclass


@dataclass
class BrowserTab:
    def __init__(self, home_page: str):
        self.current_page = home_page
        self.forward_stack = []
        self.backward_stack = []

    def visit(self, url: str):
        self.backward_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack = []

    def backward(self):
        if not self.backward_stack:
            return self.current_page
        self.forward_stack.append(self.current_page)
        self.current_page = self.backward_stack.pop()
        return self.current_page

    def forward(self):
        if not self.forward_stack:
            return self.current_page

        self.backward_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        return self.current_page
    