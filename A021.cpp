// PaizaWakusei.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <algorithm>

void getIsland(const int &height, const int &width, 
                const int y, const int x, 
                int &area, int &perimeter,
                std::vector<std::vector<char>>& image) {
    // Explorated ground update to 'x' (in order no to count it again as new area / to calculate the perimeter)
    image[y][x] = 'x';

    ++area;

    // Perimeter - Check if ground surrounded by water or ground or out of array
    // UP
    if ((y - 1) >= 0) {
        if ((image[y - 1][x] != '#') && (image[y - 1][x] != 'x'))
            ++perimeter;
    }
    else
        ++perimeter;
    // RIGHT
    if ((x + 1) < width) {
        if ((image[y][x + 1] != '#') && (image[y][x + 1] != 'x'))
            ++perimeter;
    }
    else
        ++perimeter;
    // DOWN
    if ((y + 1) < height) {
        if ((image[y + 1][x] != '#') && (image[y + 1][x] != 'x'))
            ++perimeter;
    }
    else
        ++perimeter;
    // LEFT
    if ((x - 1) >= 0) {
        if ((image[y][x - 1] != '#') && (image[y][x - 1] != 'x'))
            ++perimeter;
    }
    else
        ++perimeter;

    // Area - Check if not out of array and if ground
    // UP
    if ((y - 1) >= 0) {
        if (image[y - 1][x] == '#') {
            getIsland(height, width, y - 1, x, area, perimeter, image);
        }
    }
    // RIGHT
    if ((x + 1) < width) {
        if (image[y][x + 1] == '#') {
            getIsland(height, width, y, x+1, area, perimeter, image);
        }
    }
    // DOWN
    if ((y + 1) < height) {
        if (image[y + 1][x] == '#') {
            getIsland(height, width, y+1, x, area, perimeter, image);
        }
    }
    // LEFT
    if ((x - 1) >= 0) {
        if (image[y][x - 1] == '#') {
            getIsland(height, width, y, x-1, area, perimeter, image);
        }
    }
}

int main()
{
    std::list<std::pair<int, int>> islands;

    int height = 0, width = 0;
    std::vector<std::vector<char>> image;
    std::vector<std::vector<char>> image_explored;
    std::string input;

    int island_p = 0;
    int island_a = 0;
    
    // INPUT MAP
    std::cin >> height >> width;
    std::cin.ignore();

    for (int i = 0; i < height; ++i) {
        std::getline(std::cin, input);
        std::vector<char>line(input.begin(), input.end());
        image.push_back(line);
        input = "";
    }
    image_explored = image;

    // CALCULATE AREA AND PERIMETER
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            if (image_explored[y][x] == '#') {
                getIsland(height, width, y, x, island_a, island_p, image_explored);
                islands.push_back(std::make_pair(island_a, island_p));

                island_a = 0;
                island_p = 0;
                
            }
        }
    }
    
    // SORT BY AREA THEN BY PERIMETER
    islands.sort([](auto const& elem1 , auto const& elem2) {
        if(elem1.first == elem2.first)
            return elem1.second > elem2.second;
        return elem1.first > elem2.first;
    });

    // OUTPUT
    /* Not needed by paiza. 2022-02-23
    std::cout << "\n";
    std::cout << "Output : \n";*/

    for (auto const& data : islands)
        std::cout << data.first << " " << data.second << "\n";
    //std::cout << "-------------------------------\n"; Not needed by paiza 2022-02-23

    return 0;
}
