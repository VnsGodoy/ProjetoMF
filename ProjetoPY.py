#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define INPUT_SIZE 4
#define LEARNING_RATE 10
#define MAX_ITERATIONS 1000

// Função de ativação (degrau)
int activationFunction(float sum) {
    return (sum >= 0) ? 1 : 0;
}

// Função para treinar o perceptron
void trainPerceptron(int inputs[][INPUT_SIZE], int targets[], float weights[], int num_inputs) {
    int iteration = 0;
    int error = 0;

    while (iteration < MAX_ITERATIONS) {
        error = 0;

        for (int i = 0; i < num_inputs; i++) {
            float sum = 0;

            for (int j = 0; j < INPUT_SIZE; j++) {
                sum += inputs[i][j] * weights[j];
            }

            int output = activationFunction(sum);

            int delta = targets[i] - output;

            if (delta != 0) {
                error = 1;

                for (int j = 0; j < INPUT_SIZE; j++) {
                    weights[j] += LEARNING_RATE * delta * inputs[i][j];
                }
            }
        }

        if (error == 0) {
            break;
        }

        iteration++;
    }
}

int main() {
    int inputs[][INPUT_SIZE] = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    int targets[] = {0, 0, 0, 1};
    float weights[INPUT_SIZE] = {1};

    clock_t start_time = clock();

    trainPerceptron(inputs, targets, weights, 4);

    clock_t end_time = clock();
    double execution_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("Weights: ");
    for (int i = 0; i < INPUT_SIZE; i++) {
        printf("%.2f ", weights[i]);
    }

    printf("\nExecution Time: %.4f seconds\n", execution_time);

    return 0;
}
