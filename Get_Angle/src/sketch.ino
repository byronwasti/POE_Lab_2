#include <Servo.h>
Servo ser;
int angle = 90;
int tmp;

void setup()
{
    ser.attach(9);
    pinMode(7, OUTPUT);
    pinMode(8,OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);

    if (Serial.available() > 0){
        
        digitalWrite(7,HIGH);
        digitalWrite(8,HIGH);
        tmp = Serial.read();
        Serial.print(tmp);
        if ( tmp > 49 ) angle += 1;
        else angle -= 1;
        Serial.print(" : ");
        Serial.println(angle);
    }

    ser.write(angle);
    delay(15);
    //Serial.println(angle);
}
