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
int direction = 0;

// Sets up whether to start 3D Scanning
int enabled = 0;

// Sets whether to stop 3D scanning
int ENDER = 0;

// How long to wait for the servo to reach position
int delayer = 150;

// Typical Setup function
void setup() {
    
    // Open serial port at 9600 baud rate
    Serial.begin(9600);    

    // Set up LED debugging
    pinMode(7, OUTPUT);
    pinMode(8,OUTPUT);

    // Set up both Servos
    bser.attach(9);
    tser.attach(6);
}

int Take_Data(){

    if (direction == 0){
        bpos += steps;
        if (bpos >= bend){
            direction = 1;
            tpos += steps;
        }
    }
    else {
        bpos -= steps;
        if (bpos <= bstart){
            direction = 0;
            tpos += steps;
        }
    }

    // Return ending condition
    if (tpos > tend) return 1;

    // Write positions to servos
    bser.write(bpos);
    tser.write(tpos);

    delay(delayer);

    // Read sensor for distance
    sensorValue = analogRead(sensorPin);

    // Continue doing processes
    return 0;
}

// Main function which just loops
void loop() {

    // Stops pinging LEDs
    digitalWrite(7, LOW);
    digitalWrite(8,LOW);

    // Sends data when pinged
    if (Serial.available() > 0) {
        
        // Debugging LED, set high when pinged
        digitalWrite(7, HIGH);

        // Flush out all of the "A's" that were being sent
        Serial.flush();

        // Set up enabled for better delay handling
        enabled = 1;

        // read the incoming byte:
        incomingByte = Serial.read();

        // Set ping out pin high
        digitalWrite(8,HIGH);

        // Write to serial
        if (ENDER == 1) {
            Serial.println("STOP");
            delay(1000);
        }
        else {
            Serial.print(sensorValue);
            Serial.print(",");
            Serial.print(bpos);
            Serial.print(",");
            Serial.println(tpos);
        }

        // Go to next position
        ENDER = Take_Data();
    }
    else if (enabled == 0){

        // Just sends out 'a' over the serial
        // This allows for better connection
        Serial.println('a');
        delay(1000);
    }
    
}
