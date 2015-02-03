#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"
int sensorPin = A0;
int sensorValue = 0;

void setup(){
    Serial.begin(9600);
}

void loop(){
    sensorValue = analogRead(sensorPin);

    Serial.println(sensorValue);
    delay(2);
}

