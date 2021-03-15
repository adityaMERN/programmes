#include <bits/stdc++.h>
#define ll long long
using namespace std;
 ll a[1001][1001],b[1001][1001];
bool ans(ll a[1001][1001],ll b[1001][1001],ll r, ll c){
    ll i,j;
    for(i=0;i<r;i++){
        for(j=0;j<c;j++)
        {
            if(a[i][j]!=b[i][j]){
                return false;
            }
        }
    }
    return true;
}
int main(){
    ll t,x,r,c;
    cin>>t;
    while(t--){
        cin>>r>>c>>x;
        ll i,j,k,diff;
        for(i=0;i<r;i++){
            for(j=0;j<c;j++)
                cin>>a[i][j];
        }
        for(i=0;i<r;i++){
            for(j=0;j<c;j++)
                cin>>b[i][j];
        }
        if(r<x&&c<x)
        {
            if(ans(a,b,r,c))
            cout<<"Yes\n";
            else
            cout<<"No\n";
            
        }
        else if(r<x){
            for(i=0;i<r;i++){
                for(j=0;j<=(c-x);j++){
                    if(a[i][j]==b[i][j])
                    continue;
                    else{
                        diff=b[i][j]-a[i][j];
                        a[i][j]+=diff;
                        k=1;
                        while(k<x){
                            a[i][j-k]+=diff;
                            k++;
                        }
                    }
                }
            }
            if(ans(a,b,r,c))
            cout<<"Yes\n";
            else
            cout<<"No\n";
                
        }
        else if(c<x){
            for(i=0;i<r;i++){
                for(j=0;j<=(r-x);j++){
                    if(a[j][i]==b[j][i])
                    continue;
                    else{
                        diff=b[j][i]-a[j][i];
                        a[j][i]+=diff;
                        k=1;
                        while(k<x){
                            a[j+k][i]+=diff;
                            k++;
                        }
                    }
                }
            }
            if(ans(a,b,r,c))
            cout<<"Yes\n";
            else
            cout<<"No\n";
                
        }
        else if(c>x&&r>=x){
            for(i=0;i<r;i++){
                for(j=0;j<=(c-x);j++){
                    if(a[i][j]==b[i][j])
                    continue;
                    else{
                        diff=b[i][j]-a[i][j];
                        a[i][j]+=diff;
                        k=1;
                        while(k<x){
                            a[i][j+k]+=diff;
                            k++;
                        }
                    }
                }
            }
            for(i=0;i<r;i++){
                for(j=0;j<=(r-x);j++){
                    if(a[j][i]==b[j][i])
                    continue;
                    else{
                        diff=b[j][i]-a[j][i];
                        a[j][i]+=diff;
                        k=1;
                        while(k<x){
                            a[j+k][i]+=diff;
                            k++;
                        }
                    }
                }
            }
            if(ans(a,b,r,c))
            cout<<"Yes\n";
            else
            cout<<"No\n";
                
        }
        
        
    }
    return 0;
}