#include <ETH.h>
#include <WiFi.h>
#include <WiFiAP.h>
#include <WiFiClient.h>
#include <WiFiGeneric.h>
#include <WiFiMulti.h>
#include <WiFiScan.h>
#include <WiFiServer.h>
#include <WiFiSTA.h>
#include <WiFiType.h>
#include <WiFiUdp.h>


void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();

    knownNetworks.push("SSID #0");
    knownNetworks.push("SSID #1");
    knownNetworks.push("SSID #2");
    knownNetworks.push("SSID #3");
    // and so on
}
void loop() {
    scan();
    printFeatures();
    delay(3000);
}

void scan() {
    int numNetworks = WiFi.scanNetworks();

    resetFeatures();

    // assign RSSIs to feature vector
    for (int i = 0; i < numNetworks; i++) {
        String ssid = WiFi.SSID(i);
        uint16_t networkIndex = knownNetworks.indexOf(ssid);

        // only create feature if the current SSID is a known one
        if (!isnan(networkIndex))
            features[networkIndex] = WiFi.RSSI(i);
    }
}

// reset all features to 0
void resetFeatures() {
    const uint16_t numFeatures = sizeof(features) / sizeof(double);

    for (int i = 0; i < numFeatues; i++)
        features[i] = 0;
}

void printFeatures() {
    const uint16_t numFeatures = sizeof(features) / sizeof(float);
    
    for (int i = 0; i < numFeatures; i++) {
        Serial.print(features[i]);
        Serial.print(i == numFeatures - 1 ? 'n' : ',');
    }
}
