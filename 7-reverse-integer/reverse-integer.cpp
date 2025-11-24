class Solution {
public:
    int reverse(int x) {
        long long reversed =0, i=0, temp=0;
        if(x < INT_MIN){
        return 0;
        }
        long long n = x;
        if(n<0){
            n *= -1;
        }
        while (n > 0){
            temp = n%10;
            reversed += temp;
            reversed *= 10;
            n /=10;
        }
        if(reversed/10 >= INT_MAX){
            return 0;
        }
        if(x < 0){
            reversed /= 10;
            reversed *= -1;
            return reversed;
        }
        return reversed/10;
        
    }
};