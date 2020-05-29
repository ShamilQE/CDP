from time import sleep, time


def test_challenge3(copart):
    for car in copart.find("[ng-repeat*='popularSearch'] > a"):
        href = car.get_attribute('href')
        print(f'{car.text} - {href}')


def test_challenge3_copart(py):
    py.visit('https://copart.com')
    popular_models = py.find("li[ng-repeat*='popularSearch'] > a")
    for model in popular_models:
        print(f'{model.text()} - {model.get_attribute("href")}')
    assert py.should('popular_models.length == 20')


def test_challenge3_copart_honda_search(py):
    py.visit('https://copart.com')
    py.get('[data-uname="homePageFindAVehicle"]').click()
    py.get('[data-uname="vehicleFinderTab"]').click()
    py.get("[data-uname=\"vehiclefinderTypedropdownbox\"]").select('Automobile')
    py.get('[data-uname="vehiclefinderMakedownbox"]').select('Honda')
    py.get('[data-uname="vehiclefinderModeldownbox"]').select('CRV')
    py.get('[data-uname="vehiclefinderLocationdropdownbox"]').select('UT - Salt Lake City')
    py.get('[ng-click="search(form)"]').click()
    assert py.should().contain_title('Honda')
    py.get('[name="serverSideDataTable_length"]').select('100').click()











