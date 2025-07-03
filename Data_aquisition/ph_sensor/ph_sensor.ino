#include "DFRobot_PH.h"
#include <EEPROM.h>

#define PH_PIN A1
float voltage, phValue, temperature = 25;
DFRobot_PH ph;

void setup()
{
    Serial.begin(115200);  
    ph.begin();
    Serial.println("pH sensor is starting...");
}

void loop()
{
    static unsigned long timepoint = millis();
    if (millis() - timepoint > 10000U) {  // 10 seconds interval
        timepoint = millis();
        voltage = analogRead(PH_PIN) / 1024.0 * 5000;  // Convert analog reading to mV
        phValue = ph.readPH(voltage, temperature);     // Calculate pH
        Serial.print("temperature:");
        Serial.print(temperature, 1);
        Serial.print("^C  pH:");
        Serial.println(phValue, 2);
    }

    // Handle serial commands for calibration
    if (Serial.available() > 0) {
        String cmd = Serial.readStringUntil('\n');
        cmd.trim(); // Remove trailing newline/spaces

        if (cmd == "enterph") {
            Serial.println(">>>Enter PH Calibration Mode<<<");
            Serial.println(">>>Please put the probe into the 4.0 or 7.0 standard buffer solution<<<");
        } 
        else if (cmd == "calph") {
            Serial.println(">>>Calibrating current buffer...<<<");
        } 
        else if (cmd == "exitph") {
            Serial.println(">>>Exiting calibration mode and saving...<<<");
        }

        // Apply calibration logic regardless of which command
        voltage = analogRead(PH_PIN) / 1024.0 * 5000;
        ph.calibration(voltage, temperature);
    }
}
