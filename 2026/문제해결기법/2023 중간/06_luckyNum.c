#include <stdio.h>
#include <stdlib.h>

int main(void){
	// input ====
	int N, K;
	scanf("%d", &N);
	scanf("%d", &K);

	int *A = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++){
		scanf("%d", &A[i]);
	}
	// logic ====
	int count = 0;
	for (int i = 0; i < N; i++){
		int now = A[i];
		
		while (now > 0){
			int num = now % 10; //1의자리숫자
			if (num == K){
				count += 1;
			}
			now /= 10;
		}
	}
	// output ====
	printf("%d", count);

	free(A);

}