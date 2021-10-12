#include <stdio.h>
#include <string.h>
int main(){
    char str[1000];
    scanf("%[^\n]%*c", str);
    int length = strlen(str);
    for(int i=0;i<length;i++){
        if(str[i] == ' '){
            printf("\n");
        }
        else{
            printf("%c",str[i]);
        }
    }
}