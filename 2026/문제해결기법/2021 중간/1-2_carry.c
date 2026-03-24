#include <stdio.h>
#include <string.h>

void reverse(char* str){
	int len = strlen(str);

	for (int i = 0; i < len/2; i++){
		char tmp = str[i];
		str[i] = str[len-i-1];
		str[len-i-1] = tmp;
	}
}

int main(void) {
	char A[100], B[100];
	scanf("%s", A);
	scanf("%s", B);

	// 1: 문자열 뒤집기 ====
	reverse(A);
	reverse(B);

	// 2: 각 숫자 첫째자리부터 carry 계산 ====
	int CARRY = 0;
	int lenA = strlen(A);
	int lenB = strlen(B);
	int maxLen = (lenA > lenB) ? lenA : lenB;

	int flag = 0;
	for (int i = 0; i < maxLen; i++){
		int valA = (i < lenA) ? A[i]-'0' : 0; //아스키 정수로 만들기
		int valB = (i < lenB) ? B[i]-'0' : 0;

		if (valA + valB + flag >= 10){
			CARRY += 1;
			flag = 1;
		} else {
			flag = 0;
		}
	}

	printf("%d", CARRY);
}


/* 
## [접근 계획] ====

- 문자열, reverse함수 이용
1. 받은 숫자 두개 문자열로 reverse처리
2. 각 숫자 첫째자리부터 carry계산


## [참고사항] ====

C: 
	5/2 = 2

py:
	5/2 = 2.5
	5//2 = 2
*/