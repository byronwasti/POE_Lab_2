#include <Servo.h>
Servo ser;
int angle = 90;

void setup()
{
    ser.attach(9);
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available() > 0) angle = Serial.read();

    ser.write(angle);
    delay(15);
}
