//https://www.codechef.com/APRIL21B/problems/CHAOSEMP

#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main() {
    ll testcase,q,d;
    cin>>testcase>>q>>d;
    while(testcase--)
    {
        ll lx=(-1ll)*1e18;
        ll rx=1e18;
        ll ly=(-1ll)*1e18;
        ll ry=1e18;
        lx--;
        rx++;
        ly--;
        ry++;
        ll current=1;
        string cc;
        ll z=-1;
        while(true)
        {
            if(current==1)
            {
                if(rx>=(lx+2))
                {   
                    if(ry>=(ly+2)){
                        ll midx=(rx+lx)/2;
                        ll midy=(ry+ly)/2;
                        cout<<current<<" "<<midx<<" "<<midy<<endl;
                        cin>>cc;
                        if(cc.compare("O")==0||cc.compare("FAILED")==0)
                        break;
                        if(cc[0]=='X')
                        {
                            lx=midx-1;
                            rx=midx+1;

                        }else if(cc[0]=='P'){
                            if(d==0)
                            {
                                rx=midx-1;

                            }else{
                                rx=midx;
                                lx--;
                            }
                        }else{
                            if(d==0)
                            {
                                lx=midx+1;

                            }else{
                                lx=midx;
                                rx++;
                            }
                        }
                        if(cc[1]=='Y')
                        {
                            ly=midy-1;
                            ry=midy+1;

                        }else if(cc[1]=='P')
                        {
                            if(d==0)
                            {
                                ry=midy-1;
                            }else{
                                ry=midy;
                                ly--;
                            }
                        }else{
                            if(d==0)
                            {
                                ly=midy+1;
                            }else{
                                ly=midy;
                                ry++;
                            }
                        }
                        if(d==0)
                        {

                        }else{
                            if((rx<=(lx+3))&&(ry<=(ly+3)))
                            {
                                current=2;
                            }
                        }

                    }
                    
                }
                else{
                    current=2;
                    cout<<current<<" "<<lx<<" "<<ly<<" "<<rx<<" "<<ry<<endl;
                    cin>>cc;
                    break;
                }
            }
            else{
                if((rx==(lx+3)))
                {
                    if((ry==(ly+3))){
                        cout<<current<<" "<<lx<<" "<<ly<<lx+2<<" "<<ry<<endl;
                        cin>>cc;
                        if(cc.compare("O")==0)
                        {break;}
                        else if(cc.compare("IN")==0){
                            rx=lx+2; 
                        }       else
                    {
                        lx=lx+2;
                        rx++; 
                    }
                    }

                }
                if((rx==(lx+2)))
                {
                    if(ry==(ly+3)){
                        cout<<current<<" "<<lx<<" "<<ly<<" "<<rx<<" "<<ly+2<<endl;
                    cin>>cc;
                    if(cc.compare("O")==0)
                    {}
                    else if(cc.compare("IN")==0){
                        cout<<current<<" "<<lx<<" "<<ly<<" "<<rx<<" "<<ly+2<<endl;
                        cin>>cc;
                    }else
                    {   
                        cout<<current<<" "<<lx<<" "<<ly+2<<" "<<rx<<" "<<ly+4<<endl;
                        cin>>cc;
                    }
                    break;
                    }
                }
                if((rx==(lx+3))){
                    if(ry==(ly+2)){
                        cout<<current<<" "<<lx<<" "<<ly<<" "<<lx+2<<" "<<ry<<endl;
                    cin>>cc;
                    if(cc.compare("O")==0)
                        {}
                    else if(cc.compare("IN")==0){
                    cout<<current<<" "<<lx<<" "<<ly<<" "<<lx+2<<" "<<ry<<endl;
                    cin>>cc;

                    }else{
                    cout<<current<<" "<<lx+2<<" "<<ly<<" "<<lx+4<<" "<<ry<<endl;
                    cin>>cc;
                    }
                    break;
                    }
                }
                else{
                    cout<<current<<" "<<lx<<" "<<ly<<" "<<rx<<" "<<ry<<endl;
                    cin>>cc;
                    break;
                }
            }
            cout.flush();
        }
    cout.flush();  
    }
    
}
