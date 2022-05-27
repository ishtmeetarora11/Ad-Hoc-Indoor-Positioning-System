#!/usr/bin/env python
# coding: utf-8

# In[1]:


from micromlgen import port_wifi_indoor_positioning
import json

if __name__ == '__main__':
    samples = '''
    {"__location": "room1", "Alfa-X": -58, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -52, "Dinesh 902": -93, "CrazyTabbar": -93, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -48}
    {"__location": "room1", "Alfa-X": -65, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -73, "Bagichi": -92}
    {"__location": "room1", "Alfa-X": -68, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -64}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -93, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -66, "Bagichi": -92}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -64, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -58, "Bagichi": -91, "CrazyTabbar": -91}
    {"__location": "room1", "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -91, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -45, "Bagichi": -89, "CrazyTabbar": -90}
    {"__location": "room1", "Alfa-X": -55, "Bagichi": -91, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -61, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -76, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -81, "Dinesh 902": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -75, "Dinesh 902": -91, "CrazyTabbar": -93, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -66, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -66, "Bagichi": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -76, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -82, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -77, "Bagichi": -93, "Dinesh 902": -94, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -92, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -73, "Bagichi": -89, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -66, "CrazyTabbar": -93, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -68, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -59, "Bagichi": -92, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -57, "Bagichi": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -57, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -57, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -92, "Dinesh 902": -93}
    {"__location": "room1", "Alfa-X": -63, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -65, "Bagichi": -89, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -94, "Bagichi": -96}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -90, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -59, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -70, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -65, "Bagichi": -92, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -66, "CrazyTabbar": -94, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -61, "Bagichi": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -61, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -61, "CrazyTabbar": -94, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -63, "Bagichi": -91, "Dinesh 902": -93, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -48, "CrazyTabbar": -91, "Dinesh 902": -92}
    {"__location": "room1", "Alfa-X": -55, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -55, "Bagichi": -90, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -60, "Bagichi": -92}
    {"__location": "room1", "Alfa-X": -69, "CrazyTabbar": -92, "Bagichi": -93}
    {"__location": "room1", "Alfa-X": -61, "Bagichi": -92, "REYANSH": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -90, "Bagichi": -93}
    {"__location": "room1", "Alfa-X": -57, "CrazyTabbar": -89, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -60, "Bagichi": -91, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -56, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -58, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -58, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -64, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -92, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -47}
    {"__location": "room1", "Alfa-X": -58, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -91, "CrazyTabbar": -99}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -53, "Bagichi": -95, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -47, "CrazyTabbar": -96}
    {"__location": "room1", "Alfa-X": -56, "CrazyTabbar": -96}
    {"__location": "room1", "Alfa-X": -50}
    {"__location": "room1", "Alfa-X": -55, "Bagichi": -91, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -46, "Dinesh 902": -93}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -91, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -89}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -44, "Bagichi": -90, "REYANSH": -91, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -91, "Dinesh 902": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -48, "CrazyTabbar": -90, "Bagichi": -92, "REYANSH": -93}
    {"__location": "room1", "Alfa-X": -49, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -50, "Bagichi": -92, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -50, "Bagichi": -90, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -90, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -92, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -54, "Bagichi": -95, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -53, "Bagichi": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -56, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -54, "Bagichi": -93, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -91, "REYANSH": -93}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -90}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -93, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -90, "CrazyTabbar": -93}
    {"__location": "room2", "Alfa-X": -40, "Bagichi": -89, "narang88": -93}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81, "narang88": -93}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -82, "narang88": -90}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -89, "narang88": -96}
    {"__location": "room2", "Bagichi": -83, "narang88": -92}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -83, "narang88": -94}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -83, "narang88": -94}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81, "narang88": -93}
    {"__location": "room2", "Alfa-X": -61, "Bagichi": -84, "narang88": -91}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -89, "narang88": -92}
    {"__location": "room2", "Alfa-X": -59, "Bagichi": -88, "narang88": -93}
    {"__location": "room2", "Alfa-X": -74, "narang88": -93, "Bagichi": -95}
    {"__location": "room2", "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -65, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -83, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -81, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -69, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -68, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -80, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -67, "narang88": -94}
    {"__location": "room2", "Alfa-X": -61, "Bagichi": -80}
    {"__location": "room2", "Alfa-X": -57, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -56, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -68, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -65, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -67, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -63, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -76, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -65, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -72, "Bagichi": -94}
    {"__location": "room2", "Alfa-X": -72, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -76, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -73, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -62, "Bagichi": -89}
    {"__location": "room2", "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -87, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -82, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -79, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -81, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -78, "Bagichi": -81, "narang88": -93}
    {"__location": "room2", "Alfa-X": -64, "Bagichi": -88, "narang88": -94}
    {"__location": "room2", "Alfa-X": -64, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -70, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -68, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -68, "narang88": -96}
    {"__location": "room2", "Alfa-X": -74, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -84, "Bagichi": -88}
    {"__location": "room2", "Bagichi": -82}
    {"__location": "room2", "Bagichi": -83, "Alfa-X": -92}
    {"__location": "room2", "Alfa-X": -63, "Bagichi": -80}
    {"__location": "room2", "Alfa-X": -78, "Bagichi": -82, "narang88": -93}
    {"__location": "room2", "Alfa-X": -78, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -72, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -66, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -63, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -64, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -71, "Bagichi": -92, "narang88": -94}
    {"__location": "room2", "Alfa-X": -60, "Bagichi": -90, "narang88": -93}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -82, "narang88": -95}
    {"__location": "room2", "Alfa-X": -53, "Bagichi": -79}
    {"__location": "room2", "Alfa-X": -44, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -92}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -51, "Bagichi": -89, "narang88": -92}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -90, "narang88": -93}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -86}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -92}
    {"__location": "room2", "Bagichi": -87, "narang88": -94}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -86, "narang88": -92}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -90, "narang88": -91}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -55, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -56, "Bagichi": -89, "narang88": -91}
    {"__location": "room2", "Alfa-X": -56, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -92, "narang88": -93}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -84, "narang88": -94}
    {"__location": "room2", "Alfa-X": -53, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -51, "Bagichi": -90, "narang88": -93}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -89, "narang88": -92}
    {"__location": "room2", "Alfa-X": -55, "Bagichi": -87, "narang88": -88}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -85, "narang88": -93}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -85, "narang88": -92}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -49}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -51, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -62, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -60, "Bagichi": -83, "narang88": -94}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -40, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -34, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -33, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -80}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -86}
    {"__location": "room2", "Alfa-X": -37, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -86}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -38, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -39, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -40, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -86, "narang88": -94}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -90, "narang88": -92}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -85, "narang88": -94}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -86, "narang88": -93}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -93, "narang88": -95}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -68}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -44, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -52, "Bagichi": -65}
    {"__location": "room3", "Bagichi": -64, "Alfa-X": -67}
    {"__location": "room3", "Bagichi": -76}
    {"__location": "room3", "Alfa-X": -64, "Bagichi": -69}
    {"__location": "room3", "Bagichi": -64, "Alfa-X": -73}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -67}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -67, "Bagichi": -70}
    {"__location": "room3", "Alfa-X": -66, "Bagichi": -67}
    {"__location": "room3", "Alfa-X": -65, "Bagichi": -70}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -68}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -64}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -67}
    {"__location": "room3", "Bagichi": -64, "Alfa-X": -68}
    {"__location": "room3", "Alfa-X": -66, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -60, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -60, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -65, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -79}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -68}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -66}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -70}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -60, "Bagichi": -64}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -69}
    {"__location": "room3", "Bagichi": -68, "Alfa-X": -69}
    {"__location": "room3", "Bagichi": -65}
    {"__location": "room3", "Bagichi": -69, "Alfa-X": -80}
    {"__location": "room3", "Bagichi": -65, "narang88": -95}
    {"__location": "room3", "Alfa-X": -58, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -55, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -69, "narang88": -92}
    {"__location": "room3", "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -54, "Bagichi": -66}
    {"__location": "room3", "Alfa-X": -54, "Bagichi": -68}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -65}
    {"__location": "room3", "Bagichi": -67, "Alfa-X": -69}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -71, "narang88": -95}
    {"__location": "room3", "Bagichi": -70, "Alfa-X": -77, "narang88": -91}
    {"__location": "room4", "Alfa-X": -38, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -37, "Bagichi": -65}
    {"__location": "room4", "Alfa-X": -40, "Bagichi": -73, "narang88": -95}
    {"__location": "room4", "Alfa-X": -33, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -32, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -30, "Bagichi": -69}
    {"__location": "room4", "Alfa-X": -43, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -65}
    {"__location": "room4", "Alfa-X": -61, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -65}
    {"__location": "room4", "Bagichi": -65, "Alfa-X": -66}
    {"__location": "room4", "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -63, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -64, "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -64, "Bagichi": -71}
    {"__location": "room4", "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -59, "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -56, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -56, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -69}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -73}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -72}
    {"__location": "room4", "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -56, "Bagichi": -73}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -71}
    {"__location": "room4", "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -71}
    {"__location": "room4", "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -70}
    {"__location": "room4", "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -72}
    {"__location": "room4", "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -72}
    {"__location": "room4", "Bagichi": -76}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -40, "Bagichi": -75}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -41, "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -41, "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -40, "Bagichi": -76}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -74}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -41, "Bagichi": -76}
    {"__location": "room4", "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -37, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -37, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -70}
    {"__location": "room4", "Bagichi": -74}
    '''
    X, y, classmap, converter_code = port_wifi_indoor_positioning(samples)
    print(converter_code)


# In[2]:


from sklearn.tree import DecisionTreeClassifier
from micromlgen import port_wifi_indoor_positioning, port
import pandas as pd

if __name__ == '__main__':
    samples = '''
    {"__location": "room1", "Alfa-X": -58, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -52, "Dinesh 902": -93, "CrazyTabbar": -93, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -48}
    {"__location": "room1", "Alfa-X": -65, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -73, "Bagichi": -92}
    {"__location": "room1", "Alfa-X": -68, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -64}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -93, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -66, "Bagichi": -92}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -64, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -58, "Bagichi": -91, "CrazyTabbar": -91}
    {"__location": "room1", "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -91, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -45, "Bagichi": -89, "CrazyTabbar": -90}
    {"__location": "room1", "Alfa-X": -55, "Bagichi": -91, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -61, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -76, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -81, "Dinesh 902": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -75, "Dinesh 902": -91, "CrazyTabbar": -93, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -66, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -66, "Bagichi": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -76, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -82, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -77, "Bagichi": -93, "Dinesh 902": -94, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -92, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -73, "Bagichi": -89, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -66, "CrazyTabbar": -93, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -68, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -59, "Bagichi": -92, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -57, "Bagichi": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -57, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -57, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -92, "Dinesh 902": -93}
    {"__location": "room1", "Alfa-X": -63, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -65, "Bagichi": -89, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -94, "Bagichi": -96}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -90, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -59, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -70, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -65, "Bagichi": -92, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -66, "CrazyTabbar": -94, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -61, "Bagichi": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -61, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -61, "CrazyTabbar": -94, "Bagichi": -95}
    {"__location": "room1", "Alfa-X": -63, "Bagichi": -91, "Dinesh 902": -93, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -48, "CrazyTabbar": -91, "Dinesh 902": -92}
    {"__location": "room1", "Alfa-X": -55, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -55, "Bagichi": -90, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -60, "Bagichi": -92}
    {"__location": "room1", "Alfa-X": -69, "CrazyTabbar": -92, "Bagichi": -93}
    {"__location": "room1", "Alfa-X": -61, "Bagichi": -92, "REYANSH": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -62, "Bagichi": -91, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -90, "Bagichi": -93}
    {"__location": "room1", "Alfa-X": -57, "CrazyTabbar": -89, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -60, "Bagichi": -91, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -56, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -58, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -58, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -64, "Bagichi": -92, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -60, "CrazyTabbar": -92, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -47}
    {"__location": "room1", "Alfa-X": -58, "Bagichi": -93, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -91, "CrazyTabbar": -99}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -53, "Bagichi": -95, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -47, "CrazyTabbar": -96}
    {"__location": "room1", "Alfa-X": -56, "CrazyTabbar": -96}
    {"__location": "room1", "Alfa-X": -50}
    {"__location": "room1", "Alfa-X": -55, "Bagichi": -91, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -46, "Dinesh 902": -93}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -91, "Bagichi": -94}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -89}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -44, "Bagichi": -90, "REYANSH": -91, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -91, "Dinesh 902": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -48, "CrazyTabbar": -90, "Bagichi": -92, "REYANSH": -93}
    {"__location": "room1", "Alfa-X": -49, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -50, "Bagichi": -92, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -50, "Bagichi": -90, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -90, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -92, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -54, "Bagichi": -95, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -53, "Bagichi": -92, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -56, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -54, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -54, "Bagichi": -93, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -91, "REYANSH": -93}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -94}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -92}
    {"__location": "room1", "Alfa-X": -50, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -51, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -90}
    {"__location": "room1", "Alfa-X": -52, "CrazyTabbar": -91}
    {"__location": "room1", "Alfa-X": -53, "CrazyTabbar": -93}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -93, "CrazyTabbar": -95}
    {"__location": "room1", "Alfa-X": -52, "Bagichi": -90, "CrazyTabbar": -93}
    {"__location": "room2", "Alfa-X": -40, "Bagichi": -89, "narang88": -93}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81, "narang88": -93}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -82, "narang88": -90}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -89, "narang88": -96}
    {"__location": "room2", "Bagichi": -83, "narang88": -92}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -83, "narang88": -94}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -83, "narang88": -94}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81, "narang88": -93}
    {"__location": "room2", "Alfa-X": -61, "Bagichi": -84, "narang88": -91}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -89, "narang88": -92}
    {"__location": "room2", "Alfa-X": -59, "Bagichi": -88, "narang88": -93}
    {"__location": "room2", "Alfa-X": -74, "narang88": -93, "Bagichi": -95}
    {"__location": "room2", "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -65, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -83, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -81, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -69, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -68, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -80, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -67, "narang88": -94}
    {"__location": "room2", "Alfa-X": -61, "Bagichi": -80}
    {"__location": "room2", "Alfa-X": -57, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -56, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -68, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -65, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -67, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -63, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -76, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -65, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -72, "Bagichi": -94}
    {"__location": "room2", "Alfa-X": -72, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -76, "Bagichi": -91}
    {"__location": "room2", "Alfa-X": -73, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -62, "Bagichi": -89}
    {"__location": "room2", "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -87, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -82, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -79, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -81, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -78, "Bagichi": -81, "narang88": -93}
    {"__location": "room2", "Alfa-X": -64, "Bagichi": -88, "narang88": -94}
    {"__location": "room2", "Alfa-X": -64, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -70, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -68, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -68, "narang88": -96}
    {"__location": "room2", "Alfa-X": -74, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -84, "Bagichi": -88}
    {"__location": "room2", "Bagichi": -82}
    {"__location": "room2", "Bagichi": -83, "Alfa-X": -92}
    {"__location": "room2", "Alfa-X": -63, "Bagichi": -80}
    {"__location": "room2", "Alfa-X": -78, "Bagichi": -82, "narang88": -93}
    {"__location": "room2", "Alfa-X": -78, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -72, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -66, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -63, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -64, "Bagichi": -90}
    {"__location": "room2", "Alfa-X": -71, "Bagichi": -92, "narang88": -94}
    {"__location": "room2", "Alfa-X": -60, "Bagichi": -90, "narang88": -93}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -82, "narang88": -95}
    {"__location": "room2", "Alfa-X": -53, "Bagichi": -79}
    {"__location": "room2", "Alfa-X": -44, "Bagichi": -83}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -92}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -51, "Bagichi": -89, "narang88": -92}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -90, "narang88": -93}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -86}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -92}
    {"__location": "room2", "Bagichi": -87, "narang88": -94}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -86, "narang88": -92}
    {"__location": "room2", "Alfa-X": -52, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -90, "narang88": -91}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -55, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -56, "Bagichi": -89, "narang88": -91}
    {"__location": "room2", "Alfa-X": -56, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -92, "narang88": -93}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -84, "narang88": -94}
    {"__location": "room2", "Alfa-X": -53, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -51, "Bagichi": -90, "narang88": -93}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -89, "narang88": -92}
    {"__location": "room2", "Alfa-X": -55, "Bagichi": -87, "narang88": -88}
    {"__location": "room2", "Alfa-X": -50, "Bagichi": -85, "narang88": -93}
    {"__location": "room2", "Alfa-X": -49, "Bagichi": -85, "narang88": -92}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -49}
    {"__location": "room2", "Alfa-X": -47, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -51, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -62, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -60, "Bagichi": -83, "narang88": -94}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -54, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -40, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -88}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -34, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -33, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -81}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -80}
    {"__location": "room2", "Alfa-X": -36, "Bagichi": -84}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -86}
    {"__location": "room2", "Alfa-X": -37, "Bagichi": -85}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -86}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -45, "Bagichi": -89}
    {"__location": "room2", "Alfa-X": -38, "Bagichi": -82}
    {"__location": "room2", "Alfa-X": -39, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -40, "Bagichi": -87}
    {"__location": "room2", "Alfa-X": -35, "Bagichi": -86, "narang88": -94}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -90, "narang88": -92}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -85, "narang88": -94}
    {"__location": "room2", "Alfa-X": -48, "Bagichi": -86, "narang88": -93}
    {"__location": "room2", "Alfa-X": -46, "Bagichi": -93, "narang88": -95}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -68}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -44, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -52, "Bagichi": -65}
    {"__location": "room3", "Bagichi": -64, "Alfa-X": -67}
    {"__location": "room3", "Bagichi": -76}
    {"__location": "room3", "Alfa-X": -64, "Bagichi": -69}
    {"__location": "room3", "Bagichi": -64, "Alfa-X": -73}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -67}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -67, "Bagichi": -70}
    {"__location": "room3", "Alfa-X": -66, "Bagichi": -67}
    {"__location": "room3", "Alfa-X": -65, "Bagichi": -70}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -68}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -64}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -67}
    {"__location": "room3", "Bagichi": -64, "Alfa-X": -68}
    {"__location": "room3", "Alfa-X": -66, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -60, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -60, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -65, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -79}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -68}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -66}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -63, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -70}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -61, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -60, "Bagichi": -64}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -62, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -69}
    {"__location": "room3", "Bagichi": -68, "Alfa-X": -69}
    {"__location": "room3", "Bagichi": -65}
    {"__location": "room3", "Bagichi": -69, "Alfa-X": -80}
    {"__location": "room3", "Bagichi": -65, "narang88": -95}
    {"__location": "room3", "Alfa-X": -58, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -59, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -55, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -69, "narang88": -92}
    {"__location": "room3", "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -69}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -64}
    {"__location": "room3", "Alfa-X": -57, "Bagichi": -65}
    {"__location": "room3", "Alfa-X": -54, "Bagichi": -66}
    {"__location": "room3", "Alfa-X": -54, "Bagichi": -68}
    {"__location": "room3", "Alfa-X": -56, "Bagichi": -65}
    {"__location": "room3", "Bagichi": -67, "Alfa-X": -69}
    {"__location": "room3", "Bagichi": -69}
    {"__location": "room3", "Bagichi": -65, "Alfa-X": -71, "narang88": -95}
    {"__location": "room3", "Bagichi": -70, "Alfa-X": -77, "narang88": -91}
    {"__location": "room4", "Alfa-X": -38, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -37, "Bagichi": -65}
    {"__location": "room4", "Alfa-X": -40, "Bagichi": -73, "narang88": -95}
    {"__location": "room4", "Alfa-X": -33, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -32, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -30, "Bagichi": -69}
    {"__location": "room4", "Alfa-X": -43, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -65}
    {"__location": "room4", "Alfa-X": -61, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -65}
    {"__location": "room4", "Bagichi": -65, "Alfa-X": -66}
    {"__location": "room4", "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -63, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -64, "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -64, "Bagichi": -71}
    {"__location": "room4", "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -59, "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -56, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -56, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -69}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -73}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -72}
    {"__location": "room4", "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -56, "Bagichi": -73}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -53, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -57, "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -71}
    {"__location": "room4", "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -54, "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -71}
    {"__location": "room4", "Bagichi": -70}
    {"__location": "room4", "Alfa-X": -51, "Bagichi": -70}
    {"__location": "room4", "Bagichi": -67}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -67}
    {"__location": "room4", "Bagichi": -71}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -68}
    {"__location": "room4", "Alfa-X": -52, "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -50, "Bagichi": -68}
    {"__location": "room4", "Bagichi": -66}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -72}
    {"__location": "room4", "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -72}
    {"__location": "room4", "Bagichi": -76}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -40, "Bagichi": -75}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -41, "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -41, "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -40, "Bagichi": -76}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -74}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -41, "Bagichi": -76}
    {"__location": "room4", "Bagichi": -72}
    {"__location": "room4", "Alfa-X": -39, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -75}
    {"__location": "room4", "Alfa-X": -37, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -37, "Bagichi": -73}
    {"__location": "room4", "Bagichi": -74}
    {"__location": "room4", "Alfa-X": -55, "Bagichi": -70}
    {"__location": "room4", "Bagichi": -74}
    '''
    X, y, classmap, converter_code = port_wifi_indoor_positioning(samples)
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    print(classmap)


# In[3]:


import json
import csv

with open('dataset1.json') as json_file:
    data = json.load(json_file)

wifi_data = data['wifi_ssid']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for ssid in wifi_data:
    if count == 0:

        # Writing headers of CSV file
        header = ssid.keys()
        csv_writer.writerow(header)
        count += 1
        
    # Writing data of CSV file
    csv_writer.writerow(ssid.values())

data_file.close()


# In[4]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
x_train, x_val, y_train, y_val = train_test_split(X, y, test_size = 0.7, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_pred = knn.predict(x_val)
acc_knn = round(accuracy_score(y_pred, y_val) * 100, 2)

from sklearn.ensemble import RandomForestClassifier

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_val)
acc_randomforest = round(accuracy_score(y_pred, y_val) * 100, 2)

from sklearn.tree import DecisionTreeClassifier

decisiontree = DecisionTreeClassifier()
decisiontree.fit(x_train, y_train)
y_pred = decisiontree.predict(x_val)
acc_decisiontree = round(accuracy_score(y_pred, y_val) * 100, 2)
print(acc_decisiontree)

from sklearn.svm import LinearSVC

linear_svc = LinearSVC()
linear_svc.fit(x_train, y_train)
y_pred = linear_svc.predict(x_val)
acc_linear_svc = round(accuracy_score(y_pred, y_val) * 100, 2)

from sklearn.svm import SVC

svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_val)
acc_svc = round(accuracy_score(y_pred, y_val) * 100, 2)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(x_train, y_train)
y_pred = logreg.predict(x_val)
acc_logreg = round(accuracy_score(y_pred, y_val) * 100, 2)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

gaussian = GaussianNB()
gaussian.fit(x_train, y_train)
y_pred = gaussian.predict(x_val)
acc_gaussian = round(accuracy_score(y_pred, y_val) * 100, 2)

models = pd.DataFrame({
    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression', 
              'Random Forest', 'Naive Bayes', 'Linear SVC', 
              'Decision Tree'],
    'Score': [acc_svc, acc_knn, acc_logreg, 
              acc_randomforest, acc_gaussian,acc_linear_svc, acc_decisiontree]})
models.sort_values(by='Score', ascending=False)


# In[ ]:





# In[ ]:




