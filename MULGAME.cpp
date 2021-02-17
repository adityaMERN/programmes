/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <map>
using namespace std;

int main()
{
    //taking testcase input
    int testcase;
    cin >> testcase;
    while(testcase-->0)
    {
        //taking n,q,m input
        int n,q,m;
        cin >> n >> q >>m;
        //taking the array input
        int A[n];
        for (int each=0;each<n;each++){
            cin >> A[each];
        }
        int B[1000001]={};
        int test[2]={};
        //main logic
        map <pair<int,int>, int> m2;
        while(q--){
            int left,right;
            cin >> left>>right;
            left--,right--;
            if (A[left]>m)
                continue;
            else if (A[left]<=m && A[right]>m){
                B[A[left]]++;
                B[m+1]--;
            }
            else if (A[right]<=m){
                B[A[left]]++;
                B[m+1]--;
                m2[{A[left],A[right]}]++;
                
            }
        }
        for(auto aa : m2){
            int t1=aa.first.first;
            int t2=aa.first.second;
            int t3=aa.second;
            B[t2+t1]-=t3;
            B[t2+2*t1]+=t3;
            int t4=t2+2*t1;
            while(t4+t2<=m){
                t4+=t2;
                B[t4]-=t3;
                B[t4+t1]+=t3;
                t4+=t1;
                
            }
        }
        int mx=0;
        for(int i=0;i<=m;i++){
            B[i]+=B[i-1];
            mx=max(mx,B[i]);
            
        }
        cout<<mx<<endl;
    }
}
