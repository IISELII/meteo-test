from selenium import webdriver

def test_streamlit_app():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8501/")  # Assurez-vous que votre application Streamlit est en cours d'exécution

    # Trouvez l'entrée et le bouton de recherche
    city_input = driver.find_element_by_css_selector(".stText") 
    search_button = driver.find_element_by_css_selector(".stButton")

    # Entrez la valeur et cliquez sur le bouton de recherche
    city_input.send_keys("Paris")
    search_button.click()

    # Attendez que les résultats soient affichés
    driver.implicitly_wait(10)
    
    # Vérifiez les résultats
    results = driver.find_elements_by_css_selector(".stText")
    assert "Aujourd'hui :" in results[0].text
    assert "Demain :" in results[1].text
    assert "Après Demain :" in results[2].text

    # Vérifiez la carte (c'est un peu complexe car Streamlit utilise pydeck pour les cartes)
    # Ici, pour la simplicité, nous vérifions juste si un élément pydeck existe
    map_element = driver.find_element_by_css_selector(".deckgl-overlay")
    assert map_element is not None

    driver.quit()
