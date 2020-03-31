import re, requests

class Wifi:
    def __init__(self, username, password, wifi_client_ip):
        self.username = username
        self.password = password
        self.wifi_client_ip = wifi_client_ip


    def login(self, gw_id, mac, wlan, redir):

        ''' Login to @wifi.id using http post method. Returns response status (True or False) and message.
            The message can be an error message or {"message"} response from the server '''

        auth_url = 'https://welcome2.wifi.id/authnew/login/check_login.php?ipc=' + str(self.wifi_client_ip) + '&gw_id=' + str(gw_id) + \
                   '&mac=' + str(mac) + '&redirect=' + str(redir) + '&wlan=' + str(wlan)
        credentials = {'username': str(self.username) + '@spin2', 'password': self.password}

        # Print credentials and auth_url
        print('$ Login using: ' + str(credentials))
        print()
        print('$ Sending HTTP POST request to: ' + str(auth_url))
        print()

        # Try POST request to auth_url
        try:
            response = requests.post(auth_url, data = credentials)
        except:
            return False, 'ERROR: Unable to reach URL: ' + str(auth_url)
            response = None

        # Check if response is as expected
        if response:
            try:
                return True, response.json()['message']
            except:
                return True, 'ERROR: Wrong server response'


    @staticmethod
    def _get_login_params_from_url(login_url):

        ''' Extract parameters from @wifi.id login URL. Returns: gw_id, mac, wlan, redirect_url '''

        match_data = re.search(r'gw_id=(.+)&client_mac=(.+)&wlan=(.+)&s(.+)&redirect=(.+)', login_url, re.IGNORECASE)
        return match_data.group(1), match_data.group(2), match_data.group(3), match_data.group(5)


    def login_with_url(self, login_url):

        ''' Get extracted params from url and do login '''

        gw_id, mac, wlan, redir = self._get_login_params_from_url(login_url)
        return self.login(gw_id, mac, wlan, redir)
