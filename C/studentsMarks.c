#include <stdio.h>
int main(){
    int array[] = {},number_of_students,sum=0;
    char gender;
    scanf("%d",&number_of_students);
    for(int i=0;i<number_of_students;i++){
        scanf("%d",&array[i]);
    }
    scanf("%s",&gender);
    if(gender =='b'){
        for(int i=0;i<number_of_students;i=i+2){
            sum = sum +array[i];
        }
    }
    else if(gender == 'g'){
        for (int i = 1; i < number_of_students; i=i+2){
            sum = sum + array[i];
        }
    }
    printf("%d",sum);
}