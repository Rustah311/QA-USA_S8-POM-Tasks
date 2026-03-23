import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_custom_bike_option():
    driver = webdriver.Chrome()
    # Step 1: Open the app - update the URL after starting the server
    driver.get('https://cnt-dec10d58-12bd-4d93-a76d-1bbc36a6b4a9.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 2: Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    ...

    # Select the "Custom" option.
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Bike" icon.
    ...
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 3: Verify the Bike text is displayed correctly
    actual_value = ...
    expected_value = ...
    assert ...
    driver.quit()
