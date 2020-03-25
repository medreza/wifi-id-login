# wifi-id-login
The @wifi.id has been a lifesaver for the past 7 years of my life. But sometimes, it asks for login too many. If you're lucky, you get asked one login each day. If not, you can get four to five in a day. Wouldn't it be easier if this repetitive task can be automated?

## Disclaimer
This module is just a Python interface for @wifi.id login, **not a kind of hack tool** or something like that. You need a valid and legal @wifi.id account to use this.

*Program ini merupakan antarmuka Python untuk mengotomasikan proses login ke @wifi.id, **bukan hack tool** atau semacamnya. Anda tetap harus memiliki akun @wifi.id yang didapatkan secara legal :)*

## Usage
* #### Import the module and define your credentials
  ```python
  import wifiid_login as wifi

  username = '<your @wifi.id username>'
  password = '<your @wifi.id password>'
  ```

* #### Define your login params
  ##### Get the params from @wifi.id login page URL which usually starts with [https://welcome2.wifi.id/login/...](#)
  ```python
  my_ip = '<IP address of your connected device/interface to @wifi.id>'

  gw_id = '<@wifi.id gateway ID>'
  mac = '<your device/interface MAC address>'
  wlan = '<@wifi.id WLAN ID>'
  redirect = '<redirect URL>'
  ```

  ##### or you can extract them by passing the login page URL to ```get_login_params_from_url(url)```
  ```python
  my_ip = '<IP address of your connected device/interface to @wifi.id>'

  login_page_url = 'https://welcome2.wifi.id/login/....'
  gw_id, mac, wlan, redirect = wifi.get_login_params_from_url(login_page_url)
  ```
* #### ... and login!
  ```python
  wifi.login(username, password, my_ip, gw_id, mac, wlan, redirect)
  ```

## License
GNU GPLv3
