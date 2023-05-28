class Driver:
    def __init__(self, name):
        self.name = name
        self.drug_test_passed = False

    def pass_drug_test(self):
        self.drug_test_passed = True

    def fail_drug_test(self):
        self.drug_test_passed = False

class Delivery:
    def __init__(self, driver):
        self.driver = driver

    def is_driver_sober(self):
        return self.driver.drug_test_passed

# Example usage:
john = Driver('John')
john.pass_drug_test()  # John passed his drug test

delivery = Delivery(john)
print(delivery.is_driver_sober())  # This will print 'True'
