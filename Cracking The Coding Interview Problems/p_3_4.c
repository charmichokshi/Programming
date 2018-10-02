// Problem : Program to implement a Queue using two Stacks and Array.

#include<stdio.h>
#define MAX 10        ///declaring MAX as 10

//initializing global variables
int size = 0;        ///size of the queue
int s1[MAX];        ///first stack
int s2[MAX];        ///auxiliary stack
int top = -1;        ///variable to point at top of stack
int cnt = 0;        ///counter to count present numbers in stack
int c = 0;          ///counter for total entered numbers

//declaring user defined functions
void add();
void delete();
void get_rear();
int isempty();
int isfull();
void display();
void transfer_to_1();        ///function to pop from the stack 1 and push into stack 2
void transfer_to_2();        ///function to pop from the stack 2 and push into stack 1

void main()        //main function starts from here
{
    int choice;

    printf("\n***Program to implement a Queue using two Stacks***\n");

    printf("\nEnter the size of Queue: ");
    scanf("%d", &size);

    s1[size];    ///allocating the size entered by user for queue
    s2[size];

    do
    {
        display();        ///calling function display to print current queue

        printf("\n***Main Menu***\n");            //main menu
        printf("\n1. Add Element");
        printf("\n2. Delete an Element");
        printf("\n3. Find the Element at Rear");
        printf("\n4. Check if Queue is Empty");
        printf("\n0. Exit");

        printf("\nEnter your Choice: ");
        scanf("%d", &choice);

        switch(choice)        ///according to users choice functions will be called
        {
            case 1:
                add();
            break;

            case 2:
                delete();
            break;

            case 3:
                get_rear();
            break;

            case 4:
                printf("\nEmpty Status: %s", isempty() ?"true" :"false");
            break;

            case 0:

            break;

            default :
                printf("\nInvalid Choice...\n\n");
            break;
        }
    }while(choice != 0);        ///loop will iterate until user enters 0
}        //main function ends here

void add()        //function to add element into queue
{
    int num;

    if(isfull() || c >= size)        ///if queue is full then we can not add new element
        printf("\nQueue is full, Can not add element.\n");

    else if(c < size)       ///if entered numbers are less than size
    {
        printf("\nEnter an Element to add in the Queue: ");
        scanf("%d", &num);

        top++;       ///increasing top of the stack by 1
        s1[top] = num;       ///storing that number in stack 1

        printf("\n\n%d Pushed Successfully into Queue...\n", num);

        cnt++;        ///increasing cnt and c by 1
        c++;
    }
}

void delete()        //function to delete element from queue
{
    int num;

    if(isempty())        ///if queue is empty then we can not delete element
        printf("\nQueue is Empty, Can not delete an Element.\n");

    else
    {
        transfer_to_2();    ///calling function to pop every element from stack 1 and push into stack 2

        num = s2[cnt-1];    ///tacking the top element of 2Nd stack, which is a firstly added element(FIFO approach of Queue)

        cnt--;        ///since we have deleted 1 element, decreasing counter and pointer to top element by 1
        top--;

        transfer_to_1();    ///calling function to pop remaining elements from the stack 1 and push into stack 2

        if(cnt == 0)
        {
            top = -1;        ///queue is empty, starting from scratch
            c = 0;
        }

        printf("\n%d Deleted Successfully from the Queue.\n", num);
    }
}

void get_rear()        //function to get rear element of queue
{
    if(isempty())
        printf("\nQueue is Empty, No Rear Element present.\n");

    else
        printf("\nRear Element: %d", s1[top]);        ///rear element of queue is a top most element of stack 1
}


int isempty()     //function to check whether the stack is empty or not
{
   if(top == -1)        //checking by minimum size
      return 1;

   else
      return 0;
}

int isfull()      //function to check whether the stack is full or not
{
   if(top == size-1)    //checking by maximum size
      return 1;

   else
      return 0;
}


void transfer_to_2()    //function to reverse stack 1
{
    int i, j = top;

    for(i=0; i<cnt; i++, j--)    ///starting from the top of stack 1 till last element
    {
        s2[i] = s1[j];        ///popping 1 by 1 element of stack 1 and pushing it in stack 2
    }
}

void transfer_to_1()    //function to reverse stack 2
{
    int i, j = cnt-1;

    for(i=0; i<cnt; i++, j--)        ///starting from the top of stack 2 till last element
    {
        s1[i] = s2[j];        ///popping 1 by 1 element of stack 2 and pushing it in stack 1
    }
}

void display()        //function to display current queue
{
    int i;

    printf("\n\n\tPresent Queue");
    printf("\n\t--------------\n");

    if(isempty())       ///in case of Empty queue
    {
        printf("\t    EMPTY");
        printf("\n\t--------------\n");
    }

    else
    {
        int j;

        printf("\t");

        transfer_to_2();    ///reversing stack 1 and then printing it

        for(i=0, j = top; j<size; i++, j++)        ///loop to print null spaces if needed
        {
            printf("  ");
        }

        for(i=cnt; i>0; i--)        ///starting from the top of stack 2 till last element
        {
            printf("%d  ", s2[i-1]);
        }

        printf("\n\t--------------\n");
    }
}
