//radio head ASK
#include <RH_ASK.h>

//dependant spi libary
#include <SPI.h>

//ask shift object
RH_ASK rf_Transmitter;

void setup() {
  
//initalize ask obj.

rf_Transmitter.init();

}

void loop() {
  // put your main code here, to run repeatedly:
const char *message = "Hi yardstick one!";

rf_Transmitter.send((uint8_t *)message, strlen(message));
rf_Transmitter.waitPacketSent();

delay(1000);


}
