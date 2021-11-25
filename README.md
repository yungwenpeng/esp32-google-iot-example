# ESP32 With Google IOT Core  
  
## ESP-IDF Training  
Repository showing "how-to-build" fully functional IoT product with ESP-IDF framework.  
  
## Wi-Fi Provisioning Manager Example  
Add Wi-Fi Provisioning Manager,  
Refer to : https://github.com/espressif/esp-idf/tree/master/examples/provisioning/wifi_prov_mgr  
  
## Smart Outlet Example  
Add Google IoT Core Example,  
Refer to : https://github.com/espressif/esp-google-iot/tree/master/examples/smart_outlet  
    Generating an Elliptic Curve keys -> refer [here](https://cloud.google.com/iot/docs/how-tos/credentials/keys#generating_an_elliptic_curve_keys)  
        copy P-256 Elliptic Curve key (ec_private.pem) to example/main/certs/private_key.pem  
  
  
## How to use  
  $ idf.py menuconfig  
  -> Config Example Provisioning Configuration & Example Google IoT Core Configuration  
  Note : copy ECkey first  
  $ idf.py build  
  $ idf.py -p /dev/ttyUSB0 flash monitor  
     