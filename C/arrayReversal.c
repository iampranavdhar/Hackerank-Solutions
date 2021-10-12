#include <stdio.h>
int main(){
    int index;
    scanf("%d",&index);
    int array[1000]={};
    for(int i=0;i<index;i++){
        scanf("%d",&array[i]);
    }
    for(int i=index-1;i>=0;i--){
        printf("%d ",array[i]);
    }
}