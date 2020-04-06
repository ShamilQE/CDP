from selenium.webdriver.common.keys import Keys


#def test_google_search(py):
 #       py.visit('http://google.com')
  #      py.get('[name="q"]').type('puppies', Keys.ENTER)
   #     assert  'puppies' in py.title



def test_copart_search_exotics(py):
        py.visit('https://copart.com')
        py.get('#input-search').type('exotics', Keys.ENTER)
        assert py.contains('PORSCHE')







