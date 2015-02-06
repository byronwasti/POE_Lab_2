#include <Servo.h>

int incomingByte = 0;   // for incoming serial data
int sensorPin = A0;
int sensorValue = 0;

// Creating the bottom and top servos
Servo bser;
Servo tser; 

// Giving these initial values
const int bstart = 0;
const int bend = 180;
const int tstart = 0;
const int tend = 180;

// Setting up variables to hold servo positions
int bpos = bstart;
int tpos = tstart;

// Variable to control how many data points to take
int steps = 5;

void setup() {
    
    // Open serial port at 9600 baud rate
    Serial.begin(9600);    

    // Set up pin 3 as output for debugging
    pinMode(3, OUTPUT);

    // Set up both Servos
    bser.attach(9);
    tser.attach(6);
}


int enabled = 0;
int i = 0;

void loop() {
    digitalWrite(3, LOW);

    // send data only when you receive data:
    if (Serial.available() > 0) {
        Serial.flush();
        i++;
        enabled = 1;

        digitalWrite(3, HIGH);

        // read the incoming byte:
        incomingByte = Serial.read();

        delay(100);

        // say what you got:
        if ( i < 5){
            Serial.print("I received: ");
            Serial.println(incomingByte,DEC);
        }
        else Serial.println("STOP");
    }
    else if (enabled == 1){
        //Serial.println("Testing");
        delay(100);
    }
    else{
        Serial.println('a');
        delay(1000);
    }
    
}
