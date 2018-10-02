// Problem : implementation of stack using array.

#include <stdio.h>
#include <stdlib.h>

void push();    //declaring user defined functions
void pop();
void peek();
int isempty();
int isfull();
void display();

int size;       //declaration of global variables
int stack[];
int top = -1;
int i=0;
int data;

void main() {        //main function

    int choice;

    printf("\n***Program to implement stack***\n\n");

    printf("\nEnter the size of stack: ");      //taking size of stack
    scanf("%d", &size);
    stack[size];        //allocating memory to the stack array

    do
    {
        display();      //displaying current stack

        printf("\n1. PUSH an Element");
        printf("\n2. POP Element");
        printf("\n3. Find item on top of stack");
        printf("\n4. Check if stack is full");
        printf("\n5. Check if stack is empty");
        printf("\n0. Exit");

        printf("\n\nEnter your Choice: ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1:
                push();     //calling function
            break;

            case 2:
                pop();
            break;

            case 3:
                peek();
            break;

            case 4:
                printf("\nStack full: %s\n" , isfull()?"true":"false");
            break;

            case 5:
                printf("\nStack empty: %s\n", isempty()?"true":"false");
            break;

            case 0:

            break;

            default :
                printf("\nInvalid Choice...\n");
            break;
        }
    }while(choice != 0);        //loop will iterate until user enters 0
}      //end of main function

int isempty() {     //function to check whether the stack is empty or not

   if(top == -1)        //checking by minimum size
      return 1;
   else
      return 0;
}

int isfull() {      //function to check whether the stack is full or not

   if(top == size-1)    //checking by maximum size
      return 1;
   else
      return 0;
}

void push() {       //function to add an element into the stack

   if(!isfull()) {      //if not empty then we can push

       printf("\nEnter an Element to PUSH: ");
       scanf("%d", &data);

       top = top + 1;       //increasing top of the stack by 1
       stack[top] = data;       //storing data

       printf("\n\nPushed Successfully...\n");
   }else {
      printf("\nCould not PUSH data, Stack is full.\n");
   }
}

void pop() {        //function to pop element

   if(!isempty()) {

      data = stack[top];    //taking top element in data variable
      top = top - 1;        //decreasing top of the stack by 1

      printf("\n%d Popped Successfully...\n", data);
   }else {
      printf("\nCould not POP data, Stack is empty.\n");
   }
}

void peek() {   //function to display top of the stack element

    if(!isempty())
        printf("\nTop Element: %d\n", stack[top]);

    else
        printf("\nCould not find top of element, Stack is empty.\n");
}

void display() {    //function to print the current stack in whole code

    printf("\n***Current Stack***");

    if(!isempty()) {
        printf("\n");
        for(i=top; i>-1; i--)   //printing one by one element
        {
            printf("\t%d \n", stack[i]);
        }
        printf("\n");
    } else
        printf("\n\tNULL\n");
}
