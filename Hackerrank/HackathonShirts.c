#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int cnt=0;
    int q; 
    int v; 
    int n;
    
    scanf("%d",&q);
    for(int l=0; l<q; l++){
        cnt=0;
        scanf("%d",&n);
        
        int sizes[n];
        for(int sizes_i = 0; sizes_i < n; sizes_i++){
           scanf("%d",&sizes[sizes_i]);    
        }
        scanf("%d",&v);
        int smallest[v]; 
        int largest[v]; 
                    
        for(int a1 = 0; a1 < v; a1++){
            scanf("%d %d",&smallest[a1],&largest[a1]);
        }
     
        for(int a0 = 0; a0 < n; a0++){
             for(int a1 = 0; a1 < v; a1++){
                 if(sizes[a0] >= smallest[a1] ) {
                     if( sizes[a0] <= largest[a1]){
                        cnt++;
                        break
                     }
                }   
            }         
        }
        printf("%d\n",cnt);
    }
    return 0;
}
