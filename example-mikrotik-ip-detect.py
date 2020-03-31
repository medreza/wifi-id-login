from wifiid_login import Wifi
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
