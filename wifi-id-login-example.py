import wifiid_login as wifi

def main():
    # Your @wifi.id username
    username_wifi_id = '<username>'
    
    # Your @wifi.id password
    password_wifi_id = '<password>'
    
    # IP address of your connected device/interface to @wifi.id AP
    ip_client_wifi_id = '<your IP address>'
    
    # Your @wifi.id login page link. It usually starts with https://welcome2.wifi.id/login/...
    login_page_url = '<https://welcome2.wifi.id/login/...>'

    gw_id, mac, wlan, redir = wifi.get_login_params_from_url(login_page_url)
    got_response, msg = wifi.login(username_wifi_id, password_wifi_id, ip_client_wifi_id, gw_id, mac, wlan, redir)

    print(got_response)
    print(msg)

if __name__ == "__main__":
    main()
