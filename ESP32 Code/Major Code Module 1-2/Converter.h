#pragma once
namespace Eloquent {
    namespace Projects {
        class WifiIndoorPositioning {
            public:
                float features[6] = {0};
                /**
                * Get feature vector
                */
                float* scan() {
                    uint8_t numNetworks = WiFi.scanNetworks();

                    for (uint8_t i = 0; i < 6; i++) {
                        features[i] = 0;
                    }

                    for (uint8_t i = 0; i < numNetworks; i++) {
                        int featureIdx = ssidToFeatureIdx(WiFi.SSID(i));

                        if (featureIdx >= 0) {
                            features[featureIdx] = WiFi.RSSI(i);
                        }
                    }

                    return features;
                }

            protected:
                /**
                * Convert SSID to featureIdx
                */
                int ssidToFeatureIdx(String ssid) {
                    if (ssid.equals("Alfa-X"))
                    return 0;

                    if (ssid.equals("Bagichi"))
                    return 1;

                    if (ssid.equals("CrazyTabbar"))
                    return 2;

                    if (ssid.equals("Dinesh 902"))
                    return 3;

                    if (ssid.equals("REYANSH"))
                    return 4;

                    if (ssid.equals("narang88"))
                    return 5;

                    return -1;
                }
            };
        }
    }
