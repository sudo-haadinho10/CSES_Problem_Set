#include <stdio.h>
#include <stdlib.h>
 
long n;
 
int main(int argc,char *argv[]){
    scanf("%lu",&n);
    printf("%lu ",n);
 
    while(n!=1){
 
    if(n%2==0){
        n=n/2;
        printf("%lu ",n);
    }
    else{
        n=(n*3)+1;
        printf("%lu ",n);
 
    }
}
 
}
