


def test_challenge3(copart):
    for car in copart.find("[ng-repeat*='popularSearch'] > a"):
        href = car.get_attribute('href')
        print(f'{car.text} - {href}')




