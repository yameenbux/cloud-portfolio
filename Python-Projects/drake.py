from playwright.sync_api import sync_playwright
import time

# Event page URL for Drake's Manchester show
event_url = "https://www.ticketmaster.co.uk/drake-with-partynextdoor-ome-pecial-hows-4-uk-manchester-25-07-2025/event/37006272F01B6BF4"

# Personal and payment information (test values)
user_info = {
    "full_name": "Adam Patel",
    "email": "test@gmail.com",
    "address": "123 Test Road",
    "city": "Manchester",
    "postcode": "M26 1GG",
    "card_number": "4657371912340123",
    "card_expiry": "10/27",
    "card_cvv": "458"
}

def run():
    with sync_playwright() as p:
        # Launch Chromium browser (not headless so you can interact)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to event page...")
        page.goto(event_url)

        # Wait for ticket options to load
        page.wait_for_timeout(15000)

        print("Looking for lowest priced tickets...")

        # Attempt to click the cheapest ticket button
        try:
            ticket_buttons = page.query_selector_all("button[aria-label*='from']")
            if ticket_buttons:
                ticket_buttons[0].click()
                print("Selected the cheapest ticket option.")
            else:
                print("Could not find ticket options.")
                return
        except Exception as e:
            print(f"Error selecting ticket: {e}")
            return

        # Wait for checkout page to load
        page.wait_for_timeout(10000)

        # Fill in user info
        try:
            print("Filling in user information...")
            page.fill('input[name="firstName"]', user_info["full_name"].split()[0])
            page.fill('input[name="lastName"]', user_info["full_name"].split()[1])
            page.fill('input[name="email"]', user_info["email"])
            page.fill('input[name="confirmEmail"]', user_info["email"])
            page.fill('input[name="address1"]', user_info["address"])
            page.fill('input[name="city"]', user_info["city"])
            page.fill('input[name="zip"]', user_info["postcode"])
        except Exception as e:
            print(f"Form fill error (user info): {e}")

        # Fill in payment details (note: these fields may be secured/blocked)
        try:
            print("Filling in payment information...")
            page.fill('input[name="cardNumber"]', user_info["card_number"])
            page.fill('input[name="expirationDate"]', user_info["card_expiry"])
            page.fill('input[name="cvNumber"]', user_info["card_cvv"])
        except Exception as e:
            print(f"Form fill error (payment): {e}")

        print("Manual CAPTCHA may be required now. Complete it manually.")
        input("After finishing checkout, press Enter here to close the browser...")
        browser.close()

if __name__ == "__main__":
    run()
