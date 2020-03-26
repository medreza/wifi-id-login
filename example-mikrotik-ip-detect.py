import wifiid_login as wifi
import routeros_api # https://github.com/socialwifi/RouterOS-api
import json


def main():
    # Your @wifi.id username
    username = '<your username>'

    # Your @wifi.id password
    password = '<your password>'

    # Get MikroTik WLAN IP address (wlan1 interface connected to @wifi.id) via RouterOS API
    mikrotik_connection = routeros_api.RouterOsApiPool('<your mikrotik IP address>',
                                                       username='<your mikrotik username>',
                                                       password='<your mikrotik password>')
    mikrotik_api = mikrotik_connection.get_api()
    mikrotik_wan_ip =  mikrotik_api.get_resource('/ip/address')
    mikrotik_wan_ip = str(mikrotik_wan_ip.get(interface='wlan1')).replace("\'", "\"")
    mikrotik_wan_ip = json.loads(mikrotik_wan_ip[1:-1])['address']
    mikrotik_wan_ip = mikrotik_wan_ip.split('/')[0]
    mikrotik_connection.disconnect()

    # IP address of your connected device/interface to @wifi.id
    client_ip = mikrotik_wan_ip

    # Your @wifi.id login page link. It usually starts with https://welcome2.wifi.id/login/...
    login_page_url = '<https://welcome2.wifi.id/login/...>'

    # Get login parameters from login page URL
    gw_id, mac, wlan, redir = wifi.get_login_params_from_url(login_page_url)

    # Login to @wifi.id
    got_response, msg = wifi.login(username, password, client_ip, gw_id, mac, wlan, redir)

    if got_response:
        print("Server response: " + str(msg))
    else:
        print("Login failed. " + str(msg))

if __name__ == "__main__":
    main()
