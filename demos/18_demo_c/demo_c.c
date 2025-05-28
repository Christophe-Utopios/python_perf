#include <stdio.h>

__declspec(dllexport) int add(int a, int b) {
    return a + b;
}


__declspec(dllexport) void increment(int* a) {
    (*a)++;
}

__declspec(dllexport) void add_arrays(int* arr1, int* arr2, int* result, int length) {
    for (int i = 0; i < length; i++) {
        result[i] = arr1[i] + arr2[i];
    }
}

__declspec(dllexport) void print_message(const char* msg) {
    printf("C says: %s\n", msg);
}
