/*
--- Day 4: The Ideal Stocking Stuffer ---
 Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys. To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.  The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash. For example:
If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
 If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so. If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
*/
#include <iostream>
#include <stdio.h>
#include <time.h>
#include <vector>
#include <string>
//#include "md5.h"

using namespace std; 

unsigned int s[64] =
{7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21};

unsigned int k[64] =
{0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391};

//Initialize variables:
int a0 = 0x67452301;   //A
int b0 = 0xefcdab89;   //B
int c0 = 0x98badcfe;   //C
int d0 = 0x10325476;   //D


unsigned int leftrotate(unsigned int x, unsigned int c){
    return (x << c) | (x >> (32-c));
}

//only works for inputs less than 512 bits
string md5(string *input){
	char message[64];
    for (int i = 0; i < input->length(); i++){
        message[i] = input->at(i);
    }
    message[input->length()] = 0x80;
    int orig_length = input->length() * 8;
    if (orig_length > 0xff && orig_length <= 0xffff) {
    	message[56] = orig_length >> 8;
    	message[57] = orig_length & 0xff;
    }
    else {
    	message[56] = orig_length & 0xff;
    }

    unsigned int M[16];

    for (int i = 0; i < 16; i++){
    	M[i] = message[i] << 24 | message[i+1] << 16 | message[i+2] << 8 | message[i+3];
    }

//Initialize hash value for this chunk:
    unsigned int A = a0;
    unsigned int B = b0;
    unsigned int C = c0;
    unsigned int D = d0;
    unsigned int F,g,dTemp;

    for (int i = 0; i < 64; i++){
    	if (i >= 0 && i < 16){
    		F = (B & C) | (~B & D);
    		g = i;
    	}
    	else if (i >= 16 && i < 32){
    		F = (D & B) | (~D & C);
    		g = ((5 * i) + 1) % 16;
    	}
    	else if (i >= 32 && i < 48){
    		F = B ^ C ^ D;
    		g = ((3*i) + 5) % 16;
    	}
    	else {
    		F = C ^ (B | ~D);
            g = (7*i) % 16;
    	}
    	dTemp = D;
    	D = C;
    	C = B;
    	B = B + leftrotate((A + F + k[i] + M[g]),s[i]);
    	A = dTemp;
    }

    a0 = a0 + A;
    b0 = b0 + B;
    c0 = c0 + C;
    d0 = d0 + D;

    std::cout << std::hex;
    std::cout << a0 << endl;
    std::cout << b0 << endl;
    std::cout << c0 << endl;
    std::cout << d0 << endl;
    char digest[16] = 
    {a0 >> 24, a0 >> 16, a0 >> 8, a0,
     b0 >> 24, b0 >> 16, b0 >> 8, b0,
     c0 >> 24, c0 >> 16, c0 >> 8, c0,
     d0 >> 24, d0 >> 16, d0 >> 8, d0};	
    //append b0 append c0 append d0}  //(Output is in little-endian)

    return string(digest);

}

void problem_main(){
	string input = "";
	string output =  md5(&input);
	for (int i = 0; i < output.length(); i++){
		printf("%02x",output.at(i));
	}
	printf("\n");

}



int main(){
	std::cout<<"\n";
	clock_t t1,t2;
	t1=clock();

	problem_main();

	t2=clock();
	cout<<"\nProgram Execution Time: ";
	float diff ((float)t2-(float)t1);
	float seconds = diff / CLOCKS_PER_SEC;
	cout<<seconds<<" seconds."<<endl;
	return 0;
}
