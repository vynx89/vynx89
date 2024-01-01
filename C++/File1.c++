#include <iostream>

int main() {
    int count;

    std::cout << "Enter a number to start the countdown: ";
    std::cin >> count;

    if (count < 0) {
        std::cout << "Please enter a positive number." << std::endl;
        return 1;
    }

    std::cout << "Countdown:" << std::endl;

    for (int i = count; i >= 0; i--) {
        std::cout << i << std::endl;
    }

    return 0;
}