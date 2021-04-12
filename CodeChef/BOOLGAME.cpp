#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define DE(a) cout<< '>' << #a <<':' << a << endl;
#define RE(i,n) for (ll i=0;i<n;i++)
#define FOR(i,a,b) for(ll i =a;a<b;i++)
#define FORRANGE(i,a,b,c) for (ll i=a;i<b;i+=c)
#define REVFOR(j,i,a) for(ll j=i;j>=a;j--)
#define MULTIFOR(j,a,b,c,d) for(ll j=a;j<b && c<d;j++)
#define pback(x) push_back(x)
#define mpair(x,y) make_pair(x,y)
#define frst first
#define scnd second
#define dbl long double
#define all(x) x.begin(),x.end()
int main()
{
    ll testcase;

    cin>>testcase;
    while(testcase--)
    {
        ll n,m,k;
        ll idx,w,val,old_mask;
        vector<ll> g(n+1);
        RE(i,n)
        {
            cin>>g[i+1];
        }
        vector<vector<pair<ll,ll > > > arr(n+1);
        RE(i,m)
        {
            ll u,v,d;
            arr[u].pback(mpair(i,d));
            arr[v].pback(mpair(i,d));
        }
        vector<vector<pair<ll,ll > > > dp(n+1);
        dp[0].pback(mpair(0,0));
        FOR(i,1,n+1)
        {
            vector<pair<ll,ll > > temp;
            temp.insert(temp.end(),all(dp[i-1]));
            ll current=0,mask=0;
            set <ll> open;
            REVFOR(j,i,1)
            {
                current+=g[j];
                mask^=1LL<<j;
                for(auto & [idx,w]:arr[j])
                {
                    if(open.count(idx)){
                        current+=w;
                    }
                    else{
                        open.insert(idx);
                    }
                }
                if(j>1){
                    for( auto & [val,old_mask] : dp[j-2]){
                        temp.pback(mpair(val+current,mask^old_mask));
                    }
                }
                else{
                    temp.pback(mpair(current,mask));

                }
            }
            sort(all(temp));
            reverse(all(temp));
            set<ll> select;
            ll filled=0;
            MULTIFOR(j,0,temp.size(),filled,k)
            {
                if(select.count(temp[j].scnd)) continue;
                dp[i].pback(temp[j]);
                filled++;
                select.insert(temp[j].scnd);
            }


        }
        RE(i,k)
        {
            cout<<dp[n][i].frst<<" ";
        }
        cout<<endl;
    }
}