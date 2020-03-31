from wifiid_login import Wifi

def main():
    # Your @wifi.id username
    username = '<your username>'

    # Your @wifi.id password
    password = '<your password>'

    # IP address of your connected device/interface to @wifi.id access point
    client_ip = '<your IP address>'

    # Your @wifi.id login page link. It usually starts with https://welcome2.wifi.id/login/...
    login_page_url = '<https://welcome2.wifi.id/login/...>'

    # Create wifi_id object
    wifi_id = Wifi(username, password, client_ip)

    # Login to @wifi.id with params from login URL
    got_response, msg = wifi_id.login_with_url(login_page_url)

    if got_response:
        print("Server response: " + str(msg))
    else:
        print("Login failed. " + str(msg))

if __name__ == "__main__":
    main()
