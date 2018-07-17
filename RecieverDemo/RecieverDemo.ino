
#include <RH_ASK.h>

#include <SPI.h>

RH_ASK rf_reciever;

void setup() {
  //init
rf_reciever.init();

Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:

//set buffer to size of expected i
  uint8_t buffer[17];

  uint8_t buflength = sizeof(buffer);
//check if reived packet is correct size
  if(rf_reciever.recv(buffer, &buflength))
  {
  Serial.print("message recieved: ");
  Serial.println((char*)buffer);
  }
  

}
