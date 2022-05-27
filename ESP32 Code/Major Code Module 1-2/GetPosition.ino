#include <common.h>
#include <Firebase.h>
#include <FirebaseFS.h>
#include <Firebase_ESP_Client.h>
#include <Utils.h>




#include <WiFi.h>
/*#include <Arduino.h>
#include <Firebase_ESP_Client.h>*/


#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"

#include "Converter.h"
#include "Classifier.h"

#define WIFI_SSID "Alfa-X" 
#define WIFI_PASSWORD "bhavya123" 

#define DATABASE_URL "https://virtual-navigator-9324d-default-rtdb.firebaseio.com/"
#define API_KEY "AIzaSyAeSC0qp61YN9Xsvjhi68p0VZY7z_qT9m8"

FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
int count = 0; 
bool isAuthenticated = false;

String route[3][3] = {{"Courtyard","+1","+1"} , {"+1","The Great Hall","Garden"} , {"Exit 1","+1","+1"}};

int counter = 0;

Eloquent::Projects::WifiIndoorPositioning positioning;
Eloquent::ML::Port::DecisionTree classifier;

void setup() {
  Serial.begin(115200);
  delay(1000);
  WiFi_setup();
  Firebase_setup(); 
}

void loop() {
  positioning.scan();
  Serial.print("You're in ");
  String destination="";
  destination = classifier.predictLabel(positioning.features);
  Serial.println(destination);
  /*if (Firebase.ready() && signupOK && (millis() - sendDataPrevMillis > 15000 || sendDataPrevMillis == 0)){
    sendDataPrevMillis = millis();
  }*/
  String ssid=WIFI_SSID;
  int rssi = WiFi.RSSI();
  
  /*if(counter == 0)
  {
    path[counter] = destination;
    counter++;
  }
  else
  {
    if(path[counter-1] != destination)
    {
      path[counter] = destination;
      counter++;
    }
  }*/
  Firebase.RTDB.setString(&fbdo,"UmJMul34a0OXM6g3SnjGkRfdUQF3/Location", destination);
  Firebase.RTDB.setString(&fbdo,"UmJMul34a0OXM6g3SnjGkRfdUQF3/Network SSID", ssid);
  Firebase.RTDB.setInt(&fbdo,"UmJMul34a0OXM6g3SnjGkRfdUQF3/Network RSSI", rssi);
  /*String s = "";
  for(int j=0;j<counter;j++)
  {
    s=s+path[j];
    if(j!=counter-1)
      s=s+"-";
  }
  Firebase.RTDB.setString(&fbdo,"UmJMul34a0OXM6g3SnjGkRfdUQF3/Path", s);*/
  String final = "";
  if(Firebase.RTDB.getString(&fbdo,"UmJMul34a0OXM6g3SnjGkRfdUQF3/Destination"))
  {
    final = fbdo.stringData();
    getDirections(final,destination);
    /*Serial.println(final);*/
  }
  
  
  delay(3000);
}

void WiFi_setup()
{
   WiFi.begin(WIFI_SSID, WIFI_PASSWORD);                       
   Serial.print("Connecting"); 
   while (WiFi.status() != WL_CONNECTED) { 
     Serial.print("."); 
     delay(500);
   }
   Serial.println(); 
   Serial.print("Connected: "); 
   Serial.println(WiFi.localIP());
}
void Firebase_setup()
{
  config.api_key = API_KEY;
   config.database_url = DATABASE_URL;
   Firebase.reconnectWiFi(true);
   Serial.println("------------------------------------");
   Serial.println("Sign up new user...");
   if (Firebase.signUp(&config, &auth, "", ""))
   {
      Serial.println("Success");
      isAuthenticated = true;
   }
   else
   {
     Serial.printf("Failed, %s\n", config.signer.signupError.message.c_str());
     isAuthenticated = false;
   }

   config.token_status_callback = tokenStatusCallback;
   Firebase.begin(&config, &auth);
}
void getDirections(String final, String destination)
{
  if(final == destination)
  {
    return;
  }
  int i1=0,j1=0,i2=0,j2=0;
  for(int k=0;k<3;k++)
  {
    for(int l=0;l<3;l++)
    {
      String s = route[k][l];
      if(s == final)
      {
        i2=k;
        j2=l;
      }
      if(s == destination)
      {
        i1=k;
        j1=l;
      }
    }
  }
  String path = "";
  if(i1<=i2 && j1<=j2)
  {
    while(i1!=i2)
    {
      path = path + " Go Straight ";
      i1++;
      if(i1!=i2)
      {
        path = path + "=>";
      }
      if(i1==i2 && j1!=j2)
      {
        path = path + "=>";
      }
    }
    if(j1!=j2)
    {
      path = path + " Turn Left ";
      path = path + "=>";
      while(j1!=j2)
      {
        path = path + " Go Straight ";
        j1++;
        if(j1!=j2)
        {
          path = path + "=>";
        }
      }
    }
  }

  else if(i1<=i2 && j1>j2)
  {
    while(i1!=i2)
    {
      path = path + " Go Straight ";
      i1++;
      if(i1!=i2)
      {
        path = path + "=>";
      }
      if(i1==i2 && j1!=j2)
      {
        path = path + "=>";
      }
    }
    if(j1!=j2)
    {
      path = path + " Turn Right ";
      path = path + "=>";
      while(j1!=j2)
      {
        path = path + " Go Straight ";
        j1--;
        if(j1!=j2)
        {
          path = path + "=>";
        }
      }
    }
  }

  else if(i1>=i2 && j1>=j2)
  {
      path = path + " Turn Back ";
      path = path + "=>";
      if(i1!=i2)
      {
         while(i1!=i2)
        {
          path = path + " Go Straight ";
          i1--;
          if(i1!=i2)
          {
             path = path + "=>";
          }
          if(i1==i2 && j1!=j2)
          {
            path = path + "=>";
          }
        }
      }
        if(j1!=j2)
        {
          path = path + " Turn Left ";
          path = path + "=>";
          while(j1!=j2)
          {
            path = path + " Go Straight ";
            j1--;
            if(j1!=j2)
            {
              path = path + "=>";
            }
          }
        }
      
  }

  else
  {
    path = path + " Turn Back ";
      path = path + "=>";
      if(i1!=i2)
      {
         while(i1!=i2)
        {
          path = path + " Go Straight ";
          i1--;
          if(i1!=i2)
          {
             path = path + "=>";
          }
          if(i1==i2 && j1!=j2)
          {
            path = path + "=>";
          }
        }
      }
      if(j1!=j2)
    {
      path = path + " Turn Right ";
      path = path + "=>";
      while(j1!=j2)
      {
        path = path + " Go Straight ";
        j1++;
        if(j1!=j2)
        {
          path = path + "=>";
        }
      }
    }
      
  }
  Firebase.RTDB.setString(&fbdo,"UmJMul34a0OXM6g3SnjGkRfdUQF3/Path", path);
}
