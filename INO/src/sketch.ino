#include <Servo.h>

int sensorPin = A0;
int sensorValue = 0;

Servo bottom_ser;   // Create Horiz rotation servo
Servo top_ser;      // Create Vert rotation servo

int pos_bot;
int pos_top;

const int bot_start = 0;
const int bot_end = 180;
const int top_start = 0;
const int top_end = 180;

void setup(){
    bottom_ser.attach(9);
    top_ser.attach(6);
    Serial.begin(9600);
}

void Sweep_Right(){
    for( pos_bot = bot_start; pos_bot <= bot_end; pos_bot++)
            /// Must figure out actual values for this
    {
        bottom_ser.write(pos_bot);
        Print_Pos();
        delay(15);
    }
}

void Sweep_Left(){
    for( pos_bot = bot_end; pos_bot >= bot_start; pos_bot--) // This should increment
                                    // the opposite way of Sweep_Right
    {
        bottom_ser.write(pos_bot);
        Print_Pos();
        delay(15);
    }
}

void Print_Pos(){
    sensorValue = analogRead(sensorPin);

    Serial.print(sensorValue);
    Serial.print(",");
    Serial.print(pos_bot);
    Serial.print(",");
    Serial.print(pos_top);
    Serial.print("\n");
}

void loop(){

    for( pos_top = top_start; pos_top <= top_end; pos_top ++) // WONT WORK
                        // The initial value must be tan -1 ( 15cm / H(in cm))
                        // End value must be related somehow
    {   
        Print_Pos();
        top_ser.write(pos_top);
        switch( pos_top%2) // Should check to see if this works
        {
            case 0: Sweep_Right(); break;
            case 1: Sweep_Left(); break;
        }
    }
    Serial.println("DONE");
}
