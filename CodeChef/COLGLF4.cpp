//Question link : https://www.codechef.com/MARCH21B/problems/COLGLF4


#include<iostream>
#include<vector>
#include<algorithm>
#define Int long long int
using namespace std;


int main()
{
    Int t;
    cin>>t;
    while(t--){
        Int n,e,h,a,b,c;
        cin>>n>>e>>h>>a>>b>>c;
        vector<Int>solution;
        vector<Int>k;
        
        Int count=0;
        Int temp=0;
        for(int i=0;i<=n+1;i++)
        {
            k.push_back(i);
            
        }
        for(Int m=0;m<=n;m++){
            Int x1=lower_bound(k.begin(),k.end(),(2*n-e-2*m))-k.begin();
            Int x2=upper_bound(k.begin(),k.end(),(h-3*m))-k.begin()-1;
            if (x2<x1|| x1==n+1)
            continue;
            if (x2==n+1&& x2+3*m>h)
            continue;
            Int kk;
            if (c>a)
            kk=(x1<(n-m)?x1:(n-m));
            else
            kk= (x2<(n-m)?x2:(n-m));
            Int o=n-kk-m;
            if(kk+2*m>=2*n-e && kk+3*m<=h){
                solution.push_back(a*o+b*m+c*kk);
            }
            
        }
        if(solution.size()==0)
        cout<<"-1"<<endl;
        else{
            Int min=solution[0];
            for(Int i=0;i<solution.size();i++){
                if(solution[i]<min)
                min=solution[i];
            }
            cout<<min<<endl;
        }
        
        
    }
    return 0;
}
