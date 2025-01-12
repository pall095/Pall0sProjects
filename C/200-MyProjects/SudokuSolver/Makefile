output: sudoku.o utils.o 
	gcc sudoku.o utils.o -o sudoku

sudoku.o: sudoku.c
	gcc -c sudoku.c

utils.o: utils.c
	gcc -c utils.c

clean: 
	rm *.o sudoku