ESSAY
Ritiro @m 0

TEXT
This platform does not explicitly allow you to withdraw from the exam; the purpose of this question is to allow you to do so. If you wish to withdraw from the exam, you must write **"WITHDRAWN"** in the answer to this question; if the answer is left blank, the exam will be corrected.


ESSAY
Numeric systems

TEXT
Sort in increasing order the following 8-bit numbers, represented in 2's complement: 
CB, 7F, AA

ANSWER
Risposta:

ESSAY
Computer architecture

TEXT
What is the RAM? What is its purpose?

ANSWER
Risposta:

ESSAY
Python

TEXT
How to convert a string into uppercase in  Python?

ANSWER
Risposta:


CHEATSHEET


QUESTION
Concorso Prodotti

TEXT
# Green Index

Write a program in Python that, starting from data on the population of different nations, and the number of animals and plants in each of them, identifies for each nation:

- the density of animals per population,
- the density of plants per population, and
- calculates the Green Index.

Then print the following results:

- the nation with the highest density of animals per population,
- the nation with the highest density of plants per population, and
- the first three nations, in descending order of Green Index.
  

### Input

The program reads two text files: one containing data about the population and the other containing the number of animals and plants in different nations.

The first file, named `population.txt`, contains population data in the following format:

``` <nation name>;<population> ```

The second file, named `animal_plant_count.txt`, contains the number of animals and plants in the various nations according to the following format:

``` <nation name>;<number of animals>;<number of plants> ```

Assume that the format of both files is correct and that all the nations contained in the file `animal_plant_count.txt` are also present in the  file `population.txt`.

### Operations

The program calculates the density of animal and plants, for each nations, according to the formulas:

```Animal density = Number of animals / Population```


```Plant Density  =  Number of plants piante / Population```


Then, calculate the Green Index for each nation according to the formula:

```Green index(nation) = average( animal density(nation), plant density(nazione) ) * 100```

### OUTPUT

Finally, it will be necessary to identify and print, following the format of the proposed output example:

- the nation with the highest density of animals,
- the nation with the highest density of plants, and
- the top 3 nations in descending order of Green Index.


### Example of output:

```
The nation with the highest ratio of animals per population is the USA with a ratio of 0.018.
The nation with the highest ratio of plants per population is China with a ratio of 0.0049.
The top 3 nations in descending order of Green Index are:

1. China - Green Index: 2.45
2. USA - Green Index: 2.33
3. Brazil - Green Index: 1.35
```

Finally, the program must print the three requested information.

### Example of file  population.txt:

```
Italy;60360000
Germany;83190556
France;67076000
Spain;47351567
USA;331002651
China;1439323776
India;1380004385
Brazil;212559417
Japan;126476461
Russia;145912025
```

### Esempio of file animal_plant_count.txt:

```
Italy;234500;1200000
Germany;300000;800000
France;280000;950000
Spain;200000;600000
USA;6000000;4500000
China;8000000;7000000
India;7000000;5800000
Brazil;2500000;2200000
Japan;1800000;1500000
Russia;3200000;2800000
```


FILES
population.txt
animal_plant_count.txt