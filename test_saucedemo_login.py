from playwright.sync_api import sync_playwright


def test_saucedemo_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Headless=True runs without UI
        page = browser.new_page()

        # Step 1: Navigate to SauceDemo login page
        page.goto("https://www.saucedemo.com/")
        page.wait_for_load_state("domcontentloaded")

        # Step 2: Enter valid credentials
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")

        # Step 3: Click login button
        page.click("input[type='submit']")
        page.wait_for_load_state("networkidle")

        # ✅ Step 4: Assert successful login
        assert "inventory.html" in page.url, "❌ Login failed: URL did not change!"
        assert page.is_visible(".title"), "❌ Login failed: 'Products' title not found!"

        print("✅ Login successful!")

        # Step 5: Log out
        page.click("#react-burger-menu-btn")  # Open menu
        page.wait_for_timeout(1000)  # Wait for menu animation
        page.click("#logout_sidebar_link")  # Click logout

        # ✅ Step 6: Assert successful logout
        assert "saucedemo.com" in page.url, "❌ Logout failed!"
        assert page.is_visible("input[name='user-name']"), "❌ Logout failed: Login form not found!"

        print("✅ Logout successful!")

        browser.close()


# Run the test
test_saucedemo_login()
