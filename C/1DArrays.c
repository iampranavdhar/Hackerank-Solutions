#include <stdio.h>
int main(){
    int num_elements,summ=0;
    scanf("%d",&num_elements);
    int array[1000] = {};
    for(int i=0;i<num_elements;i++){
        scanf("%d",&array[i]);
    }
    for(int i=0;i<num_elements;i++){
        summ = summ + array[i];
    }
    printf("%d",summ);
}