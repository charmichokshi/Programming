#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    
    int n; 
    scanf("%d",&n);
    int squares[n];
    
    for(int squares_i = 0; squares_i < n; squares_i++){
       scanf("%d",&squares[squares_i]);
    }
    
    int d; 
    int m; 
    scanf("%d %d",&d,&m);
    
    int cnt=0, sum, c=0;
    
    for(int i=0; i<n; i++)
    {
        sum=0;
        c=0;
        for(int j=i; c<m; j++)
        {
            sum += squares[j];
            c++;
        }
        if(d == sum)
            cnt++;
    }
    printf("%d",cnt);
    return 0;
}
