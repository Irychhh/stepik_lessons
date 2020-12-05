# Data
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
add_to_basket_locator = 'button.btn-add-to-basket'

exp_btn_text_dict = {
        "ru": "Добавить в корзину",
        "en_GB": "Add to basket",
        "es": "Añadir al carrito",
        "fr": "Ajouter au panier"
}

def test_check_add_to_basket_button(browser):
    expected_lang_code = browser.user_language
    expected_btn_text = exp_btn_text_dict[expected_lang_code]

    # Arrange
    browser.get(link)

    # Act
    button_add_to_basket = browser.find_element_by_css_selector(add_to_basket_locator)
    successful_button_text = button_add_to_basket.text

    # Assert
    assert expected_btn_text in successful_button_text, "the button text is incorrect"
