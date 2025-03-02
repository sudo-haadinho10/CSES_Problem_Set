#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


long sum=0;
long sum2=0;

long SumRange(long num1,long num2){
   
    for(long i=num1;i<num2+1;i++){
        sum+=i;
    }
    return sum;
 }

int main(int argc,char *argv[]){
    long n;
    scanf("%lu",&n);
    long * array1=(long *)malloc((n-1)*sizeof(long));
    for(int i=0;i<n-1;i++){
        scanf("%lu",(array1+i));
        sum2+=*(array1+i);
    }
    

    long sum1=SumRange(1,n);
    long final=sum1-sum2;
    printf("%lu",final);

    return 0;

}