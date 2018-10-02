// Problem : Program to implement Queue using Array.

#include<stdio.h>

int size=0;     ///declaring global variables
int queue[10];
int front=-1, rear=-1;

void enqueue();     ///declaring user defined functions
void dequeue();
void get_front();
void get_rear();
int isempty();
int isfull();
void display();

void main()     ///main function starts from here
{
    int choice;

    printf("\n***Program to implement Queue using Array***\n");

    printf("\nEnter the size of Queue: ");      ///taking the size of queue from user
    scanf("%d", &size);

    queue[size];        ///allocating that much size to queue array

    do
    {
        display();      ///calling function to display present queue after each operation

        printf("\n\n     ***Main Menu***\n");       ///main menu
        printf("\n1. Insert an element in Queue");
        printf("\n2. Delete an element from Queue");
        printf("\n3. Get front(1st element) of Queue");
        printf("\n4. Get rear(last element) of Queue");
        printf("\n5. Check for Empty Queue");
        printf("\n6. Check for Full Queue");
        printf("\n0. Exit");

        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:         ///calling the functions according to users choice
                enqueue();
            break;

            case 2:
                dequeue();
            break;

            case 3:
                get_front();
            break;

            case 4:
                get_rear();
            break;

            case 5:
                printf("\nEmpty Status: %s", (isempty() ?"true\n" :"false\n"));
            break;

            case 6:
                printf("\nFull Status: %s", (isfull() ?"true\n" :"false\n"));
            break;

            case 0:

            break;

            default:
                printf("\nInvalid Choice...\n");
            break;
        }
    }while(choice != 0);
}       ///main function ends here

int isempty()
{
    if(front == -1)     ///if front is -1(which is it's initial value) than queue is empty
        return 1;
    else
        return 0;
}

int isfull()
{
    if(rear+1 >= size)      ///if rear is equal to size of queue than queue is full(initial value of rear is -1 so just to check adding 1 here)
        return 1;
    else
        return 0;
}

void enqueue()
{
    int num;

    if(isfull())    ///if queue is full than we can not perform enqueue operation
    {
        printf("\nQueue is Full...Can not insert an Element.\n");
    }

    else
    {
        printf("\nEnter an Element to insert: ");   ///else taking that number from user
        scanf("%d", &num);

        if(rear == -1)  ///is we are en queuing very first element than setting front to 0, to point at first position
            front = 0;

        rear = rear+1;  ///for any case increasing rear by 1 to point at the last element of queue
        queue[rear] = num;  ///storing the number at that position

        printf("\n%d inserted Successfully.\n", num);
    }
}

void dequeue()
{
    int num;

    if(isempty())
    {
        printf("\nQueue is Empty...Can not delete an Element.\n");
    }

    else
    {
        num = queue[front];     ///dequeue operation from 1st element of queue (FIFO)

        if(front == rear)   ///if we are deleting the last element than after that both front and rear should point at -1
        {
            front = -1;
            rear = -1;
        }

        else    ///else just increasing front by 1 to point at next element in the queue
        {
            front = front+1;
        }

        printf("\nDeleted Element: %d", num);
    }
}

void get_front()
{
    if(isempty())
        printf("\nQueue is Empty!!\n");

    else
        printf("\nFront of queue is: %d", queue[front]);    ///just printing the element where the front is pointing in the queue
}

void get_rear()
{
    if(isempty())
        printf("\nQueue is Empty!!\n");

    else
        printf("\nRear of queue is: %d", queue[rear]);      ///just printing the element at rear position
}

void display()
{
    int i;

    printf("\n\n\tPresent Queue");
    printf("\n\t--------------\n");

    if(front == -1 && rear == -1)   ///if queue is empty than printing EMPTY
    {
        printf("\t    EMPTY");
        printf("\n\t--------------\n");
    }

    else
    {
        printf("\t  ");
        for(i=0; i<front; i++)  ///loop to add spaces for the elements which are deleted from the queue
        {
            printf("   ", queue[i]);
        }
        for(i=front; i<=rear ; i++)     ///loop to display present elements starting from front to rear
        {
            printf("%d  ", queue[i]);
        }
        printf("\n\t--------------\n");
    }
}
