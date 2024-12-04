#include <iostream>
#include<vector>
using namespace std;
class Perceptron {
private:
    std::vector<double> weights;
    double learning_rate = 0.1;
    int input_size;
    double bias;
public:
    Perceptron(int input_size) {
        this->input_size = input_size;
        this->weights = std::vector<double>(input_size+1);
        for(int i = 0; i < input_size+1; i++) {
            this->weights.push_back((rand()%2001-1000)/1000.0);
        }
        bias = (rand() % 2001 - 1000)/1000;
    }
    int activation(double sum) {
        return (sum>=0) ? 1: 0;
    }
    void train(std::vector<std::vector<double>> inputs, std::vector<int> expected_outputs, int epochs) {
        for(int epoch = 0;epoch <epochs; epoch++) {
            for(int i = 0;i<inputs.size();i++){
                std::vector<double> input = inputs[i];

                int expected_output = expected_outputs[i];

                int calculated_output = predict(input);

                int error = expected_output - calculated_output;

                for(int j = 0;j<weights.size()-1;j++) {
                    weights[j] += learning_rate * error * input[j];
                }
                bias += learning_rate * error;
            }
        }
    }
    int predict(const std::vector<double>& input) {
        double sum = bias;
        for(int i = 0; i < input_size; i++) {
            sum += weights[i] * input[i];
        }
        return activation(sum);
    }
};

int main() {
    std::vector<std::vector<double>> inputs ={{0, 0}, {0, 1}, {1, 0}, {1, 1}};

    std::vector<int> expected_outputs = {0,0,0,1};

    Perceptron p(3);
    p.train(inputs, expected_outputs, 10000);

    std::cout << "Predicción para [0, 0]: " << p.predict({0, 0}) << std::endl;
    std::cout << "Predicción para [0, 1]: " << p.predict({0, 1}) << std::endl;
    std::cout << "Predicción para [1, 0]: " << p.predict({1, 0}) << std::endl;
    std::cout << "Predicción para [1, 1]: " << p.predict({1, 1}) << std::endl;

}
