# "Accidents" dataset source
[French Goverment Open Data Site] (https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/)

Data downloaded:
- `characteristiques-2018.csv`
- `lieux-2018.csv`
- `vehicules-2018.csv`
- `usagers-2018.csv`

Metadata downloaded:
- `description-des-bases-de-donnees-onisr-annees-2005-a-2018.pdf` (renamed to `Description_BD_ONISR.pdf`)
- `Licence_Ouverte.pdf` (Open data license)

# "Accidents" Preprocessing
To create the preprocessed tables execute (requires the pyKhiops package):
```
python preprocessing.py
```
The codification of each table is specified in the `AccidentsPreprocess.kdic` file.

Below you will find a translation to English of the table descriptions found in the
`Description_BD_ONISR.pdf` document. Each field is followed by its original name in French in
parentheses.

## Preprocessing description and notes
- The preprocessing translates the name of all columns to English
- Most of the fields have numerical values which are described in the `Description_BD_ONISR.pdf`
  document. The preprocessing transforms them to self-explanatory values in English that match the
  description below with no spaces (in CamelCase convention).
- The accident date columns are collapsed to one of type `Date` .
- Some composed columns are split to two or more columns.
- Many fields have an undocumented `00` or `0` value. These have been translated to `Unknown` or
  `None` if `Unknown` is a valid value.
- The field `School` (`env1`) has undocumented values.
- Latitudes and Longitudes are not coherent for accidents outside metropolitan France.

## Table Accident
AccidentId (Num_Acc)
  - Accident id

Day (jour)
  - Accident day

Month (mois)
  - Accident month

Year (an)
  - Accident year

Time (hrmn)
  - Accident time

Light (lum)
  - Light conditions of the accident
    - 1 = Broad daylight
    - 2 = Twilight or dawn
    - 3 = Night without street lighting
    - 4 = Night with street lighting off
    - 5 = Night with street lighting on

Department (dep)
  - Department : Code INSEE (Institut National de la Statistique et des Etudes Economiques)
    of the department followed by a '0' (201 Corse-du-Sud - 202 Haute-Corse)

Com (com)
  - Commune : Code INSEE of the commune. 3 digits right padded.

InAgglomeration (agg)
  - Type of localisation of the accident:
    - 1 = Outside an urban agglomeration
    - 2 = Inside an urban agglomération

IntersectionType (int)
  - Type of intersection where the accident happened:
    - 1 = No intersection
    - 2 = X-type intersection
    - 3 = T-type intersection
    - 4 = Y-type intersection
    - 5 = Intersection with more than 4 branches
    - 6 = Roundabout
    - 7 = Square
    - 8 = Level crossing
    - 9 = Other intersection

Weather (atm)
  - Weather conditions:
    - 1 = Normal
    - 2 = Light rain
    - 3 = Heavy rain
    - 4 = Snow or hail
    - 5 = Fog or smoke
    - 6 = Strong wind or storm
    - 7 = Very good
    - 8 = Overcast
    - 9 = Other

ColType (col)
  - Collision type:
    - 1 = Two vehicles - frontal
    - 2 = Two vehicles – behind
    - 3 = Two vehicles – side
    - 4 = Three or more vehicles – chain
    - 5 = Three or more vehicles - multiple collisions
    - 6 = Other collision
    - 7 = No collision

Address (adr)
  Postal address : available only for in-agglomeration accidents

GPS (gps)
  - GPS code:
    - 1 character indicating the geographical origin :
      - M = Metropolitan France
      - A = Antilles (Martinique or Guadeloupe)
      - G = Guyane
      - R = Réunion
      - Y = Mayotte

Latitude (lat), Longitude(long)
- Geographical coordinates in decimal degrees:
  - lat : Latitude
  - long : Longitude

## Table Place
AccidentId (Num_Acc):
  - Id of the accident

RoadType (catr):
  - Road type :
    - 1 = Highway
    - 2 = National road
    - 3 = Departmental road
    - 4 = Communal road
    - 5 = Private road
    - 6 = Public parking
    - 9 = Other

RoadNum (voie)
  - Road number

RoadSecNum (V1)
  - Secondary road number (example : 2 = bis, 3 = ter,  etc.)

RoadLetter (V2)
  - Road letter

Circulation (circ)
  - Circulation regime:
    - 1 = One-way
    - 2 = Two-way
    - 3 = Divided highway
    - 4 = Lanes with variable way

LaneNumber (nbv)
  Total number of lanes

SpecialLane (vosp)
  - If specified the site had a special lane (whether or not the accident happened in that lane):
    - 1 = Separated bike lane
    - 2 = Bike lane
    - 3 = Reserved lane

Slope (prof)
  - Slope profile at the accident site:
    - 1 = Flat
    - 2 = Uphill
    - 3 = Top of a hill
    - 4 = Bottom of a hill

Marker (pr)
  - Location marker number (the closest upstream)

MarkerDist (pr1)
  - Distance in meters to the closest upstream location marker

Layout (plan)
  - Layout of the road :
    - 1 = Straight
    - 2 = Left curve
    - 3 = Right curve
    - 4 = "S" curve

StripWidth (lartpc)
  - Width of the median strip (if any)

LaneWidth (larrout)
  - Width of the lane dedicated to vehicle circulation. Does not include emergency shoulders, median strips and parkings.

SurfCond (surf)
  - Surface Conditions
    - 1 = Normal
    - 2 = Wet
    - 3 = Puddles
    - 4 = Flooded
    - 5 = Snow
    - 6 = Mud
    - 7 = Ice
    - 8 = Oil
    - 9 = Other

Infra (infra)
- Infrastructure & facilities:
  - 1 = Tunnel/Underpass
  - 2 = Bridge/Overpass
  - 3 = Interchange/Collector
  - 4 = Railroad
  - 5 = Controlled intersection
  - 6 = Pedestrian zone
  - 7 = Toll Zone

Localization (situ)
  - Accident localization:
    - 1 =  Lane
    - 2 =  Emergency shoulder
    - 3 =  Shoulder
    - 4 =  Sidewalk
    - 5 =  Bike lane

School (env1)
  - Specified if a school is nearby


## Table Vehicles
AccidentId (Num_Acc)
  - Accident id

VehicleId (Num_Veh)
  - Vehicle id

Direction (senc)
  - Direction of the vehicle
    - 1 = Increasing location marker or street number
    - 2 = Decreasing location marker or street number

Category (catv)
  - Vehicle category:
    - 01 = Bicycle
    - 02 = Moped (engine displacement < 50cm3)
    - 03 = Quadricycle
    - 04 = Unused since 2006 (registered scooter)
    - 05 = Unused since 2006 (motorcycle)
    - 06 = Unused since 2006 (sidecar)
    - 07 = Car (< 3.5T)
    - 08 = Unused (VL + caravan trailer)
    - 09 = Unused (VL + trailer)
    - 10 = Utility vehicle (1.5T <= total weight <= 3.5T) with or without trailer
    - 11 = Unused since 2006 (Utility vehicle + caravan trailer)
    - 12 = Unused since 2006 (Utility vehicle + trailer)
    - 13 = Large goods vehicle (3.5T < total weight <= 7.5T)
    - 14 = Large goods vehicle (total weight > 7,5T)
    - 15 = Large goods vehicle (total weight > 3,5T) with trailer
    - 16 = Truck
    - 17 = Truck + semi-trailer
    - 18 = Unused since 2006 (public transport)
    - 19 = Unused since 2006 (tramway)
    - 20 = Special engine
    - 21 = Tractor
    - 30 = Scooter (engine displacement < 50 cm3)
    - 31 = Motorbike (50cm3 < engine displacement <= 125 cm3)
    - 32 = Scooter (50cm3 < engine displacement <= 125 cm3)
    - 33 = Motorbike (engine displacement > 125cm3)
    - 34 = Scooter (engine displacement > 125cm3)
    - 35 = Quad bike (engine displacement <= 50cm3)
    - 36 = Heavy Quad bike (engine displacement > 50cm3)
    - 37 = Bus
    - 38 = Coach
    - 39 = Train
    - 40 = Tramway
    - 99 = Other vehicle (of which pedestrian using roller skates or kick scooter requalified since 2018)

FixedObstacle (obs)
  - Impacted fixed obstacle:
    - 01 = Stationary vehicle
    - 02 = Tree
    - 03 = Metallic barrier
    - 04 = Concrete barrier
    - 05 = Other barrier
    - 06 = Building, wall, bridge pier
    - 07 = Traffic sign support or emergency call box
    - 08 = Post
    - 09 = Street furniture
    - 10 = Parapet
    - 11 = Traffic island, refuge, milestone
    - 12 = Sidewalk edge
    - 13 = Ditch, talus, rocky wall
    - 14 = Other fixed obstacle within a lane
    - 15 = Other fixed obstacle within a sidewalk or shoulder
    - 16 = Exit of lane without obstacle

MobileObstacle (obsm)
  - Impacted mobile obstacle:
    - 1 = Pedestrian
    - 2 = Vehicle
    - 4 = Railed vehicle
    - 5 = Domestic animal
    - 6 = Wild animal
    - 9 = Other

ImpactPoint (choc)
  - Initial impact point :
    - 1 = Front
    - 2 = Right front
    - 3 = Left front
    - 4 = Back
    - 5 = Right back
    - 6 = Left back
    - 7 = Right side
    - 8 = Left side
    - 9 = Multiple impacts (barrels)

Maneuver (manv)
  - Principal maneuver before the accident:
    - 01 = No change of direction
    - 02 = Same direction, same lane
    - 03 = Between two lanes
    - 04 = Reverse
    - 05 = Wrong way
    - 06 = Crossing the median strip
    - 07 = In the bus lane, same direction
    - 08 = In the bus lane, inversed direction
    - 09 = Insertion
    - 10 = U-turn in the lane
    - 11 = Change to the left lane
    - 12 = Change to the right lane
    - 13 = Swerve to the left
    - 14 = Swerve to the right
    - 15 = Turn to the left
    - 16 = Turn to the right
    - 17 = Passing to the left
    - 18 = Passing to the right
    - 19 = Crossing the lane
    - 20 = Parking
    - 21 = Avoidance maneuver
    - 22 = Door opening
    - 23 = Stopped (not parked)
    - 24 = Parked (with occupants)

PassengerNumber (occutc)
  - Number of vehicle passengers in a public transport

## Table "Users"
AccidentId (Num_Acc)
  - Accident id

VehicleId (num_veh)
  - Vehicle id

Seat (place):
  - Seat location of the user at the accident's time
```
Public transport

|-----------------------------------
|4  7  7  7                7  7 | 1 |\
|-----------------------------------| \
|5  8  8  8                8  8 | 6 | |
|5  8  8  8                8  8 |   | |
|5  8  8  8                8  8 | 6 | /
|3  9  9  9                9  9 | 2 |/
|-----------------------------------

Car
--------
|4  7  1|\
|5  8  6||
|3  9  2|/
--------

Moto/Sidecar

         \
2--|--1--|
   |     /
   3
```

Category (catu)
  - User category:
    - 1 = Driver
    - 2 = Passenger
    - 3 = Pedestrian
    - 4 = Pedestrian using roller skates or kick scooter (category moved to vehicles, see Vehicle.Category 99 - Other)

Gravity (grav)
  - Accident gravity : 3 categories for injured users and 1 for the unscathed
    - 1 = Unscathed
    - 2 = Death
    - 3 = Injured and hospitalized
    - 4 = Mildly Injured

Gender (sexe)
  - User's gender
    - 1 = Male
    - 2 = Female

BirthYear (An_nais)
  - User's birthdate

TripReason (trajet)
  - Reason of the accident's trip
    - 1 = Home - Work
    - 2 = Home - School
    - 3 = Shopping
    - 4 = Professional Usage
    - 5 = Leisure
    - 9 = Other

Safety (secu)
 - Two chars :
  - The first is the safety device
    - 1 = Seat Belt
    - 2 = Helmet
    - 3 = Device for Children
    - 4 = High-Visibility Vest
    - 9 = Other
  - The second indicates if it was used
    - 1 = Yes
    - 2 = No
    - 3 = Unknown

PedestrianLocation (locp)
  - Location of a pedestrian :
    - On sidewalk :
      - 1 = More than 50m of a pedestrian crossing
      - 2 = Less than 50m of a pedestrian crossing

    - On pedestrian crossing:
      - 3 = Without warning lights
      - 4 = With warning light

    - Various :
      - 5 = On sidewalk
      - 6 = On shoulder
      - 7 = On emergency shoulder
      - 8 = On service road

PedestrianAction (actp)
  - Pedestrian action :
    - Moving
      - 0 = Not available
      - 1 = With the vehicle
      - 2 = Against the vehicle

    - Various
      - 3 = Crossing
      - 4 = Covered
      - 5 = Playing or Running
      - 6 = With mascot
      - 9 = Other

PedestrianCompany (etatp)
    1 = Alone
    2 = With someone
    3 = With a group
