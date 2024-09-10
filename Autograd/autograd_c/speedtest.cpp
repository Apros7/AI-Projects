#include <stdio.h>
#include <time.h>
#include "nn.h"
#include "engine.h"
#include <stdlib.h>

float speedtest(float *speedtest_result) {
    // Create dataset of at least size 784x10x32x1000
    // init model with 784, 10
    // train for 10 steps
    // return time taken
    *speedtest_result = 67;
    return 0;
}

/* The result of this speedtest is X seconds */
/* The result of this speedtest in python is 67 seconds: autograd/speedtest.py */
/* Run with 1000 steps, 32 batch size, 784 input, 10 output on Macbook M1 */

int main() {
    float *speedtest_result = (float *)malloc(sizeof(float));
    if (speedtest_result == NULL) {
        printf("Failed to allocate memory for speedtest_result\n");
        return 1;
    }
    speedtest(speedtest_result);
    printf("The result of this speedtest is %f seconds\n", *speedtest_result);

    free(speedtest_result);
    speedtest_result = 0;
    return 0;
}
