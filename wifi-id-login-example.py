import wifiid_login as wifi

def main():
    # Your @wifi.id username
    username = '<your username>'
    
    # Your @wifi.id password
    password = '<your password>'
    
    # IP address of your connected device/interface to @wifi.id access point
    client_ip = '<your IP address>'
    
    # Your @wifi.id login page link. It usually starts with https://welcome2.wifi.id/login/...
    login_page_url = '<https://welcome2.wifi.id/login/...>'

    # Get login parameters from login page URL
    gw_id, mac, wlan, redir = wifi.get_login_params_from_url(login_page_url)

    # Login to @wifi.id
    got_response, msg = wifi.login(username, password, client_ip, gw_id, mac, wlan, redir)

    print(got_response)
    print(msg)

if __name__ == "__main__":
    main()
