int sensorPin = A0;
int sensorValue = 0;

void setup(){
    Serial.begin(9600);
}

void loop(){
    sensorValue = analogRead(sensorPin);
    
    Serial.print(sensorValue);
    Serial.print("\n");
    delay(2);
}
