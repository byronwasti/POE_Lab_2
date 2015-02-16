#include <Servo.h>

// for incoming serial data
int incomingByte = 0;   

int sensorPin = A0;

// Setting up variables for taking average reading
int sensorValue = 0;
int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
int sensorValue5 = 0;

// Creating the bottom and top servos
Servo bser;
Servo tser; 

// Giving initial and end points for servos
const int bstart = 65; 
const int bend = 125; 
const int tstart = 52;
const int tend = 110;

// Setting up variables to hold servo positions
int bpos = bstart;
int tpos = tstart;

// Variable to control how many data points to take
int steps = 1;

// Sets up whether to start 3D Scanning
int enabled = 0;

// Sets whether to stop 3D scanning
int ENDER = 0;

// How long to wait for the servo to reach position
int delayer = 60;

// Typical Setup function
void setup() {
    
    // Open serial port at 9600 baud rate
    Serial.begin(9600);    

    // Set up LED debugging
    pinMode(7, OUTPUT);
    pinMode(8,OUTPUT);

    // Set kill button with internal pullup
    pinMode(2, INPUT_PULLUP);

    // Set up both Servos
    bser.attach(9);
    tser.attach(6);
}

int Take_Data(){

    // Which way the gimbal is panning
    static int direction = 0;

    // Setting up movements
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
    sensorValue1 = analogRead(sensorPin);
    delay(15);
    sensorValue2 = analogRead(sensorPin);
    delay(15);
    sensorValue3 = analogRead(sensorPin);
    delay(15);
    sensorValue4 = analogRead(sensorPin);
    delay(15);
    sensorValue5 = analogRead(sensorPin);


    sensorValue = (sensorValue + sensorValue2 + sensorValue3 + sensorValue4 + sensorValue5)/5;
    

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
        if ( digitalRead(2) == 0 ) ENDER = 1;
    }
    else if (enabled == 0){

        // Just sends out 'a' over the serial
        // This allows for better connection
        Serial.println('a');
        delay(1000);
    }
    
}
