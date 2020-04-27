from pylenium.element import Element
from selenium.webdriver.common.keys import Keys


def test_google_search_puppies(py):
        py.visit('http://google.com')
        py.get('[name="q"]').type('puppies', Keys.ENTER)
        assert py.should().contain_title('puppies')
        #assert 'puppies' in py.title


def test_copart_search_exotics(py):
        py.visit('https://copart.com')
        py.get('#input-search').type('exotics', Keys.ENTER)
        assert py.contains('PORSCHE')


def test_facebook_search_for_Macbook(py):
        py.visit('https://facebook.com')
        py.get('[name="email"]').type('xxxxx@gmail.com')
        py.get('[name="pass"]').type('xxxxx', Keys.ENTER)
        py.get('[title="Marketplace"]'), Keys.ENTER
        py.get('[type="text"]').type('macbook', Keys.ENTER)
        assert py.contains('MacBook Air')


def test_homedepot_topseller(py):
        py.visit('https://homedepot.com')
        py.get('[id="headerSearch"]').type('electric', Keys.ENTER)
        py.get('[data-defaultsortbylabel="Best Match"]'), Keys.ENTER
        py.get('[data-value="P_Topseller_Sort|1"'), Keys.ENTER
        assert py.contains('Top Sellers')


