# Bookings

A hotel chain manages its room reservations through a Python program.

The program reads a file **hotels.txt** that contains the description of each hotel. Each line in the file has this format:

```
	hotel_ID:hotel_name:room_number:price
```

Where **hotel_name** is the name of the hotel (may contain spaces), **hotel_ID** is the identification code of the hotel (does not contain spaces), **room_number** is the number of rooms in the hotel, all of which are understood to be free, price is the price of each room. The fields are **separated by the ':' character**.

The program reads a second file **bookings.txt** that contains the reservation requests made on that same day through the hotel chain's portal. Each line in this file is made like this:

```
	ID_request ID_hotel number_rooms
```

Where **request_ID** is the sequence code identifying the reservation request (contains no spaces), **hotel_ID** is the identifier of the hotel to be reserved, **room_number** is the number of rooms to be reserved. The fields are **separated by a space**. Booking requests are shown in chronological order, and those made first always take precedence over later ones.


Assume that the files are not empty and that their format is correct.

**Output**

The program must:
1.  Read the **bookings.txt** file and make reservations, identifying requests that cannot be confirmed based on the number of available rooms. For such requests, ***it should print an on-screen message showing the code of the unconfirmed reservation*** (see example below). The related reservation should be ignored.

2.  After completing the reservations, the program ***should print on the screen***:

    - the number of successful requests and the number of unconfirmed requests

    - the final status of hotel reservations, showing the number of free rooms in each hotel (see example below)

    - the name of the hotel with the largest number of rooms still available (assume it is only one)

# Example:

If the file **hotels.txt** has this content:
```
	MIPN160:Milano Porta Nuova:6:120.00
	T0123:Taormina:12:180.00
	BRC13:Barcelona:13:80.00
	DEOL1:Amsterdam Doelen:15:60.00
	SUE33:Madrid Suecia:10:110.00
	EIND:Eindhoven:18:55.00
	PALAC:Madrid Palacio:12:105.00
```

If the file **bookings.txt** has this content:
```
	ID000 MIPN160 2
	ID001 MIPN160 3
	ID002 DEOL1 3
	ID003 T0123 1
	ID004 BRC13 3
	ID005 DEOL1 1
	ID006 SUE33 1
	ID007 BRC13 5
	ID008 T0123 3
	ID009 EIND 1
	ID010 DEOL1 4
	ID011 PALAC 2
	ID012 MIPN160 2
```

**The output should be**

```
Unconfirmed request: code ID012
Confirmed reservations: 12, unconfirmed requests: 1

Hotel status:
    Hotel Milano Porta Nuova: 6 rooms (1 free)
    Hotel Taormina: 12 rooms (8 free)
    Hotel Barcelona: 13 rooms (5 free)
    Hotel Amsterdam Doelen: 15 rooms (7 free)
    Hotel Madrid Suecia: 10 rooms (9 free)
    Hotel Eindhoven: 18 rooms (17 free)
    Hotel Madrid Palacio: 12 rooms (10 free)

Hotel with more free rooms: Eindhoven
```
