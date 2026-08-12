'''6. The system should handle customer information, including name, contact details, and driver's license information.
'''

class CustomerDetails:
    def __init__(self, name, contact_details, driver_license_info):
        self.name = name
        self.contact_details = contact_details
        self.driver_license_info = driver_license_info
    
    def get_name(self):
        return self.name

    def get_contact_details(self):
        return self.contact_details

    def get_driver_license_info(self):
        return self.driver_license_info

    def customer_info(self):
        return f"Name:{self.name}, contact_details:{self.contact_details}, driver_license_info:{self.driver_license_info}"