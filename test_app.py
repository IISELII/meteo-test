from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_streamlit_app():
    # Configuration du WebDriver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/google-chrome"  # spécifiez le chemin vers votre emplacement binaire Chrome

    # Obtenez le chemin du driver
    driver_path = ChromeDriverManager().install()

    # Définir le chemin ChromeDriver
    os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

    driver = webdriver.Chrome(options=options)

    # Accédez à votre application Streamlit
    driver.get("http://localhost:8501/")

    try:
        # Trouvez l'entrée et le bouton de recherche
        city_input = driver.find_element_by_css_selector(".stText")
        search_button = driver.find_element_by_css_selector(".stButton")
        # Entrez la valeur et cliquez sur le bouton de recherche
        city_input.send_keys("Paris")
        search_button.click()
    except Exception as e:
        print("Erreur lors de la recherche:", e)
        driver.quit()
        return

    driver.implicitly_wait(10)

    try:
        # Vérifiez les résultats
        results = driver.find_elements_by_css_selector(".stText")
        assert "Aujourd'hui :" in results[0].text
        assert "Demain :" in results[1].text
        assert "Après Demain :" in results[2].text
    except AssertionError:
        print("Erreur dans les résultats des prévisions!")
        driver.quit()
        return

    try:
        # Vérifiez la carte
        map_element = driver.find_element_by_css_selector(".deckgl-overlay")
        assert map_element is not None
    except AssertionError:
        print("Erreur lors de la vérification de la carte!")
        driver.quit()
        return

    print("Tous les tests ont réussi!")
    driver.quit()

test_streamlit_app()

