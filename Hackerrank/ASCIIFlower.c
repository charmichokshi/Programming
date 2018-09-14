#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int r; 
    int c; 
    scanf("%d %d",&r,&c);    
    
    for(int i=0; i<r; i++)
        {
        
        for(int j=0; j<c; j++)
            {
            
            printf("..O..");
            }
        printf("\n");
                 for(int j=0; j<c; j++)
                {
                printf("O.o.O");
                 }
        printf("\n");
                     for(int j=0; j<c; j++)
                    {
                    printf("..O..");
                     }
        
        printf("\n");
    }
    return 0;
}
