import undetected_chromedriver as uc

driver = None


def get_driver():
    global driver

    if driver is None:
        options = uc.ChromeOptions()
        options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"

        driver = uc.Chrome(
            options=options,
            version_main=151
        )

        driver.maximize_window()

    return driver


def close_driver():
    global driver

    if driver:
        driver.quit()
        driver = None