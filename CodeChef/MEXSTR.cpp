*#include <bits/stdc++.h>
using namespace std;
#define ll long long;
#define ld long double;
constexpr int MAXN=(int)10e6;
int dp[MAXN+2],dp1[MAXN+2];
int next0[MAXN],next1[MAXN];
void function(){
    string 
}



int main(){
    long long int testcase;
    cin>>testcase;
    while (testcase--){
        string s;
        cin>>s;
        int flag=0;
        for(int i=0;i<s.size();i++){
            if(s[i] == '0'){
                flag=1;
            }
            
        }
        if(flag==0)
        cout<<"0"<<endl;
        else
        cout<<generate(s)<<endl;
    }
    return 0;
}