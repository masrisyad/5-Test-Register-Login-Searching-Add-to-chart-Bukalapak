from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.bukalapak.com/')
wait = WebDriverWait(driver, 30)


def Register(Email, passwordRegist):
    BtnRegister = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//p[normalize-space()='Daftar']")))
    BtnRegister.click()
    # time.sleep(10)

    assert 'Daftar' in driver.title
    fillEmail = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "bl-text-field__input")))
    fillEmail.send_keys('masrisyad2@gmail.com')
    # print(fillEmail)

    BtnDftr = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Daftar')]")))
    BtnDftr.click()

    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "bl-modal__wrapper")))

    valid = wait.until(EC.visibility_of_element_located(
        (By.TAG_NAME, "strong"))).text
    assert Email == valid

    verification = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Ya, kirim kode')]")))
    verification.click()
    time.sleep(30)

    VerificationBtn = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[normalize-space()='Verifikasi']")))
    VerificationBtn.click()
    print("DONE")

    NamaLengkap = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[aria-label='Nama lengkap']")))
    NamaLengkap.send_keys('Risyad Abdala')
    # driver.quit()
    Password = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[aria-label='Password']")))
    Password.send_keys(passwordRegist)

    BtnSmpn = driver.find_element_by_xpath("//span[contains(text(),'Simpan')]")
    BtnSmpn.click()


def Login(mail, PasswordUser):
    BtnLogin = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(text(),'Login')]")))
    BtnLogin.click()

    fillMail = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#user_session_username")))
    fillMail.send_keys(mail)

    FillPassword = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#user_session_password")))
    FillPassword.send_keys(PasswordUser)

    ButtonLogin = driver.find_element_by_xpath(
        "//button[contains(text(),'Login')]")
    ButtonLogin.click()

    Confirmation = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Kirim kode lewat SMS')]")))
    Confirmation.click()
    time.sleep(20)
    # NomorOtp = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='otp']")))
    # NomorO
    ConfirmationOtp = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(text(),'Konfirmasi')]")))
    ConfirmationOtp.click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(text(),'Nomor handphone berhasil dikonfirmasi')]")))

    BtnOke = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Oke')]")))
    BtnOke.click()


def Searching(Cari):
    KolomSearch = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#v-omnisearch__input")))
    KolomSearch.send_keys(Cari)
    KolomSearch.send_keys(Keys.RETURN)

    # hasilPencarian = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mt-12"))).text
    # assert Cari in hasilPencarian


def AddToChart():
    print("Cari Barang")

    Choosebarang = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[normalize-space()='handphone samsung s9']")))
    NamaBarang = driver.find_element_by_xpath(
        "//a[normalize-space()='handphone samsung s9']").text
    Choosebarang.click()

    ClickAdd = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".c-main-product__action__cart.bl-button.bl-button--outline.bl-button--medium")))
    ClickAdd.click()

    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".c-dialog__content")))

    BtnLihatKeranjang = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//button[normalize-space()='Lihat Keranjang']")))
    BtnLihatKeranjang.click()

    validationChart = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'handphone samsung s9')]"))).text
    assert NamaBarang == validationChart


def main():
    Email = 'masrisyad2@gmail.com'
    Password = 'ujicoba'
    Pencarian = 'Handphone'
    Register(Email, Password)
    Login(Email, Password)
    Searching(Pencarian)
    AddToChart()
    driver.quit()

# def if __name__ == '__main__':


main()
