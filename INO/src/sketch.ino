int sensorPin = A0;
int sensorValue = 0;

Servo bottom_ser;   // Create Horiz rotation servo
Servo top_ser;      // Create Vert rotation servo

int pos_bot;
int pos_top;

void setup(){
    bottom_ser.attach(9);
    top_ser.attach(6);
    Serial.begin(9600);
}

void Sweep_Right(){
    for( pos_bot = 0; pos_bot <= 30; pos_bot += 1)
            /// Must figure out actual values for this
    {
        bottom_ser.write(pos_bot);
        Print_Pos();
        delay(15);
    }
}

void Sweep_Left(){
    for( pos_bot = 0; pos_bot <= 30; pos_bot += 1) // This should increment
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

    for( pos_top = 0; pos_top <= 17; pos_top += 1 ) // WONT WORK
                        // The initial value must be tan -1 ( 15cm / H(in cm))
                        // End value must be related somehow
    {   
        Print_Pos();
        switch( pos_top%2) // Should check to see if this works
        {
            case 0: Sweep_Right(); break;
            case 1: Sweep_Left(); break;
        }
    }
    Serial.println("DONE");
}
