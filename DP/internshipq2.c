#include <stdio.h>
#include <stdlib.h>
#define MAX_ARRAYSIZE (100)
int max(int prices[],int n) {
      int currentBuy = prices[0];
      int currentSell = prices[0];
      int maxProfit=0;
      for(int i = 0; i < n + 1; i++){
          if(prices[i] < currentBuy){
              currentBuy = prices[i];
              currentSell = prices[i + 1];
              if(currentSell - currentBuy > maxProfit){
                    maxProfit = currentSell - currentBuy;
              }
          } 
          else if(prices[i] > currentSell){
              currentSell = prices[i];
              if(currentSell - currentBuy > maxProfit){
                    maxProfit = currentSell - currentBuy;
                }
           }
        }
        return maxProfit;
};
int main(){
    int prices[MAX_ARRAYSIZE];
    for (int j=0;j<MAX_ARRAYSIZE;j++){
        scanf("%d,",prices[j]);
    }
    int n = sizeof(prices)/sizeof(prices[0]);
    int x=max(prices,n);
    printf("%d",x);
}
