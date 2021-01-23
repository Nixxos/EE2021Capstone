//SoundboardCode

void setup() {
  Serial.begin(115200);
  pinMode(7, INPUT);    //Button 1
  pinMode(6, INPUT);    //Button 1
  pinMode(5, INPUT);    //Button 3
  pinMode(4, INPUT);    //Button 4
  pinMode(3, INPUT);    //Button 5
  pinMode(2, OUTPUT);   //LED
  pinMode(11, OUTPUT);    //Speaker


}

void loop() {
  int anyButton;    
  byte opcode = getOpcode();    //Get user input

  do    //Wait for button to be pressed to send opcode audio signal
  {
    Serial.println("wait for button press");
    anyButton = (digitalRead(7) || digitalRead(6) || digitalRead(5) || digitalRead(4) || digitalRead(3));
    delay(50);
  }while ((anyButton)== 0);

  blinky();   //Blink led for feedback

  bool pulse[8];    //Array for binary opcode digits

  tone(11, 1350);
  delay(3000);
  noTone(11);
  delay(4000);

  Serial.println(opcode);

  for(byte i = 0; i <= 7; i++)    //Separate binary digits and place in array
  {
     float k = (float) i;
     double bubble = pow(2,k) + .2;
     long expon = (long)bubble;
     
     pulse[i] = ((opcode & ((expon))) >> i);
     //Serial.println(pulse[i]);
  }

  for(byte j = 0; j <= 4; j++)    //Transmit signal
  {
    if (pulse[j] == 1)    //High frequency for 1
    {
      highNote(pulse[j]);
    }
    else    //Low frequency for 0
    {
      lowNote(pulse[j]);
    }
  }
  Serial.println("program resetting");    //End
  delay(3000);
}


byte getOpcode()    //Get user input from buttons
{
  int pellet;
  int ghost1;
  int ghost2;
  int wipe;
  long total;
  byte opcode;
  do{   //Ensure second and third button presses are not identical
    int pos1=0;
    int pos2=0;
    int posa1=0;
    int posa2=0;
    int posa3=0;
    int posa4=0;
    int posa5=0;
    int posb1=0;
    int posb2=0;
    int posb3=0;
    int posb4=0;
    int posb5=0;
    Serial.println("get opcode");
    do{   //First button press
      pos1 = digitalRead(7);
      pos2 = digitalRead(6);
      Serial.println("first loop");
      Serial.println(pos1);
      Serial.println(pos2);
    }while ((pos1 || pos2) == 0);

    pellet = pos2;    //Convert to 1 hot
  
    blinky();
    do{   //Second button press
      posa1 = digitalRead(7);
      posa2 = digitalRead(6);
      posa3 = digitalRead(5);
      posa4 = digitalRead(4);
      posa5 = digitalRead(3);
      Serial.println("second loop");
      Serial.println(posa1);
      Serial.println(posa2);
      Serial.println(posa3);
      Serial.println(posa4);
      Serial.println(posa5);
    } while ((posa1 || posa2 || posa3 || posa4 || posa5) == 0);

    ghost1 = posa2 + (2*posa3) + (3*posa4) + (4*posa5);   //Convert to 1 hot

    blinky();
  
    do{   //Third button press
      posb1 = digitalRead(7);
      posb2 = digitalRead(6);
      posb3 = digitalRead(5);
      posb4 = digitalRead(4);
      posb5 = digitalRead(3);
      Serial.println("third loop");
    } while ((posb1 || posb2 || posb3 || posb4 || posb5) == 0);

    ghost2 = posb2 + (2*posb3) + (3*posb4) + (4*posb5);   //Convert to 1 hot
    blinky();
    wipe = 0;

    if (ghost1 == ghost2)   //Wipe if invalid input
    {
      wipe = 1;
      delay(100);
      blinky();
      delay(100);
      blinky();
      delay(100);
      blinky();
      delay(100);
    }
  } while (wipe == 1);

  total = ghost2 + (ghost1 * 10) + (pellet * 100);    //Bit swizzel
  Serial.println(total);
  Serial.println(pellet);
  delay(100);

  switch (total) {    //1 hot to binary
   case 1: opcode = 0; break;
   case 2: opcode = 1; break;
   //case 3: opcode = 2; break; invalid
   case 4: opcode = 2; break;
   case 10: opcode = 3; break;
   //case 12: opcode = 5; break; invalid
   case 13: opcode = 4; break;
   case 14: opcode = 5; break;
   case 20: opcode = 6; break;
   //case 21: opcode = 9; break; invalid
   case 23: opcode = 7; break;
   case 24: opcode = 8; break;
   //case 30: opcode = 12; break; invalid
   case 31: opcode = 9; break;
   case 32: opcode = 10; break;
   case 34: opcode = 11; break;
   case 40: opcode = 12; break;
   case 41: opcode = 13; break;
   case 42: opcode = 14; break;
   case 43: opcode = 15; break;
   case 101: opcode = 16; break;
   case 102: opcode = 17; break;
   //case 103: opcode = 18; break; invalid
   case 104: opcode = 18; break;
   case 110: opcode = 19; break;
   //case 112: opcode = 20; break; invalid
   case 113: opcode = 20; break;
   case 114: opcode = 21; break;
   case 120: opcode = 22; break;
   //case 121: opcode = 29; break; invalid
   case 123: opcode = 23; break;
   case 124: opcode = 24; break;
   //case 130: opcode = 32; break; invalid
   case 131: opcode = 25; break;
   case 132: opcode = 26; break;
   case 134: opcode = 27; break;
   case 140: opcode = 28; break;
   case 141: opcode = 29; break;
   case 142: opcode = 30; break;
   case 143: opcode = 31; break;
   default: Serial.println("Invalid state!");
  }
  return opcode;
}

void blinky()   //Blink LED for visual feed back
{
  digitalWrite(2, HIGH);
  delay(800);
   
  digitalWrite(2, LOW);
  delay(500);
}

void lowNote(byte j)    //Play low note
{
  //tone(11, 1150);
  delay(2000);
  //noTone(11);
  Serial.println(j);
  delay(3000);
}

void highNote(byte j)   //Play high note
{
  tone(11, 1150);
  delay(2000);
  noTone(11);
  Serial.println(j);
  delay(3000);
}
