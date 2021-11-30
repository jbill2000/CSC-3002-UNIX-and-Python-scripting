math: main.o perimeter.o area.o
	g++ main.o perimeter.o area.o -o math

main.o: main.cpp
	g++ -c main.cpp

perimeter.o: perimeter.cpp
	g++ -c perimeter.cpp

area.o: area.cpp
	g++ -c area.cpp

clean:
	rm *.o math
