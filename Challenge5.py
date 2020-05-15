from pprint import pprint
import should as should

def test_find_select_count(py):
    py.visit("https://www.hobbyeasy.com/en/category/AF35K/100/1/maker/all.html")
    # count names of makers
    assert py.find("[href*='makers']").should().have_length(100)
    # count how much every items in maker
    makers = dict()
    for maker in py.find("[href*='makers']"):
        if maker.text() in makers:
            makers[maker.text()] +=1
        else:
            makers[maker.text() ] =1
    pprint(makers)

def test_challange5_copart(py, copart):
    py.find("[href*='lotsearchLotmodel']")
        # count how much every items in maker
    lotsearchLotmodel = dict()
    for maker in py.find("[href*='lotsearchLotmodel']"):
        if maker.text() in lotsearchLotmodel:
            lotsearchLotmodel[maker.text()] += 1
        else:
            lotsearchLotmodel[maker.text()] = 1
    pprint(lotsearchLotmodel)