#include <Servo.h>
Servo ser;
int angle = 90;
int tmp;

void setup()
{
    ser.attach(9);
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available() > 0){
        tmp = Serial.read();
        Serial.print(tmp);
        if ( tmp > 49 ) angle += 1;
        else angle -= 1;
        Serial.print(" : ");
        Serial.println(angle);
    }

    //ser.write(angle);
    delay(15);
    //Serial.println(angle);
}
