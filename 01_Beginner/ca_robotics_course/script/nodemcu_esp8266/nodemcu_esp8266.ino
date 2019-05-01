#include <ESP8266WiFi.h>
#include <WiFiUdp.h>


int INbPin1 = D2;
int INaPin1 = D1;
int INaPin2 = D4;
int INbPin2 = D3;

//4321
//psrb esp
//17 18 19 20
//rbps driver

WiFiUDP Udp;

const char* ssid = "itumodem";
const char* password = "itumodem";
unsigned int localPort = 8888;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];


void setup() {
//  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(INaPin1, OUTPUT);
  pinMode(INbPin1, OUTPUT);
  pinMode(INaPin2, OUTPUT);
  pinMode(INbPin2, OUTPUT);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.print("\nConnected! IP address: ");
  Serial.println(WiFi.localIP());
  Serial.printf("UDP server on port %d\n", localPort);
  Udp.begin(localPort);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if(packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for(int i = 0; i < 4; i++){
      Serial.print(remote[i], DEC);
      if(i < 3) {Serial.print(".");}
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());
    
    // read the packet into packetBuffet
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.println("Contents: ");
    String directions = "";
    for(int i=0; i<=UDP_TX_PACKET_MAX_SIZE; i++){
      if(packetBuffer[i] == '*'){
        move_bot(directions);
        break;
      }
      directions += packetBuffer[i];
    }
  }
  delay(10);
}

void move_bot(String a){
  int commaIndex = a.indexOf(',');
  int secondCommaIndex = a.indexOf(',', commaIndex + 1);
  String firstValue = a.substring(0, commaIndex);
  String secondValue = a.substring(commaIndex + 1, secondCommaIndex);
  int linear = firstValue.toInt();
  int angular = secondValue.toInt();
  Serial.print("Linear :");
  Serial.println(linear);
  Serial.print("Angular :");
  Serial.println(angular);
  Serial.println("-------------------------");
  if(linear > 0 && angular == 0){
    // FORWARD
    Serial.println("FORWARD");
    digitalWrite(INaPin1, HIGH);
    digitalWrite(INaPin2, HIGH);

    digitalWrite(INbPin1, LOW);
    digitalWrite(INbPin2, LOW);
    delay(2000);
    stop();
  }
  else if(linear < 0 && angular == 0){
    // REVERSE
    Serial.println("REVERSE");
    digitalWrite(INaPin1, LOW);
    digitalWrite(INaPin2, LOW);

    digitalWrite(INbPin1, HIGH);
    digitalWrite(INbPin2, HIGH);
    delay(2000);
    stop();
  }
  else if(linear == 0 && angular > 0){
    // LEFT
    Serial.println("LEFT");
    digitalWrite(INaPin1, HIGH);
    digitalWrite(INaPin2, LOW);

    digitalWrite(INbPin1, LOW);
    digitalWrite(INbPin2, HIGH);
    delay(1000);
    stop();
  }
  else if(linear == 0 && angular < 0){
    // RIGHT
    Serial.println("RIGH");
    digitalWrite(INaPin1, LOW);
    digitalWrite(INaPin2, HIGH);

    digitalWrite(INbPin1, HIGH);
    digitalWrite(INbPin2, LOW);
    delay(1000);
    stop();
  }
  else{
    stop();
  }
}

void stop(){
  digitalWrite(INaPin1, LOW);
  digitalWrite(INaPin2, LOW);

  digitalWrite(INbPin1, LOW);
  digitalWrite(INbPin2, LOW);
}



//  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//  delay(1000);                       // wait for a second
//  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
//  delay(1000);                       // wait for a second
