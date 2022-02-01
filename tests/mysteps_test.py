from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.wish_list_page import WishListPage
from tests.base_test import BaseTest


class MyStepsTest(BaseTest):

    def test_steps(self):
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        wish_list_page = WishListPage(self.driver)

        # Anasayfaya gider ve onaylar.
        assert self.locator.BASE_URL == base_page.get_url()
        # Login ekranını açar.
        home_page.go_to_sign_in()
        # Kullanıcı girişi yapar.
        login_page.sign_in()
        # Search Box'a samsung yazılır ve aratılır.
        home_page.search_keyword()
        # Gelen sayafada Samsung için ürün oldugunu onaylar.
        search_page.keyword_control()
        # Arama listesinde 2.sayfaya gider ve 2. sayfada oldugunu onaylar.
        search_page.go_to_second_page()
        # 2.sayfadaki 3.ürünün içindeki Add To List butonuna tıklar.
        search_page.choose_the_third_product()
        # Wish listi görüntüler.
        product_page.add_to_wish_list()
        # Açılan sayfada bir önceki sayfada izlemeye alınmış ürünün listede bulundugunu onaylar.
        search_page.check_product_in_wish_list()
        # Ürün Wish Listten silinir.
        wish_list_page.remove_product_in_wish_list()
        # Wish Listten silindiği onaylanır.
        wish_list_page.is_the_wish_list_empty()
