# wifi-id-login
The @wifi.id has been a lifesaver for the past 7 years of my life. But sometimes, it asks for login too many. If you're lucky, you get asked one login each day. If not, you can get four to five in a day. Wouldn't it be easier if this repetitive task can be automated?

## Disclaimer
This module is just a Python interface for @wifi.id login, **not a kind of hack/bypass tool** or something like that. You need a valid and legal @wifi.id account to use this.

*Program ini merupakan antarmuka Python untuk mengotomasikan proses login ke @wifi.id, **bukan hack/bypass tool** atau semacamnya. Anda tetap harus memiliki akun @wifi.id yang didapatkan secara legal :)*

## Usage
* #### Import the module, define your credentials, and create wifi instance
  ```python
  from wifiid_login import Wifi

  username = '<your @wifi.id username>'
  password = '<your @wifi.id password>'
  my_ip = '<IP address of your connected device/interface to @wifi.id>'
  
  wifi_id = Wifi(username, password, my_ip)
  ```

* #### Define your login params and login!
  ##### Define the params manually from @wifi.id login URL (which usually starts with [https://welcome2.wifi.id/login/...](#)) ..
  ```python
  gw_id = '<@wifi.id gateway ID>'
  mac = '<your device/interface MAC address>'
  wlan = '<@wifi.id WLAN ID>'
  redirect = '<redirect URL>'
  ```
  ##### .. and do login
  ```python
  wifi_id.login(gw_id, mac, wlan, redirect)
  ```

* #### Alternatively, you can simply login by passing the login page URL to ```login_with_url(url)``` method
  ```python
  login_page_url = 'https://welcome2.wifi.id/login/....'
  wifi_id.login_with_url(login_page_url)
  ```


## License
GNU GPLv3
