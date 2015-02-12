#include <Servo.h>
Servo ser1;
Servo ser2;
int angle1 = 90;
int angle2 = 90;
int tmp;

void setup()
{
    ser1.attach(9); 
    ser2.attach(6); 
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
        switch(tmp){
            case 49: angle1+=1;break;
            case 50: angle1-=1;break;
            case 51: angle2+=1;break;
            case 52: angle2-=1;break;
            default: break;
        }
        //if ( tmp == 49 ) angle += 1;
        //else angle -= 1;
        Serial.print(" : ");
        Serial.print(angle1);
        Serial.print(" : ");
        Serial.print(angle2);
        Serial.print(" at ");
        Serial.println(analogRead(A0));
    }

    ser1.write(angle1);
    ser2.write(angle2);
    delay(15);
    //Serial.println(angle);
}
