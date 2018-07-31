class Component(object):
    def get(self):
        """
        Return first element what found by selector
        """

    def get_all(self):
        """
        Return all elements what found by selector
        """


class Input(Component):
    @property
    def value(self):
        """
        Get current value of input
        """

    @value.setter
    def value(self, value):
        """
        Set value of inout
        """


class Button(Component):
    def click(self):
        """
        Click on element
        """


class Link(Component):
    @property
    def href(self):
        """
        Get href of link element
        """

    @property
    def text(self):
        """
        Get href of link element
        """


class PageObjectBase(object):
    def __enter__(self):
        """
        Wait until all elements will be present at page
        After that return page
        """

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class GoogleSearchPage(PageObjectBase):
    search_input = Input()
    search_button = Button()


class GoogleSearchResultPage(PageObjectBase):
    found_link = Link()
