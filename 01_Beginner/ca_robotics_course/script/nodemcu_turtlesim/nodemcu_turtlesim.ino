#include <ros.h>
#include <std_msgs/Int32.h>
std_msgs::Int32 int_msg;
ros::NodeHandle nh;

const char* ssid = "itumodem";
const char* password = "itumodem";
IPAddress server(192,168,8,101);    // ini IP si roscore (master pc)
const uint16_t serverPort = 11411;

const int IRSensor = A0;
ros::Publisher IR_Sensor("values", &int_msg);


void setup() {
  Serial.begin(57600);
  nh.initNode();
  nh.advertise(IR_Sensor);
  pinMode(IRSensor, INPUT);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  nh.getHardware()->setConnection(server, serverPort);
}

void loop() {
  if(nh.connected()) {
    int_msg.data = analogRead(IRSensor);
    IR_Sensor.publish(&int_msg);
    Serial.println(int_msg.data);
    Serial.println(analogRead(IRSensor));
    Serial.println("---------------------");
  }
  nh.spinOnce();
  delay(1000);
}

/*
 cara nge test nya adalah
 1. roscore dulu
 2. rosrun rosserial_python serial_node.py tcp
 3. rostopic list ,,, muncul tocic /values
 */
