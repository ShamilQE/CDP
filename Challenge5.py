import should as should
from pprint import pprint
from selenium.webdriver.common.keys import Keys

import pytest
from pylenium import Pylenium


# def test_find_select_count(py):
#     py.visit("https://www.hobbyeasy.com/en/category/AF35K/100/1/maker/all.html")
#     # count names of makers
#     assert py.find("[href*='makers']").should().have_length(100)
#     # count how much every items in maker
#     makers = dict()
#     for maker in py.find("[href*='makers']"):
#         if maker.text() in makers:
#             makers[maker.text()] +=1
#         else:
#             makers[maker.text() ] =1
#     pprint(makers)


def test_copart_porsche_model_count(py):
    py.visit('https://copart.com')
    py.get('#input-search').type('Porsche')
    py.get('[type="submit"]').click()
    py.get('[name="serverSideDataTable_length"]').select('100').click()
    #py.wait(5)
    assert py.find('[data-uname="lotsearchLotnumber"]').should().have_length(100)

    lotsearchLotmodel = dict()
    for maker in py.find('[data-uname="lotsearchLotmodel"]'):
        if maker.text() in lotsearchLotmodel:
            lotsearchLotmodel[maker.text()] += 1
        else:
            lotsearchLotmodel[maker.text()] = 1
    pprint(lotsearchLotmodel)





































