// notes for Pointers in C language


// Pointers are variables that store address of other variables.

// *p=12; this implies "deferencing" i.e changing the value of the pointing variable. 
// int - 4 bytes
// char - 1 byte
// float - 4 bytes

#include <stdio.h>

int main(){
    int a;
    int *p;       //This code snipppet points to value of a.
    a=10;
    p=&a;         //In this code snippet variable "p" points to address of variable "a".
    printf("address = %d, value = \n",p,*p);
    char *q;
    q=(char*) p;  // typecasting
    printf("Size of char is %d bytes\n", sizeof(char));
    printf("Address = %d, value = %d",q,*q);

    return 0;

    
}
