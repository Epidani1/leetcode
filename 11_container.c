/*
*Leetcode Challenge 11: Container with most water
*Description: Given [n] non-negative integers where each integer represents height, find max. rectangle 
*formed by joining two vertical lines. 
*Source: https://leetcode.com/problems/container-with-most-water/ 
*/

#include <stdio.h>

int max(int x, int y) {
    if (x > y) return x;
    else return y;
}

int min(int x, int y) {
    if (x > y) return y;
    else return x;
}

int maxArea(int *height, int arrayNum) {
    int maxArea = 0;
    for (int i = 0; i<arrayNum; i++) {
        for (int j = i+1; j<arrayNum; j++) {
            maxArea = max(maxArea, min(height[i], height[j])*(j-i)); //compare the rectangle formed by height[i] and height[j] to maxArea and replace maxArea if the formed rectangle is larger
        }
    }
    return maxArea;
}

// int main(void) {
//     int arr[] = {1,8,6,2,5,4,8,3,7};
//     int maxSize = maxArea(arr, sizeof(arr)/sizeof(int));
//     return 0;
// }

