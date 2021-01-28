# AutoDrop - Summary
An "Iron Python" program designed to calculate and control a payload drop on a model plane for the SAE Aero Competition.
This repository's purpose is to display coding capability and versitality.


## Scope and Purpose
The program should automatically signal an arduino system to drop a payload on to a pre-determined target of 30ft in diameter.
Aerodynamic drag should be accounted into the calculations (drag varies by speed).
It should be possible to send a drop signal manually for safety regulations.


## Details
Iron Python was used because it was the only language that integrated with the plane control command software (Mission Planner).
An arduino system was used to contol the on board servos.
### Issues with Iron Python and Mission Planner System
- Stability issues with some normal Python libraries
- Multi-threading was limited (caused safety and auto signal to need to be implemented differently)
- Testing time was limited because the plane system needed to be completed for in air testing


## Program Process
1. Mark Target
2. Set air constanstants (hard coded)
3. Use a multi-diferential solver with GPS data to determine velocity vectors
4. Use velocity vectors and height to determine time and distance to impact
5. Match projectile path to target location
6. Drop if projectile will hit target
7. Check if saftey signal was recieved


## Final Product
Final testing was able to drop within 50ft of accuracy, but time constraints limited further provable improvement.
Improvements were made, but were not able to be tested at competition due to unforseen signal issues. 
(Plane was also destroyed due to mechanical issues. This prevented post competition testing.)

