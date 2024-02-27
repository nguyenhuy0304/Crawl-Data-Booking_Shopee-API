from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(email, password):
    try:
        driver = webdriver.Chrome()
        driver.get(
            "https://account.booking.com/sign-in?"
            "op_token=EgVvYXV0aCLdAgoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4q_AFVcm9CSnFTUk5fY0p6TzJ2d0VuTzdycl92NzBncExyTEZ1TDc0Z2RlNlB2Tnc5T1FscEFISEI5MlpWVGZpNFd1eWplaDE0dm50S0Q5aHBXM3ladWdpLXY0SEZoLVFhRDdSbGk5dkRzSmN0MmE4ZXNpZEU1VHo0WkRyTDB3M3Y5Um9UNEU3dUh1SzMxZXNfTmM3Q2l4NWtNUkxpRFk0cnhEVVBaRXo5enJXV2psdVBnNHBpUlBNaUh4LUJzRTNSWVA1Z19WVWRSSHdOQTVzcWhGVGkzSDlET013dUJFWHY4dThsQjE4Z3BfdUJJLUtGaDQxSUgzcGYxWGx1TkVCBGNvZGUqFgiOyBIwwaf46Ii8JDoAQgBYgd3j_AU")
        wait = WebDriverWait(driver, 30)
        # find the element where we have to
        # enter the xpath
        # fill the  email
        driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)

        # click on next button
        driver.find_element(By.XPATH,
                            '//button[@class="Iiab0gVMeWOd4XcyJGA3 wPxWIS_rJCpwAWksE0s3 Ut3prtt_wDsi7NM_83Jc'
                            ' TuDOVH9WFSdot9jLyXlw EJWUAldA4O1mP0SSFXPm whxYYRnvyHGyGqxO4ici"]').click()

        # find the element where we have to
        # enter the xpath
        # fill the password
        # driver.find_element(By.XPATH, '//*[@placeholder="Enter your password"]').send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     "//input[@placeholder='Enter your password']"))).send_keys(
            password)

        # find the element Sign in
        # request using xpath
        # clicking on that element

        driver.find_element(By.XPATH,
                            '//button[@class="Iiab0gVMeWOd4XcyJGA3 wPxWIS_rJCpwAWksE0s3 Ut3prtt_wDsi7NM_83Jc '
                            'TuDOVH9WFSdot9jLyXlw EJWUAldA4O1mP0SSFXPm whxYYRnvyHGyGqxO4ici"]').click()

        return driver
    except Exception as e:
        return e


def search(driver, keys):
    try:
        wait = WebDriverWait(driver, 30)
        # Truy cập đến ô điền key để tìm kiếm:
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     "//input[@placeholder='Where are you going?']"))).send_keys(keys)
        # Click vào nốt (Button) Search:
        search = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                              '//button[@class="a83ed08757 c21c56c305 '
                                                              'a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]'))).click()

        return search
    except Exception as e:
        return e


# Login với email và mật khẩu đăng nhập vào Booking:
email = 'Your email....'
password = 'Your passwoard...'
dri = login(email, password)
#
key_word = 'Hochiminh'
search(dri, key_word)
#
print(dri, type(dri))
print("-- Finish --")
